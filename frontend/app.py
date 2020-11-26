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


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ClickHouse Data Model'
        self.left = 50
        self.top = 50
        self.width = 1100
        self.height = 650
        self.i = 40
        self.j = 80
        self.counter = 1
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # HEADER
        ## 1st row at 50
        self.db_label = QLabel('Database', self)
        self.db_label.setGeometry(50, 50, 100, 20)
        self.entry_db = QLineEdit(self)
        self.entry_db.setGeometry(QRect(100, 50, 100, 20))

        # self.db_engine_label = QLabel('DB Engine', self)
        # self.db_engine_label.setGeometry(250, 50, 100, 20)
        # self.db_engine_box = QComboBox(self)
        # self.db_engine_box.setGeometry(350, 50, 100, 20)
        # self.db_engine_box.addItems(['', 'MySQL', 'Lazy'])
        # self.db_engine_box.adjustSize()

        ## 2nd row at 100
        self.tab_label = QLabel('Table', self)
        self.tab_label.setGeometry(50, 100, 100, 20)
        self.entry_tab = QLineEdit(self)
        self.entry_tab.setGeometry(QRect(100, 100, 100, 20))

        self.tab_engine_label = QLabel('Tab Engine', self)
        self.tab_engine_label.setGeometry(250, 100, 100, 20)

        self.tab_engine_box = QComboBox(self)
        self.tab_engine_box.setGeometry(350, 100, 100, 20)
        self.tab_engine_box.addItems(tab_engine_options)
        self.tab_engine_box.setCurrentText('MergeTree')
        self.tab_engine_box.setEditable(True)
        self.tab_engine_box.adjustSize()

        self.setting_label = QLabel('Setting', self)
        self.setting_label.setGeometry(600, 100, 100, 20)
        self.entry_setting = QLineEdit(self)
        # self.entry_setting = QLineEdit('index_granularity = 8192', self)
        self.entry_setting.setGeometry(QRect(650, 100, 100, 20))
        self.entry_setting.adjustSize()

        self.addColButton = QPushButton('AddColumn', self)
        self.addColButton.setGeometry(QRect(800, 100, 100, 20))
        self.addColButton.clicked.connect(self.addColumn)
        self.rmvColButton = QPushButton('RemoveColumn', self)
        self.rmvColButton.setGeometry(QRect(900, 100, 100, 20))
        self.rmvColButton.clicked.connect(self.rmvColumn)

        # self.layout_header = QGridLayout(self)
        # self.layout_header.setGeometry(QRect(50, 50, 500, 100))
        # self.layout_header.setContentsMargins(0, 0, 0, 0)
        # self.layout_header.addWidget(self.db_label, 0, 0)
        # self.layout_header.addWidget(self.entry_db, 0, 1)
        # self.layout_header.addWidget(self.db_engine_label, 0, 2)
        # self.layout_header.addWidget(self.db_engine_box, 0, 3)
        # self.layout_header.addWidget(self.tab_label, 1, 0)
        # self.layout_header.addWidget(self.entry_tab, 1, 1)
        # self.layout_header.addWidget(self.tab_engine_label, 1, 2)
        # self.layout_header.addWidget(self.tab_engine_box, 1, 3)
        # self.layout_header.addWidget(self.setting_label, 1, 4)
        # self.layout_header.addWidget(self.entry_setting, 1, 5)

        # BODY
        ## 3rd Row at 150: Column scrollArea
        self.scrollLayout = QFormLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        # scroll area widget contents
        self.scrollArea = QScrollArea(self)  # Scroll Area which contains the widgets
        self.scrollArea.setGeometry(QRect(50, 150, 900, 250))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        # self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        ## Make the first ColumnWidget visible
        self._column = ColumnWidget(self)
        self.scrollLayout.addRow(self._column)

        # FOOTER
        self.footer = QWidget(self)
        footer_layout = QVBoxLayout()
        self.footer.setLayout(footer_layout)
        self.footer.setGeometry(QRect(50, 425, 900, 200))
        ## footer widgets
        self.result_query = QPlainTextEdit()
        self.result_query.setFixedSize(888, 150)
        # self.result_query.setGeometry(QRect(50, 425, 900, 150))
        self.result_query.setStyleSheet("border :3px solid black")
        self.createButton = QPushButton('CREATE')
        # self.createButton.setGeometry(QRect(50, 600, 100, 20))
        self.createButton.clicked.connect(self.create_table)

        footer_layout.addWidget(self.result_query, alignment=Qt.AlignCenter)
        footer_layout.addWidget(self.createButton, alignment=Qt.AlignLeft)

        # Other variables
        # _new_tab_engine = TabEngine(self.tab_engine_box.currentText())
        # _new_tab_engine.add_settings(self.entry_setting.text())
        # _new_tab = Tables(name=self.entry_tab.text(),
        #                        database=self.entry_db.text(),
        #                        tab_engine=_new_tab_engine)

        # self.shortcut_create = QShortcut(self)
        # self.shortcut_create.setKey("Ctrl+C")
        # self.shortcut_create.activated.connect(self.create_table)

        self.show()

    def addColumn(self):
        self._column = ColumnWidget(self)
        self.scrollLayout.addRow(self._column)

    def rmvColumn(self):
        self.scrollLayout.removeRow(self.scrollWidget.children()[-1])

    def create_table(self):
        _new_tab = Tables(name=self.entry_tab.text(),
                          database=self.entry_db.text())
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

# TODO: outbound Widgets & horizontal + vertical main scrolls

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
