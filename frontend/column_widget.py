from lib.columns import Columns
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox
from lib.utils import Extractor

data_type_options = list(Extractor.txt_to_dict('assets','data_type_families.txt').file.keys())
data_type_options.sort()


class ColumnWidget(QWidget):
    def __init__(self, parent=None):
        super(ColumnWidget, self).__init__(parent)
        self._col = QLabel('Column Name')
        self._col.setFixedSize(80, 20)
        self._col.setAlignment(Qt.AlignRight)
        self._entry_col = QLineEdit()
        self._entry_col.setObjectName('col_name')
        self._entry_col.setFixedSize(100, 20)
        self._entry_col.textChanged.connect(self.make_col)

        self._nullable = QCheckBox('Nullable')
        self._nullable.setFixedSize(100, 20)
        self._nullable.setObjectName('_nullable')
        self._nullable.stateChanged.connect(self.make_col)
        self._ordered = QCheckBox('Ordered')
        self._ordered.setObjectName('_ordered')
        self._ordered.setFixedSize(100, 20)
        self._ordered.stateChanged.connect(self.make_col)
        self._partitioned = QCheckBox('Partitioned')
        self._partitioned.setObjectName('_partitioned')
        self._partitioned.setFixedSize(100, 20)
        self._partitioned.stateChanged.connect(self.make_col)
        self._sampled = QCheckBox('Sampled')
        self._sampled.setObjectName('_sampled')
        self._sampled.setFixedSize(100, 20)
        self._sampled.stateChanged.connect(self.make_col)

        self._datatype = QLabel('Data Type')
        self._datatype.setFixedSize(50, 20)
        self._datatype.setAlignment(Qt.AlignRight)
        self._entry_datatype = QComboBox()
        self._entry_datatype.addItems(data_type_options)
        self._entry_datatype.adjustSize()
        self._entry_datatype.setCurrentText('String')
        self._entry_datatype.setEditable(True)
        # self._entry_datatype.setFixedSize(100, 20)
        self._entry_datatype.currentTextChanged.connect(self.make_col)

        self._func = QLabel('Function')
        self._func.setFixedSize(50, 20)
        self._func.setAlignment(Qt.AlignRight)
        self._entry_func = QLineEdit()
        self._entry_func.setFixedSize(100, 20)
        self._entry_func.textChanged.connect(self.make_col)

        self._codec = QLabel('CODEC')
        self._codec.setFixedSize(50, 20)
        self._codec.setAlignment(Qt.AlignRight)
        self._entry_codec = QLineEdit()
        self._entry_codec.setFixedSize(100, 20)
        self._entry_codec.textChanged.connect(self.make_col)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self._col, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_col, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._datatype, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_datatype, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._func, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_func, alignment=Qt.AlignLeft)
        hlayout1.addWidget(self._codec, alignment=Qt.AlignRight)
        hlayout1.addWidget(self._entry_codec, alignment=Qt.AlignLeft)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self._nullable, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self._ordered, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self._partitioned, alignment=Qt.AlignCenter)
        hlayout2.addWidget(self._sampled, alignment=Qt.AlignCenter)

        vlayout = QVBoxLayout()

        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

        is_nullable = 1 if self._nullable.isChecked() else 0
        self.new_col = Columns(col_name=self._entry_col.text(),
                               data_type=self._entry_datatype.currentText(),
                               nullable=is_nullable,
                               function=self._entry_func.text(),
                               codec=self._entry_codec.text())

    def make_col(self):
        is_nullable = 1 if self._nullable.isChecked() else 0
        self.new_col = Columns(col_name=self._entry_col.text(),
                               data_type=self._entry_datatype.currentText(),
                               nullable=is_nullable,
                               function=self._entry_func.text(),
                               codec=self._entry_codec.text())
