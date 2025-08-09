class HinhVuong:
    def __init__(self, canh):
        self.canh = canh

    def tinh_chu_vi(self):
        return 4 * self.canh
    
hv = HinhVuong(3)
print(hv.tinh_chu_vi())