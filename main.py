# import db_connect as db
# import pandas as pd
# from lib.tab_engines import TabEngine
# from lib.functions import query_add_func
from lib.utils import Extractor
import pprint

# test = TabEngine(engine_name='ReplicatedMergeTree',  # partition_columns='sadf',
#                  sample_columns='abc', other_settings='sadf', order_columns=['safd', 'asdf'],
#                  ttl='date + INTERVAL 1 DAY')
if __name__ == '__main__':
    # print('test1: ', test.xto_query())
    # print(test.attributes)
    # input_test = Extractor.csv_to_dict2('../data/input_test.csv').file
    # print(query_add_func(input_test[0]['Type_clh'], func='Nullable'))
    input = Extractor.txt_to_dict('assets', 'column_input.txt')
    pprint.pprint(input)
    # or for a file-like stream:
    # template = pkg_resources.open_text(templates, 'temp_file')


