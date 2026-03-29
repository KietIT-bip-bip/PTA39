# oop: object-oriented promgramming
# tao lop vat nuoi ( giong, mau sac, tuoi, can nang)
class VatNuoi :
    #khai bao thuoc tinh
    def __init__(self, giong="", mauSac="", tuoi=0, canNang=0) :
        #__: private
        self.__giong = giong
        self.__mauSac = mauSac
        self.__tuoi = tuoi
        self.__canNang = canNang

    def __str__(self) -> str:
        return f"VatNuoi: { self.__giong}, {self.__mauSac}, {self.__tuoi}, {self.__canNang}"
    
    # getter va setter ( lay va cai dat gia tri thuoc tinh  )
    # get/set + ten thuoc tinh
    def getGiong (self):
        return self.__giong
    
    def getMauSac (self):
        return self.__mauSac
    
    def getTuoi (self):
        return self.__tuoi
    
    def getCanNang (self):
        return self.__canNang
    
    def setGiong (self, GiongMoi):
        self.__giong = GiongMoi
    
    def setMauSac (self, mauSacMoi):
        self.__mauSac = mauSacMoi
    
    def setTuoi (self, TuoiMoi):
        self.__tuoi = TuoiMoi
    
    def setCanNang (self, CanNangMoi):
        self.__canNang = CanNangMoi
#tao doi tuong
meo1 = VatNuoi("meo", "den")
print(meo1 )