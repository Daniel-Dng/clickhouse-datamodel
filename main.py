# import db_connect as db
# import pandas as pd
# from lib.tab_engines import TabEngine
# from lib.functions import query_add_func
# from lib.utils import Extractor

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

# test = TabEngine(engine_name='ReplicatedMergeTree',  # partition_columns='sadf',
#                  sample_columns='abc', other_settings='sadf', order_columns=['safd', 'asdf'],
#                  ttl='date + INTERVAL 1 DAY')
if __name__ == '__main__':
    # print('test1: ', test.to_query())
    # print(test.attributes)
    # input_test = Extractor.csv_to_dict2('../data/input_test.csv').file
    # print(query_add_func(input_test[0]['Type_clh'], func='Nullable'))


    template = pkg_resources.read_text('lib', 'input_test.csv')
    print(template)
    # or for a file-like stream:
    # template = pkg_resources.open_text(templates, 'temp_file')


