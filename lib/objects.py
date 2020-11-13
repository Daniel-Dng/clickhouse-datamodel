# from lib.tab_engines import TabEngine

from lib.functions import query_TTL, query_prikey, query_settings, query_sample_by, query_partition_by, query_add_func, \
    query_order_by, query_columns


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name


class Tables:
    class Columns:
        def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
                     is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
            # super().__init__(self, name, database='', tab_engine='', columns='')
            self.name = name
            self.datatype = datatype
            self.function = function
            self.is_in_sorting_key = is_in_sorting_key
            self.is_in_primary_key = is_in_primary_key
            self.is_in_partition_key = is_in_partition_key
            self.compression_codec = compression_codec
            self.is_in_sampling_key = is_in_sampling_key
            # self.full_query = f"{self.name} {self.datatype}"

        # @staticmethod
        # def add_func(datatype,):
        #     return query_add_func(datatype, function)
        # @classmethod
        # def add_datatype(cls, datatype, function):
        #     type_with_func = query_add_func(datatype, func=function)
        #     return cls(datatype=type_with_func)
        @staticmethod
        def check_condition(condition):
            if condition == 1:
                return 1
            else:
                return 0

        def to_query(self):
            return f"{self.name} {self.datatype}"

    class TabEngine:
        # attributes = ['engine_name', 'partition_columns', 'other_settings', 'order_columns', 'sample_columns', 'ttl']
        def __init__(self, engine_name, **kwargs):
            self.engine_name = engine_name
            self.full_query = f"{engine_name} "

        @staticmethod
        def add_order(col):
            return query_order_by(col)

        @staticmethod
        def add_partition(col):
            return query_partition_by(col)

        @staticmethod
        def add_settings(setting):
            return query_settings(setting)

        @staticmethod
        def add_sample(col):
            return query_sample_by(col)

        @staticmethod
        def add_ttl(col):
            return query_TTL(col)

        @classmethod
        def tab_engine_query(cls, engine_name):
            engine_name = f"ENGINE {engine_name}"
            return cls(engine_name)

    def __init__(self, name, database='', tab_engine='', **kwargs):
        self.tab_engine = tab_engine
        self.name = name
        if database != '':
            self.database = database + '.'
        else:
            self.database = database
        self.columns = list()
        self.partition_columns = kwargs.get('partition_columns')
        self.other_settings = kwargs.get('other_settings')
        self.order_columns = kwargs.get('order_columns')
        self.sample_columns = kwargs.get('sample_columns')
        self.ttl = kwargs.get('ttl')

    def __str__(self):
        return "CREATE TABLE IF NOT EXISTS {} " \
               "({}) " \
               "{} ;".format(self.database,
                             self.name,
                             ','.join(self.columns),
                             self.tab_engine)

    def add_columns(self, col, type, function=''):
        self.columns.append(query_columns(col, type, function))

    # def to_query(self):
    #     full_query =''
    #     for x in self.columns:
    #         _query_col = f"{self.columns} {self.Columns.to_query()}"
    #         full_query = full_query + _query_col
    #     return _query_col


class Prikey(Tables.Columns):
    def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
                 is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
        super().__init__(name, datatype, function, 1, 1,
                         is_in_partition_key, compression_codec, is_in_sampling_key)
