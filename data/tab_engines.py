import pandas as pd
from lib.tab_engines_functions import query_order_by, query_partition_by, query_sample_by, query_settings, query_TTL

sys_tab = pd.read_csv('table_engines.csv', index_col='name').T.to_dict()

if __name__ == '__main__':
    class TabEngine:
        def __init__(self, engine_name,
                     order_columns='', partition_columns='', other_settings='', **kwargs):
            self.engine_name = engine_name
            self.order_columns = order_columns
            self.partition_columns = partition_columns
            self.other_settings = other_settings
            ## Other optional attributes
            self.sample_columns = kwargs.get('sample_columns')
            self.ttl = kwargs.get('ttl')

            if not isinstance(engine_name, str):
                raise TypeError("must be a String of supported Table Engines")
            else:
                if engine_name not in sys_tab.keys():
                    raise KeyError('The input is not a supported Table Engine, which including',
                                   sys_tab.keys())
            # Attributes
            self.supports_settings = sys_tab[self.engine_name]['supports_settings']
            self.supports_skipping_indices = sys_tab[self.engine_name]['supports_skipping_indices']
            self.supports_sort_order = sys_tab[self.engine_name]['supports_sort_order']
            self.supports_ttl = sys_tab[self.engine_name]['supports_ttl']
            self.supports_replication = sys_tab[self.engine_name]['supports_replication']
            self.supports_deduplication = sys_tab[self.engine_name]['supports_deduplication']
            ## Family of Table Engine
            if 'MergeTree' in self.engine_name:
                self.family = 'MergeTree'
            elif 'Log' in self.engine_name:
                self.family = 'Log'
            elif self.engine_name in ['MySQL', 'ODBC', 'JDBC', 'Kafka', 'HDFS', 'RabbitMQ', 'MongoDB', 'S3', 'COSN']:
                self.family = 'Integration'
            else:
                self.family = 'Special'

        # Conditional Attribute:
        def partition_by(self):
            _query = ''
            if self.partition_columns != '':
                _query = _query + query_partition_by(self.partition_columns)
            return _query

        def order_by(self):
            _query = ''
            if (self.supports_sort_order == 1) & (self.order_columns != ''):
                _query = _query + query_order_by(self.order_columns)
            return _query

        def sample_by(self):
            _query = ''
            if self.sample_columns is not None:
                _query = _query + query_sample_by(self.sample_columns)
            return _query

        def settings(self):
            _query = ''
            if (self.supports_settings == 1) & (self.other_settings != ''):
                _query = _query + query_settings(self.other_settings)
            return _query

        def TTL(self):
            _query = ''
            if self.ttl is not None:
                _query = _query + query_TTL(self.ttl)
            return _query

        # Full Query Compiler Operations
        def to_query(self):
            full_query = f'ENGINE {self.engine_name} {self.order_by()} {self.partition_by()} {self.sample_by()} {self.settings()} {self.TTL()}'
            return full_query

    class MergeTree(TabEngine):
        def __getattr__(self, attr):
            return getattr(self.TabEngine, attr)
        def __init__(self, order_columns, mergetree_type, TabEngine, **kwargs):
            self.mergetree_type = mergetree_type
            self.TabEngine = TabEngine
            # if 'MergeTree' in self.mergetree_type:
            #     super(MergeTree, self).__init__(self.mergetree_type)
            # else:
            #     raise TypeError("The TabEngine is not in MergeTree Family")
            self.order_columns = order_columns
            self.partition_columns = kwargs.get('partition_columns')

    test = TabEngine(engine_name='MySQL', partition_columns='sadf',
                     sample_columns='abc', other_settings='sadf',
                     ttl='date + INTERVAL 1 DAY')
    test_2 = MergeTree(TabEngine=test, order_columns=['srasd', 'sadfsadf'], mergetree_type='MergeTree',
                       partition_columns=['sadf', 'sadf'])
    print('test2: ', test_2.to_query())
