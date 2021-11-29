from my_app import db
from sqlalchemy import Float, ForeignKey, Boolean, Column, NCHAR, String, Integer, NVARCHAR, \
    DateTime, Numeric, PrimaryKeyConstraint
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


class LopHoc(db.Model):
    __tablename__ = "LopHoc"
    MaLopHoc = Column(Integer, primary_key=True, autoincrement=True)
    TenLop = Column(NVARCHAR(50), nullable=False)
    SiSo = Column(Integer, nullable=False)

    def __str__(self):
        return self.TenLop


class HocSinh(db.Model):
    __tablename__ = "HocSinh"
    MaHocSinh = Column(Integer, primary_key=True, autoincrement=True)
    TenHocSinh = Column(NVARCHAR(50), nullable=False)
    NgaySinh = Column(DateTime, nullable=False)
    GioiTinh = Column(NVARCHAR(50), nullable=False)
    Email = Column(String(50), nullable=True)
    Anh = Column(NVARCHAR(50), nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='HocSinh', lazy=True)
    diaChi = relationship('DiaChiHS', backref='HocSinh', lazy=True)
    taiKhoan = relationship('TaiKhoan', backref='HocSinh', lazy=True)

    def __str__(self):
        return self.TenHocSinh


class HocKy(db.Model):
    __tablename__ = "HocKy"
    MaHocKy = Column(Integer, primary_key=True, autoincrement=True)
    TenHocKy = Column(Integer, nullable=False)

    def __str__(self):
        return self.TenHocKy





class TaiKhoan(db.Model, UserMixin):
    __tablename__ = "TaiKhoan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    roles = Column(Integer, nullable=False)  # 1: Admin
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)

    def __str__(self):
        return self.username


class DiaChiHS(db.Model):
    __tablename__ = "DiaChiHS"
    MaDiaChi = Column(Integer, primary_key=True, autoincrement=True)
    PhuongXa = Column(NVARCHAR(50), nullable=False)
    QuanHuyen = Column(NVARCHAR(50), nullable=False)
    TinhThanhPho = Column(NVARCHAR(50), nullable=False)
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)

    def __str__(self):
        return "Phường: " + self.PhuongXa + ", " + self.TinhThanhPho


class Diem(db.Model):
    __tablename__ = "Diem"
    MaDiem = Column(Integer, primary_key=True, autoincrement=True)
    LoaiDiem = Column(NVARCHAR(50), nullable=False)
    SoDiem = Column(Float, nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='Diem', lazy=True)

    def __str__(self):
        return "Loại điểm: " + str(self.LoaiDiem) + ", SoDiem: " + str(self.SoDiem)


class MonHoc(db.Model):
    __tablename__ = "MonHoc"
    MaMonHoc = Column(Integer, primary_key=True, autoincrement=True)
    TenMonHoc = Column(NVARCHAR(50), nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='MonHoc', lazy=True)

    def __str__(self):
        return self.TenMonHoc


class DiemMonHocHocSinh(db.Model):
    __tablename__ = "DiemMonHocHocSinh"
    __table_args__ = {'extend_existing': True}
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)
    maDiem = Column(Integer, ForeignKey(Diem.MaDiem), nullable=False)
    maMonHoc = Column(Integer, ForeignKey(MonHoc.MaMonHoc), nullable=False)
    db.PrimaryKeyConstraint(maHocSinh, maDiem, maMonHoc)

    def __str__(self):
        return self.maHocSinh


class HocSinhLopHoc(db.Model):
    __tablename__ = "LopHocHocSinh"
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)
    maHocKy = Column(Integer, ForeignKey(HocKy.MaHocKy), nullable=False)
    maLopHoc = Column(Integer, ForeignKey(LopHoc.MaLopHoc), nullable=False)
    db.PrimaryKeyConstraint(maHocSinh, maHocKy, maLopHoc)

    def __str__(self):
        return self.maHocSinh


if __name__ == '__main__':
    db.create_all()
