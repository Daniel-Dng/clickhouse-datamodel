from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from frontend.column_widget import ColumnWidget
from lib.tables import Tables
from lib.tab_engines import TabEngine
from lib.extractors import Extractor
from lib.utils import query_add_func, query_rmv_func
import re

tab_engine_options = list(Extractor.txt_to_dict('assets', 'table_engines.txt').file.keys())
tab_engine_options.sort()


# noinspection PyAttributeOutsideInit,PyArgumentList
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ClickHouse Query Builder'
        self.left = 200
        self.top = 50
        self.width = 1100
        self.height = 650
        # self.i = 40
        # self.j = 80
        self.counter = 1
        self.last_time_move = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # HEADER
        ## header contents
        ## 1st row
        self.db_label = QLabel('Database:')
        self.entry_db = QLineEdit()
        # self.db_engine_label = QLabel('DB Engine:', self)
        # self.db_engine_box = QComboBox(self)
        # self.db_engine_box.addItems(['', 'MySQL', 'Lazy'])
        # self.db_engine_box.adjustSize()
        self.cluster_label = QLabel('On Cluster:')
        self.entry_cluster = QLineEdit()

        ## 2nd row
        self.tab_label = QLabel('Table:')
        self.entry_tab = QLineEdit()
        self.tab_engine_label = QLabel('Tab Engine:')
        self.tab_engine_box = QComboBox()
        self.tab_engine_box.addItems(tab_engine_options)
        self.tab_engine_box.adjustSize()
        self.tab_engine_box.setCurrentText('ReplicatedMergeTree')
        # self.tab_engine_box.setEditable(True)
        self.ttl_label = QLabel('TTL:')
        self.entry_ttl = QLineEdit()
        self.setting_label = QLabel('Setting:')
        self.entry_setting = QLineEdit()
        # self.entry_setting = QLineEdit('index_granularity = 8192', self)
        self.prikey_label = QLabel('Primary Key:')
        self.entry_prikey = QLineEdit()

        self.addColButton = QPushButton('<AddColumn>')
        self.addColButton.clicked.connect(self.addColumn)
        self.addColButton.clicked.connect(self.reset_column_name)
        self.addColButton.setFixedSize(100, 20)
        self.addColButton.setShortcut('Ctrl+A')

        self.rmvColButton = QPushButton('<RemoveColumn>')
        self.rmvColButton.setFixedSize(100, 20)
        self.rmvColButton.clicked.connect(self.rmvColumn)
        self.rmvColButton.setShortcut('Ctrl+B')

        ## header widget & layout
        self.header = QWidget()
        header_layout = QGridLayout()
        self.header.setLayout(header_layout)
        header_layout.setContentsMargins(10, 10, 10, 10)
        header_layout.addWidget(self.db_label, 0, 0)
        header_layout.addWidget(self.entry_db, 0, 1)
        header_layout.addWidget(self.cluster_label, 0, 2)
        header_layout.addWidget(self.entry_cluster, 0, 3)
        # header_layout.addWidget(self.db_engine_label, 0, 2)
        # header_layout.addWidget(self.db_engine_box, 0, 3)
        header_layout.addWidget(self.tab_label, 1, 0)
        header_layout.addWidget(self.entry_tab, 1, 1)
        header_layout.addWidget(self.tab_engine_label, 1, 2)
        header_layout.addWidget(self.tab_engine_box, 1, 3)
        header_layout.addWidget(self.prikey_label, 1, 4)
        header_layout.addWidget(self.entry_prikey, 1, 5)
        header_layout.addWidget(self.setting_label, 1, 6)
        header_layout.addWidget(self.entry_setting, 1, 7)
        header_layout.addWidget(self.ttl_label, 1, 8)
        header_layout.addWidget(self.entry_ttl, 1, 9)

        header_layout.addWidget(self.addColButton, 2, 8, alignment=Qt.AlignCenter)
        header_layout.addWidget(self.rmvColButton, 2, 9, alignment=Qt.AlignCenter)

        # BODY
        ## Column scrollArea
        self.scrollLayout = QFormLayout()
        self.scrollLayout.setObjectName('body_layout')
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        # scroll area widget contents
        self.scrollArea = QScrollArea()  # scrollArea which contains the widgets
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        self.small_vscrollbar = self.scrollArea.verticalScrollBar()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.installEventFilter(self)

        # FOOTER
        ## footer contents
        self.result_query = QPlainTextEdit()
        self.result_query.setFixedSize(1000, 150)
        self.result_query.setStyleSheet("border :3px solid black")
        self.result_query.setAcceptDrops(True)
        self.createButton = QPushButton('QUERY')
        self.createButton.setShortcut('Ctrl+Q')
        self.createButton.clicked.connect(self.create_query)
        self.reverseButton = QPushButton('REVERSE')
        self.reverseButton.setShortcut('Ctrl+R')
        self.reverseButton.clicked.connect(self.reverse)
        self.buttons = QWidget()
        self.button_layout = QHBoxLayout()
        self.buttons.setLayout(self.button_layout)
        self.button_layout.addWidget(self.createButton, alignment=Qt.AlignLeft)
        self.button_layout.addWidget(self.reverseButton, alignment=Qt.AlignLeft)

        ## footer widget & layout
        self.footer = QWidget()
        footer_layout = QVBoxLayout()
        self.footer.setLayout(footer_layout)
        footer_layout.addWidget(self.result_query, alignment=Qt.AlignCenter)
        footer_layout.addWidget(self.buttons, alignment=Qt.AlignLeft)

        # Other variables + features
        self.main_menu()

        # ROOT
        self.root_layout = QFormLayout()
        self.Root_Widget = QWidget()
        self.Root_Widget.setObjectName('root')
        self.Root_Widget.setLayout(self.root_layout)
        self.Root_ScrollArea = QScrollArea(self)
        self.Root_ScrollArea.setObjectName('root_scroll_area')
        self.Root_ScrollArea.setGeometry(0, 0, self.width - 21, self.height)  # Lowered down by the height of menu bar
        self.Root_ScrollArea.setWidgetResizable(True)
        # self.Root_ScrollArea.installEventFilter(self)
        self.hscroll_bar = self.Root_ScrollArea.horizontalScrollBar()
        self.vscroll_bar = self.Root_ScrollArea.verticalScrollBar()
        # self.Root_Widget.setGeometry(0, 0, self.width, self.height)
        self.Root_ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Root_ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Root_ScrollArea.setWidget(self.Root_Widget)
        # self.Root_Widget.setMinimumSize(0, 0)
        self.root_layout.insertRow(0, self.header)
        self.root_layout.insertRow(1, self.scrollArea)
        self.root_layout.insertRow(3, self.footer)
        self.setCentralWidget(self.Root_ScrollArea)

        self.show()

    # FUNCTIONS
    ## Body Functions
    def addColumn(self):
        self._column = ColumnWidget(self)
        self.scrollLayout.insertRow(0, self._column)
        self._column.col_name_label.setText(
            'Column ' + str(self.scrollLayout.rowCount() - self.scrollLayout.getWidgetPosition(self._column)[0]))
        self._column.col_position = self.scrollLayout.count() - self.scrollLayout.getWidgetPosition(self._column)[0]
        self._column.destroyed.connect(self.reset_column_name)

    def reset_column_name(self):
        count = 0
        for col_widget in self.scrollWidget.findChildren(ColumnWidget):
            count += 1
            # print(self.scrollLayout.count() - self.scrollLayout.getWidgetPosition(col_widget)[0], 'new pos:', count)
            # print('after_changed')
            col_widget.col_name_label.setText('Column ' + str(count))
            # col_widget.setObjectName('Column ' + str(count))
            col_widget.col_position = count

    def rmvColumn(self):
        self.scrollLayout.removeRow(self.scrollWidget.children()[-1])

    ## Footer Functions
    def create_query(self):
        _new_tab = Tables(name=self.entry_tab.text(),
                          database=self.entry_db.text(),
                          cluster=self.entry_cluster.text())
        _new_tab_engine = TabEngine(self.tab_engine_box.currentText())
        partitioned_cols = []
        ordered_col = []
        sampled_cols = []
        for col_widget in self.scrollWidget.findChildren(ColumnWidget):
            col_name = col_widget.findChild(QLineEdit, 'col_name').text()
            if str(col_name).strip() != '':
                _new_tab.add_columns(str(col_widget.new_col))
                for child_widget in col_widget.findChildren(QCheckBox):
                    if child_widget.isChecked():
                        if child_widget.objectName() == '_partitioned':
                            if (child_widget.parent().children()[-1].text() != '<additional_func>') & (
                                    child_widget.parent().children()[-1].text() != ''):
                                col_name = query_add_func(col_name, child_widget.parent().children()[-1].text())
                            partitioned_cols.append(col_name)
                            _new_tab_engine.add_partition(partitioned_cols)
                            col_name = col_widget.findChild(QLineEdit, 'col_name').text()

                        elif child_widget.objectName() == '_sampled':
                            if (child_widget.parent().children()[-1].text() != '<additional_func>') & (
                                    child_widget.parent().children()[-1].text() != ''):
                                col_name = query_add_func(col_name, child_widget.parent().children()[-1].text())
                            sampled_cols.append(col_name)
                            _new_tab_engine.add_sample(sampled_cols)
                            col_name = col_widget.findChild(QLineEdit, 'col_name').text()

                        elif child_widget.objectName() == '_ordered':
                            if (child_widget.parent().children()[-1].text() != '<additional_func>') & (
                                    child_widget.parent().children()[-1].text() != ''):
                                col_name = query_add_func(col_name, child_widget.parent().children()[-1].text())
                            ordered_col.append(col_name)
                            _new_tab_engine.add_order(ordered_col)
                            col_name = col_widget.findChild(QLineEdit, 'col_name').text()

        _new_tab_engine.add_settings(self.entry_setting.text())
        _new_tab_engine.add_ttl(self.entry_ttl.text())
        _new_tab_engine.add_prikey(self.entry_prikey.text())
        _new_tab.add_engine(_new_tab_engine)
        self.result_query.setPlainText(str(_new_tab))

    def reverse_query(self, text):
        rows_in_txt = str(text).replace(' IF NOT EXISTS ', ' ').split('\n')
        # Removing all existing entries
        ## Tab, Db, Tab_Engine
        self.entry_tab.setText('')
        self.entry_db.setText('')
        self.entry_cluster.setText('')
        self.entry_setting.setText('')
        ## Columns
        for i in range(self.scrollLayout.count()):
            self.rmvColumn()

        # Adding new info (Reverse query)
        ## DB & TABLE & CLUSTER
        first_row_elements = rows_in_txt[0].split(' ')
        for first_row_element in first_row_elements:
            if '.' in first_row_element:
                self.entry_db.setText(first_row_element.split('.')[0])
                self.entry_tab.setText(first_row_element.split('.')[1])
        if 'ON CLUSTER' in rows_in_txt[0]:
            cluster_name = re.findall('ON CLUSTER \'(.*?)\'', rows_in_txt[0])[0]
            # cluster_name = re.sub('\'$|^\'', '', cluster_name)
            self.entry_cluster.setText(cluster_name)

        ## TAB ENGINE
        last_row_elements = rows_in_txt[-2].split()
        self.tab_engine_box.setCurrentText(last_row_elements[1])
        ### ordered
        ordered_cols = {}
        if 'ORDER' in rows_in_txt[-2]:
            ordered_chunk = re.findall('ORDER BY (.*?) ', rows_in_txt[-2])[0]
            ordered_chunk = re.sub('\)$|^\(', '', ordered_chunk).split(',')
            for col in ordered_chunk:
                if '(' in col:
                    col_name = query_rmv_func(col)[0]
                    add_func = query_rmv_func(col)[1]
                    ordered_cols[col_name] = add_func
                else:
                    ordered_cols[col] = ''
        ### partitioned
        partitioned_cols = {}
        if 'PARTITION' in rows_in_txt[-2]:
            partition_chunk = re.findall('PARTITION BY (.*?) ', rows_in_txt[-2])[0]
            partition_chunk = re.sub('\)$|^\(', '', partition_chunk).split(',')
            for col in partition_chunk:
                if '(' in col:
                    col_name = query_rmv_func(col)[0]
                    add_func = query_rmv_func(col)[1]
                    partitioned_cols[col_name] = add_func
                else:
                    partitioned_cols[col] = ''

        ### sampled
        sampled_cols = {}
        if 'SAMPLE' in rows_in_txt[-2]:
            sampled_chunk = re.findall('SAMPLE BY (.*?) ', rows_in_txt[-2])[0]
            sampled_chunk = re.sub('\)$|^\(', '', sampled_chunk).split(',')
            for col in sampled_chunk:
                if '(' in col:
                    col_name = query_rmv_func(col)[0]
                    add_func = query_rmv_func(col)[1]
                    sampled_cols[col_name] = add_func
                else:
                    sampled_cols[col] = ''

        ### TAB ENGINE SETTING
        if 'SETTINGS' in rows_in_txt[-2]:
            engine_settings = re.findall('SETTINGS (.*?) ', rows_in_txt[-2])[0]
            self.entry_setting.setText(engine_settings)

        ### TAB ENGINE PRIKEY
        if 'PRIMARY KEY' in rows_in_txt[-2]:
            engine_prikey = re.findall('PRIMARY KEY \((.*?)\) ', rows_in_txt[-2])[0]
            self.entry_prikey.setText(engine_prikey)

        ### TAB ENGINE TTL
        if 'TTL' in rows_in_txt[-2]:
            engine_ttl = re.findall('TTL (.*?) ', rows_in_txt[-2])[0]
            self.entry_ttl.setText(engine_ttl)


        ## COLUMNS
        for col_rows in rows_in_txt[2:(len(rows_in_txt) - 3)]:
            col_elements = col_rows.split(' ')
            self.addColumn()
            self._column._entry_col.setText(col_elements[0])
            if 'Nullable(' in col_elements[1]:
                self._column._nullable.setChecked(1)
                self._column._entry_datatype.setCurrentText(query_rmv_func(col_elements[1])[0])
            # TODO: adding datatype function parser (where Nullable inside a function)
            elif '(' in col_elements[1]:
                datatype = query_rmv_func(col_elements[1])[0]
                datatype_func = query_rmv_func(col_elements[1])[1]
                self._column._entry_datatype.setCurrentText(datatype)
                self._column._entry_func.setText(datatype_func)
            else:
                self._column._entry_datatype.setCurrentText(col_elements[1])
            ### CODEC
            if col_elements[2] != ',':
                if 'CODEC(' in col_elements[2]:
                    self._column._entry_codec.setText(query_rmv_func(col_elements[2])[0])
            ### ORDER
            if col_elements[0] in ordered_cols.keys():
                self._column._ordered.setChecked(1)
                if ordered_cols[col_elements[0]] != '':
                    self._column._ordered_func.setText(ordered_cols[col_elements[0]])
            ### PARTITION
            if col_elements[0] in partitioned_cols.keys():
                self._column._partitioned.setChecked(1)
                if partitioned_cols[col_elements[0]] != '':
                    self._column._partitioned_func.setText(partitioned_cols[col_elements[0]])
            ### SAMPLE
            if col_elements[0] in sampled_cols.keys():
                self._column._sampled.setChecked(1)
                if sampled_cols[col_elements[0]] != '':
                    self._column._sampled_func.setText(sampled_cols[col_elements[0]])

    def reverse(self):
        try:
            text = self.result_query.toPlainText()
            self.reverse_query(text)
        except Exception:
            pass

    ## Menu Bar Functions
    def main_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        # menu actions within Menu Bar
        menu_file = menu_bar.addMenu('File')
        save_action = QAction('Save Query', self)
        save_action.triggered.connect(self.file_save)
        save_action.setShortcut('Ctrl+S')
        menu_file.addAction(save_action)

        open_action = QAction('Open Query', self)
        open_action.triggered.connect(self.file_open)
        open_action.setShortcut('Ctrl+O')
        menu_file.addAction(open_action)

    # noinspection PyBroadException,PyProtectedMember
    def file_open(self):
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(name[0], 'r')
            with file:
                text = file.read()
                self.result_query.setPlainText(text)
            self.reverse_query(text)
        except Exception:
            pass

    # noinspection PyBroadException
    def file_save(self):
        text = self.result_query.toPlainText()
        try:
            name = QFileDialog.getSaveFileName(self, 'Save File')
            print(name[0])
            file = open(name[0], 'w')
            file.write(text)
            file.close()
        except Exception:
            pass

    ## Additional Features
    ### Mouse Scrolling
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove:
            # print(event.pos().y())
            if self.last_time_move == 0:
                self.last_time_move = event.pos().y()
            vdistance = self.last_time_move - event.pos().y()
            # hdistance = self.last_time_move - event.pos().x()
            self.small_vscrollbar.setValue(self.small_vscrollbar.value() + vdistance)
            # self.vscroll_bar.setValue(self.vscroll_bar.value() + vdistance)
            # self.hscroll_bar.setValue(self.hscroll_bar.value() + hdistance)
            self.last_time_move = event.pos().y()
        elif event.type() == QEvent.MouseButtonRelease:
            self.last_time_move = 0
        return QWidget.eventFilter(self, source, event)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())