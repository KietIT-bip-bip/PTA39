from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from PyQt6 import uic

class Home (QMainWindow):
    def __init__(self):
        super().__init__()  # ke thua cac thuoc tinh tu lop QmainWindow
        # load file giao dien
        uic.loadUi("B4/home.ui",self)
        #chay app
        self.show()

# khai bao 1 lan duy nhat
app = QApplication(sys.argv)
home = Home() 
sys.exit(app.exec())
