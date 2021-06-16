"""Classes for working with browsercompat resources."""
from __future__ import unicode_literals

from collections import defaultdict, OrderedDict
from difflib import Differ
from itertools import chain
from json import dumps
from logging import getLogger

logger = getLogger('tools.resources')


class Link(object):
    """Proxy for database IDs in a collection."""

    class NoId(object):
        """Placeholder for local objects without an ID."""

    def __init__(self, collection, linked_type, linked_id=None):
        self.collection = collection
        self.linked_type = linked_type
        if linked_id is None:
            self.linked_id = Link.NoId()
        else:
            self.linked_id = linked_id

    def get(self):
        assert self.collection
        return self.collection.get(self.linked_type, self.id)

    @property
    def id(self):
        if self.collection:
            raw_id = self.collection.get_override_id(
                self.linked_type, self.linked_id)
        else:
            raw_id = self.linked_id

        if isinstance(raw_id, Link.NoId):
            return None
        else:
            return raw_id

    def set_collection(self, collection):
        assert (not self.collection) or (self.collection == collection)
        self.collection = collection


class LinkList(object):
    """Proxy for a set of database IDs in a collection."""

    def __init__(self, collection, linked_type, linked_ids):
        self.collection = collection
        self.links = [
            Link(collection, linked_type, lid) for lid in linked_ids]

    @property
    def ids(self):
        return [l.id for l in self.links]

    def set_collection(self, collection):
        assert (not self.collection) or (self.collection == collection)
        self.collection = collection
        for item in self.links:
            item.set_collection(collection)


class Resource(object):
    """A browsercompat resource.

    Derived classes *must* define two class-level attributes:
    _resource_type - the name of the API resource, such as 'browsers'
    _id_data - a tuple of property names (own properties or properties on
        related resources) that would identify a resource if IDs differed.

    Derived classes may define other class-level attributes:
    _writeable_property_fields - a tuple of property names that can be set
        by a client.
    _readonly_property_fields - a tuple of property names that may be on a
        resource but can't / shouldn't be written by a client.
    _writeable_link_fields - a dictionary of link names to the pair
        (linked resource type, True if to-many field), writable by client
    _readonly_link_fields - a dictionary of link names to link properties,
        that can't / shouldn't be written by the client.
    """

    # A writable linked field has many elements where order matters
    # Write order of resource.sorted is:
    # 1) New resource w/o sorted list
    # 2) New sorted
    # 3) Updated resource w/ sorted list
    # 4) Updated sorted
    SORTED = 'SORTED'

    # A writable linked field is an order association (many to many)
    # Write order of resource.sorted is:
    # 1) New sorted
    # 2) New resource w/ sorted list
    # 3) Updated sorted
    # 4) Updated resource w/ sorted list
    SORTED_M2M = 'SORTED_M2M'

    def __init__(self, collection=None, **properties):
        """Initialize a Resource.

        Keyword Arguments:
        -- collection - A collection to associate with this Resource

        Additional keyword arguments will be assigned as fields.
        """
        # Avoid _getattr__ infinite loop
        object.__setattr__(self, '_fields', set())
        object.__setattr__(self, '_property_fields', set())
        object.__setattr__(self, '_link_fields', {})

        self._data = {}
        self._collection = collection

        assert hasattr(self, '_resource_type'), 'Must set _resource_type'
        assert hasattr(self, '_id_data'), 'Must set _id_data'
        assert tuple(sorted(self._id_data)) == tuple(self._id_data), \
            '_id_data must be sorted'

        # Get field definitions, setting to default if not defined
        wprops = getattr(self, '_writeable_property_fields', ())
        self._writeable_property_fields = wprops
        rprops = getattr(self, '_readonly_property_fields', ())
        self._readonly_property_fields = rprops
        wlinks = getattr(self, '_writeable_link_fields', {})
        self._writeable_link_fields = wlinks
        rlinks = getattr(self, '_readonly_link_fields', {})
        self._readonly_link_fields = rlinks

        # Load fields
        for field in chain(wprops, rprops):
            assert field not in self._fields, 'Duplicate field "%s"' % field
            self._fields.add(field)
            self._property_fields.add(field)
        link_fields = chain(
            [('id', (self._resource_type, False))],
            wlinks.items(), rlinks.items())
        for field, attributes in link_fields:
            assert field not in self._fields, 'Duplicate field "%s"' % field
            self._fields.add(field)
            self._link_fields[field] = attributes
        assert self._fields, 'Must set fields'

        # Load properties
        for key, val in properties.items():
            assert key in self._fields
            setattr(self, key, val)

    def __getattr__(self, name):
        """Retrieve resource properties and links."""
        if name in self._fields:
            if self._data:
                return self._data.get(name, None)
            else:
                return None
        raise AttributeError(
            '%r object has no attribute %r' % (self.__class__, name))

    def __setattr__(self, name, value):
        """Set resource properties and links."""
        if name in self._property_fields:
            # Directly assign properties
            self._data[name] = value
        elif name in self._link_fields:
            # Convert to Link or LinkList before assigning links
            resource_type, is_list = self._link_fields[name]
            link_class = LinkList if is_list else Link
            link_value = link_class(self._collection, resource_type, value)
            self._data[name] = link_value
        else:
            object.__setattr__(self, name, value)

    def from_json_api(self, json_api):
        """Load from a JSON API representation.

        Both readable and writable fields are read, and additional items,
        such links, metadata, and unknown fields, are discarded.
        """
        assert self._resource_type in json_api.keys(), 'Unexpected json_api'

        items = chain(
            json_api[self._resource_type].items(),
            json_api[self._resource_type].get('links', {}).items()
        )
        for key, value in items:
            if key in self._fields:
                assert key not in self._data
                setattr(self, key, value)

    def get_data_id(self):
        data_id = [self._resource_type]
        for name in self._id_data:
            # Load properties in related resources
            resource = self
            orig_name = name
            while '.' in name:
                link_name, name = name.split('.', 1)
                assert link_name in resource._link_fields
                link = getattr(resource, link_name)
                resource = self._collection.get(
                    link.linked_type, link.id)
                assert resource, \
                    'When looking up "%s", could not find ID %r in %s.' % (
                        orig_name, link.id, link.linked_type)
            data_item = getattr(resource, name)
            if data_item is None:
                data_id.append('')
            else:
                data_id.append(data_item)
        return tuple(data_id)

    def set_collection(self, collection):
        assert (self._collection is None) or (self._collection == collection)
        self._collection = collection
        for field_name in self._link_fields:
            field = getattr(self, field_name)
            if field:
                field.set_collection(collection)

    def to_json_api(self, with_sorted=True):
        """Export to JSON API representation.

        Only writable properties and links are included.

        Keyword Arguments:
        with_sorted -- If True (default), then writable links representing a
        sort order are included.
        """
        assert self._data, 'No data to export'

        data = OrderedDict()
        for field in self._writeable_property_fields:
            if field in self._data:
                raw_value = self._data[field]
                if hasattr(raw_value, 'keys') and 'en' in raw_value:
                    # Sort languages
                    value = OrderedDict()
                    value['en'] = raw_value['en']
                    for lang in sorted(raw_value.keys()):
                        if lang != 'en':
                            value[lang] = raw_value[lang]
                else:
                    value = raw_value

                data[field] = value
        for field, attr in self._writeable_link_fields.items():
            is_sorted = attr[1] == Resource.SORTED
            if not with_sorted and is_sorted:
                continue
            if field in self._data:
                link = self._data[field]
                if isinstance(link, Link):
                    value = link.id
                else:
                    assert isinstance(link, LinkList)
                    value = link.ids
                data.setdefault('links', {})[field] = value
        return {self._resource_type: data}


class Browser(Resource):
    _resource_type = 'browsers'
    _writeable_property_fields = ('slug', 'name', 'note')
    _writeable_link_fields = {
        'versions': ('versions', Resource.SORTED),
    }
    _readonly_link_fields = {
        'history': ('historical_browsers', True),
        'history_current': ('historical_browsers', False),
    }
    _id_data = ('slug',)


class Version(Resource):
    _resource_type = 'versions'
    _writeable_property_fields = (
        'version', 'release_day', 'retirement_day', 'status',
        'release_notes_uri', 'note')
    _writeable_link_fields = {
        'browser': ('browsers', False),
    }
    _readonly_property_fields = ('order',)
    _readonly_link_fields = {
        'supports': ('supports', True),
        'history': ('historical_versions', True),
        'history_current': ('historical_versions', False),
    }
    _id_data = ('browser.slug', 'version')


class Feature(Resource):
    _resource_type = 'features'
    _writeable_property_fields = (
        'slug', 'mdn_uri', 'experimental', 'standardized', 'stable',
        'obsolete', 'name')
    _writeable_link_fields = {
        'parent': ('features', False),
        # TODO bug 1216786: remove sections
        'sections': ('sections', Resource.SORTED_M2M),
        'references': ('references', Resource.SORTED),
        'children': ('features', Resource.SORTED),
    }
    _readonly_link_fields = {
        'supports': ('supports', True),
        'history': ('historical_features', True),
        'history_current': ('historical_features', False),
    }
    _id_data = ('slug',)


class Reference(Resource):
    _resource_type = 'references'
    _writeable_property_fields = ('note',)
    _writeable_link_fields = {
        'feature': ('features', False),
        'section': ('sections', False),
    }
    _readonly_link_fields = {
        'history': ('historical_references', True),
        'history_current': ('historical_references', False),
    }
    _id_data = (
        'feature.slug', 'section.specification.mdn_key', 'section.subpath_en')


class Support(Resource):
    _resource_type = 'supports'
    _writeable_property_fields = (
        'support', 'prefix', 'prefix_mandatory', 'alternate_name',
        'alternate_mandatory', 'requires_config', 'default_config',
        'protected', 'note')
    _writeable_link_fields = {
        'version': ('versions', False),
        'feature': ('features', False),
    }
    _readonly_link_fields = {
        'history': ('historical_supports', True),
        'history_current': ('historical_supports', False),
    }
    _id_data = ('feature.slug', 'version.browser.slug', 'version.version')


class Specification(Resource):
    _resource_type = 'specifications'
    _writeable_property_fields = ('slug', 'mdn_key', 'name', 'uri')
    _writeable_link_fields = {
        'maturity': ('maturities', False),
        'sections': ('sections', Resource.SORTED),
    }
    _readonly_link_fields = {
        'history': ('historical_specifications', True),
        'history_current': ('historical_specifications', False),
    }
    _id_data = ('mdn_key',)


class Section(Resource):
    _resource_type = 'sections'
    # TODO bug 1216786: remove note
    _writeable_property_fields = ('number', 'name', 'subpath', 'note')
    _writeable_link_fields = {
        'specification': ('specifications', False),
    }
    # TODO bug 1216786: remove features
    _readonly_link_fields = {
        'features': ('features', True),
        'references': ('references', True),
        'history': ('historical_sections', True),
        'history_current': ('historical_sections', False),
    }
    _id_data = ('specification.mdn_key', 'subpath_en')

    @property
    def subpath_en(self):
        if self.subpath is None:
            return None
        return self.subpath.get('en', None)


class Maturity(Resource):
    _resource_type = 'maturities'
    _writeable_property_fields = ('slug', 'name')
    _readonly_link_fields = {
        'specifications': ('specifications', True),
        'history': ('historical_maturities', True),
        'history_current': ('historical_maturities', False)
    }
    _id_data = ('slug',)


class Collection(object):
    """A collection of resources."""

    resource_by_type = {
        'browsers': Browser,
        'versions': Version,
        'features': Feature,
        'references': Reference,
        'supports': Support,
        'sections': Section,
        'specifications': Specification,
        'maturities': Maturity,
    }

    def __init__(self, client=None):
        """Initialize a Collection.

        Keyword Arguments:
        client -- API Client that can read and write resources
        """
        self._repository = {}
        self._override_ids = {}
        self._id_index = {}
        self.client = client

    def add(self, resource):
        """Add a resource to the collection."""
        resource_type = resource._resource_type
        self._repository.setdefault(resource_type, []).append(resource)

        # Set collection
        resource.set_collection(self)

        # Add to ID index
        resources = self._id_index.setdefault(resource_type, {})
        id_link = resource.id
        if id_link:
            resource_id = id_link.id
            assert resource_id not in resources
            resources[resource_id] = resource

    def get(self, resource_type, db_id):
        """Get a resource by database ID."""
        return self._id_index.get(resource_type, {}).get(db_id, None)

    def get_all_by_data_id(self):
        """Get all items with a unique index lookup."""
        indexed = {}
        for resource_type in self._repository.keys():
            indexed.update(self.get_resources_by_data_id(resource_type))
        return indexed

    def get_override_id(self, resource_type, resource_id):
        """Get an overriden resource ID."""
        return self._override_ids.get(
            resource_type, {}).get(resource_id, resource_id)

    def get_resources(self, resource_type):
        """Get all the resources of the resource type."""
        return self._repository.get(resource_type, [])

    def get_resources_by_data_id(self, resource_type):
        """Get a dict mapping a resource by its unique index."""
        resources = {}
        for item in self.get_resources(resource_type):
            data_id = item.get_data_id()
            assert data_id not in resources
            resources[data_id] = item
        return resources

    def filter(self, resource_type, **properties):
        """Get all resources matching the property values."""
        assert properties
        resources = self.get_resources(resource_type)
        matches = []
        for resource in resources:
            match = True
            for name, value in properties.items():
                if name in resource._link_fields:
                    link = getattr(resource, name)
                    if link:
                        match &= (link.id == value)
                    else:
                        match &= (value is None)
                else:
                    match &= (getattr(resource, name) == value)
            if match:
                matches.append(resource)
        return matches

    def load_all(self, resource_type):
        """Read all API data into the collection."""
        assert self.client, 'load_all requires an API Client'
        original_count = len(self._repository.get(resource_type, []))
        response = self.client.get_resource_collection(resource_type)
        resource_class = self.resource_by_type[resource_type]
        for item in response[resource_type]:
            resource = resource_class(collection=self)
            resource.from_json_api({resource_type: item})
            self.add(resource)
        done_count = len(self._repository.get(resource_type, []))
        return done_count - original_count

    def load_collection(self, from_collection):
        """Load data from another collection.

        This is useful for loading an original collection, altering the
        resources, and then syncing the changes back to the original
        collection.
        """
        assert not self.client, "Don't set client when using load_collection."
        assert not self._repository, "Can't load with existing resources"
        for data_id, resource in from_collection.get_all_by_data_id().items():
            json_api = resource.to_json_api()
            if resource.id:
                json_api[resource._resource_type]['id'] = resource.id.id
            new_resource = type(resource)()
            new_resource.from_json_api(json_api)
            self.add(new_resource)

    def override_ids_to_match(self, sync_collection):
        """Change IDs to match another collection."""
        self._override_ids = {}

        # Find all matching items with the other collection
        sync_index = sync_collection.get_all_by_data_id()
        my_index = self.get_all_by_data_id()
        sync_keys = set(sync_index.keys())
        my_keys = set(my_index.keys())
        match_keys = sorted(sync_keys & my_keys)

        # Map IDs in self collection to IDs in sync_collection
        new_ids = {}
        for key in match_keys:
            sync_item = sync_index[key]
            sync_id = sync_item.id.linked_id
            assert sync_id is not None
            self_item = my_index[key]
            if not self_item.id:
                self_item.id = Link(self, self_item._resource_type, None)
                self_item.id.linked_id = self_item.id
            self_id = self_item.id.linked_id
            assert self_id is not None
            resource_type = key[0]
            new_ids.setdefault(resource_type, {})[self_id] = sync_id

        # Update the IDs
        for key, item in my_index.items():
            resource_type = key[0]

            # Update the item ID
            if item.id:
                assert item.id.linked_id is not None
                old_id = item.id.linked_id
                new_id = new_ids.get(resource_type, {}).get(old_id, old_id)
                self._override_ids.setdefault(
                    resource_type, {})[old_id] = new_id

        # Redo ID index
        self._id_index = {}
        for resource_type, resources in self._repository.items():
            self._id_index[resource_type] = {}
            for resource in resources:
                id_link = resource.id
                if id_link:
                    resource_id = id_link.id
                    assert resource_id not in resources
                    self._id_index[resource_type][resource_id] = resource

    def remove(self, resource):
        """Remove a resource from the collection."""
        resource_type = resource._resource_type
        self._repository[resource_type].remove(resource)
        id_link = resource.id
        if id_link:
            resource_id = id_link.id
            del self._id_index[resource_type][resource_id]


class CollectionChangeset(object):
    """Determine changes from one collection to another."""

    def __init__(
            self, original_collection, new_collection, skip_deletes=False):
        """Initialize a CollectionChangeset.

        Keyword Arguments:
        original_collection -- The original Collection
        new_collection -- The new Collection
        client -- A Client that can access the original Collection
        """
        self.original_collection = original_collection
        self.new_collection = new_collection
        self.skip_deletes = skip_deletes
        assert self.original_collection.client, \
            'original_collection must have a client.'

        self.new_collection.override_ids_to_match(self.original_collection)

        self._populate_changes()

    def _populate_changes(self):
        """Populate the changes attribute."""
        orig_index = self.original_collection.get_all_by_data_id()
        my_index = self.new_collection.get_all_by_data_id()
        orig_keys = set(orig_index.keys())
        my_keys = set(my_index.keys())

        self.changes = {
            'new': OrderedDict(),
            'same': OrderedDict(),
            'changed': OrderedDict(),
            'deleted': OrderedDict(),
        }

        def new_resource_keys_with_dependencies(resource, new_keys):
            """
            Select new keys in desired creation order.

            Order is:
            1) Any non-sorted linked resources (i.e., browser before version),
               or sorted M2M linked resources (i.e., sections before feature)
            2) The resource
            3) Any sorted linked resources (i.e., child features after parent)

            As they are ordered, keys are removed from new_keys to avoid double
            creation.
            """
            if not resource:
                return []
            else:
                my_key = resource.get_data_id()
                if my_key not in new_keys:
                    return []
                else:
                    new_keys.remove(my_key)

            pre_links = []
            post_links = []
            for link_name, lmeta in resource._writeable_link_fields.items():
                is_sorted = (lmeta[1] == Resource.SORTED)
                link_attr = getattr(resource, link_name, None)

                if isinstance(link_attr, Link):
                    links = [link_attr]
                elif isinstance(link_attr, LinkList):
                    links = link_attr.links
                else:
                    assert link_attr is None
                    links = []

                for link in links:
                    linked = link.get()
                    link_keys = new_resource_keys_with_dependencies(
                        linked, new_keys)
                    if is_sorted:
                        post_links.extend(link_keys)
                    else:
                        pre_links.extend(link_keys)
            keys = pre_links + [my_key] + post_links
            logger.debug('  DEPS %s -> %s', my_key, keys)
            return keys

        # Handle new items with sort fields
        new_keys = sorted(my_keys - orig_keys)
        for k in new_keys[:]:
            item = my_index[k]
            has_sorted = False
            for _, link_type in item._writeable_link_fields.values():
                if link_type == Resource.SORTED:
                    has_sorted = True
            if has_sorted:
                item_keys = new_resource_keys_with_dependencies(item, new_keys)
                logger.debug('  SORT %s -> %s', item.get_data_id(), item_keys)
                for ik in item_keys:
                    self.changes['new'][ik] = my_index[ik]

        # Sort remaining new items
        for k in new_keys[:]:
            item = my_index[k]
            item_keys = new_resource_keys_with_dependencies(item, new_keys)
            for ik in item_keys:
                self.changes['new'][ik] = my_index[ik]

        # Collect deleted items
        del_keys = orig_keys - my_keys
        for k in sorted(del_keys):
            self.changes['deleted'][k] = orig_index[k]

        # Sort same / changed items
        match_keys = orig_keys & my_keys
        for k in sorted(match_keys):
            orig_item = orig_index[k]
            orig_json = orig_item.to_json_api()
            my_item = my_index[k]
            my_json = my_item.to_json_api()
            if orig_json == my_json:
                self.changes['same'][k] = my_item
            else:
                my_item._original = orig_item
                self.changes['changed'][k] = my_item

    def change_original_collection(self, checkpoint=100):
        """Commit changes to the original Collection.

        Keyword Arguments:
        -- logger_name - The name of the logger that gets progress message
        -- checkpoint - Item count between progress messages

        Return is a dictionary of resource types to a dictionary of actions
        ('new', 'deleted', 'changed') and the counts of those actions.
        """
        client = self.original_collection.client

        logger.info('Opening changeset...')
        client.open_changeset()

        counts = defaultdict(lambda: defaultdict(int))
        try:
            for item in self.changes['new'].values():
                resource_type = item._resource_type
                json_api = item.to_json_api(with_sorted=False)
                response = client.create(
                    resource_type, json_api[resource_type])
                if not item.id:
                    item.id = Link.NoId()
                old_id = item.id.linked_id
                new_id = response['id']
                item._collection._override_ids.setdefault(
                    resource_type, {})[old_id] = new_id
                counts[resource_type]['new'] += 1
                count = counts[resource_type]['new']
                if (count % checkpoint == 0):  # pragma nocover
                    logger.info('Imported %d %s' % (count, resource_type))

            if not self.skip_deletes:
                for item in self.changes['deleted'].values():
                    resource_type = item._resource_type
                    client.delete(resource_type, item.id.id)
                    item._collection.remove(item)
                    counts[resource_type]['deleted'] += 1
                    count = counts[resource_type]['deleted']
                    if (count % checkpoint == 0):  # pragma nocover
                        logger.info('Deleted %d %s' % (count, resource_type))

            for item in self.changes['changed'].values():
                json_api = item.to_json_api()
                resource_type = item._resource_type
                client.update(
                    resource_type, item.id.id, json_api[resource_type])
                counts[resource_type]['changed'] += 1
                count = counts[resource_type]['changed']
                if (count % checkpoint == 0):  # pragma nocover
                    logger.info('Changed %d %s' % (count, resource_type))
        finally:
            logger.info('Closing changeset, updating cache...')
            client.close_changeset()
        return counts

    def summarize(self):
        """Get human-friendly summary of changes."""
        out = []
        client = self.original_collection.client

        # Summarize new resources
        for item in self.changes['new'].values():
            rep = self.format_item(item)
            out.append('New:\n%s' % rep)

        # Summarize deleted resources
        for item in self.changes['deleted'].values():
            url = client.url(item._resource_type, item.id.id)
            rep = self.format_item(item)
            if self.skip_deletes:
                fmt = 'Deleted (but skipped) %s:\n%s'
            else:
                fmt = 'Deleted %s:\n%s'
            out.append(fmt % (url, rep))

        # Summarize changed resources
        for item in self.changes['changed'].values():
            url = client.url(item._resource_type, item.id.id)
            rep = self.format_diff(item)
            out.append('Changed: %s:\n%s' % (url, rep))

        return '\n'.join(out)

    def format_item(self, item):
        """Create human-friendly representation of an item."""
        return dumps(
            item.to_json_api(with_sorted=False),
            indent=2, separators=(',', ': '))

    def format_diff(self, item):
        """Create human-friendly representation of a difference."""
        orig_item = item._original
        orig_json = dumps(
            orig_item.to_json_api(),
            indent=2, separators=(',', ': '))
        new_json = dumps(
            item.to_json_api(),
            indent=2, separators=(',', ': '))
        diff = ''.join(Differ().compare(
            orig_json.splitlines(1), new_json.splitlines(1)))
        return diff
