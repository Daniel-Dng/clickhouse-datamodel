from lib.tab_engines import TabEngine
from lib.tab_engines_functions import query_prikey


## OBJECTS
# class Databases:
#     attributes = ['name','db_engine']

class Tables:
    attributes = ['name', 'pri_key', 'engine', 'partition_by', 'order_by', 'sample_by', 'settings', 'TTL',
                  'supports_settings', 'supports_skipping_indices', 'supports_sort_order', 'supports_ttl',
                  'supports_replication', 'supports_deduplication']

    def __init__(self, tab_name, pri_key, engine):  # , partition_by, order_by, sample_by, settings, TTL):
        self.tab_name = tab_name
        self.engine = engine
        # self.full_query = ''


class Columns:
    # attributes = ['name', 'data_type', 'nullable', 'codec']
    def __init__(self, full_query):  # name, data_type, nullable, codec):
        self.full_query = full_query

    @classmethod
    def create(cls, self):
        full_query = ''
        if self.nullable == 'NO':
            full_query = full_query + self.name + " " + self.data_type
        else:
            full_query = full_query + self.name + " " + 'Nullable(' + self.data_type + ')'
        return full_query


# print((TabEngine.to_query('ádf', 'MergeTree').full_query).strip())






