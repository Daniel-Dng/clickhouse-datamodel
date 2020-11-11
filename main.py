
# import db_connect as db
import pandas as pd
from lib.tab_engines import TabEngine

test = TabEngine(engine_name='ReplicatedMergeTree',  # partition_columns='sadf',
                 sample_columns='abc', other_settings='sadf', order_columns=['safd', 'asdf'],
                 ttl='date + INTERVAL 1 DAY')

print('test1: ', test.to_query())
print(test.attributes)

