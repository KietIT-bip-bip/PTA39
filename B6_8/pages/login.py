from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re  
#mock data
account = {"fullname": "Kiet", "email": "abc@gmail.com", "password": "123"}

class LoginPage(QMainWindow):   
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir
                
        # load file ui
        ui_path = self.root_dir + "/GUI/login.ui"
        uic.loadUi(ui_path, self)  

        # bat su kien cho cac nut bam
        # 1. nut login
        self.login.clicked.connect(self.handle_login) # click vao nut login -> goi ham handle_login

        # 2. nut chuyen register
        self.nav_register.clicked.connect(self.goto_register) # click vao nut chuyen register

        # chay app
        self.show()



    #-----------------------------# xu ly xu kien--------------------------------
    def handle_login(self):
           # lay du lieu tu input form
            email_input = self.email.text().strip() # lay du lieu tu email input, xoa khoang
            password_input = self.password.text()
            # validate du lieu


    def goto_register(self):
        from pages.register import RegisterPage
        register_page = RegisterPage(main_window=self.main_window,
                                     root_dir=self.root_dir)

    #------------------------------ham ho o (private) -----------------------------------------
    def __goto_home(self):
        from pages.home import HomePage
        home_page = HomePage(main_window=self.main_window,
                                     root_dir=self.root_dir)

    def __validate_input(self, email, password):
        #kim tra email
        regex = r'^[a-zA-ZO-9._%+-]+@[a-zA-ZO-9.-]+\.[a-zA-Z]{2,}S'
        if re.fullmatch(regex, email) is None:
            return " Email khong hop le!"
        
        # kiem tra password 
        if len(password ) < 6:
            return " Passsword phai tu 6 chu so tro len!"

        # kiem tra mock data
        if email != account['email'] or password != account['password']:
            return " Email hoac Password khong chinh xac"
        return None # hop le, khong co loi
    
    def show_message(self):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Đây là nội dung thông báo của bạn!")
        msg.setIcon(QMessageBox.Icon.Information) # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok) # Nút bấm OK
        
        # Hiển thị hộp thoại
        msg.exec()