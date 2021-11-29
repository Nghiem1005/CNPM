from my_app import app
from my_app.models import Diem, HocSinh, LopHoc, MonHoc

def get_hocsinh(malop=None):
    hocsinhs = HocSinh.query
    if malop:
        hocsinhs = hocsinhs.join(LopHoc, HocSinh.maLopHoc==LopHoc.MaLopHoc).filter(LopHoc.TenLop.contains(malop))
    return hocsinhs.all()


def get_Allhocsinh(malop=None):
    hocsinhs  = HocSinh.query
    if malop:
        hocsinhs = hocsinhs.join(LopHoc, HocSinh.MaHocSinh==LopHoc.MaLopHoc).filter(LopHoc.TenLop.contains(malop))
    return hocsinhs.all()

