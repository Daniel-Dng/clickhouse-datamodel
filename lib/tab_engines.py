import pandas as pd
from lib.tab_engines_functions import query_prikey, query_partition_by, query_sample_by, query_settings, query_TTL
from lib.utils import Extractor

sys_tab = Extractor.csv_to_dict2('../data/table_engines.csv').file
print(sys_tab[0])

class TabEngine:
    # attributes = ['engine_name', 'partition_columns', 'other_settings', 'order_columns', 'sample_columns', 'ttl']

    def __init__(self, engine_name, **kwargs):
        self.engine_name = engine_name
        self.partition_columns = kwargs.get('partition_columns')
        self.other_settings = kwargs.get('other_settings')
        self.order_columns = kwargs.get('order_columns')
        self.sample_columns = kwargs.get('sample_columns')
        self.ttl = kwargs.get('ttl')
        # if not isinstance(engine_name, str):
        #     raise TypeError("must be a String of supported Table Engines")
        # else:
        #     if engine_name not in self.sys_tab.keys():
        #         raise KeyError('The input is not a supported Table Engine, which including',
        #                        self.sys_tab.keys())
        self.full_query = f"{self.engine_name}" \
                          f"\n{self.partition_columns}" \
                          f"\n{self.order_columns}" \
                          f"\n{self.sample_columns}" \
                          f"\n{self.ttl}" \
                          f"\n{self.other_settings}"

    # Attributes
    @classmethod
    def to_query(cls,engine_name,_partition_by='',_order_col='',
                 _settings='',_sample_col='',_ttl=''):
        engine_query = f"ENGINE {engine_name}"
        partition_query = query_partition_by(_partition_by)
        other_settings = query_settings(_settings)
        order_query = query_prikey(_order_col)
        sample_query = query_sample_by(_sample_col)
        ttl_query = query_TTL(_ttl)
        return cls(engine_query, partition_columns=partition_query, order_columns=order_query,
                   sample_columns=sample_query, ttl=ttl_query, other_settings=_settings)

# test  = TabEngine.to_query('View',['asdfasd','asdf'],'sadfsad',
#                            _sample_col=['asdf','asdfasd'],_settings='index_granularity=1213').full_query
# print(test)
