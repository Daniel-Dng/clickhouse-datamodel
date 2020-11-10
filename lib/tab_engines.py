import pandas as pd
from lib.tab_engines_functions import query_order_by, query_partition_by, query_sample_by, query_settings, query_TTL

sys_tab = pd.read_csv('../data/table_engines.csv', index_col='name').T.to_dict()

if __name__ == '__main__':
    class TabEngine:
        attributes = ['engine_name', 'partition_columns', 'other_settings', 'order_columns', 'sample_columns', 'ttl']

        def __init__(self, engine_name, **kwargs):
            self.engine_name = engine_name
            self.partition_columns = kwargs.get('partition_columns')
            self.other_settings = kwargs.get('other_settings')
            self.order_columns = kwargs.get('order_columns')
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
            # Family of Table Engine
            if 'MergeTree' in self.engine_name:
                self.family = 'MergeTree'
            elif 'Log' in self.engine_name:
                self.family = 'Log'
            elif self.engine_name in ['MySQL', 'ODBC', 'JDBC', 'Kafka', 'HDFS', 'RabbitMQ', 'MongoDB', 'S3', 'COSN']:
                self.family = 'Integration'
            else:
                self.family = 'Special'

        # Conditional Functions:
        def partition_by(self):
            _query = ''
            if self.partition_columns is not None:
                _query = _query + query_partition_by(self.partition_columns)
            return _query

        def sample_by(self):
            _query = ''
            if self.sample_columns is not None:
                _query = _query + query_sample_by(self.sample_columns)
            return _query

        def order_by(self):
            _query = ''
            if (self.supports_sort_order == 1) & (self.order_columns is not None):
                _query = _query + query_order_by(self.order_columns)
            elif self.supports_sort_order == 0:
                pass
            else:
                raise SyntaxError("MergeTree Engines require order_columns and vice versa ")
            return _query

        def settings(self):
            _query = ''
            if (self.supports_settings == 1) & (self.other_settings != ''):
                _query = _query + query_settings(self.other_settings)
            return _query

        def TTL(self):
            _query = ''
            if (self.ttl is not None) & (self.supports_ttl == 1):
                _query = _query + query_TTL(self.ttl)
            return _query

        # Full Query Compiler Operations
        def to_query(self):
            full_query = f'ENGINE {self.engine_name} {self.order_by()} {self.partition_by()} {self.sample_by()} {self.settings()} {self.TTL()} '
            return full_query


    # test = TabEngine(engine_name='ReplicatedMergeTree',  # partition_columns='sadf',
    #                  sample_columns='abc', other_settings='sadf', order_columns=['safd', 'asdf'],
    #                  ttl='date + INTERVAL 1 DAY')
    #
    # print('test1: ', test.to_query())
    # print(test.attributes)
