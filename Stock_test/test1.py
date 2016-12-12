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

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btn1 = QPushButton("Login", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Check state", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        print("chech1")
        i = self.kiwoom.dynamicCall("CommConnect()")
        print("check2")
        print(i)
        ret = i


    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 1:
            self.statusBar().showMessage("Connected")
        else :
            self.statusBar().showMessage("Not Connected")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


