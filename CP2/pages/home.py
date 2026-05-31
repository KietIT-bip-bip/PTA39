from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from pages.details import DetailsPage
class HomePage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        
        # load file ui
        ui_path = self.root_dir + "/GUI/home.ui"
        uic.loadUi(ui_path, self)
        
        #  bat su kien chuyen close ve home 
        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.go_to_detail) 
        
        # hien thi giao dien
        self.show()
        
    #  ham close -> home
    def go_to_detail(self):
        """Hàm xử lý khi nhấn nút chỉnh sửa: Ẩn trang Home và mở trang Detail"""
        self.hide() # Ẩn trang HomePage hiện tại đi

        self.detail_page = DetailsPage(main_window=self, root_dir=self.root_dir)