from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from frontend.column_widget import ColumnWidget
from lib.tables import Tables
from lib.tab_engines import TabEngine
from lib.extractors import Extractor
from lib.utils import query_add_func

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
        self.tab_engine_box.setCurrentText('MergeTree')
        # self.tab_engine_box.setEditable(True)
        self.setting_label = QLabel('Setting:')
        self.entry_setting = QLineEdit()
        # self.entry_setting = QLineEdit('index_granularity = 8192', self)

        self.addColButton = QPushButton('<AddColumn>')
        self.addColButton.clicked.connect(self.addColumn)
        self.addColButton.clicked.connect(self.reset_column_name)
        self.addColButton.setFixedSize(100, 20)
        self.addColButton.setShortcut('Ctrl+E')

        self.rmvColButton = QPushButton('<RemoveColumn>')
        self.rmvColButton.setFixedSize(100, 20)
        self.rmvColButton.clicked.connect(self.rmvColumn)
        self.rmvColButton.setShortcut('Ctrl+R')

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
        header_layout.addWidget(self.setting_label, 1, 4)
        header_layout.addWidget(self.entry_setting, 1, 5)
        header_layout.addWidget(self.addColButton, 1, 7)
        header_layout.addWidget(self.rmvColButton, 1, 8)

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
        self.createButton = QPushButton('CREATE')
        self.createButton.setShortcut('Ctrl+Q')
        self.createButton.clicked.connect(self.create_table)

        ## footer widget & layout
        self.footer = QWidget()
        footer_layout = QVBoxLayout()
        self.footer.setLayout(footer_layout)
        footer_layout.addWidget(self.result_query, alignment=Qt.AlignCenter)
        footer_layout.addWidget(self.createButton, alignment=Qt.AlignLeft)

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
    def create_table(self):
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
        _new_tab.add_engine(_new_tab_engine)
        self.result_query.setPlainText(str(_new_tab))

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

    # noinspection PyBroadException
    def file_open(self):
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(name[0], 'r')
            with file:
                text = file.read()
                self.result_query.setPlainText(text)
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
