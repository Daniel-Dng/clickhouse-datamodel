import pandas as pd
from lib.functions import query_prikey, query_partition_by, query_sample_by, query_settings, query_TTL

sys_tab = pd.read_csv('../data/table_engines.csv', index_col='name').T.to_dict()
# print(sys_tab_dict)
if __name__ == '__main__':
    class TabEngine:
        def __init__(self, engine_name, partition_columns):
            self.engine_name = engine_name
            self.partition_columns = partition_columns
            # Attributes
            self.supports_settings = sys_tab[self.engine_name]['supports_settings']
            self.supports_skipping_indices = sys_tab[self.engine_name]['supports_skipping_indices']
            self.supports_sort_order = sys_tab[self.engine_name]['supports_sort_order']
            self.supports_ttl = sys_tab[self.engine_name]['supports_ttl']
            self.supports_replication = sys_tab[self.engine_name]['supports_replication']
            self.supports_deduplication = sys_tab[self.engine_name]['supports_deduplication']

        @staticmethod
        def support_order(engine_name):
            if sys_tab[engine_name]['supports_sort_order'] == 1:
                return True
            else:
                return False
        @staticmethod
        def support_settings(engine_name):
            if sys_tab[engine_name]['supports_settings'] == 1:
                return True
            else:
                return False
        # @classmethod
        # def check_support(cls,engine_name,partition_columns):
        #     part1 = "ENGINE " + engine_name
        #     part2 = query_partition_by(partition_columns)
        #     return cls(part1, part2)
        #
        # @staticmethod
        # def to_string_query(partition_columns):
        #     return query_partition_by(partition_columns)


    test = TabEngine('MergeTree',['asdf','sadsd'])
    print(test.full_query())
    if (TabEngine.support_order('MergeTree')) == True:
        print('sadf')
    # print('test1', test.full_query())
    # test2 = TabEngine.to_query('MergeTree',['asdf','sadsd'])
    # test2.full_query()
    # print(TabEngine.to_string_query('asdds'))
