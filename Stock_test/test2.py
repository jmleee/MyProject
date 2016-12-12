import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        self.text_edit=QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 200, 80)
        self.text_edit.setEnabled(False)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.kiwoom.OnEventConnect.connect(self._OnEventConnect)

    def _OnEventConnect(self, ErrCode):
        if ErrCode == 0:
            self.text_edit.append("Login success")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()