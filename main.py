# import db_connect as db
# import pandas as pd
# from lib.tab_engines import TabEngine
from lib.objects import Tables
from lib.utils import Extractor
from lib.tab_engines import TabEngine

import pprint

if __name__ == '__main__':
    # input_test = Extractor.txt_to_df('assets', 'input_test.txt').file
    # print(input_test)
    ## Test 1
    # for db in input_test.database.unique():
    #     # print(db)
    #     for table in input_test[input_test.database == db].table.unique():
    #         tab_instance = Tables(table, database=db, tab_engine=input_test[(input_test.database == db) &
    #                                                                         (input_test.table == table)][
    #             'tab_engine'].values[0])
    #         # print(input_test[(input_test.database == db) & (input_test.table == table)]['tab_engine'].values[0])
    #         for col in input_test[(input_test.table == table) & (input_test.database == db)].index:
    #             # print(col)
    #             tab_instance.add_columns(col,
    #                                      input_test[(input_test.table == table) &
    #                                                 (input_test.index == col) &
    #                                                 (input_test.database == db)]['type'].values[0],
    #                                      input_test[(input_test.table == table) &
    #                                                 (input_test.index == col) &
    #                                                 (input_test.database == db)]['function'].values[0]
    #                                      )
    #         print(tab_instance)
    # test = Tables.TabEngine('MergeTree')
    # test.add_settings('asdfdsf')
    # print(test)

    ## Test 2
    input_test = Extractor.txt_to_df('assets', 'input_test.txt').file
    for db in input_test.database.unique():
        for table in input_test[input_test.database == db].table.unique():
            tab_instance = Tables(table, database=db)
            tab_engine=TabEngine(input_test[(input_test.database == db) & (input_test.table == table)]['tab_engine'].values[0])
            tab_engine.add_order(list(input_test[(input_test.database == db) & (input_test.table == table) & input_test.is_in_sorting_key ==1].index.values))
            tab_instance.add_engine(tab_engine)
            for col in input_test[(input_test.table == table) & (input_test.database == db)].index:
                # print(col)
                tab_instance.add_columns(col,
                                         input_test[(input_test.table == table) &
                                                    (input_test.index == col) &
                                                    (input_test.database == db)]['type'].values[0],
                                         input_test[(input_test.table == table) &
                                                    (input_test.index == col) &
                                                    (input_test.database == db)]['function'].values[0]
                                         )
            print(tab_instance)
