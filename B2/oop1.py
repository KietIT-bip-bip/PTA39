# oop: object-oriented promgramming
# tao lop vat nuoi(giong, mau sac, tuoi, can nang)

# VatNuoi: kieu du lieu tham chieu (doi tuong)
class VatNuoi:
    # khai bao thuoc tinh
    def __init__(self, giong="", mauSac="", tuoi=0, canNang=0):
        # __ : private
        self.__giong = giong
        self.__mauSac = mauSac
        self.__tuoi = tuoi
        self.__canNang = canNang
        
    def __str__(self) -> str:
        return f"VatNuoi: {self.__giong}, {self.__mauSac}, {self.__tuoi}, {self.__canNang}"
        
    # getter va setter (lay va cai dat gia tri thuoc tinh)
    # "get"/"set" + ten thuoc tinh
    def getGiong (self):
        return self.__giong
    
    def getMauSac (self):
        return self.__mauSac
    
    def getTuoi (self):
        return self.__tuoi
    
    def getCanNang (self):
        return self.__canNang
    
    def setGiong (self, giongMoi):
        if giongMoi == "": print("Gia tri khong duoc de trong")
        else: self.__giong = giongMoi
        
    def setMauSac (self, mauSacMoi):
        if mauSacMoi == "": print("Gia tri khong duoc de trong")  
        else: self.__mauSac = mauSacMoi
    
    def setTuoi (self, tuoiMoi):
        if tuoiMoi < 0: print("Gia tri khong duoc la so am")  
        else: self.__tuoi = tuoiMoi
    
    def setCanNang (self, canNangMoi):
        if canNangMoi < 0: print("Gia tri khong duoc la so am")  
        else: self.__canNang = canNangMoi
     
# tao doi tuong
meo1 = VatNuoi("meo", "den")
print(meo1)

# gan gia tri cho thuoc tinh
print(meo1.getTuoi())
meo1.setTuoi(tuoiMoi=2)

meo1.setCanNang(canNangMoi=3.5)
print(meo1.getCanNang())

print(meo1)