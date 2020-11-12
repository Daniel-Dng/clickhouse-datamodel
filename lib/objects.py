from lib.tab_engines import TabEngine
from lib.functions import query_prikey


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name


class Tables:
    def __init__(self, name, database, tab_engine):
        self.name = name
        self.db = database
        self.engine = tab_engine


class Columns:
    def __init__(self, name, type, is_in_sorting_key,is_in_primary_key,
                 is_in_partition_key, compression_codec, is_in_sampling_key):
        self.name = name
        self.type = type
        self.is_in_sorting_key = is_in_sorting_key
        self.is_in_primary_key = is_in_primary_key
        self.is_in_partition_key = is_in_partition_key
        self.compression_codec = compression_codec
        self.is_in_sampling_key = is_in_sampling_key





















# class Databases:
#     attributes = ['name','db_engine']
#
# class Tables:
#     attributes = ['name', 'pri_key', 'engine', 'partition_by', 'order_by', 'sample_by', 'settings', 'TTL',
#                   'supports_settings', 'supports_skipping_indices', 'supports_sort_order', 'supports_ttl',
#                   'supports_replication', 'supports_deduplication']
#
#     def __init__(self, tab_name, engine, pri_key):  # , partition_by, order_by, sample_by, settings, TTL):
#         self.tab_name = tab_name
#         self.engine = engine
#         self.pri_key = pri_key
#         # self.full_query = ''
#
#         def
#
# class Columns:
#     # attributes = ['name', 'data_type', 'nullable', 'codec']
#     def __init__(self, full_query):  # name, data_type, nullable, codec):
#         self.full_query = full_query
#
#     @classmethod
#     def create(cls, self):
#         full_query = ''
#         if self.nullable == 'NO':
#             full_query = full_query + self.name + " " + self.data_type
#         else:
#             full_query = full_query + self.name + " " + 'Nullable(' + self.data_type + ')'
#         return full_query


# print((TabEngine.to_query('ádf', 'MergeTree').full_query).strip())






