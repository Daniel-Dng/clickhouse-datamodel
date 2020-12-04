# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QScrollArea, QLabel)
# from PyQt5.QtCore import QEvent
#
#
# class TestWindow(QWidget):
#     def __init__(self):
#         super(TestWindow, self).__init__()
#         self.resize(800, 600)
#         self.move(0, 0)
#         # self.setMouseTracking(False)
#         self.last_time_move = 0
#         self.initUI()
#
#     def initUI(self):
#         self.scroll_area = QScrollArea(self)
#         self.scroll_area.setGeometry(0, 0, 800, 600)
#         self.scroll_area.setWidgetResizable(True)
#         self.scroll_bar = self.scroll_area.verticalScrollBar()
#
#         self.scroll_contents = QWidget()
#         self.scroll_contents.setGeometry(0, 0, 400, 800)
#         self.scroll_contents.setMinimumSize(380, 1000)
#
#         self.label_1 = QLabel(self.scroll_contents)
#         self.label_1.move(50, 100)
#         self.label_1.setText("HelloRyan")
#
#         self.label_2 = QLabel(self.scroll_contents)
#         self.label_2.move(50, 200)
#         self.label_2.setText("hello")
#
#         self.label_3 = QLabel(self.scroll_contents)
#         self.label_3.move(50, 300)
#         self.label_3.setText("-----------")
#
#         self.label_4 = QLabel(self.scroll_contents)
#         self.label_4.move(50, 400)
#         self.label_4.setText("542543255235432543252")
#
#         self.label_5 = QLabel(self.scroll_contents)
#         self.label_5.move(50, 500)
#         self.label_5.setText("5432543262542")
#
#         self.label_6 = QLabel(self.scroll_contents)
#         self.label_6.move(50, 600)
#         self.label_6.setText("4325432532")
#
#         self.scroll_area.setWidget(self.scroll_contents)
#         self.scroll_area.installEventFilter(self)
#
#     # def mouseMoveEvent(self, event):
#     # 	if event.pos().x() > 0 and event.pos().x() < 400 and event.pos().y() > 0 and event.pos().y() < 400:
#     # 		if self.last_time_move == 0:
#     # 			self.last_time_move = event.pos().y()
#     # 		distance = self.last_time_move - event.pos().y()
#     # 		self.scroll_bar.setValue(self.scroll_bar.value() + distance)
#     # 		self.last_time_move = event.pos().y()
#     # 		print("move%d" % event.pos().y())
#     # def mouseReleaseEvent(self, event):
#     # 	self.last_time_move = 0
#     # 	print("up")
#
#     def eventFilter(self, source, event):
#         if event.type() == QEvent.MouseMove:
#             print(event.pos().y())
#             if self.last_time_move == 0:
#                 self.last_time_move = event.pos().y()
#             distance = self.last_time_move - event.pos().y()
#             self.scroll_bar.setValue(self.scroll_bar.value() + distance)
#             self.last_time_move = event.pos().y()
#         elif event.type() == QEvent.MouseButtonRelease:
#             self.last_time_move = 0
#         return QWidget.eventFilter(self, source, event)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     test = TestWindow()
#     test.show()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5 import QtGui, QtCore
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
# class Window(QMainWindow):
#
#     def __init__(self):
#         super(Window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle("PyQT tuts!")
#         # self.setWindowIcon(QIcon('pythonlogo.png'))
#
#         extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
#         extractAction.setShortcut("Ctrl+Q")
#         extractAction.setStatusTip('Leave The App')
#         extractAction.triggered.connect(self.close_application)
#
#         openEditor = QAction("&Editor", self)
#         openEditor.setShortcut("Ctrl+E")
#         openEditor.setStatusTip('Open Editor')
#         openEditor.triggered.connect(self.editor)
#
#         openFile = QAction("&Open File", self)
#         openFile.setShortcut("Ctrl+O")
#         openFile.setStatusTip('Open File')
#         openFile.triggered.connect(self.file_open)
#
#         saveFile = QAction("&Save File", self)
#         saveFile.setShortcut("Ctrl+S")
#         saveFile.setStatusTip('Save File')
#         saveFile.triggered.connect(self.file_save)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#
#         fileMenu = mainMenu.addMenu('&File')
#         fileMenu.addAction(extractAction)
#         fileMenu.addAction(openFile)
#         fileMenu.addAction(saveFile)
#
#         editorMenu = mainMenu.addMenu("&Editor")
#         editorMenu.addAction(openEditor)
#
#         self.home()
#
#     def home(self):
#         btn = QPushButton("Quit", self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.minimumSizeHint())
#         btn.move(0, 100)
#
#         # extractAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
#         # extractAction.triggered.connect(self.close_application)
#         self.toolBar = self.addToolBar("Extraction")
#         # self.toolBar.addAction(extractAction)
#
#         fontChoice = QAction('Font', self)
#         fontChoice.triggered.connect(self.font_choice)
#         # self.toolBar = self.addToolBar("Font")
#         self.toolBar.addAction(fontChoice)
#
#         color = QtGui.QColor(0, 0, 0)
#
#         fontColor = QAction('Font bg Color', self)
#         fontColor.triggered.connect(self.color_picker)
#
#         self.toolBar.addAction(fontColor)
#
#         checkBox = QCheckBox('Enlarge Window', self)
#         checkBox.move(300, 25)
#         checkBox.stateChanged.connect(self.enlarge_window)
#
#         self.progress = QProgressBar(self)
#         self.progress.setGeometry(200, 80, 250, 20)
#
#         self.btn = QPushButton("Download", self)
#         self.btn.move(200, 120)
#         self.btn.clicked.connect(self.download)
#
#         # print(self.style().objectName())
#         self.styleChoice = QLabel("Windows Vista", self)
#
#         comboBox = QComboBox(self)
#         comboBox.addItem("motif")
#         comboBox.addItem("Windows")
#         comboBox.addItem("cde")
#         comboBox.addItem("Plastique")
#         comboBox.addItem("Cleanlooks")
#         comboBox.addItem("windowsvista")
#
#         comboBox.move(50, 250)
#         self.styleChoice.move(50, 150)
#         comboBox.activated[str].connect(self.style_choice)
#
#         cal = QCalendarWidget(self)
#         cal.move(500, 200)
#         cal.resize(200, 200)
#
#         self.show()
#
#     def file_open(self):
#         name = QFileDialog.getOpenFileName(self, 'Open File')
#         file = open(name, 'r')
#
#         self.editor()
#
#         with file:
#             text = file.read()
#             self.textEdit.setText(text)
#
#     def file_save(self):
#         name = QFileDialog.getSaveFileName(self, 'Save File')
#         file = open(name, 'w')
#         text = self.textEdit.toPlainText()
#         file.write(text)
#         file.close()
#
#     def color_picker(self):
#         color = QColorDialog.getColor()
#         self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
#
#     def editor(self):
#         self.textEdit = QTextEdit()
#         self.setCentralWidget(self.textEdit)
#
#     def font_choice(self):
#         font, valid = QFontDialog.getFont()
#         if valid:
#             self.styleChoice.setFont(font)
#
#     def style_choice(self, text):
#         self.styleChoice.setText(text)
#         QApplication.setStyle(QStyleFactory.create(text))
#
#     def download(self):
#         self.completed = 0
#
#         while self.completed < 100:
#             self.completed += 0.0001
#             self.progress.setValue(self.completed)
#
#     def enlarge_window(self, state):
#         if state == QtCore.Qt.Checked:
#             self.setGeometry(50, 50, 1000, 600)
#         else:
#             self.setGeometry(50, 50, 500, 300)
#
#     def close_application(self):
#         choice = QMessageBox.question(self, 'Extract!',
#                                             "Get into the chopper?",
#                                             QMessageBox.Yes | QMessageBox.No)
#         if choice == QMessageBox.Yes:
#             print("Extracting Naaaaaaoooww!!!!")
#             sys.exit()
#         else:
#             pass
#
#
# def run():
#     app = QApplication(sys.argv)
#     GUI = Window()
#     sys.exit(app.exec_())
#
#
# run()