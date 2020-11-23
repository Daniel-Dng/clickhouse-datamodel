# from lib.tab_engines import TabEngine
from lib.functions import (query_columns)


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name
        self.table_name = ''

    def add_table(self, table_name):
        self.table_name = table_name
        return self


class Tables:
    # class Columns:
    #     def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
    #                  is_in_partition_key=0, is_in_sampling_key=0):
    #         self.name = name
    #         self.datatype = datatype
    #         self.function = function
    #         self.is_in_sorting_key = is_in_sorting_key
    #         self.is_in_primary_key = is_in_primary_key
    #         self.is_in_partition_key = is_in_partition_key
    #         # self.compression_codec = compression_codec
    #         self.is_in_sampling_key = is_in_sampling_key
    #
    #     # @staticmethod
    #     # def add_func(datatype,):
    #     #     return query_add_func(datatype, function)
    #     # @classmethod
    #     # def add_datatype(cls, datatype, function):
    #     #     type_with_func = query_add_func(datatype, func=function)
    #     #     return cls(datatype=type_with_func)
    #
    #     def to_query(self):
    #         return f"{self.name} {self.datatype}"

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
        return "CREATE TABLE IF NOT EXISTS {}{} " \
               "({}) " \
               "{} ;".format(self.database,
                             self.name,
                             ','.join(self.columns),
                             self.tab_engine)

    def add_columns(self, col, datatype='', function=''):
        if datatype != '':
            self.columns.append(query_columns(col, datatype, function))
        else:
            self.columns.append(col)
        return self

    def add_engine(self, engine_name):
        self.tab_engine = engine_name
        return self

