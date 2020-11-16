# from lib.tab_engines import TabEngine
# import pandas as pd
from lib.functions import (query_TTL, query_prikey, query_settings,
                           query_sample_by, query_partition_by, query_add_func,
                           query_order_by, query_columns)
from lib.utils import Extractor


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name


class Tables:
    class Columns:
        def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
                     is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
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

        def to_query(self):
            return f"{self.name} {self.datatype}"

    # class TabEngine:
    #     sys_dict = Extractor.txt_to_dict('assets', 'table_engines.txt').file
    #     def __init__(self, engine_name):
    #         self.engine_name = engine_name
    #         self.full_query = f"{engine_name} "
    #         self.order_col = ''
    #         self.partition_col = ''
    #         self.primary_col = ''
    #         self.sample_col = ''
    #         self.ttl = ''
    #         self.settings = ''
    #
    #     def __str__(self):
    #         return f"ENGINE {self.engine_name} " \
    #                f"{self.order_col} " \
    #                f"{self.partition_col} " \
    #                f"{self.primary_col} " \
    #                f"{self.sample_col} " \
    #                f"{self.sample_col} " \
    #                f"{self.settings} "
    #
    #     # @staticmethod
    #     #     sys_tab[self.engine_name]['supports_sort_order']
    #     # def check_condition(condition):
    #     #     if condition == 1:
    #     #         return 1
    #     #     else:
    #     #         return 0
    #
    #     def add_order(self, col):
    #         if self.sys_dict[self.engine_name]['supports_sort_order'] == '1':
    #             self.order_col = query_order_by(col)
    #         else:
    #             raise ValueError('Table Engine does not support sort order')
    #
    #     # @staticmethod
    #     def add_partition(self, col):
    #         if 'MergeTree' in self.engine_name:
    #             self.partition_col = query_partition_by(col)
    #
    #     # @staticmethod
    #     def add_settings(self, setting):
    #         if self.sys_dict[self.engine_name]['supports_settings'] == '1':
    #             self.order_col = query_settings(setting)
    #         else:
    #             raise ValueError('Table Engine does not support settings')
    #
    #     def add_sample(self, col):
    #         self.sample_col = query_sample_by(col)
    #
    #     def add_ttl(self, col):
    #         if self.sys_dict[self.engine_name]['supports_ttl'] == '1':
    #             self.ttl = query_TTL(col)
    #         else:
    #             raise ValueError('Table Engine does not support settings')

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

    def add_columns(self, col, datatype, function=''):
        self.columns.append(query_columns(col, datatype, function))
        return self

    def add_engine(self, engine_name):
        self.tab_engine = engine_name
        return self


# class Prikey(Tables.Columns):
#     def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
#                  is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
#         super().__init__(name, datatype, function, 1, 1,
#                          is_in_partition_key, compression_codec, is_in_sampling_key)


