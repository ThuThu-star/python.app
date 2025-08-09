class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
hcn = HinhChuNhat(10, 4)
print("Chu vi:", hcn.tinh_chu_vi())