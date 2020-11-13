# import db_connect as db
# import pandas as pd
# from lib.tab_engines import TabEngine
from lib.objects import Tables
from lib.utils import Extractor
# import pprint

# test = TabEngine(engine_name='ReplicatedMergeTree',  # partition_columns='sadf',
#                  sample_columns='abc', other_settings='sadf', order_columns=['safd', 'asdf'],
#                  ttl='date + INTERVAL 1 DAY')
if __name__ == '__main__':
    input_test = Extractor.txt_to_dict('assets', 'input_test.txt').file

    test = Tables('ps_clicks', database='entities', tab_engine='MergeTree')
    # col = Tables.Columns('ps_id', 'string')#.to_query()
    test.add_columns('cl_id', 'String', 'ToYYYMM')
    test.add_columns('time_cl', 'UInt8', 'xxHash64')

    print(test)