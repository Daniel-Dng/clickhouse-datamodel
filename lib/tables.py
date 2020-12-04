from lib.utils import (query_columns)


## OBJECTS
class Database:
    def __init__(self, name):
        self.name = name
        self.table_name = ''

    def add_table(self, table_name):
        self.table_name = table_name
        return self


class Tables:
    def __init__(self, name, database='', cluster='', tab_engine='', **kwargs):
        self.tab_engine = tab_engine
        self.name = name
        if database != '':
            self.database = database + '.'
        else:
            self.database = database
        if cluster != '':
            self.cluster = 'ON CLUSTER ' + cluster
        else:
            self.cluster = cluster
        self.columns = list()
        self.partition_columns = kwargs.get('partition_columns')
        self.other_settings = kwargs.get('other_settings')
        self.order_columns = kwargs.get('order_columns')
        self.sample_columns = kwargs.get('sample_columns')
        self.ttl = kwargs.get('ttl')

    def __str__(self):
        return "CREATE TABLE IF NOT EXISTS {}{} {}\n" \
               "(\n{}\n)\n" \
               "{}\n;".format(self.database,
                              self.name,
                              self.cluster,
                              ',\n'.join(self.columns),
                              self.tab_engine)

    def add_columns(self, col, datatype='', function=''):
        if datatype != '':
            self.columns.append(query_columns(col, datatype, function))
        else:
            self.columns.append(col)
        return self

    def rmv_columns(self, col, datatype='', function=''):
        if datatype != '':
            self.columns.remove(query_columns(col, datatype, function))
        else:
            self.columns.remove(col)
        return self

    def add_engine(self, engine_name):
        self.tab_engine = engine_name
        return self

    def add_cluster(self, cluster):
        self.cluster = cluster
        return self
