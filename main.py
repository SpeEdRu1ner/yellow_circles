import sys

from UI import Ui_MainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow, Ui_MainWindow):
    button: QPushButton
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.paint_circle)

    def paint_circle(self):

        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        size = randint(5, 500)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(30, 100, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())