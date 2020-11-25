import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QScrollArea, QLabel)
from PyQt5.QtCore import QEvent


class TestWindow(QWidget):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.resize(800, 600)
        self.move(0, 0)
        # self.setMouseTracking(False)
        self.last_time_move = 0
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(0, 0, 400, 400)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_bar = self.scroll_area.verticalScrollBar()

        self.scroll_contents = QWidget()
        self.scroll_contents.setGeometry(0, 0, 400, 800)
        self.scroll_contents.setMinimumSize(380, 1000)

        self.label_1 = QLabel(self.scroll_contents)
        self.label_1.move(50, 100)
        self.label_1.setText("HelloRyan")

        self.label_2 = QLabel(self.scroll_contents)
        self.label_2.move(50, 200)
        self.label_2.setText("hello")

        self.label_3 = QLabel(self.scroll_contents)
        self.label_3.move(50, 300)
        self.label_3.setText("-----------")

        self.label_4 = QLabel(self.scroll_contents)
        self.label_4.move(50, 400)
        self.label_4.setText("542543255235432543252")

        self.label_5 = QLabel(self.scroll_contents)
        self.label_5.move(50, 500)
        self.label_5.setText("5432543262542")

        self.label_6 = QLabel(self.scroll_contents)
        self.label_6.move(50, 600)
        self.label_6.setText("4325432532")

        self.scroll_area.setWidget(self.scroll_contents)
        self.scroll_area.installEventFilter(self)

    # def mouseMoveEvent(self, event):
    # 	if event.pos().x() > 0 and event.pos().x() < 400 and event.pos().y() > 0 and event.pos().y() < 400:
    # 		if self.last_time_move == 0:
    # 			self.last_time_move = event.pos().y()
    # 		distance = self.last_time_move - event.pos().y()
    # 		self.scroll_bar.setValue(self.scroll_bar.value() + distance)
    # 		self.last_time_move = event.pos().y()
    # 		print("move%d" % event.pos().y())
    # def mouseReleaseEvent(self, event):
    # 	self.last_time_move = 0
    # 	print("up")

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove:
            print(event.pos().y())
            if self.last_time_move == 0:
                self.last_time_move = event.pos().y()
            distance = self.last_time_move - event.pos().y()
            self.scroll_bar.setValue(self.scroll_bar.value() + distance)
            self.last_time_move = event.pos().y()
        elif event.type() == QEvent.MouseButtonRelease:
            self.last_time_move = 0
        return QWidget.eventFilter(self, source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TestWindow()
    test.show()
    sys.exit(app.exec_())
