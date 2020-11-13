import pandas as pd
from lib.functions import query_prikey, query_partition_by, query_sample_by, query_settings, query_TTL,query_order_by
from lib.utils import Extractor

# sys_tab = Extractor.csv_to_dict2('../data/table_engines.csv').file
# print(sys_tab[0])
class TabEngine():
    # attributes = ['engine_name', 'partition_columns', 'other_settings', 'order_columns', 'sample_columns', 'ttl']
    def __init__(self, engine_name, **kwargs):
        self.engine_name = engine_name
        # self.full_query = self.add_tab_engine(engine_name)
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
    def add_tab_engine(cls,engine_name):
        return cls(engine_name)


test =(TabEngine.add_tab_engine('asdf'))
print(test.add_partition('asdf') , test.add_order('asdfsd'))
# test  = TabEngine.to_query('View',['asdfasd','asdf'],'sadfsad',_settings='index_granularity=1213').full_query
# print(test)






