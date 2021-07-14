import collections
import io
import linecache
import pickletools
import types
from pathlib import Path
from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)
from urllib.parse import quote

import torch
from torch.serialization import location_tag, normalize_storage_type

from ._file_structure_representation import Folder, _create_folder_from_file_list
from ._glob_group import GlobPattern, _GlobGroup
from ._importlib import _normalize_path
from ._mangling import is_mangled
from ._package_pickler import create_pickler
from ._stdlib import is_stdlib_module
from .find_file_dependencies import find_files_source_depends_on
from .importer import Importer, OrderedImporter, sys_importer


class EmptyMatchError(Exception):
    """This is an exception that is thrown when a mock or extern is marked as
    allow_empty=False, and is not matched with any module during packaging.
    """

    pass


class DeniedModuleError(Exception):
    """This is an exception that is thrown when a pattern added with deny matches
    a module required during the packaging process.
    """

    pass


class PackageExporter:
    """Exporters allow you to write packages of code, pickled python data, and
    arbitrary binary and text resources into a self-contained package.

    Imports can load this code in a hermetic way, such that code is loaded
    from the package rather than the normal python import system. This allows
    for the packaging of PyTorch model code and data so that it can be run
    on a server or used in the future for transfer learning.

    The code contained in packages is copied file-by-file from the original
    source when it is created, and the file format is a specially organized
    zip file. Future users of the package can unzip the package, and edit the code
    in order to perform custom modifications to it.

    The importer for packages ensures that code in the module can only be loaded from
    within the package, except for modules explicitly listed as external using :method:`extern_module`.
    The file `extern_modules` in the zip archive lists all the modules that a package externally depends on.
    This prevents "implicit" dependencies where the package runs locally because it is importing
    a locally-installed package, but then fails when the package is copied to another machine.


    Dependencies
    ------------

    When source code is added to the package, the exporter optionally can scan it
    for further code dependencies (`dependencies=True`). It looks for import statements,
    resolves relative references to qualified module names, and calls :method:`require_module`
    on each it finds, recursively resolving dependencies.
    """

    """A importer that will be searched in order to find the modules referenced by other modules or by
    pickled objects. The default module environment just uses sys_importer, which searches the Python environment.
    """
    importer: Importer

    def __init__(
        self,
        f: Union[str, Path, BinaryIO],
        importer: Union[Importer, Sequence[Importer]] = sys_importer,
        verbose: bool = True,
    ):
        """
        Create an exporter.

        Args:
            f: The location to export to. Can be a  string/Path object containing a filename,
                or a Binary I/O object.
            importer: If a single Importer is passed, use that to search for modules.
                If a sequence of importers are passsed, an Orderedporter will be constructed out of them.
            verbose: Print information about dependency resolution to stdout.
                Useful for tracking down why certain files get included.
        """
        if isinstance(f, (Path, str)):
            f = str(f)
            self.buffer: Optional[BinaryIO] = None
        else:  # is a byte buffer
            self.buffer = f

        self.zip_file = torch._C.PyTorchFileWriter(f)
        self.zip_file.set_min_version(6)
        self.serialized_storages: Dict[str, Any] = {}
        self.external: List[str] = []
        self.provided: Dict[str, bool] = {}
        self.verbose = verbose

        if isinstance(importer, Importer):
            self.importer = importer
        else:
            if not isinstance(importer, collections.abc.Sequence):
                raise TypeError(
                    "importer arg should be an Importer or a sequence of Importers, "
                    f"got {type(importer)} instead."
                )
            self.importer = OrderedImporter(*importer)

        self.patterns: List[
            Tuple[Any, Callable[[str], None], bool]
        ] = []  # 'any' is 're.Pattern' but breaks old mypy
        self.matched_patterns: Set[int] = set()
        self.debug_deps: List[Tuple[str, str]] = []
        self._unique_id = 0

    def save_source_file(
        self, module_name: str, file_or_directory: str, dependencies=True
    ):
        """Adds the local file system `file_or_directory` to the source package to provide the code
        for `module_name`.

        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            file_or_directory (str): the path to a file or directory of code. When a directory, all python files in the directory
                are recursively copied using :meth:`save_source_file`. If a file is named "/__init__.py" the code is treated
                as a package.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        path = Path(file_or_directory)
        if path.is_dir():
            to_save = []  # list of tuples with arguments to save_source_string
            module_path = module_name.replace(".", "/")
            for filename in path.glob("**/*.py"):
                relative_path = filename.relative_to(path).as_posix()
                archivename = module_path + "/" + relative_path
                if filename.is_dir():
                    self.provided[archivename] = True
                else:
                    submodule_name = None
                    if filename.name == "__init__.py":
                        submodule_name = archivename[: -len("/__init__.py")].replace(
                            "/", "."
                        )
                        is_package = True
                    else:
                        submodule_name = archivename[: -len(".py")].replace("/", ".")
                        is_package = False

                    self.provided[submodule_name] = True
                    # we delay the call to save_source_string so that we record all the source files
                    # being provided by this directory structure _before_ attempting to resolve the dependencies
                    # on the source. This makes sure we don't try to copy over modules that will just get
                    # overwritten by this directory blob
                    to_save.append(
                        (
                            submodule_name,
                            _read_file(str(filename)),
                            is_package,
                            dependencies,
                            str(filename),
                        )
                    )

            for item in to_save:
                self.save_source_string(*item)
        else:
            is_package = path.name == "__init__.py"
            self.save_source_string(
                module_name,
                _read_file(file_or_directory),
                is_package,
                dependencies,
                file_or_directory,
            )

    def file_structure(
        self, *, include: "GlobPattern" = "**", exclude: "GlobPattern" = ()
    ) -> Folder:
        """Returns a file structure representation of package's zipfile.

        Args:
            include (Union[List[str], str]): An optional string e.g. "my_package.my_subpackage", or optional list of strings
                for the names of the files to be inluded in the zipfile representation. This can also be
                a glob-style pattern, as described in :meth:`mock`

            exclude (Union[List[str], str]): An optional pattern that excludes files whose name match the pattern.
        """
        return _create_folder_from_file_list(
            self.zip_file.archive_name(),
            self.zip_file.get_all_written_records(),
            include,
            exclude,
        )

    def get_unique_id(self) -> str:
        """Get an id. This id is guaranteed to only be handed out once for this package."""
        ret = str(self._unique_id)
        self._unique_id += 1
        return ret

    def save_source_string(
        self,
        module_name: str,
        src: str,
        is_package: bool = False,
        dependencies: bool = True,
        orig_file_name: str = None,
    ):
        """Adds `src` as the source code for `module_name` in the exported package.

        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            src (str): The python source code to save for this package
            is_package (bool, optional): If True, this module is treated as a package. Packages are allowed to have submodules
                (e.g. my_package.my_subpackage.my_subsubpackage), and resources can be saved inside them. Defaults to False.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
            orig_file_name (str, optional): If present, used in logging to identifying where the source came from. Defaults to None.
        """
        self.provided[module_name] = True
        extension = "/__init__.py" if is_package else ".py"
        filename = module_name.replace(".", "/") + extension
        self._write(filename, src)
        if dependencies:
            package = (
                module_name if is_package else module_name.rsplit(".", maxsplit=1)[0]
            )
            dep_pairs = find_files_source_depends_on(src, package)
            dep_list = {}
            for dep_module_name, dep_module_obj in dep_pairs:
                # handle the case where someone did something like `from pack import sub`
                # where `sub` is a submodule. In this case we don't have to save pack, just sub.
                # this ensures we don't pick up additional dependencies on pack.
                # However, in the case where `sub` is not a submodule but an object, then we do have
                # to save pack.
                if dep_module_obj is not None:
                    possible_submodule = f"{dep_module_name}.{dep_module_obj}"
                    if self._module_exists(possible_submodule):
                        dep_list[possible_submodule] = True
                        # we don't need to save `pack`
                        continue
                if self._module_exists(dep_module_name):
                    dep_list[dep_module_name] = True

            for dep in dep_list.keys():
                self.debug_deps.append((module_name, dep))

            if self.verbose:
                dep_str = "".join(f"  {dep}\n" for dep in dep_list.keys())
                file_info = (
                    f"(from file {orig_file_name}) "
                    if orig_file_name is not None
                    else ""
                )
                print(f"{module_name} {file_info}depends on:\n{dep_str}\n")

            for dep in dep_list.keys():
                self.require_module_if_not_provided(dep)

    def _import_module(self, module_name: str):
        try:
            return self.importer.import_module(module_name)
        except ModuleNotFoundError as e:
            if not is_mangled(module_name):
                raise
            msg = (
                f"Module not found: '{module_name}'. Modules imported "
                "from a torch.package cannot be re-exported directly."
            )
            raise ModuleNotFoundError(msg) from None

    def _module_exists(self, module_name: str) -> bool:
        try:
            self._import_module(module_name)
            return True
        except Exception:
            return False

    def _write_dep_graph(self, failing_module=None):
        edges = "\n".join(f'"{f}" -> "{t}";' for f, t in self.debug_deps)
        failing = "" if failing_module is None else f'"{failing_module}" [color=red];'
        template = f"""\
digraph G {{
rankdir = LR;
node [shape=box];
{failing}
{edges}
}}
"""
        arg = quote(template, safe="")
        return f"https://dreampuf.github.io/GraphvizOnline/#{arg}"

    def _get_source_of_module(self, module: types.ModuleType) -> str:
        filename = getattr(module, "__file__", None)
        result = (
            None
            if filename is None or not filename.endswith(".py")
            else linecache.getlines(filename, module.__dict__)
        )
        if result is None:
            extra = ""
            if self.verbose:
                extra = f" See the dependency graph for more info: \n{self._write_dep_graph(module.__name__)}"
            raise ValueError(
                f'cannot save source for module "{module.__name__}" because '
                f'its source file "{filename}" could not be found.{extra}'
            )
        return "".join(result)

    def require_module_if_not_provided(self, module_name: str, dependencies=True):
        if self._module_is_already_provided(module_name):
            return
        self.require_module(module_name, dependencies)

    def require_module(self, module_name: str, dependencies=True):
        """This is called by dependencies resolution when it finds that something in the package
        depends on the module and it is not already present. It then decides how to provide that module.
        The default resolution rules will mark the module as extern if it is part of the standard library,
        and call `save_module` otherwise. Clients can subclass this object
        and override this method to provide other behavior, such as automatically mocking out a whole class
        of modules"""

        root_name = module_name.split(".", maxsplit=1)[0]
        if self._can_implicitly_extern(root_name):
            if self.verbose:
                print(
                    f"implicitly adding {root_name} to external modules "
                    f"since it is part of the standard library and is a dependency."
                )
            self.save_extern_module(root_name)
            return

        for i, (pattern, action, _) in enumerate(self.patterns):
            if pattern.matches(module_name):
                action(module_name)
                self.matched_patterns.add(i)
                return

        self.save_module(module_name, dependencies)

    def save_module(self, module_name: str, dependencies=True):
        """Save the code for `module_name` into the package. Code for the module is resolved using the `importers` path to find the
        module object, and then using its `__file__` attribute to find the source code.
        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        module = self._import_module(module_name)
        source = self._get_source_of_module(module)
        self.save_source_string(
            module_name,
            source,
            hasattr(module, "__path__"),
            dependencies,
            module.__file__,
        )

    def save_pickle(
        self, package: str, resource: str, obj: Any, dependencies: bool = True
    ):
        """Save a python object to the archive using pickle. Equivalent to :func:`torch.save` but saving into
        the archive rather than a stand-alone file. Stanard pickle does not save the code, only the objects.
        If `dependencies` is true, this method will also scan the pickled objects for which modules are required
        to reconstruct them and save the relevant code.

        To be able to save an object where `type(obj).__name__` is `my_module.MyObject`,
        `my_module.MyObject` must resolve to the class of the object according to the `importer` order. When saving objects that
        have previously been packaged, the importer's `import_module` method will need to be present in the `importer` list
        for this to work.

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            obj (Any): The object to save, must be picklable.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        filename = self._filename(package, resource)
        # Write the pickle data for `obj`
        data_buf = io.BytesIO()
        pickler = create_pickler(data_buf, self.importer)
        pickler.persistent_id = self._persistent_id
        pickler.dump(obj)
        data_value = data_buf.getvalue()

        if dependencies:
            all_dependencies = []
            for opcode, arg, pos in pickletools.genops(data_value):
                if opcode.name == "GLOBAL":  # a global reference
                    assert isinstance(arg, str)
                    module, field = arg.split(" ")
                    if module not in all_dependencies:
                        all_dependencies.append(module)

            for dep in all_dependencies:
                self.debug_deps.append((package + "." + resource, dep))

            if self.verbose:
                dep_string = "".join(f"  {dep}\n" for dep in all_dependencies)
                print(f"{resource} depends on:\n{dep_string}\n")

            for module_name in all_dependencies:
                self.require_module_if_not_provided(module_name)

        self._write(filename, data_value)

    def save_text(self, package: str, resource: str, text: str):
        """Save text data to the package

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            text (str): The contents to save
        """
        return self.save_binary(package, resource, text.encode("utf-8"))

    def save_binary(self, package, resource, binary: bytes):
        """Save raw bytes to the package.

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            binary (str): The data to save.
        """
        filename = self._filename(package, resource)
        self._write(filename, binary)

    def mock(
        self,
        include: "GlobPattern",
        *,
        exclude: "GlobPattern" = (),
        allow_empty: bool = True,
    ):
        """Replace some required modules with a mock implementation.  Mocked modules will return a fake
        object for any attribute accessed from it. Because we copy file-by-file, the dependency resolution will sometimes
        find files that are imported by model files but whose functionality is never used
        (e.g. custom serialization code or training helpers).
        Use this function to mock this functionality out without having to modify the original code.

        Args:
            include (Union[List[str], str]): A string e.g. "my_package.my_subpackage", or list of strings
                for the names of the modules to be mocked out. Strings can also be a glob-style pattern
                string that may match multiple modules. Any required dependencies that match this pattern
                string will be mocked out automatically.

                Examples:
                  'torch.**' -- matches torch and all submodules of torch, e.g. 'torch.nn' and torch.nn.functional'
                  'torch.*' -- matches 'torch.nn' or 'torch.functional', but not 'torch.nn.functional'

            exclude (Union[List[str], str]): An optional pattern that excludes some patterns that match the include string.
                e.g. include='torch.**', exclude='torch.foo' will mock all torch packages except 'torch.foo' Default: []

            allow_empty (bool): An optional flag that specifies whether the mock implementation(s) specified by this call
                to the `mock` method must be matched to some module during packaging. If a mock is added with allow_empty=False,
                and `close` is called (either explicitly or via `__exit__`) and the mock has not been matched to a module
                used by the package being exported, an exception is thrown. If allow_empty=True, no such exception is thrown.

        """
        self.patterns.append(
            (_GlobGroup(include, exclude), self.save_mock_module, allow_empty)
        )

    def extern(
        self,
        include: "GlobPattern",
        *,
        exclude: "GlobPattern" = (),
        allow_empty: bool = True,
    ):
        """Include `module` in the list of external modules the package can import.
        This will prevent dependency discover from saving
        it in the package. The importer will load an external module directly from the standard import system.
        Code for extern modules must also exist in the process loading the package.

        Args:
            include (Union[List[str], str]): A string e.g. "my_package.my_subpackage", or list of strings
                for the names of the modules to be externed. This can also be a glob-style pattern, as described in :meth:`mock`

            exclude (Union[List[str], str]): An optional pattern that excludes some patterns that match the include string.

            allow_empty (bool): An optional flag that specifies whether the extern modules specified by this call
                to the `extern` method must be matched to some module during packaging. If an extern module glob pattern is added
                with allow_empty=False, and `close` is called (either explicitly or via `__exit__`) before any modules match that
                pattern, an exception is thrown. If allow_empty=True, no such exception is thrown.

        """
        self.patterns.append(
            (_GlobGroup(include, exclude), self.save_extern_module, allow_empty)
        )

    def deny(self, include: "GlobPattern", *, exclude: "GlobPattern" = ()):
        """Blocklist modules who names match the given glob patterns from the list of modules the package can import.
        If a dependency on any matching packages is found, an error is thrown.

        Args:
            include (Union[List[str], str]): A string e.g. "my_package.my_subpackage", or list of strings
                for the names of the modules to be externed. This can also be a glob-style pattern, as described in :meth:`mock`

            exclude (Union[List[str], str]): An optional pattern that excludes some patterns that match the include string.
        """
        self.patterns.append(
            (_GlobGroup(include, exclude), self._reject_denied_module, True)
        )

    def save_extern_module(self, module_name: str):
        """Add `module_name` to the list of external modules, regardless of whether it is
        required by other modules.

        Prefer using `extern` to only mark modules extern if they are actually required by the packaged code.
        """
        if module_name not in self.external:
            self.external.append(module_name)

    def save_mock_module(self, module_name: str):
        """Add `module_name` to the package, implemented it with a mocked out version that
        can be imported but does not include any implementations.

        Prefer using `mock` to only include this module if it is required by other modules.
        """
        if "_mock" not in self.provided:
            self.save_source_file(
                "_mock", str(Path(__file__).parent / "_mock.py"), dependencies=False
            )
        is_package = hasattr(self._import_module(module_name), "__path__")
        self.save_source_string(module_name, _MOCK_IMPL, is_package, dependencies=False)

    def _reject_denied_module(self, module_name: str):
        """Throw an exception containing a message that `module_name` was explicitly blocklisted via
        `deny` and was still required during packaging.
        """
        raise DeniedModuleError(
            f"{module_name} was required during packaging but has been explicitly blocklisted"
        )

    def _module_is_already_provided(self, qualified_name: str) -> bool:
        for mod in self.external:
            if qualified_name == mod or qualified_name.startswith(mod + "."):
                return True
        return qualified_name in self.provided

    def _persistent_id(self, obj):
        if torch.is_storage(obj):
            storage_type = normalize_storage_type(type(obj))
            obj_key = str(obj._cdata)
            location = location_tag(obj)
            self.serialized_storages[obj_key] = obj

            return ("storage", storage_type, obj_key, location, obj.size())
        if hasattr(obj, "__reduce_package__"):
            return ("reduce_package", *obj.__reduce_package__(self))

        return None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def _write(self, filename, str_or_bytes):
        if is_mangled(filename):
            raise RuntimeError(
                f"Tried to save a torch.package'd module as '{filename}'. "
                "Directly saving torch.package'd modules is not allowed."
            )
        if isinstance(str_or_bytes, str):
            str_or_bytes = str_or_bytes.encode("utf-8")
        self.zip_file.write_record(filename, str_or_bytes, len(str_or_bytes))

    def close(self):
        """Write the package to the filesystem. Any calls after close are now invalid.
        It is preferable to use resource guard syntax instead:

            with PackageExporter("file.zip") as e:
                ...
        """
        if self.verbose:
            print(f"Dependency graph for exported package: \n{self._write_dep_graph()}")

        # Check that all mock and extern modules with allow_empty=False were matched.
        for i, (pattern, _, allow_empty) in enumerate(self.patterns):
            if not allow_empty and i not in self.matched_patterns:
                raise EmptyMatchError(
                    f"Exporter did not match any modules to {pattern}, which was marked as allow_empty=False"
                )

        # Write each tensor to a file named tensor/the_tensor_key in the zip archive
        for key in sorted(self.serialized_storages.keys()):
            name = f".data/{key}.storage"
            storage = self.serialized_storages[key]
            # location information is saved in python, but to actually
            # get the data from non cpu tensors we need to move them over first
            if storage.device.type != "cpu":
                storage = storage.cpu()
            num_bytes = storage.size() * storage.element_size()
            self.zip_file.write_record(name, storage.data_ptr(), num_bytes)
        contents = "\n".join(self.external) + "\n"
        self._write(".data/extern_modules", contents)
        del self.zip_file
        if self.buffer:
            self.buffer.flush()

    def _filename(self, package, resource):
        package_path = package.replace(".", "/")
        resource = _normalize_path(resource)
        return f"{package_path}/{resource}"

    def _can_implicitly_extern(self, module_name: str):
        return module_name == "torch" or (
            module_name not in _DISALLOWED_MODULES and is_stdlib_module(module_name)
        )


# even though these are in the standard library, we do not allow them to be
# automatically externed since they offer a lot of system level access
_DISALLOWED_MODULES = ["sys", "io"]

_MOCK_IMPL = """\
from _mock import MockedObject
def __getattr__(attr: str):
    return MockedObject(__name__ + '.' + attr, _suppress_err=True)
"""


def _read_file(filename: str) -> str:
    with open(filename, "rb") as f:
        b = f.read()
        return b.decode("utf-8")
