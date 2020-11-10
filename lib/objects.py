
from ..lib.tab_engines_functions import *
from ..data.tab_engines import *

## OBJECTS
# class Databases:
#     attributes = ['name','db_engine']

class Tables:
    attributes = ['name', 'pri_key', 'engine', 'partition_by', 'order_by', 'sample_by', 'settings', 'TTL',
                  'supports_settings','supports_skipping_indices','supports_sort_order','supports_ttl',
                  'supports_replication','supports_deduplication']
    def __init__(self,tab_name, pri_key, engine, partition_by, order_by, sample_by, settings, TTL,
                 supports_settings):
        self.tab_name = tab_name
        self.engine = engine
        self.supports_settings = supports_settings
        self.pri_key = pri_key
        self.partition_by = partition_by
        self.order_by = order_by
        self.sample_by = sample_by
        self.settings = settings
        self.TTL = TTL


class Columns:
    attributes = ['name', 'data_type', 'nullable','codec']

    def __init__(self, name, data_type, nullable,codec):
        self.name = name
        self.data_type = data_type
        self.nullable = nullable
        self.codec = codec

    def to_query(self):
        _string = ''
        if self.nullable == 'NO':
            _string = _string + self.name + " " + self.data_type
        #             print(self.name , self.data_type)
        else:
            _string = _string + self.name + " " + 'Nullable(' + self.data_type + ')'
        #             print(self.name , 'Nullable(', self.data_type +')')
        return _string
