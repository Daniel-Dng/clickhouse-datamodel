from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton

from lib.columns import Columns
from lib.extractors import Extractor

data_type_options = list(Extractor.txt_to_dict('assets', 'data_type_families.txt').file.keys())
data_type_options.sort()


class ColumnWidget(QWidget):
    def __init__(self, parent=None):
        super(ColumnWidget, self).__init__(parent)
        # 1st group of widgets + layout
        self.col_name_label = QLabel('Column Name:')
        self.col_name_label.setFixedSize(80, 20)
        self.col_name_label.setAlignment(Qt.AlignRight)
        self._entry_col = QLineEdit()
        self._entry_col.setObjectName('col_name')
        self._entry_col.setFixedSize(100, 20)
        self._entry_col.textChanged.connect(self.make_col)

        self._datatype = QLabel('Data Type:')
        self._datatype.setFixedSize(80, 20)
        self._datatype.setAlignment(Qt.AlignRight)
        self._entry_datatype = QComboBox()
        self._entry_datatype.addItems(data_type_options)
        self._entry_datatype.adjustSize()
        self._entry_datatype.setCurrentText('String')
        self._entry_datatype.setEditable(True)
        # self._entry_datatype.setFixedSize(100, 20)
        self._entry_datatype.currentTextChanged.connect(self.make_col)

        self._func = QLabel('Function:')
        self._func.setFixedSize(80, 20)
        self._func.setAlignment(Qt.AlignRight)
        self._entry_func = QLineEdit()
        self._entry_func.setFixedSize(100, 20)
        self._entry_func.textChanged.connect(self.make_col)

        self._codec = QLabel('CODEC:')
        self._codec.setFixedSize(80, 20)
        self._codec.setAlignment(Qt.AlignRight)
        self._entry_codec = QLineEdit()
        self._entry_codec.setFixedSize(100, 20)
        self._entry_codec.textChanged.connect(self.make_col)

        # self.addcol = QPushButton('+')
        # self.addcol.setFixedSize(20, 20)
        # self.addcol.clicked.connect(self.addcol_func)
        self.rmvcol = QPushButton('-')
        self.rmvcol.setFixedSize(20, 20)
        self.rmvcol.clicked.connect(self.deleteLater)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.col_name_label, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_col, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._datatype, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_datatype, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._func, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_func, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._codec, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_codec, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self.rmvcol, alignment=Qt.AlignRight)
        # hlayout1.addWidget(self.addcol, alignment=Qt.AlignLeft)

        # 2nd group of widgets + layout
        self._nullable = QCheckBox('Nullable')
        self._nullable.setFixedSize(100, 20)
        self._nullable.setObjectName('_nullable')
        self._nullable.stateChanged.connect(self.make_col)

        self.dummy_order = QWidget()
        self.dummy_order_layout = QVBoxLayout()
        self.dummy_order.setLayout(self.dummy_order_layout)
        self._ordered = QCheckBox('Ordered')
        self._ordered.setObjectName('_ordered')
        self._ordered.setFixedSize(100, 20)
        self._ordered.stateChanged.connect(self.make_col)
        self._ordered_func = QLineEdit()
        self._ordered_func.setFixedSize(100, 15)
        self._ordered_func.setText('<additional_func>')
        self._ordered_func.setObjectName('_ordered_func')
        self.dummy_order_layout.addWidget(self._ordered)
        self.dummy_order_layout.addWidget(self._ordered_func)

        self.dummy_partitioned = QWidget()
        self.dummy_partitioned_layout = QVBoxLayout()
        self.dummy_partitioned.setLayout(self.dummy_partitioned_layout)
        self._partitioned = QCheckBox('Partitioned')
        self._partitioned.setObjectName('_partitioned')
        self._partitioned.setFixedSize(100, 20)
        self._partitioned.stateChanged.connect(self.make_col)
        self._partitioned_func = QLineEdit()
        self._partitioned_func.setFixedSize(100, 15)
        self._partitioned_func.setText('<additional_func>')
        self._partitioned_func.setObjectName('_partitioned_func')
        self.dummy_partitioned_layout.addWidget(self._partitioned)
        self.dummy_partitioned_layout.addWidget(self._partitioned_func)

        self.dummy_sampled = QWidget()
        self.dummy_sampled_layout = QVBoxLayout()
        self.dummy_sampled.setLayout(self.dummy_sampled_layout)
        self._sampled = QCheckBox('Sampled')
        self._sampled.setObjectName('_sampled')
        self._sampled.setFixedSize(100, 20)
        self._sampled.stateChanged.connect(self.make_col)
        self._sampled_func = QLineEdit()
        self._sampled_func.setFixedSize(100, 15)
        self._sampled_func.setText('<additional_func>')
        self._sampled_func.setObjectName('_partitioned_func')
        self.dummy_sampled_layout.addWidget(self._sampled)
        self.dummy_sampled_layout.addWidget(self._sampled_func)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self._nullable, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self.dummy_order, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self.dummy_partitioned, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self.dummy_sampled, alignment=Qt.AlignCenter)

        # Outbound Vertical Layout
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        self.setLayout(vlayout)

        # Other Variables
        self.col_position = 0

    def make_col(self):
        is_nullable = 1 if self._nullable.isChecked() else 0
        self.new_col = Columns(col_name=self._entry_col.text(),
                               data_type=self._entry_datatype.currentText(),
                               nullable=is_nullable,
                               function=self._entry_func.text(),
                               codec=self._entry_codec.text())

    # def addcol_func(self):
    #     print(self.parent().children()[0].getWidgetPosition(self)[0]-1)
    #     print(self.col_position)
        # self.parent().children()[0].insertRow(self.col_position-1, ColumnWidget())

# TODO: add_button that adds column next to the current one
