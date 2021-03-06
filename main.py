# import db_connect as db
# import pandas as pd
# from lib.tables import Tables
# from lib.extractors import Extractor
# from lib.tab_engines import TabEngine
import sys
from frontend.app import App
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('icon.png'))
    ex = App()
    sys.exit(app.exec_())

    # input_test = Extractor.txt_to_df('assets', 'input_test.txt').file
    # print(input_test)
    # # Test 1
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
    # Test 2
    # input_test = Extractor.txt_to_df('assets', 'input_test.txt').file
    # for db in input_test.database.unique():
    #     for table in input_test[input_test.database == db].table.unique():
    #         tab_instance = Tables(table, database=db)
    #         tab_engine = TabEngine(
    #             input_test[(input_test.database == db) & (input_test.table == table)]['tab_engine'].values[0])
    #         tab_engine.add_order(list(input_test[(input_test.database == db) & (
    #                     input_test.table == table) & input_test.is_in_sorting_key == 1].index.values))
    #         tab_engine.add_sample(list(input_test[(input_test.database == db) & (
    #                 input_test.table == table) & input_test.is_in_sampling_key == 1].index.values))
    #         tab_engine.add_partition(list(input_test[(input_test.database == db) & (
    #                 input_test.table == table) & input_test.is_in_partition_key == 1].index.values))
    #         tab_engine.add_prikey(list(input_test[(input_test.database == db) & (
    #                 input_test.table == table) & input_test.is_in_primary_key == 1].index.values))
    #         tab_engine.add_settings('index_granularity = 8129')
    #         tab_instance.add_engine(tab_engine)
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
    #         [print('table_names: ',x.split('.')[1]) for x in str(tab_instance).replace(' IF NOT EXISTS ', ' ').split('\n')[0].split() if '.' in x]
