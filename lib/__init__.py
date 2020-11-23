# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
# # Only needed for access to command line arguments
# import sys
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.setWindowTitle("My Awesome App")
#
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText("Enter your text")
#
#         #widget.setReadOnly(True) # uncomment this to make readonly
#
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)
#
#         self.setCentralWidget(widget)
#
#
#     def return_pressed(self):
#         print("Return pressed!")
#         self.centralWidget().setText("BOOM!")
#
#     def selection_changed(self):
#         print("Selection changed")
#         print(self.centralWidget().selectedText())
#
#     def text_changed(self, s):
#         print("Text changed...")
#         print(s)
#
#     def text_edited(self, s):
#         print("Text edited...")
#         print(s)
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show() # IMPORTANT!!!!! Windows are hidden by default.
#
# # Start the event loop.
# app.exec_()
#
