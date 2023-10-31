import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def run(self, qp):
        h = -150
        for i in range(2):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            size = randint(10, 150)
            h += 150
            qp.drawEllipse(150, h, size, size)


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
