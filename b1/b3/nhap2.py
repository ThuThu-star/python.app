class HocSinh:
    def __init__(self, HoTen, DiaChi, ChieuCao, CanNang, HocLuc):
        self.HoTen = HoTen
        self.DiaChi = DiaChi
        self.ChieuCao = ChieuCao
        self.CanNang = CanNang
        self.HocLuc = HocLuc

    def cap_nhap_dia_chi(self, dia_chi_moi):
        self.DiaChi = dia_chi_moi

    def cap_nhap_suc_khoe(self, suc_khoe_moi):
        self.ChieuCao = chieu_cao_moi
        self.CanNang = can_nanh_moi

hs1 = HocSinh("Nguyễn Văn A", "Thành phố Hồ Chí Minh", 155, 50, "Khá")
print(hs1.HoTen)
print(hs1.DiaChi)
print(hs1.ChieuCao)
print(hs1.CanNang)
print(hs1.HocLuc)


