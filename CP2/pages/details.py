from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

class DetailsPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        
        # load file ui
        ui_path = self.root_dir + "/GUI/deltail.ui"
        uic.loadUi(ui_path, self)
        
        #  bat su kien chuyen close ve detail
        if hasattr(self, 'closeButton'):
            self.closeButton.clicked.connect(self.back_to_home)
        
        # hien thi giao dien
        self.show()
        
    # ham close -> detail
    def back_to_home(self):
        """Hàm xử lý khi nhấn Close: Ẩn trang detail và hiện lại trang Home"""
        self.close()             # Đóng/Ẩn cửa sổ chi tiết hiện tại
        self.main_window.show()   # Kích hoạt hiện lại cửa sổ HomePage (main_window)
