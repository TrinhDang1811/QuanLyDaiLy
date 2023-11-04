import pyodbc
import os
from DTO import*
from datetime import datetime
ODBC_spec  = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
connect_key = "Driver={}; Server=localhost; Database=TEST_QLCDL; Trusted_Connection=yes;".format(ODBC_spec[0])

KetNoiCSDL = pyodbc.connect(connect_key)

Contro = KetNoiCSDL.cursor()
Contro.execute('SET DATEFORMAT DMY')
Contro.commit()

class TruyCapCSDL:
    def KiemTraTKCSDL(*args):
        NguoiDung = None
        Contro.execute("EXEC Proc_DangNhap @TK = ?, @MK = ?", (args[0], args[1]))
        BanGhi = Contro.fetchall()
        if BanGhi:
            NguoiDung = BanGhi
        else:
            return 'Tai Khoan Hoac Mat Khau Khong Chinh Xac'
        return NguoiDung

class TaiKhoanDangNhap:
    def KiemTraTK(*args):
        KetQua = TruyCapCSDL.KiemTraTKCSDL(args[1], args[2])
        return KetQua
    def ChangePassword(*args):
        Contro.execute("UPDATE TAIKHOAN SET MATKHAU = ? WHERE TENTAIKHOAN = ?", args[1], args[0])
        Contro.commit()
        return True

class DALdsDaiLy:
    # Get Values

    def GetDSDaiLy():
        Contro.execute('SELECT * FROM DAILY')
        Res = Contro.fetchall()
        return Res

    def GetMaDaiLy():
        Contro.execute('SELECT MaDaiLy FROM DAILY')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaLDL():
        Contro.execute('SELECT MaLoaiDaiLy FROM DAILY')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaQuan():
        Contro.execute('SELECT MaQuan FROM DAILY')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst
    
    def GetTienNo(*args):
        Contro.execute('SELECT SoTienNo FROM DAILY WHERE MaDaiLy = ?', (args[0]))
        Res = Contro.fetchall()
        return Res[0][0]

    def GetSLDaiLy():
        Contro.execute('SELECT COUNT(MaDaiLy) FROM DAILY')
        Res = Contro.fetchall()
        return str(Res[0][0])
    
    def GetDsDT():
        Contro.execute('SELECT DIENTHOAI FROM DAILY')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDsDT_Update():
        Contro.execute('SELECT MADAILY, DIENTHOAI FROM DAILY')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDsTenDL_Update(*args):
        Contro.execute('SELECT MADAILY, TENDAILY FROM DAILY WHERE MAQUAN = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDsTenDL_Insert(*args):
        Contro.execute('SELECT TENDAILY FROM DAILY WHERE MAQUAN = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDsDC():
        Contro.execute('SELECT DIACHI FROM DAILY')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res

    def GetDsDC_Update():
        Contro.execute('SELECT MADAILY, DIACHI FROM DAILY')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetTenDaiLy(*args):
        Contro.execute('SELECT TENDAILY FROM DAILY WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDienThoai(*args):
        Contro.execute('SELECT DIENTHOAI FROM DAILY WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetDiaChi(*args):
        Contro.execute('SELECT DIACHI FROM DAILY WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetNTN(*args):
        Contro.execute('SELECT NGAYTIEPNHAN FROM DAILY WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetMaDaiLy_MaQuan(*args):
        Contro.execute('SELECT MADAILY FROM DAILY WHERE MAQUAN = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def GetNgayTiepNhan(*args):
        Contro.execute('SELECT NgayTiepNhan FROM DAILY WHERE MaDaiLy = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    # Add Values
    def AddDSDaiLy(*args):
        Contro.execute('INSERT INTO DAILY VALUES(?,?,?,?,?,?,?,?)',
                       (args[0], args[1], args[2], args[3], args[4], args[5], args[6], None))
        Contro.commit()

    # Remove Values
    def RemoveDSDaiLy(*args):
        Contro.execute('DELETE FROM DAILY WHERE MaDaiLy = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSDaiLy(*args):
        Contro.execute('''UPDATE DAILY SET TenDaiLy = ?, MaLoaiDaiLy = ?, DienThoai = ?, 
                       DiaChi = ?, MaQuan = ?, NgayTiepNhan = ? WHERE MaDaiLy = ?''',
                       args[1], args[2], args[3], args[4], args[5], args[6], args[0])
        Contro.commit()

    # Finding Values
    def FindingDsDaiLy_Ngay(*args):
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        day(NgayTiepNhan) = ?
                        ''',
                        int(args[0]))
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsDaiLy_Thang(*args):
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        month(NgayTiepNhan) = ?
                        ''',
                        int(args[0]))
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsDaiLy_Nam(*args):
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        year(NgayTiepNhan) = ?
                        ''',
                        int(args[0]))
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
        
    def FindingDsDaiLy_MaDaiLy(*args):
        args1 = str(args[0])
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        MaDaiLy = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

    def FindingDsDaiLy_MaLDL(*args):
        args1 = str(args[0])
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE MaLoaiDaiLy = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
        
    def FindingDsDaiLy_Khac(*args):
        args1 = '%' + str(args[0]) + '%'
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        TenDaiLy like ?
                        OR Diachi like ?
                        OR DienThoai like ?
                        OR MaQuan = ?''',
                        args1, args1, args1, args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsDaiLy_TenDaiLy(*args):
        args1 = '%' + str(args[0]) + '%'
        Contro.execute('''SELECT MaDaiLy FROM DAILY 
                        WHERE 
                        TenDaiLy like ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
        
class DALdsLoaiDaiLy:
    # Get Values
    def GetDSLoaiDL():
        Contro.execute('SELECT * FROM LOAIDAILY')
        Res = Contro.fetchall()
        return Res

    def GetMaLoaiDL():
        Contro.execute('SELECT MaLoaiDaiLy FROM LOAIDAILY')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetSLLoaiDL():
        Contro.execute('SELECT COUNT(MaLoaiDaiLy) FROM LOAIDAILY')
        Res = Contro.fetchall()
        return str(Res[0][0])

    def GetTenLDL():
        Contro.execute('SELECT TENLOAIDAILY FROM LOAIDAILY')
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
    
    def GetTenLDL_Update():
        Contro.execute('SELECT MALOAIDAILY, TENLOAIDAILY FROM LOAIDAILY')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        return Res
    
    def Get1TenLDL(*args):
        Contro.execute('SELECT TENLOAIDAILY FROM LOAIDAILY WHERE MALOAIDAILY = ?', args[0])
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
    
    def Get1SoNoToiDa(*args):
        Contro.execute('SELECT SONOTOIDA FROM LOAIDAILY WHERE MALOAIDAILY = ?', args[0])
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
        
    # Add Values
    def AddDSLoaiDL(*args):
        Contro.execute('INSERT INTO LOAIDAILY VALUES(?, ?, ?)', (args[0], args[1], int(args[2])))
        Contro.commit()

    # Remove Values
    def RemoveDSLoaiDL(*args):
        Contro.execute('DELETE FROM LOAIDAILY WHERE MaLoaiDaiLy = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSLoaiDL(*args):
        Contro.execute('''UPDATE LOAIDAILY SET TenLoaiDaiLy = ?, SoNoToiDa = ?
                       WHERE MaLoaiDaiLy = ?''', (args[1], int(args[2]), args[0]))
        Contro.commit()

    def UpdateSN_LoaiDL(*args):
        Contro.execute("UPDATE LOAIDAILY SET SoNoToiDa = ? WHERE MaLoaiDaiLy = ?", (int(args[1]), args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_LDL(*args):
        args1 = "%" + str(args[0]) + "%"
        Contro.execute('''SELECT MaLoaiDaiLy FROM LOAIDAILY
                        WHERE 
                        MaLoaiDaiLy like ?
                        OR TenLoaiDaiLy like ?
                        OR SoNoToiDa like ? ''',
                        args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsQuan:
    # Get Values
    def GetDSQuan():
        Contro.execute('SELECT * FROM QUAN')
        Res = Contro.fetchall()
        return Res

    def GetMaQuan():
        Contro.execute('SELECT MaQuan FROM QUAN')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetSLQuan():
        Contro.execute('SELECT COUNT(MaQuan) FROM QUAN')
        Res = Contro.fetchall()
        return str(Res[0][0])

    def GetTenQuan():
        Contro.execute('SELECT TENQUAN FROM QUAN')
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
        
    def Get1TenQuan(*args):
        Contro.execute('SELECT TENQUAN FROM QUAN WHERE MAQUAN = ?', args[0])
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
        
    # Add Values
    def AddDSQuan(*args):
        Contro.execute('INSERT INTO QUAN VALUES(?, ?)', (args[0], args[1]))
        Contro.commit()

    # Remove Values
    def RemoveDSQuan(*args):
        Contro.execute('DELETE FROM QUAN WHERE MaQuan = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSQuan(*args):
        Contro.execute('UPDATE QUAN SET TenQuan = ? WHERE MaQuan = ?', (args[1], args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_Quan(*args):
        args1 = "%" + str(args[0]) + "%"
        Contro.execute('''SELECT MaQuan FROM QUAN 
                        WHERE 
                        MaQuan like ?
                        OR TenQuan like ? ''',
                        args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
        
class DALdsMatHang:
    # Get Values
    def GetDSMatHang():
        Contro.execute('SELECT * FROM MATHANG')
        Res = Contro.fetchall()
        return Res

    def GetMaMatHang():
        Contro.execute('SELECT MaMatHang FROM MATHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaDVT():
        Contro.execute('SELECT MaDVT FROM MATHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst
    
    def GetSoLuongTon(*args):
        Contro.execute('SELECT SoLuongTon FROM MATHANG WHERE MaMatHang = ?', (args[0]))
        Res = Contro.fetchall()
        return Res[0][0]

    def GetSLMatHang():
        Contro.execute('SELECT COUNT(MaMatHang) FROM MATHANG')
        Res = Contro.fetchall()
        return str(Res[0][0])

    def GetTenMatHang():
        Contro.execute('SELECT TENMATHANG FROM MATHANG')
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
        
    def GetTenMatHang_MaMH():
        Contro.execute('SELECT MAMATHANG, TENMATHANG FROM MATHANG')
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
    
    def Get1TenMatHang(*args):
        Contro.execute('SELECT TENMATHANG FROM MATHANG WHERE MAMATHANG = ?', args[0])
        Res = Contro.fetchall()
        if Res == []:
            return 0
        else:
            return Res
        
    # Add Values
    def AddDSMatHang(*args):
        Contro.execute('INSERT INTO MATHANG VALUES(?,?,?,?)', (args[0], args[1], args[2], None))
        Contro.commit()

    # Remove Values
    def RemoveDSMatHang(*args):
        Contro.execute('DELETE FROM MATHANG WHERE MaMatHang = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSMatHang(*args):
        Contro.execute('''UPDATE MATHANG SET TenMatHang = ?, MaDVT = ?
                       WHERE MaMatHang = ?''', (args[1], args[2], args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_MatHang(*args):
        args1 = "%" + str(args[0]) + "%"
        Contro.execute('''SELECT MaMatHang FROM MATHANG 
                        WHERE 
                        MaMatHang like ?
                        OR TenMatHang like ?
                        OR MaDVT like ? 
                        OR SoLuongTon like ?''',
                        args1, args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
        
class DALdsDVT:
    # Get Values
    def GetDSDVT():
        Contro.execute('SELECT * FROM DVT')
        Res = Contro.fetchall()
        return Res

    def GetMaDVT():
        Contro.execute('SELECT MaDVT FROM DVT')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetSLDVT():
        Contro.execute('SELECT COUNT(MaDVT) FROM DVT')
        Res = Contro.fetchall()
        return str(Res[0][0])
    
    def GetTenDVT():
        Contro.execute('SELECT TENDVT FROM DVT')
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        else:
            return Res

    def Get1TenDVT(*args):
        Contro.execute('SELECT TENDVT FROM DVT WHERE MADVT = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        else:
            return Res
    # Add Values
    def AddDSDVT(*args):
        Contro.execute('INSERT INTO DVT VALUES(?, ?)', (args[0], args[1]))
        Contro.commit()

    # Remove Values
    def RemoveDSDVT(*args):
        Contro.execute('DELETE FROM DVT WHERE MaDVT = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSDVT(*args):
        Contro.execute('UPDATE DVT SET TenDVT = ? WHERE MaDVT = ?', (args[1], args[0]))
        Contro.commit()
    
    # Finding Values
    def FindingDS_DVT(*args):
        args1 = "%" + str(args[0]) + "%"
        Contro.execute('''SELECT MaDVT FROM DVT
                        WHERE 
                        MaDVT like ?
                        OR TenDVT like ? ''',
                        args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsPNH:
    # Get Values
    def GetDSPhieuNH_Key(*args):
        Contro.execute('SELECT * FROM PHIEUNHAPHANG WHERE MaPhieuNhap = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSPhieuNH():
        Contro.execute('SELECT * FROM PHIEUNHAPHANG')
        Res = Contro.fetchall()
        return Res

    def GetMaPhieuNH():
        Contro.execute('SELECT MaPhieuNhap FROM PHIEUNHAPHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    # Add Values
    def AddDSPhieuNH(*args):
        Contro.execute('INSERT INTO PHIEUNHAPHANG VALUES(?, ?, ?)', (args[0], args[1], None))
        Contro.commit()

    # Remove Values
    def RemoveDSPhieuNH(*args):
        Contro.execute('DELETE FROM PHIEUNHAPHANG WHERE MaPhieuNhap = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSPhieuNH(*args):
        Contro.execute('''UPDATE PHIEUNHAPHANG SET NgayLapPhieu = ?
                           WHERE MaPhieuNhap = ?''', (args[1], args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_PNH(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MaPhieuNhap FROM PHIEUNHAPHANG
                        WHERE 
                        MaPhieuNhap like ?
                        OR NgayLapPhieu like ? 
                        OR TongTien like ? ''',
                        args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPNH_Ngay(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUNHAP FROM PHIEUNHAPHANG
                        WHERE 
                        day(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPNH_Thang(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUNHAP FROM PHIEUNHAPHANG
                        WHERE 
                        month(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPNH_Nam(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUNHAP FROM PHIEUNHAPHANG
                        WHERE 
                        year(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsCT_PNH:
    # Get Values
    def GetDSCT_PNH_Key(*args):
        Contro.execute('SELECT * FROM CT_PNH WHERE MaPhieuNhap = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSCT_PNH():
        Contro.execute('SELECT * FROM CT_PNH')
        Res = Contro.fetchall()
        return Res

    def GetMaCT_PNH():
        Contro.execute('SELECT MaCT_PNH FROM CT_PNH')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaPhieuNhap():
        Contro.execute('SELECT DISTINCT(MaPhieuNhap) FROM CT_PNH')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaMatHang():
        Contro.execute('SELECT DISTINCT(MaMatHang) FROM MATHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    # Add Values
    def AddDSCT_PNH(*args):
        Contro.execute('INSERT INTO CT_PNH VALUES(?,?,?,?,?,?)',
                       (args[0], args[1], args[2], int(args[3]), int(args[4]), None))
        Contro.commit()

    # Remove Values
    def RemoveDSCT_PNH(*args):
        Contro.execute('DELETE FROM CT_PNH WHERE MaCT_PNH = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSCT_PNH(*args):
        Contro.execute('''UPDATE CT_PNH SET MaMatHang=?, SoLuongNhap=?, DonGiaNhap=?
                        WHERE MACT_PNH = ?''',
                       (args[1], int(args[2]), int(args[3]), args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_PNH(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MaCT_PNH FROM CT_PNH
                        WHERE 
                        MaCT_PNH like ?
                        OR MaPhieuNhap like ?
                        OR MaMatHang like ?
                        OR SoLuongNhap like ?
                        OR DonGiaNhap like ? 
                        OR ThanhTien like ? ''',
                        args1, args1, args1,
                        args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsPXH:
    # Get Values
    def GetDSPhieuXH_Key(*args):
        Contro.execute('SELECT * FROM PHIEUXUATHANG WHERE MaDaiLy = ?', (args[0]))
        Res = Contro.fetchall()
        return Res

    def GetDSPhieuXH_Key1(*args):
        Contro.execute('SELECT * FROM PHIEUXUATHANG WHERE MaPhieuXuat = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSPhieuXH():
        Contro.execute('SELECT * FROM PHIEUXUATHANG')
        Res = Contro.fetchall()
        return Res

    def GetMaPhieuXH():
        Contro.execute('SELECT DISTINCT(MaPhieuXuat) FROM PHIEUXUATHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaDaiLy():
        Contro.execute('SELECT DISTINCT(MaDaiLy) FROM PHIEUXUATHANG')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    # Add Values
    def AddDSPhieuXH(*args):
        Contro.execute('INSERT INTO PHIEUXUATHANG VALUES(?,?,?,?)', (args[0], args[1], args[2], None))
        Contro.commit()

    # Remove Values
    def RemoveDSPhieuXH(*args):
        Contro.execute('DELETE FROM PHIEUXUATHANG WHERE MaPhieuXuat = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSPhieuXH(*args):
        Contro.execute('''UPDATE PHIEUXUATHANG SET MaDaiLy = ?, NgayLapPhieu = ?
                           WHERE MaPhieuXuat = ?''', (args[1], args[2], args[0]))
        Contro.commit()
    #Update Tongtien
    # def UpdateDSPhieuXH(*args):
    #     Contro.execute('''UPDATE PHIEUXUATHANG SET MaDaiLy = ?, NgayLapPhieu = ?
    #                        WHERE MaPhieuXuat = ?''', (args[1], args[2], args[0]))
    #     Contro.commit()
    
    # Finding Values
    def FindingDS_PNH(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MaPhieuXuat FROM PHIEUXUATHANG
                        WHERE 
                        MaPhieuXuat like ?
                        OR MaDaiLy like ?
                        OR NgayLapPhieu like ?
                        OR TongTien like ?''',
                        args1, args1, args1,
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

    def FindingDsPXH_Ngay(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUXUAT FROM PHIEUXUATHANG
                        WHERE 
                        day(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPXH_Thang(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUXUAT FROM PHIEUXUATHANG
                        WHERE 
                        month(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPXH_Nam(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUXUAT FROM PHIEUXUATHANG
                        WHERE 
                        year(NgayLapPhieu) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsCT_PXH:
    # Get Values
    def GetDSCT_PXH_Key(*args):
        Contro.execute('SELECT * FROM CT_PXH WHERE MaPhieuXuat = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSCT_PXH():
        Contro.execute('SELECT * FROM CT_PXH')
        Res = Contro.fetchall()
        return Res

    def GetMaCT_PXH():
        Contro.execute('SELECT MaCT_PXH FROM CT_PXH')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaPhieuXuat():
        Contro.execute('SELECT DISTINCT(MaPhieuXuat) FROM CT_PXH')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaMatHang():
        Contro.execute('SELECT DISTINCT(MaMatHang) FROM CT_PXH')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    # Add Values
    def AddDSCT_PXH(*args):
        Contro.execute('INSERT INTO CT_PXH VALUES(?,?,?,?,?,?)',
                       (args[0], args[1], args[2], int(args[3]), None, None))
        Contro.commit()

    # Remove Values
    def RemoveDSCT_PXH(*args):
        Contro.execute('DELETE FROM CT_PXH WHERE MaCT_PXH = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSCT_PXH(*args):
        Contro.execute('''UPDATE CT_PXH SET MaMatHang=?, SoLuongXuat=?
                        WHERE MaCT_PXH = ?''',
                       (args[1], int(args[2]), args[0]))
        Contro.commit()

    # Finding Values
    def FindingDS_PNH(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MaCT_PXH FROM CT_PXH
                        WHERE 
                        MaCT_PXH like ?
                        OR MaPhieuXuat like ?
                        OR MaMatHang like ?
                        OR SoLuongXuat like ?
                        OR DonGiaXuat like ? 
                        OR ThanhTien like ? ''',
                        args1, args1, args1,
                        args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsBCDS:
    # Get Values
    def GetDSBCDS_Key(*args):
        Contro.execute('SELECT * FROM BAOCAODOANHSO WHERE MaDaiLy = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSBCDS():
        Contro.execute('SELECT * FROM BAOCAODOANHSO')
        Res = Contro.fetchall()
        return Res

    def GetMaBCDoanhSo():
        Contro.execute('SELECT MaBCDoanhSo FROM BAOCAODOANHSO')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaDaiLy():
        Contro.execute('SELECT MaDaiLy FROM BAOCAODOANHSO')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetThang_MaDaiLy(*args):
        Contro.execute('SELECT Thang FROM BAOCAODOANHSO WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        else:
            return Res
    
    # Add Values
    def AddDSBCDS(*args):
        Contro.execute('INSERT INTO BAOCAODOANHSO VALUES(?,?,?,?,?,?)',
                       (args[0], int(args[1]), args[2], None, None, None))
        Contro.commit()

    # Remove Values
    def RemoveDSBCDS(*args):
        Contro.execute('DELETE FROM BAOCAODOANHSO WHERE MaBCDoanhSo = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSBCDS(*args):
        Contro.execute('''UPDATE BAOCAODOANHSO SET Thang=?, MaDaiLy=?
                        WHERE MaBCDoanhSo = ?''',
                       (int(args[1]), args[2], args[0]))
        Contro.commit()
    
    # Finding Values
    def FindingDsBCDS(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MABCDOANHSO FROM BAOCAODOANHSO 
                        WHERE 
                        MABCDOANHSO like ?
                        OR THANG like ?
                        OR MADAILY like ?
                        OR SOPHIEUXUAT like ?
                        OR TONGTRIGIA like ?
                        OR TYLE like ?''',
                        args1, args1, args1, None,
                        None, None)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
     
    def FindingDsBCDS_Thang(*args):
        Contro.execute('''SELECT MABCDOANHSO FROM BAOCAODOANHSO 
                        WHERE 
                        THANG = ?
                        ''',
                        args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res  

class DALdsBCCN:
    # Get Values
    def GetDSBCCN_Key(*args):
        Contro.execute('SELECT * FROM BAOCAOCONGNO WHERE MaDaiLy = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSBCCN():
        Contro.execute('SELECT * FROM BAOCAOCONGNO')
        Res = Contro.fetchall()
        return Res

    def GetMaBCCongNo():
        Contro.execute('SELECT MaBCCongNo FROM BAOCAOCONGNO')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaDaiLy():
        Contro.execute('SELECT MaDaiLy FROM BAOCAOCONGNO')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetThang_MaDaiLy(*args):
        Contro.execute('SELECT Thang FROM BAOCAOCONGNO WHERE MADAILY = ?', args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return 0
        else:
            return Res
        
    # Add Values
    def AddDSBCCN(*args):
        Contro.execute('INSERT INTO BAOCAOCONGNO VALUES(?,?,?,?,?,?)',
                       (args[0], int(args[1]), args[2], None, None, None))
        Contro.commit()

    # Remove Values
    def RemoveDSBCCN(*args):
        Contro.execute('DELETE FROM BAOCAOCONGNO WHERE MaBCCongNo = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSBCCN(*args):
        Contro.execute('''UPDATE BAOCAOCONGNO SET Thang=?, MaDaiLy=?
                        WHERE MaBCCongNo = ?''',
                       (int(args[1]), args[2], args[0]))
        Contro.commit()

    # Finding Values
    def FindingDsBCCN(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MABCCONGNO FROM BAOCAOCONGNO 
                        WHERE 
                        MABCCONGNO like ?
                        OR THANG like ?
                        OR MADAILY like ?
                        OR NODAU like ?
                        OR PHATSINH like ?
                        OR NOCUOI like ? ''',
                        args1, args1, args1, None,
                        None, None)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

    def FindingDsBCCN_Thang(*args):
        Contro.execute('''SELECT MABCCONGNO FROM BAOCAOCONGNO 
                        WHERE 
                        THANG like ?
                        ''',
                        args[0])
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALdsPTT:
    # Get Values
    def GetDSPTT_Key(*args):
        Contro.execute('SELECT * FROM PHIEUTHUTIEN WHERE MaDaiLy = ?', (args[0]))
        Res = Contro.fetchall()
        return Res
    
    def GetDSPTT():
        Contro.execute('SELECT * FROM PHIEUTHUTIEN')
        Res = Contro.fetchall()
        return Res

    def GetMaPTT():
        Contro.execute('SELECT DISTINCT(MaPhieuThuTien) FROM PHIEUTHUTIEN')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    def GetMaDaiLy():
        Contro.execute('SELECT DISTINCT(MaDaiLy) FROM PHIEUTHUTIEN')
        Res = Contro.fetchall()
        Lst = list()
        for i in Res:
            Lst.append(i[0].replace(' ', ''))
        return Lst

    # Add Values
    def AddDSPTT(*args):
        Contro.execute('INSERT INTO PHIEUTHUTIEN VALUES(?,?,?,?)', (args[0], args[1], args[2], int(args[3])))
        Contro.commit()

    # Remove Values
    def RemoveDSPTT(*args):
        Contro.execute('DELETE FROM PHIEUTHUTIEN WHERE MaPhieuThuTien = ?', (args[0]))
        Contro.commit()

    # Update Values
    def UpdateDSPTT(*args):
        Contro.execute('''UPDATE PHIEUTHUTIEN SET MaDaiLy = ?, NgayThuTien = ?, SoTienThu = ?
                           WHERE MaPhieuThuTien = ?''', (args[1], args[2], int(args[3]), args[0]))
        Contro.commit()

    # Finding Values
    def FindingDsPTT(*args):
        args1 = "%" + args[0] + "%"
        Contro.execute('''SELECT MAPHIEUTHUTIEN FROM PHIEUTHUTIEN
                        WHERE 
                        MAPHIEUTHUTIEN like ?
                        OR MADAILY like ?
                        OR SOTIENTHU like ?''',
                        args1, args1, args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPTT_Ngay(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUTHUTIEN FROM PHIEUTHUTIEN
                        WHERE 
                        day(NgayThuTien) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPTT_Thang(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUTHUTIEN FROM PHIEUTHUTIEN
                        WHERE 
                        month(NgayThuTien) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res
    
    def FindingDsPTT_Nam(*args):
        args1 = args[0]
        Contro.execute('''SELECT MAPHIEUTHUTIEN FROM PHIEUTHUTIEN
                        WHERE 
                        year(NgayThuTien) = ?''',
                        args1)
        Res = Contro.fetchall()
        if(Res == []):
            return False
        else:
            return Res

class DALThamSo:
    # Get Values
    def GetSDLTDMQ():
        Contro.execute('SELECT SoDaiLyToiDaMoiQuan FROM THAMSO')
        Res = Contro.fetchall()

        if(Res == []):
            return 0
        else:
            return str(Res[0][0])

    def GetSLDL_TS(*args):
        Contro.execute('''SELECT COUNT(MaDaiLy) FROM DAILY DL, QUAN Q
                       WHERE DL.MaQuan = Q.MaQuan AND Q.MaQuan = ?''', (args[0]))
        Res = Contro.fetchall()
        return str(Res[0][0])

    def GetTLDG():
        Contro.execute('SELECT TiLeDonGiaBan FROM THAMSO')
        Res = Contro.fetchall()

        if(Res == []):
            return 0
        else:
            return str(Res[0][0])

    # Update Values
    def UpdateSDLTDMQ(*args):
        Contro.execute('UPDATE THAMSO SET SoDaiLyToiDaMoiQuan = ?', (int(args[0])))
        Contro.commit()

    def UpdateTLDG(*args):
        Contro.execute('UPDATE THAMSO SET TiLeDonGiaBan = ?', float(args[0]))
        Contro.commit()
        return 'Thay đổi thành công!'
    