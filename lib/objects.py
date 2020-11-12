# from lib.tab_engines import TabEngine


from lib.functions import query_TTL, query_prikey, query_settings, query_sample_by, query_partition_by, query_add_func, \
    query_order_by


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name


class Tables:
    def __init__(self, name, database='', tab_engine, columns, **kwargs):
        self.tab_engine = tab_engine
        self.name = name
        self.db = database
        self.columns = columns
        self.partition_columns = kwargs.get('partition_columns')
        self.other_settings = kwargs.get('other_settings')
        self.order_columns = kwargs.get('order_columns')
        self.sample_columns = kwargs.get('sample_columns')
        self.ttl = kwargs.get('ttl')
        self.full_query = f"{self.columns}" \
                          f"{self.tab_engine}" \
                          f"\n{self.partition_columns}" \
                          f"\n{self.order_columns}" \
                          f"\n{self.sample_columns}" \
                          f"\n{self.ttl}" \
                          f"\n{self.other_settings}"
        self.column_query =

    @classmethod
    def to_create(cls, engine_name, _partition_by='', _order_col='',
                  _settings='', _sample_col='', _ttl=''):

        engine_query = f"ENGINE {engine_name}"
        partition_query = query_partition_by(_partition_by)
        other_settings = query_settings(_settings)
        order_query = query_prikey(_order_col)
        sample_query = query_sample_by(_sample_col)
        ttl_query = query_TTL(_ttl)
        return cls(tab_engine=engine_query, partition_columns=partition_query, order_columns=order_query,
                   sample_columns=sample_query, ttl=ttl_query, other_settings=other_settings)
    def create(self):
        return f"CREATE TABLE {self.database}.{self.name} ({self.columns}) {self.tab_engine} ;"

class Columns:
    def __init__(self, name, datatype, function='', is_in_sorting_key=0, is_in_primary_key=0,
                 is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
        self.name = name
        self.datatype = datatype
        self.function = function
        self.is_in_sorting_key = is_in_sorting_key
        self.is_in_primary_key = is_in_primary_key
        self.is_in_partition_key = is_in_partition_key
        self.compression_codec = compression_codec
        self.is_in_sampling_key = is_in_sampling_key
        self.full_query = f"{self.name} {self.datatype}"
    # @staticmethod
    # def add_func(datatype,):
    #     return query_add_func(datatype, function)
    # @classmethod
    # def add_datatype(cls, datatype, function):
    #     type_with_func = query_add_func(datatype, func=function)
    #     return cls(datatype=type_with_func)
    def to_query(self):
        _query = ""

class Prikey(Columns):
    def __init__(self, name, datatype='', is_in_sorting_key=0, is_in_primary_key=0,
                 is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
        super().__init__(name, datatype, is_in_sorting_key, 1,
                         is_in_partition_key, compression_codec, is_in_sampling_key)

# class DataType:
#     def __init__(self, datatype):
#         self.datatype = datatype


# if isinstance(x, Pri_key):
#     print('rsasd')

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
