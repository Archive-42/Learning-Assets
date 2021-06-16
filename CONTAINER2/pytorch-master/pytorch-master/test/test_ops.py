from functools import partial, wraps, reduce
import warnings

import torch

from torch.testing import \
    (FileCheck, floating_and_complex_types_and)
from torch.testing._internal.common_utils import \
    (TestCase, run_tests, IS_SANDCASTLE, clone_input_helper, make_tensor)
from torch.testing._internal.common_methods_invocations import \
    (op_db, method_tests)
from torch.testing._internal.common_device_type import \
    (instantiate_device_type_tests, ops, onlyCPU, onlyOnCPUAndCUDA, skipCUDAIfRocm, OpDTypes)
from torch.testing._internal.common_jit import JitCommonTestCase, check_against_reference
from torch.autograd.gradcheck import gradcheck, gradgradcheck

from torch.testing._internal.jit_metaprogramming_utils import create_script_fn, create_traced_fn, \
    check_alias_annotation
from torch.testing._internal.jit_utils import disable_autodiff_subgraph_inlining


# Get names of all the operators which have entry in `method_tests` (legacy testing infra)
method_tested_operators = set(map(lambda test_details: test_details[0], method_tests()))

# Tests that apply to all operators

class TestOpInfo(TestCase):
    exact_dtype = True

    # Verifies that ops have their unsupported dtypes
    #   registered correctly by testing that each claimed unsupported dtype
    #   throws a runtime error
    @skipCUDAIfRocm
    @onlyOnCPUAndCUDA
    @ops(op_db, dtypes=OpDTypes.unsupported)
    def test_unsupported_dtypes(self, device, dtype, op):
        # sample_inputs can have a function for generating the input that doesn't work for specified dtype
        # https://github.com/pytorch/pytorch/issues/49024
        with self.assertRaises(RuntimeError):
            samples = op.sample_inputs(device, dtype)
            if len(samples) == 0:
                self.skipTest("Skipped! No sample inputs!")

            # NOTE: only tests on first sample
            sample = samples[0]
            op(*sample.input, *sample.args, **sample.kwargs)

    # Verifies that ops have their supported dtypes
    #   registered correctly by testing that each claimed supported dtype
    #   does NOT throw a runtime error
    @onlyOnCPUAndCUDA
    @ops(op_db, dtypes=OpDTypes.supported)
    def test_supported_dtypes(self, device, dtype, op):
        samples = op.sample_inputs(device, dtype)
        if len(samples) == 0:
            self.skipTest("Skipped! No sample inputs!")

        # NOTE: only tests on first sample
        sample = samples[0]
        op(*sample.input, *sample.args, **sample.kwargs)

    # Verifies that ops do not have an entry in
    # `method_tests` (legacy testing infra).
    @onlyCPU
    @ops(op_db, allowed_dtypes=[torch.float32])
    def test_duplicate_method_tests(self, device, dtype, op):
        self.assertFalse(op.name in method_tested_operators)

# gradcheck requires double precision
_gradcheck_ops = partial(ops, dtypes=OpDTypes.supported,
                         allowed_dtypes=[torch.double, torch.cdouble])


class TestGradients(TestCase):
    exact_dtype = True

    # Copies inputs to inplace operations to avoid inplace modifications
    #   to leaves requiring gradient
    def _get_safe_inplace(self, inplace_variant):
        @wraps(inplace_variant)
        def _fn(t, *args, **kwargs):
            return inplace_variant(t.clone(), *args, **kwargs)

        return _fn

    def _check_helper(self, device, dtype, op, variant, check):
        if variant is None:
            self.skipTest("Skipped! Variant not implemented.")
        if not op.supports_dtype(dtype, torch.device(device).type):
            self.skipTest(f"Skipped! {op.name} does not support dtype {str(dtype)}")

        samples = op.sample_inputs(device, dtype, requires_grad=True)
        for sample in samples:
            if sample.output_process_fn_grad is not None:
                out_fn = sample.output_process_fn_grad

                def variant_out_fn(*args, **kwargs):
                    return out_fn(variant(*args, **kwargs))
            else:
                variant_out_fn = variant

            def fn(*inputs):
                output = variant_out_fn(*inputs, **sample.kwargs)
                return op.output_func(output)

            if check == 'gradcheck':
                self.assertTrue(gradcheck(fn, (*sample.input,) + sample.args,
                                          check_batched_grad=op.check_batched_grad,
                                          check_grad_dtypes=True))
            elif check == 'gradgradcheck':
                self.assertTrue(gradgradcheck(fn, (*sample.input,) + sample.args,
                                              gen_non_contig_grad_outputs=False,
                                              check_batched_grad=op.check_batched_gradgrad,
                                              check_grad_dtypes=True))
                self.assertTrue(gradgradcheck(fn, (*sample.input,) + sample.args,
                                              gen_non_contig_grad_outputs=True,
                                              check_batched_grad=op.check_batched_gradgrad,
                                              check_grad_dtypes=True))
            else:
                self.assertTrue(False, msg="Unknown check requested!")

    def _grad_test_helper(self, device, dtype, op, variant):
        return self._check_helper(device, dtype, op, variant, 'gradcheck')

    def _gradgrad_test_helper(self, device, dtype, op, variant):
        return self._check_helper(device, dtype, op, variant, 'gradgradcheck')

    def _skip_helper(self, op, dtype):
        if not op.supports_autograd:
            self.skipTest("Skipped! autograd not supported")
        if not op.test_complex_grad and dtype.is_complex:
            self.skipTest("Skipped! complex grad tests marked to skip.")

    # Tests that gradients are computed correctly
    @_gradcheck_ops(op_db)
    def test_fn_grad(self, device, dtype, op):
        self._skip_helper(op, dtype)
        self._grad_test_helper(device, dtype, op, op.get_op())

    # Method grad (and gradgrad, see below) tests are disabled since they're
    #   costly and redundant with function grad (and gradgad) tests
    # @_gradcheck_ops(op_db)
    # def test_method_grad(self, device, dtype, op):
    #     self._skip_helper(op, dtype)
    #     self._grad_test_helper(device, dtype, op, op.get_method())

    @_gradcheck_ops(op_db)
    def test_inplace_grad(self, device, dtype, op):
        self._skip_helper(op, dtype)
        if not op.test_inplace_grad:
            self.skipTest("Skipped! Inplace gradcheck marked to skip.")
        self._grad_test_helper(device, dtype, op, self._get_safe_inplace(op.get_inplace()))

    # Test that gradients of gradients are computed correctly
    @_gradcheck_ops(op_db)
    def test_fn_gradgrad(self, device, dtype, op):
        self._skip_helper(op, dtype)
        self._gradgrad_test_helper(device, dtype, op, op.get_op())

    # Method gradgrad (and grad, see above) tests are disabled since they're
    #   costly and redundant with function gradgrad (and grad) tests
    # @_gradcheck_ops(op_db)
    # def test_method_gradgrad(self, device, dtype, op):
    #     self._skip_helper(op, dtype)
    #     self._gradgrad_test_helper(device, dtype, op, op.get_method())

    @_gradcheck_ops(op_db)
    def test_inplace_gradgrad(self, device, dtype, op):
        self._skip_helper(op, dtype)
        if not op.test_inplace_grad:
            self.skipTest("Skipped! Inplace gradgradcheck marked to skip.")
        self._gradgrad_test_helper(device, dtype, op, self._get_safe_inplace(op.get_inplace()))


# Tests operators for consistency between JIT and eager, also checks
#   correctness of JIT specific alias schemas and intended
#   autodifferentiation behavior.
# Inherits from JitCommonTestCase instead of TestCase directly to share
#   functionality with original test_jit.py method operator tests
class TestCommon(JitCommonTestCase):
    exact_dtype = True

    # Compares variant's backward
    # NOTE: verifies it fails when the forward fails
    def check_variant_backward(self, input, forward_result, expected_grad, expected_exception):
        variant_exception_during_backwards = False
        try:
            forward_result.sum().backward()
            variant_grad = input.grad
            input.grad = None
        except Exception as e:
            if not expected_exception:
                self.fail("Unexpected exception during backwards!")
            variant_exception_during_backwards = True

        if expected_exception != variant_exception_during_backwards:
            self.fail("Unexpected success during backwards!")

        if not expected_exception:
            self.assertEqual(variant_grad, expected_grad)

    # Tests that the forward and backward passes of operations produce the
    #   same values for the cross-product of op variants (method, inplace)
    #   against eager's gold standard op function variant
    @ops(op_db)
    def test_variant_consistency_eager(self, device, dtype, op):
        test_backward = op.supports_autograd and (op.test_complex_grad or not dtype.is_complex)
        samples = op.sample_inputs(device, dtype, requires_grad=test_backward)
        if len(samples) == 0:
            self.skipTest("Skipped! No sample inputs!")

        for sample in samples:
            # Acquires variants to test
            method = op.get_method()
            inplace = op.get_inplace()
            inplace_ops = [inplace, ]  # list of all inplace ops: inplace variant + alias inplace variants if exist
            aliases = []
            for a_op in op.aliases:
                aliases.append(a_op.op)
                aliases.append(a_op.method_variant)
                aliases.append(a_op.inplace_variant)
                inplace_ops.append(a_op.inplace_variant)
            aliases = tuple(aliases)

            inplace_ops = tuple(v for v in inplace_ops if v is not None)
            variants = (v for v in (method, inplace) + aliases if v is not None)
            # Computes expected forward

            # below calls op's function variant
            expected_forward = op(*sample.input, *sample.args, **sample.kwargs)

            # Computes expected backward
            # NOTE: backward may fail for some dtypes
            exception_during_backwards = False
            expected_grad = None
            try:
                expected_forward.sum().backward()
                expected_grad = sample.input.grad
                sample.input.grad = None
            except Exception as e:
                exception_during_backwards = True

            # Test eager consistency
            for variant in variants:
                # Verifies that inplace operations that promote int->float fail
                #   on tensors with integer dtypes.
                if (variant in inplace_ops and not torch.can_cast(expected_forward.dtype, dtype)):
                    try:
                        variant_forward = variant(*(clone_input_helper(input) for input in sample.input),
                                                  *sample.args,
                                                  **sample.kwargs)
                    except Exception as e:
                        continue
                    self.fail("Inplace operation on integer tensor that should be promoted to float didn't fail!")
                # Compares variant's forward
                # Note: copy the tensor-type inputs when testing inplace operation
                variant_forward = variant(*(clone_input_helper(input) if variant in inplace_ops else input
                                            for input in sample.input),
                                          *sample.args,
                                          **sample.kwargs)
                self.assertEqual(variant_forward, expected_forward)

                # Compares variant's backward
                if test_backward and (variant not in inplace_ops or op.test_inplace_grad):
                    self.check_variant_backward(sample.input, variant_forward,
                                                expected_grad, exception_during_backwards)

    # Tests that the forward and backward passes of operations produce the
    #   same values for the cross-product of op variants (function, method, inplace)
    #   and runtimes (eager, traced, scripted).
    # TODO WARNING: inplace x {traced, scripted} not currently tested
    @ops(op_db)
    def test_variant_consistency_jit(self, device, dtype, op):
        test_backward = op.supports_autograd and (
            (dtype.is_complex and op.test_complex_grad) or
            (dtype.is_floating_point and (not op.skip_bfloat16_grad or dtype != torch.bfloat16)))

        samples = op.sample_inputs(device, dtype, requires_grad=test_backward)
        if len(samples) == 0:
            self.skipTest("Skipped! No sample inputs!")

        for sample in samples:

            # Acquires variants to test
            func = op.get_op()
            method = op.get_method()
            inplace = op.get_inplace()
            variants = {
                'function': func, 'method': method,
                # TODO: inplace tests currently fail
                # 'inplace': inplace,
            }

            # Test traced and scripted consistency
            for func_type, variant in variants.items():
                if variant is None:
                    continue

                # Create accessor for script function variant
                name = op.name + '_' if func_type == 'inplace' else op.name

                # run with disable_autodiff_subgraph_inlining(True) to test
                #   autodiff support. Context manager forces the graph to contain
                #   DifferentiableGraph nodes if they are present
                with disable_autodiff_subgraph_inlining():


                    # Check scripted forward, grad, and grad grad
                    script_fn = create_script_fn(self, name, func_type)

                    check_against_reference(self,
                                            script_fn,
                                            func,
                                            op.output_func,
                                            (*sample.input,) + sample.args,
                                            sample.kwargs,
                                            no_grad=not test_backward)

                    # Check traced forward, grad, and grad grad
                    traced_fn = create_traced_fn(self, variant)
                    check_against_reference(self,
                                            traced_fn,
                                            func,
                                            op.output_func,
                                            (*sample.input,) + sample.args,
                                            sample.kwargs,
                                            no_grad=not test_backward)

                    # Check alias annotation schema for correctness (make
                    #   sure inputs that aren't supposed to be modified aren't)
                    # Note: only runs in float32 and int64 because schema isn't affected by dtype,
                    #   so running it on all dtypes is would be excessive
                    if dtype in [torch.float32, torch.int32]:
                        check_alias_annotation(name, (*sample.input,) + sample.args, sample.kwargs,
                                               func_type=func_type, aten_name=op.aten_name)

                    # Check autodifferentiation of nodes for traced and scripted graphs, only need to check once per sample
                    if dtype is torch.float32:
                        # Sandcastle doesn't fuse nodes
                        if IS_SANDCASTLE:
                            # fusible nodes are expected to be found in FusionGroups in the DifferentiableGraphs
                            nonfusible_nodes = op.autodiff_nonfusible_nodes + op.autodiff_fusible_nodes
                            fusible_nodes = []
                        else:
                            nonfusible_nodes = op.autodiff_nonfusible_nodes
                            fusible_nodes = op.autodiff_fusible_nodes

                        self.assertAutodiffNode(traced_fn.last_graph, op.assert_autodiffed, nonfusible_nodes, fusible_nodes)
                        self.assertAutodiffNode(script_fn.last_graph, op.assert_autodiffed, nonfusible_nodes, fusible_nodes)

    @ops([op for op in op_db if op.aliases])
    def test_jit_alias_remapping(self, device, dtype, op):
        samples = op.sample_inputs(device, dtype, requires_grad=True)
        if len(samples) == 0:
            self.skipTest("Skipped! No sample inputs!")

        # NOTE: only tests on first sample
        sample = samples[0]

        # Prepare data for test scripting
        # Below we prepare strings of args/kwargs with and without type annotations.
        # These strings are inserted into function template strings which is then torch scripted.
        # - args string is ["t0", "t1", ...] corresponds to the input tensors required by the op
        # - args_annot_kw is the string for the template function signature, for example,
        # ["t0", "t1", "s0: float", "s1: bool", "max: float = 1.0", "min: float = 0.0"] ->
        #    def fn(t0, t1, s0: float, s1: bool, max: float = 1.0, min: float = 0.0)
        # - args_kw is the string of args/kwargs used to call the op, same as args_annot_kw but
        # without type annotations
        args = [f"t{i}" for i in range(len(sample.input))]
        args_annot_kw = args + \
            [f"s{i}: {type(v).__name__}" for i, v in enumerate(sample.args)] + \
            [f"{k}: {type(v).__name__} = {v}" for k, v in sample.kwargs.items()]
        args_kw = args + \
            [f"s{i}" for i in range(len(sample.args))] + \
            [f"{k}={v}" for k, v in sample.kwargs.items()]

        # Prepare data for test tracing
        sample_args_kwargs = ()
        if len(sample.args) > 0:
            sample_args_kwargs += (sample.args, )
        if len(sample.kwargs) > 0:
            sample_args_kwargs += (sample.kwargs, )

        original_name = op.name
        original_name_inplace = original_name + "_"
        expected_dtype = op(*sample.input, *sample.args, **sample.kwargs).dtype

        for a_op in op.aliases:
            inplace = a_op.inplace_variant
            method_or_inplace = [a_op.inplace_variant, a_op.method_variant]
            variants = (v for v in (a_op.op, a_op.method_variant, a_op.inplace_variant) if v is not None)

            # Test scripting:
            for variant in variants:
                variant_name = variant.__name__
                op_name = original_name_inplace if variant is inplace else original_name

                if variant in method_or_inplace:
                    fn_template = '''
                    def _fn(t0{c}{args_annot_kw}):
                        return t0.{alias_name}({args_kw})
                    '''
                    # remove the first input tensor
                    script = fn_template.format(
                        c=", " if len(args_kw[1:]) > 1 or len(args_annot_kw[1:]) >= 1 else "",
                        args_annot_kw=", ".join(args_annot_kw[1:]),
                        args_kw=", ".join(args_kw[1:]),
                        alias_name=variant_name,
                    )
                else:
                    fn_template = '''
                        def _fn({args_annot_kw}):
                            return variant({args_kw})
                    '''
                    script = fn_template.format(
                        args_annot_kw=", ".join(args_annot_kw),
                        args_kw=", ".join(args_kw),
                    )
                scripted = torch.jit.CompilationUnit(script)._fn

                if (variant is inplace and not torch.can_cast(expected_dtype, dtype)):
                    try:
                        inp = (clone_input_helper(input) for input in sample.input)
                        scripted(*inp, *sample.args, **sample.kwargs)
                    except Exception as e:
                        continue
                    self.fail("Inplace operation on integer tensor that should be promoted to float didn't fail!")

                inp = (clone_input_helper(input) for input in sample.input)
                scripted(*inp, *sample.args, **sample.kwargs)
                inp = (clone_input_helper(input) for input in sample.input)
                graph = scripted.graph_for(*inp, *sample.args, **sample.kwargs)
                FileCheck().check(op.aten_name).check_not(variant_name).run(graph)

            # Test tracing:
            for variant in variants:
                variant_name = variant.__name__
                op_name = original_name_inplace if variant is inplace else original_name

                def _fn(*sample_args, **sample_kwargs):
                    return variant(*sample_args, **sample_kwargs)

                inp = (*(clone_input_helper(input) for input in sample.input), ) + sample_args_kwargs
                traced = torch.jit.trace(_fn, *inp)
                inp = (*(clone_input_helper(input) for input in sample.input), ) + sample_args_kwargs
                traced(*inp)
                inp = (*(clone_input_helper(input) for input in sample.input), ) + sample_args_kwargs
                graph = traced.graph_for(*inp)
                FileCheck().check(op_name).check_not(variant_name).run(graph)

    # Validates ops implement the correct out= behavior
    # See https://github.com/pytorch/pytorch/wiki/Developer-FAQ#how-does-out-work-in-pytorch
    #   for a description of the correct behavior
    # TODO: operations that support out= but don't support float
    #   are not covered by this test.
    @ops(op_db, allowed_dtypes=(torch.float,))
    def test_out(self, device, dtype, op):
        # TODO: verify the op doesn't support the out= kwarg
        if not op.supports_out:
            self.skipTest("Skipped! Op doesn't support out= kwarg.")

        # NOTE: only tests on first sample
        samples = op.sample_inputs(device, dtype)
        sample = samples[0]

        # calls it normally to get the expected result
        expected = op(*sample.input, *sample.args, **sample.kwargs)
        op_out = partial(op, *sample.input, *sample.args, **sample.kwargs)

        # Short-circuits if output is not a single tensor or an
        #   iterable of tensors

        # Returns True if iterable is an iterable of tensors (includes empty iterables)
        #   and False o.w.
        def _is_iterable_of_tensors(iterable):
            try:
                for t in iter(iterable):
                    if not isinstance(t, torch.Tensor):
                        return False
            except TypeError as te:
                return False

            return True

        if not isinstance(expected, torch.Tensor) and not _is_iterable_of_tensors(expected):
            self.skipTest("Skipped! Only supports single tensor or iterable of tensor outputs.")

        # A wrapper around map that works with single tensors and always
        #   instantiates the map. Used below to apply transforms to
        #   single tensor and iterable tensor outputs.
        def _apply_out_transform(fn, out):
            if isinstance(out, torch.Tensor):
                return fn(out)

            # assumes (see above) that out is an iterable of tensors
            return tuple(map(fn, out))

        # Case 0: out= with the correct shape, dtype, and device
        #   but NaN values for floating point and complex tensors, and
        #   maximum values for integer tensors.
        #   Expected behavior: out= values have no effect on the computation.
        def _case_zero_transform(t):
            try:
                info = torch.iinfo(t.dtype)
                return torch.full_like(t, info.max)
            except TypeError as te:
                # for non-integer types fills with NaN
                return torch.full_like(t, float('nan'))

        out = _apply_out_transform(_case_zero_transform, expected)
        op_out(out=out)
        self.assertEqual(expected, out)

        # Case 1: out= with the correct shape, dtype, and device,
        #   but noncontiguous.
        #   Expected behavior: strides are respected.
        def _case_one_transform(t):
            return make_tensor(t.shape,
                               dtype=t.dtype,
                               device=t.device,
                               discontiguous=True)

        # Extracts strides from a tensor or iterable of tensors into a tuple
        def _extract_strides(out):
            if isinstance(out, torch.Tensor):
                return (out.stride(),)

            # assumes (see above) that out is an iterable of tensors
            return tuple(map(lambda t: t.stride(), out))

        out = _apply_out_transform(_case_one_transform, expected)
        original_strides = _extract_strides(out)

        op_out(out=out)
        final_strides = _extract_strides(out)

        self.assertEqual(expected, out)
        self.assertEqual(original_strides, final_strides)

        # Case 2: out= with the correct dtype and device, but the wrong shape
        #   Expected behavior: resize with a warning.
        def _case_two_transform(t):
            wrong_shape = list(t.shape)

            if len(wrong_shape) == 0:
                # Handles scalar tensor case (empty list)
                wrong_shape = [2]
            else:
                wrong_shape[-1] = wrong_shape[-1] + 1
            return make_tensor(wrong_shape, dtype=t.dtype, device=t.device)

        out = _apply_out_transform(_case_two_transform, expected)
        with self.assertWarnsRegex(UserWarning, "An output with one or more elements"):
            op_out(out=out)
        self.assertEqual(expected, out)

        # Case 3: out= with the correct dtype and device, but an empty
        #   tensor.
        #   Expected behavior: resize without warning.
        def _case_three_transform(t):
            return make_tensor((0,),
                               dtype=t.dtype,
                               device=t.device)

        out = _apply_out_transform(_case_three_transform, expected)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            op_out(out=out)

        # Verifies no warning is a resize warning
        for w in caught:
            if "An output with one or more elements" in str(w.message):
                self.fail("Resizing an out= argument with no elements threw a resize warning!")

        self.assertEqual(expected, out)

        # Case 4: out= with correct shape and dtype, but wrong device.
        wrong_device = None
        if torch.device(device).type != 'cpu':
            wrong_device = 'cpu'
        elif torch.cuda.is_available():
            wrong_device = 'cuda'

        if wrong_device is not None:
            def _case_four_transform(t):
                return make_tensor(t.shape, dtype=t.dtype, device=wrong_device)

            out = _apply_out_transform(_case_four_transform, expected)
            with self.assertRaises(RuntimeError):
                op_out(out=out)

        # Case 5: out= with correct shape and device, but a dtype
        #   that output cannot be "safely" cast to (long).
        #   Expected behavior: error.
        # NOTE: this case is filtered by dtype since some ops produce
        #   bool tensors, for example, which can be safely cast to any
        #   dtype. It is applied when single tensors are floating point or complex
        #   dtypes, or if an op returns multiple tensors when at least one such
        #   tensor is a floating point or complex dtype.
        _dtypes = floating_and_complex_types_and(torch.float16, torch.bfloat16)
        if (isinstance(expected, torch.Tensor) and expected.dtype in _dtypes or
                (not isinstance(expected, torch.Tensor) and
                 reduce(lambda cur, t: cur or t.dtype in _dtypes, expected, False))):
            def _case_five_transform(t):
                return make_tensor(t.shape, dtype=torch.long, device=t.device)

            out = out = _apply_out_transform(_case_five_transform, expected)
            with self.assertRaises(RuntimeError):
                op_out(out=out)


instantiate_device_type_tests(TestOpInfo, globals())
instantiate_device_type_tests(TestGradients, globals())
instantiate_device_type_tests(TestCommon, globals())

if __name__ == '__main__':
    run_tests()
