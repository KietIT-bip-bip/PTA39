from quanlydiem import QuanLyDiemHocSinh

hs1 = QuanLyDiemHocSinh("Nguyen Van A", "12A1", "THPT Nguyen Hue", 8, 7, 9)
hs2 = QuanLyDiemHocSinh("Nguyen Van B", "12A1", "THPT Nguyen Hue", 2, 5, 5)
hs3 = QuanLyDiemHocSinh("Nguyen Van C", "12A1", "THPT Nguyen Hue", 10, 9.5, 10)
hs4 = QuanLyDiemHocSinh("Nguyen Van D", "12A1", "THPT Nguyen Hue", 7, 10, 10)
hs5 = QuanLyDiemHocSinh("Nguyen Van E", "12A1", "THPT Nguyen Hue", 6, 4, 6)
hs6 = QuanLyDiemHocSinh("Nguyen Van F", "12A1", "THPT Nguyen Hue", 10, 10, 9.5)
# hien thi hs dung nhat
# tim diem so tb cao nhat
diemTBMax = max(
    hs1.tinhDiemTrungBinh(),
    hs2.tinhDiemTrungBinh(),
    hs3.tinhDiemTrungBinh(),
    hs4.tinhDiemTrungBinh(),
    hs5.tinhDiemTrungBinh(),
    hs6.tinhDiemTrungBinh(),
)
# hien thi hs co diem cao nhat
for hs in [hs1, hs2, hs3, hs4, hs5, hs6]: # duyet danh sach hoc sinh
    if (hs.tinhDiemTrungBinh()== diemTBMax): # neu diem hs tb hien tai = max
        print(hs)