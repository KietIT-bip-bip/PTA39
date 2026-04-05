#lop con 1
from lopCHa import Xe


class XeDap(Xe):
    def __int__(self, hang="", mauSac="",giaTien=0):
        super().__init__(hang, mauSac,giaTien)

    #override
    def run(self):
        #goi lai thuoc tinh PRIVATE cua lop cha
        hang = self.Xe__hang
        return f"Xe {hang} dang duoc dap"
    
# tao object
xeDap1 = XeDap("Hang 1", "Xanh la + Tim", 1000)
print(xeDap1) # ham duoc ke thua tu lop Xe
print(xeDap1.khoiDong()) # ham duoc ke thua tu lop Xe
print(xeDap1.run()) # ham duoc override tu lop Xe
