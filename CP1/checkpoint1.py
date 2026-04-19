class HocSinh:
    # 1. khởi tạo hàm
    def __init__(self, ho_ten, dia_chi, chieu_cao, can_nang):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = "Chưa xếp loại" 

    # cập nhặt địa chỉ mới
    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print(f"--- Đã cập nhật địa chỉ mới cho {self.ho_ten} ---")

    # cập nhật chiều cao và cân nặng mới
    def kham_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print(f"--- Đã cập nhật chỉ số sức khỏe cho {self.ho_ten} ---")

    #  show thông tin học sinh
    def hien_thi_thong_tin(self):
        print("---------- THÔNG TIN HỌC SINH ----------") # hehehhe cái này đẹp thí :D
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Địa chỉ:   {self.dia_chi}")
        print(f"Chiều cao: {self.chieu_cao} cm")
        print(f"Cân nặng:  {self.can_nang} kg")
        print(f"Học lực:   {self.hoc_luc}")
        print("----------------------------------------")

# kiểm thử
# khời tạo 1 đối tượng học sinh bất kì
ban_an = HocSinh("Nguyễn Văn An", "123 Đường ABC, Quận 1", 165, 55)

# show thông tin ba đầu
ban_an.hien_thi_thong_tin()

# cập nhật địa chỉ mà An chuyển nhà
ban_an.cap_nhat_dia_chi("456 Đường XYZ, Quận 3")

# cập nhật sức khỏe sau kỳ khám
ban_an.kham_suc_khoe(168, 58)

# show lại thông tin sau khi cập nhật
ban_an.hien_thi_thong_tin()