import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from lib.columns import Columns

class ColumnArea(QWidget):
    def __init__(self, parent=None):
        super(ColumnArea, self).__init__(parent)
        self._col = QLabel('Column Name')
        self._col.setFixedSize(80, 20)
        self._col.setAlignment(Qt.AlignRight)
        self._entry_col = QLineEdit()
        self._entry_col.setFixedSize(100, 20)

        self._nullable = QCheckBox('Nullable')
        self._nullable.setFixedSize(100, 20)
        # self._nullable.setFont()

        self._datatype = QLabel('Data Type')
        self._datatype.setFixedSize(50, 20)
        self._datatype.setAlignment(Qt.AlignRight)
        self._entry_datatype = QLineEdit()
        self._entry_datatype.setFixedSize(100, 20)

        self._func = QLabel('Function')
        self._func.setFixedSize(50, 20)
        self._func.setAlignment(Qt.AlignRight)
        self._entry_func = QLineEdit()
        self._entry_func.setFixedSize(100, 20)

        self._codec = QLabel('CODEC')
        self._codec.setFixedSize(50, 20)
        self._codec.setAlignment(Qt.AlignRight)
        self._entry_codec = QLineEdit()
        self._entry_codec.setFixedSize(100, 20)

        layout = QHBoxLayout()
        layout.addWidget(self._col)
        layout.addWidget(self._entry_col)
        layout.addWidget(self._nullable)
        layout.addWidget(self._datatype)
        layout.addWidget(self._entry_datatype)
        layout.addWidget(self._func)
        layout.addWidget(self._entry_func)
        layout.addWidget(self._codec)
        layout.addWidget(self._entry_codec)
        self.setLayout(layout)
        self.new_col = Columns(self._entry_col.text(),self._entry_datatype.text())



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ClickHouse Data Model'
        self.left = 50
        self.top = 50
        self.width = 1000
        self.height = 700
        self.i = 40
        self.j = 80
        self.counter = 1
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ## 1st row at 50
        self.db_label = QLabel('Database', self)
        self.db_label.setGeometry(50, 50, 100, 20)
        self.entry_db = QLineEdit(self)
        self.entry_db.setGeometry(QRect(100, 50, 100, 20))
        self.db_engine_label = QLabel('DB Engine', self)
        self.db_engine_label.setGeometry(250, 50, 100, 20)
        self.db_engine_box = QComboBox(self)
        self.db_engine_box.setGeometry(350, 50, 100, 20)
        self.db_engine_box.addItems(['', 'MySQL', 'Lazy'])
        self.db_engine_box.adjustSize()

        ## 2nd row at 100
        self.tab_label = QLabel('Table', self)
        self.tab_label.setGeometry(50, 100, 100, 20)
        self.entry_tab = QLineEdit(self)
        self.entry_tab.setGeometry(QRect(100, 100, 100, 20))

        self.tab_engine_label = QLabel('Tab Engine', self)
        self.tab_engine_label.setGeometry(250, 100, 100, 20)
        self.tab_engine_box = QComboBox(self)
        self.tab_engine_box.setGeometry(350, 100, 100, 20)
        self.tab_engine_box.addItems(
            ['MergeTree', 'ReplicatedMergeTree', 'Log', 'View', 'ReplicatedVersionedCollapsingMergeTree'])
        self.tab_engine_box.adjustSize()

        self.setting_label = QLabel('Setting', self)
        self.setting_label.setGeometry(600, 100, 100, 20)
        self.entry_setting = QLineEdit('index_granularity = 8192', self)
        self.entry_setting.setGeometry(QRect(650, 100, 100, 20))
        self.entry_setting.adjustSize()
        self.addColButton = QPushButton('<AddColumn>', self)
        self.addColButton.setGeometry(QRect(800, 100, 100, 20))
        self.addColButton.clicked.connect(self.addColumn)

        self.layout1 = QGridLayout(self)
        self.layout1.setGeometry(QRect(50, 50, 500, 100))
        # self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.addWidget(self.db_label, 0, 0)
        self.layout1.addWidget(self.entry_db, 0, 1)
        self.layout1.addWidget(self.db_engine_label, 0, 2)
        self.layout1.addWidget(self.db_engine_box, 0, 3)
        self.layout1.addWidget(self.tab_label, 1, 0)
        self.layout1.addWidget(self.entry_tab, 1, 1)
        self.layout1.addWidget(self.tab_engine_label, 1, 2)
        self.layout1.addWidget(self.tab_engine_box, 1, 3)
        self.layout1.addWidget(self.setting_label, 1, 4)
        self.layout1.addWidget(self.entry_setting, 1, 5)

        # ## 3rd Row at 150: Column scrollregion
        self.scrollLayout = QFormLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.col_layout = QVBoxLayout(self)

        # scroll area widget contents
        self.scrollArea = QScrollArea(self)  # Scroll Area which contains the widgets, set as the centralWidget
        self.scrollArea.setGeometry(QRect(50, 150, 800, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scrollArea.setLayout(self.col_layout)

        # self.col_widget = QWidget(self)  # Widget that contains the collection of Vertical Box
        # self.col_widget.setLayout(self.col_layout)
        # self.scrollArea.setWidget(self.widget)

        ## footer
        self.createButton = QPushButton('<CREATE>', self)
        self.createButton.setGeometry(QRect(800, 400, 100, 20))
        self.createButton.clicked.connect(self.create_table)
        self.show()

    def addColumn(self):
        self.col = ColumnArea(self)
        self.scrollLayout.addRow(self.col)
        # print()

    # @staticmethod
    def create_table(self):
        # print(f'CREATE TABLE {self.entry_tab.text()}')
        print(self.col.new_col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
