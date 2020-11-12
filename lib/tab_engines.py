import pandas as pd
from lib.functions import query_prikey, query_partition_by, query_sample_by, query_settings, query_TTL
from lib.utils import Extractor

# sys_tab = Extractor.csv_to_dict2('../data/table_engines.csv').file
# print(sys_tab[0])

class TabEngine:
    # attributes = ['engine_name', 'partition_columns', 'other_settings', 'order_columns', 'sample_columns', 'ttl']

    def __init__(self, engine_name, **kwargs):
        self.engine_name = engine_name
        # if not isinstance(engine_name, str):
        #     raise TypeError("must be a String of supported Table Engines")
        # else:
        #     if engine_name not in self.sys_tab.keys():
        #         raise KeyError('The input is not a supported Table Engine, which including',
        #                        self.sys_tab.keys())


    # Attributes


# test  = TabEngine.to_query('View',['asdfasd','asdf'],'sadfsad',_settings='index_granularity=1213').full_query
# print(test)
