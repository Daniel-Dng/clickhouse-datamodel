# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from  PyQt5 import QtGui,QtCore
# import sys
#
#
# class ColumnArea(QWidget):
#     def __init__(self, parent=None):
#         super(ColumnArea, self).__init__(parent)
#         self._col = QLabel('Column Name')
#         self._col.setFixedSize(80, 20)
#         self._col.setAlignment(Qt.AlignRight)
#         self._entry_col = QLineEdit()
#         self._entry_col.setFixedSize(100, 20)
#
#         self._nullable = QCheckBox('Nullable')
#         self._nullable.setFixedSize(100, 20)
#         # self._nullable.setFont()
#
#         self._datatype = QLabel('Data Type')
#         self._datatype.setFixedSize(50, 20)
#         self._datatype.setAlignment(Qt.AlignRight)
#         self._entry_datatype = QLineEdit()
#         self._entry_datatype.setFixedSize(100, 20)
#
#         self._func = QLabel('Function')
#         self._func.setFixedSize(50, 20)
#         self._func.setAlignment(Qt.AlignRight)
#         self._entry_func = QLineEdit()
#         self._entry_func.setFixedSize(100, 20)
#
#         self._codec = QLabel('CODEC')
#         self._codec.setFixedSize(50, 20)
#         self._codec.setAlignment(Qt.AlignRight)
#         self._entry_codec = QLineEdit()
#         self._entry_codec.setFixedSize(100, 20)
#
#
#         layout = QHBoxLayout()
#         layout.addWidget(self._col)
#         layout.addWidget(self._entry_col)
#         layout.addWidget(self._nullable)
#         layout.addWidget(self._datatype)
#         layout.addWidget(self._entry_datatype)
#         layout.addWidget(self._func)
#         layout.addWidget(self._entry_func)
#         layout.addWidget(self._codec)
#         layout.addWidget(self._entry_codec)
#         self.setLayout(layout)
#
#
#
# class Main(QMainWindow):
#     def __init__(self, parent = None):
#         super(Main, self).__init__(parent)
#
#         # main button
#         self.column = ColumnArea(self)
#
#
#
# app = QApplication(sys.argv)
# myWidget = Main()
# myWidget.show()
# app.exec_()
