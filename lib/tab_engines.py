import pandas as pd
from lib.functions import query_prikey, query_partition_by, query_sample_by, query_settings, query_TTL,query_order_by
from lib.utils import Extractor
from lib.objects import Tables


class TabEngine(Tables):
    sys_dict = Extractor.txt_to_dict('assets', 'table_engines.txt').file ## system tables from ClickHouse
    def __init__(self, engine_name):
        self.engine_name = engine_name
        self.full_query = f"{engine_name} "
        self.order_col = ''
        self.partition_col = ''
        self.primary_col = ''
        self.sample_col = ''
        self.ttl = ''
        self.settings = ''

    def __str__(self):
        return f"ENGINE {self.engine_name} " \
               f"{self.order_col} " \
               f"{self.partition_col} " \
               f"{self.primary_col} " \
               f"{self.sample_col} " \
               f"{self.sample_col} " \
               f"{self.settings} " \
               f"{self.ttl}"

    # @staticmethod
    #     sys_tab[self.engine_name]['supports_sort_order']
    # def check_condition(condition):
    #     if condition == 1:
    #         return 1
    #     else:
    #         return 0

    def add_order(self, col):
        if self.sys_dict[self.engine_name]['supports_sort_order'] == '1':
            self.order_col = query_order_by(col)
        else:
            raise ValueError('Table Engine does not support sort order')
        return self


    # @staticmethod
    def add_partition(self, col):
        if 'MergeTree' in self.engine_name:
            self.partition_col = query_partition_by(col)
        return self

    # @staticmethod
    def add_settings(self, setting):
        if self.sys_dict[self.engine_name]['supports_settings'] == '1':
            self.order_col = query_settings(setting)
        else:
            raise ValueError('Table Engine does not support settings')
        return self


    def add_sample(self, col):
        self.sample_col = query_sample_by(col)
        return self


    def add_ttl(self, col):
        if self.sys_dict[self.engine_name]['supports_ttl'] == '1':
            self.ttl = query_TTL(col)
        else:
            raise ValueError('Table Engine does not support settings')
        return self


