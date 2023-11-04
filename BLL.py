from DTO import*
from DAL import*
from datetime import datetime

class TaiKhoanBLL:
    def KiemTraTK(*args):
        TKDN = TaiKhoanDangNhap()
        if args[1] == u'Tài Khoản':
            return 'Chua Nhap Tai Khoan'
        if args[2] == u'Mật Khẩu':
            return 'Chua Nhap Mat Khau'
        KetQua = TKDN.KiemTraTK(args[1], args[2])
        return KetQua
    def ChangePassword(*args):
        if(args[1] != args[2]):
            return False
        else:
            if TaiKhoanDangNhap.ChangePassword(*args):
                return True

class BLLdsDaiLy:
    # Get Values
    def GetDSDaiLy():
        return DALdsDaiLy.GetDSDaiLy()

    def GetMaDaiLy():
        return DALdsDaiLy.GetMaDaiLy()

    def GetMaLDL():
        return DALdsDaiLy.GetMaLDL()

    def GetMaQuan():
        return DALdsDaiLy.GetMaQuan()
    
    def GetTienNo(*args):
        Res = DALdsDaiLy.GetTienNo(args[0])
        if Res == None:
            return 0
        else:
            return Res

    def GetSLDaiLy():
        return DALdsDaiLy.GetSLDaiLy()

    def GetMaLDL_dsLDL():
        return DALdsLoaiDaiLy.GetMaLoaiDL()
    
    def GetMaQuan_dsQuan():
        return DALdsQuan.GetMaQuan()

    def GetMaDaiLy_MaQuan(*args):
        return DALdsDaiLy.GetMaDaiLy_MaQuan(args[0])

    # Check Same Values
    def CheckSameValues_DT(*args):
        DsDT =  DALdsDaiLy.GetDsDT()
        if(DsDT != 0):
            for i in DsDT:
                if(str(args[0]) == str(i[0])):
                    return True
            return False
    
    def CheckSameValues_DT_Update(*args): #args[0] = madaily, args[1] = sodienthoai
        DsDT =  DALdsDaiLy.GetDsDT_Update()
        if(DsDT != 0):
            for i in DsDT:
                if(str(args[1]) == str(i[1])):
                    if(str(args[0]) != str(i[0])):
                        return True
            return False
        
    def CheckSameValues_DC(*args):
        DsDC =  DALdsDaiLy.GetDsDC()
        lst = []
        if (DsDC != 0):
            for i in DsDC:
                lst.append(i)
            lst_args = list(args[0])
            
            index = 0
            duong = []
            for i in lst_args:
                if i == ',':
                    break
                index+=1
                duong.append(i)
            duong = [''.join(duong)]
            other = lst_args[index:]
            other = [''.join(other)]

            check_other_duong = []
            check_other_lst = []
            for i in DsDC:
                lst_list = list(i[0])
                new_duong = []
                new_other = []
                new_index = 0
                for j in lst_list:
                    if j == ',':
                        break
                    new_index+=1
                    new_duong.append(j)

                new_duong = [''.join(new_duong)]
                new_other = lst_list[new_index:]
                new_other = [''.join(new_other)]
                
                check_other_lst.append(new_other[0])
                check_other_duong.append(new_duong[0])

            if other[0] in check_other_lst:
                if duong[0] in check_other_duong:
                    return True
                else:
                    return False
            else:
                return False
        
    def CheckSameValues_DC_Update(*args):
        DsDC =  list(DALdsDaiLy.GetDsDC_Update())
        lst = []
        if(DsDC != 0):
            for i in DsDC:
                lst.append(i[0])
            lst_args = list(args[1])
            
            index = 0
            duong = []
            for i in lst_args:
                if i == ',':
                    break
                index+=1
                duong.append(i)
            duong = [''.join(duong)]
            other = lst_args[index:]
            other = [''.join(other)]

            check_other_duong = []
            check_other_lst = []

            for i in DsDC:
                lst_list = list(i[1])
                new_duong = []
                new_other = []
                new_index = 0
                for j in lst_list:
                    if j == ',':
                        break
                    new_index+=1
                    new_duong.append(j)

                new_duong = [''.join(new_duong)]
                new_other = lst_list[new_index:]
                new_other = [''.join(new_other)]
                
                check_other_lst.append(new_other[0])
                check_other_duong.append(new_duong[0])

            if other[0] in check_other_lst:
                if duong[0] in check_other_duong:
                    for i in DsDC:
                        if(str(args[1]) == i[1]):
                            if(str(args[0]) == str(i[0])):
                                return False
                    return True
                else:
                    return False
            else:
                return False

    
    def CheckSameValues_TDL_Insert(*args):
        DsTDL =  DALdsDaiLy.GetDsTenDL_Insert(args[1])
        lst = []     
        if(DsTDL != 0):
            for i in DsTDL:
                lst.append(i[0])
            for i in lst:
                if(str(args[0]) == str(i)):
                    return True
            return False

    def CheckSameValues_TDL_Update(*args):
        DsTDL = DALdsDaiLy.GetDsTenDL_Update(args[2]) # truyền mã quận -> lấy về mã đại lý + tên đại lý trong quận     
        if(DsTDL != 0):
            for i in DsTDL:
                if(str(args[1]) == str(i[1])):
                    if(str(args[0]) == str(i[0])):
                            return False
                    return True
            return False
        
    # Add Values
    def AddDSDaiLy(*args):
        # Solve TenDaiLy
        Tendaily = list(args[0])
        tendaily = ''
        if(Tendaily[0] == u'Đ' or Tendaily[0] == u'đ'):
            tendaily = Tendaily[7:]
        else:
            tendaily = Tendaily
        tendaily = [''.join(tendaily)]
        tendaily = 'Đại lý ' + str(tendaily[0])

        # Generate MaDaiLy
        MaDL_Max = BLLdsDaiLy.GetMaDaiLy()
        number = []
        for i in MaDL_Max:
            temp = i[2:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1

        madl = 'DL' + str(max)

        if args[0] == '':
            return 'TDL rong'
        if args[2] == '':
            return 'DT rong'
        if args[3] == '':
            return 'DC rong'
        if args[5] == '':
            return 'NTN rong'
        if len(args[0]) > 20:
            return 'TDL dai'
        if len(args[2]) > 15:
            return 'DT dai'
        if len(args[3]) > 50:
            return 'DC dai'
        
        if(BLLdsDaiLy.CheckSameValues_DT(args[2])): # Check if it is the existed phone number
            return 'SDT trung'
        if(BLLdsDaiLy.CheckSameValues_DC(args[3])): # Check if it is the existed address
            return 'DC trung'
        if(BLLdsDaiLy.CheckSameValues_TDL_Insert(tendaily, args[4])):
            return 'TDL trung'
        
        if args[1] in DALdsLoaiDaiLy.GetMaLoaiDL():
            if args[4] in DALdsQuan.GetMaQuan():
                if int(DALThamSo.GetSLDL_TS(args[4])) < int(DALThamSo.GetSDLTDMQ()):
                    DALdsDaiLy.AddDSDaiLy(madl, tendaily, args[1], args[2], args[3], args[4], args[5])
                else:
                    return 'SDLTQ toi da'
            else:
                return 'MQ k ton tai'
        else:
            return 'MLDL k ton tai'

    # Remove Values                               
    def RemoveDSDaiLy(*args):
        lst = list(args[0])
        new_list = [x for x in lst if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] not in DALdsPTT.GetMaDaiLy():
            if new_list[0] not in DALdsPXH.GetMaDaiLy():
                if new_list[0] not in DALdsBCDS.GetMaDaiLy():
                    if new_list[0] not in DALdsBCCN.GetMaDaiLy():
                        DALdsDaiLy.RemoveDSDaiLy(args[0])
                    else:
                        return 'MDL in BCCN'
                else:
                    return 'MDL in BCDS'
            else:
                return 'MDL in PXH'
        else:
            return 'MDL in PTT'

    # Update Values
    def UpdateDSDaiLy(*args):
        
        # Nếu tên đại lý rỗng 
        tendaily = ''
        if args[1] == '':
            DsTendaily = list(DALdsDaiLy.GetTenDaiLy(args[0])[0])
            tendaily = DsTendaily[0]
        else:
            Tendaily = list(args[1])
            tendaily = ''
            if(Tendaily[0] == u'Đ' or Tendaily[0] == u'đ'):
                tendaily = Tendaily[7:]
            else:
                tendaily = Tendaily
            tendaily = [''.join(tendaily)]
            tendaily = 'Đại lý ' + str(tendaily[0])

        # Nếu số điện thoại rỗng
        sodienthoai = ''
        if args[3] == '':
            DsDienthoai = list(DALdsDaiLy.GetDienThoai(args[0])[0])
            sodienthoai = DsDienthoai[0]
        else:
            sodienthoai = args[3]
        
        # Nếu địa chỉ rỗng
        diachi = ''
        if args[4] == '':
            DsDiachi = list(DALdsDaiLy.GetDiaChi(args[0])[0])
            diachi = DsDiachi[0]
        else:
            diachi = args[4]

        # Nếu ngày tiếp nhận rỗng
        ntn = ''
        if args[6] == '':
            DsNTN = list(DALdsDaiLy.GetNTN(args[0])[0])
            ntn = DsNTN[0]
        else:
            ntn = args[6]

        if len(args[1]) > 20:
            return 'TDL dai'
        if len(args[3]) > 15:
            return 'DT dai'
        if len(args[4]) > 50:
            return 'DC dai'
    
        if BLLdsDaiLy.CheckSameValues_DT_Update(args[0], args[3]):
            return 'SDT trung'
        
        if(BLLdsDaiLy.CheckSameValues_TDL_Update(args[0], tendaily, args[5])):
            return 'TDL trung'
        
        if(BLLdsDaiLy.CheckSameValues_DC_Update(args[0], args[4])): # Check if it is the existed address
            return 'DC trung'
        
        if args[2] in DALdsLoaiDaiLy.GetMaLoaiDL():
            if args[5] in DALdsQuan.GetMaQuan():
                if(BLLdsDaiLy.GetMaDaiLy_MaQuan(args[5]) != 0):
                    for i in BLLdsDaiLy.GetMaDaiLy_MaQuan(args[5]):
                        if(str(args[0]) == str(i[0])):
                            if int(DALThamSo.GetSLDL_TS(args[5])) <= int(DALThamSo.GetSDLTDMQ()):
                                DALdsDaiLy.UpdateDSDaiLy(args[0], tendaily, args[2], sodienthoai, diachi, args[5], ntn, None)
                                return
                if int(DALThamSo.GetSLDL_TS(args[5])) < int(DALThamSo.GetSDLTDMQ()):
                    DALdsDaiLy.UpdateDSDaiLy(args[0], tendaily, args[2], sodienthoai, diachi, args[5], ntn, None)
                else:
                    return 'SDLTQ toi da'
            else:
                return 'MQ k ton tai'
        else:
            return 'MLDL k ton tai'
    
    # Finding Values
    def FindingDsDaiLy(*args):
        val = list(args[0])
        val1 = val[0:3]
        val1 = [''.join(val1)]
        val2 = val1[0]
        if(args[0][0] == 'D' and args[0][1] == 'L'):
            Res = DALdsDaiLy.FindingDsDaiLy_MaDaiLy(args[0])

        elif(args[0][0] == 'L' and args[0][1] == 'D' and args[0][2] == 'L'):
            Res = DALdsDaiLy.FindingDsDaiLy_MaLDL(args[0])
        
        elif(val2 == u'Ngà' or val2 == u'ngà'):
            if(len(args[0]) < 6):
                return 'Khong tim thay'
            val3 = val[5:]
            val3 = [''.join(val3)]
            Res = DALdsDaiLy.FindingDsDaiLy_Ngay(val3[0])
            
        elif(val2 == u'Thá' or val2 == u'thá'):
            if(len(args[0]) < 7):
                return 'Khong tim thay'
            val3 = val[6:]
            val3 = [''.join(val3)]
            Res = DALdsDaiLy.FindingDsDaiLy_Thang(val3[0])

        elif(val2 == u'Năm' or val2 == u'năm'):
            if(len(args[0]) < 5):
                return 'Khong tim thay'
            val3 = val[4:]
            val3 = [''.join(val3)]
            Res = DALdsDaiLy.FindingDsDaiLy_Nam(val3[0])

        else:
            Res = DALdsDaiLy.FindingDsDaiLy_Khac(args[0])
        
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsLoaiDaiLy:
    # Get Values
    def GetDSLoaiDL():
        return DALdsLoaiDaiLy.GetDSLoaiDL()

    def GetMaLoaiDL():
        return DALdsLoaiDaiLy.GetMaLoaiDL()

    def GetSLLoaiDL():
        return DALdsLoaiDaiLy.GetSLLoaiDL()
    

    def CheckSameValues_TLDL(*args):
        DsTDL =  DALdsLoaiDaiLy.GetTenLDL()
        lst = []
        if(DsTDL != 0):
            for i in DsTDL:
                lst.append(i[0])
            for i in lst:
                if(str(args[0]) == str(i)):
                    return True
            return False
        
    def CheckSameValues_TLDL_Update(*args):
        DsTLDL =  DALdsLoaiDaiLy.GetTenLDL_Update()
        if(DsTLDL != 0):
            for i in DsTLDL:
                if(str(args[1]) == str(i[1])):
                    if(str(args[0]) != str(i[0])):
                        return True
            return False
        
    # Add Values
    def AddDSLoaiDL(*args):

        # Solve Tendaily
        Tenldaily = list(args[0])
        tenldaily = ''
        if(Tenldaily[0] == u'L' or Tenldaily[0] == u'l'):
            tenldaily = Tenldaily[5:]
        else:
            tenldaily = Tenldaily
        tenldaily = [''.join(tenldaily)]
        tenldaily = 'Loại ' + str(tenldaily[0])

        if (len(tenldaily) >= 9):
            return 'TLDL khong hop le'
        # Generate MaLoaiDaiLy
        MaLDL_Max = BLLdsLoaiDaiLy.GetMaLoaiDL()
        number = []
        for i in MaLDL_Max:
            temp = i[3:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1

        maldl = 'LDL' + str(max)

        if args[0] == '':
            return 'TLDL rong'
        if args[1] == '':
            return 'SNTD rong'
        if len(args[0]) > 20:
            return 'TLDL dai'
        if int(args[1]) < 0:
            return 'STN am'
        
        else:
            if BLLdsLoaiDaiLy.CheckSameValues_TLDL(tenldaily):
                return 'TLDL trung'
        
        DALdsLoaiDaiLy.AddDSLoaiDL(maldl, tenldaily, args[1])

    # Remove Values
    def RemoveDSLoaiDL(*args):
        lst = list(args[0])
        lit = list(lst)
        new_list = [x for x in lit if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] in DALdsDaiLy.GetMaLDL():
            return 'MLDL in DAILY'
        else:
            DALdsLoaiDaiLy.RemoveDSLoaiDL(args[0])

    # Update Values
    def UpdateDSLoaiDL(*args):

        # Nếu tên loại đại lý rỗng
        tenldaily = ''
        if args[1] == '':
            DsTenLDL = list(DALdsLoaiDaiLy.Get1TenLDL(args[0])[0])
            tenldaily = DsTenLDL[0]
        else:
            Tenldaily = list(args[1])
            tenldaily = ''
            if(Tenldaily[0] == u'L' or Tenldaily[0] == u'l'):
                tenldaily = Tenldaily[5:]
            else:
                tenldaily = Tenldaily
            tenldaily = [''.join(tenldaily)]
            tenldaily = 'Loại ' + str(tenldaily[0])

        # Nếu số nợ tối đa rỗng
        sonotoida = None
        if args[2] == '':
            DsTenLDL = list(DALdsLoaiDaiLy.Get1SoNoToiDa(args[0])[0])
            sonotoida = DsTenLDL[0]
        else:
            sonotoida = args[2]

        if len(args[1]) > 20:
            return 'TLDL dai'
        
        if int(sonotoida) < 0:
            return 'SNTD am'
    
        if BLLdsLoaiDaiLy.CheckSameValues_TLDL_Update(args[0], tenldaily):
            return 'TLDL trung'
        DALdsLoaiDaiLy.UpdateDSLoaiDL(args[0], tenldaily, sonotoida)

    def UpdateSN_LoaiDL(*args):
        DALdsLoaiDaiLy.UpdateSN_LoaiDL(args[0], args[1])
    
    # Finding Values
    def FindingDsLoaiDaiLy(*args):
        Res = DALdsLoaiDaiLy.FindingDS_LDL(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsQuan:
    # Get Values
    def GetDSQuan():
        return DALdsQuan.GetDSQuan()

    def GetMaQuan():
        return DALdsQuan.GetMaQuan()

    def GetSLQuan():
        return DALdsQuan.GetSLQuan()

    # Check Same Values
    def CheckSameValues_TQ(*args):
        DsTQ =  DALdsQuan.GetTenQuan()
        lst = []
        
        if(DsTQ != 0):
            for i in DsTQ:
                lst.append(i[0])
            for i in lst:
                if(str(args[0]) == str(i)):
                    return True
            return False
        
    # Add Values
    def AddDSQuan(*args):
        # Solve Tenquan
        Tenq = list(args[0])
        tenq = ''
        if(Tenq[0] == u'Q' or Tenq[0] == u'q'):
            tenq = Tenq[5:]
        else:
            tenq = Tenq
        tenq = [''.join(tenq)]
        tenq = 'Quận ' + str(tenq[0])

        # Generate Maquan
        Maquan_Max = BLLdsQuan.GetMaQuan()
        number = []
        for i in Maquan_Max:
            temp = i[1:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1

        maquan = 'Q' + str(max)

        if args[0] == '':
            return 'TQ rong'
        if len(args[0]) > 20:
            return 'TQ dai'
        if BLLdsQuan.CheckSameValues_TQ(tenq):
            return 'TQ trung'
        DALdsQuan.AddDSQuan(maquan, tenq)

    # Remove Values
    def RemoveDSQuan(*args):
        lst = list(args[0])
        new_list = [x for x in lst if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] in DALdsDaiLy.GetMaQuan():
            return 'MQ in DAILY'
        else:
            DALdsQuan.RemoveDSQuan(args[0])

    # Update Values
    def UpdateDSQuan(*args):
        
        # Nếu tên quận rỗng
        tenq = ''
        if args[1] == '':
            DsTenQuan = list(DALdsQuan.Get1TenQuan(args[0])[0])
            tenq = DsTenQuan[0]
        else:
            Tenq = list(args[1])
            tenq = ''
            if(Tenq[0] == u'Q' or Tenq[0] == u'q'):
                tenq = Tenq[5:]
            else:
                tenq = Tenq
            tenq = [''.join(tenq)]
            tenq = 'Quận ' + str(tenq[0])

        if len(args[1]) > 20:
            return 'TQ dai'
        
        if args[1] == '':
            return 'K cập nhật'
        else: 
            if BLLdsQuan.CheckSameValues_TQ(tenq):
                return 'TQ trung'
        
        DALdsQuan.UpdateDSQuan(args[0], tenq)

    # Finding Values
    def FindingDsQuan(*args):
        Res = DALdsQuan.FindingDS_Quan(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res
    
class BLLdsMatHang:
    # Get Values
    def GetDSMatHang():
        return DALdsMatHang.GetDSMatHang()

    def GetMaMatHang():
        return DALdsMatHang.GetMaMatHang()

    def GetMaDVT():
        return DALdsMatHang.GetMaDVT()
    
    def GetSoLuongTon(*args):
        return DALdsMatHang.GetSoLuongTon(args[0])

    def GetSLMatHang():
        return DALdsMatHang.GetSLMatHang()

    def GetDVT_dsDVT():
        return DALdsDVT.GetMaDVT()
    
    # Check Same Values
    def CheckSameValues_TenMH(*args):
        DsTMH =  DALdsMatHang.GetTenMatHang()
        lst = []
        if(DsTMH != 0):
            for i in DsTMH:
                lst.append(i[0])
            for i in lst:
                if(str(args[0]) == str(i)):
                    return True
            return False
    
    def CheckSameValues_TenMH_Update(*args):
        DsTMH =  list(DALdsMatHang.GetTenMatHang_MaMH())
        if(DsTMH != 0):
            for i in DsTMH:
                if(str(args[1]) == str(i[1])):
                    if(str(args[0]) == str(i[0])):
                        return False
                    return True
            return False

    # Add Values
    def AddDSMatHang(*args):
        # Solve TenMH
        Tenmh = list(args[0])
        tenmh = [''.join(Tenmh)]
        tenmh = str(tenmh[0])

        # Generate MaDaiLy
        MaMH_Max = BLLdsMatHang.GetMaMatHang()
        number = []
        for i in MaMH_Max:
            temp = i[2:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1

        mamh = 'MH' + str(max)

        if args[0] == '':
            return 'TMH rong'
        if len(args[0]) > 20:
            return 'TMH dai'
        if BLLdsMatHang.CheckSameValues_TenMH(tenmh):
            return 'TenMH trung'

        DALdsMatHang.AddDSMatHang(mamh, tenmh, args[1])

    # Remove Values 
    def RemoveDSMatHang(*args):
        lst = list(args[0])
        new_list = [x for x in lst if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] not in BLLdsCT_PNH.GetMaMatHang():
            if new_list[0] not in BLLdsCT_PXH.GetMaMatHang():
                DALdsMatHang.RemoveDSMatHang(args[0])
            else:
                return 'MMH in CT_PXH'
        else:
            return 'MMH in CT_PNH'

    # Update Values
    def UpdateDSMatHang(*args):
        

        # Nếu tên mặt hàng trống
        tenmh = ''
        if args[1] == '':
            DsTenMH = list(DALdsMatHang.Get1TenMatHang(args[0])[0])
            tenmh = DsTenMH[0]
        else:
            Tenmh = list(args[1])
            tenmh = [''.join(Tenmh)]
            tenmh = str(tenmh[0])
        

        if len(args[1]) > 20:
            return 'TMH dai'

        if args[1] == '':
            pass
        else:
            if BLLdsMatHang.CheckSameValues_TenMH_Update(args[0], tenmh):
                return 'TenMH trung'
            
        if args[2] in DALdsDVT.GetMaDVT():
            DALdsMatHang.UpdateDSMatHang(args[0], tenmh, args[2])
        else:
            return 'MDVT k ton tai'

    # Finding Values
    def FindingDsMatHang(*args):
        Res = DALdsMatHang.FindingDS_MatHang(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res
    
class BLLdsDVT:
    # Get Values
    def GetDSDVT():
        return DALdsDVT.GetDSDVT()

    def GetMaDVT():
        return DALdsDVT.GetMaDVT()

    def GetSLDVT():
        return DALdsDVT.GetSLDVT()

    # Check Same Values
    def CheckSameValues_TenDVT(*args):
        DsTQ =  DALdsDVT.GetTenDVT()
        lst = []
        
        if(DsTQ != 0):
            for i in DsTQ:
                lst.append(i[0])

            for i in lst:
                if(str(args[0]) == str(i)):
                    return True
            return False
        
    # Add Values
    def AddDSDVT(*args):
        Tendvt = list(args[0])
        tendvt = [''.join(Tendvt)]
        tendvt = str(tendvt[0])

        # Generate Maquan
        Madvt_Max = BLLdsDVT.GetMaDVT()
        number = []
        for i in Madvt_Max:
            temp = i[3:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1

        madvt = 'DVT' + str(max)

        if args[0] == '':
            return 'TDVT rong'
        if len(args[0]) > 10:
            return 'TDVT dai'
        if BLLdsDVT.CheckSameValues_TenDVT(tendvt):
            return 'TenDVT trung'

        DALdsDVT.AddDSDVT(madvt, tendvt)

    # Remove Values
    def RemoveDSDVT(*args):
        lst = list(args[0])
        new_list = [x for x in lst if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] in DALdsMatHang.GetMaDVT():
            return 'MDVT in MATHANG'
        else:
            DALdsDVT.RemoveDSDVT(args[0])

    # Update Values
    def UpdateDSDVT(*args):
        

        # Nếu tên đơn vị tính rỗng
        tendvt = ''
        if args[1] == '':
            DsTenDVT = list(DALdsDVT.Get1TenDVT(args[0]))
            tendvt = DsTenDVT[0]
        else:
            Tendvt = list(args[1])
            tendvt = [''.join(Tendvt)]
            tendvt = str(tendvt[0])

        if len(args[1]) > 10:
            return 'TDVT dai'
        
        if args[1] == '':
            return 'K cập nhật'
        else:
            if BLLdsDVT.CheckSameValues_TenDVT(tendvt):
                return 'TenDVT trung'
        DALdsDVT.UpdateDSDVT(args[0], tendvt)

    # Finding Values
    def FindingDsDVT(*args):
        Res = DALdsDVT.FindingDS_DVT(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res
    
class BLLdsPhieuNH:
    # Get Values
    def GetDSPhieuNH_Key(*args):
        return DALdsPNH.GetDSPhieuNH_Key(args[0])
    
    def GetDSPhieuNH():
        return DALdsPNH.GetDSPhieuNH()

    def GetMaPhieuNH():
        return DALdsPNH.GetMaPhieuNH()

    # Add Values
    def AddDSPhieuNH(*args):
        # Generate MaPhieuNhap
        number = []
        for i in BLLdsPhieuNH.GetMaPhieuNH():
            number.append(int(i[3:]))

        max = int(0)
        for i in number:
            if i > max:
                max = i
        max = max + 1
        mapnh = 'PNH' + str(max)
        DALdsPNH.AddDSPhieuNH(mapnh, args[0])

    # Remove Values
    def RemoveDSPhieuNH(*args):
        lst = list(args[0])
        new_lst = [i for i in lst if i!=' ']
        new_lst = [''.join(new_lst)]
        for i in BLLdsCT_PNH.GetMaPhieuNhap():
            if str(new_lst[0]) == str(i):
                return 'MPN in CT_PNH'
        DALdsPNH.RemoveDSPhieuNH(args[0])

    # Update Values
    def UpdateDSPhieuNH(*args):
        if args[1] == '':
            return 'NLP rong'
        DALdsPNH.UpdateDSPhieuNH(args[0], args[1])
    
    # Finding Values
    def FindingDsPNH(*args):
        val = list(args[0])
        val1 = val[0:3]
        val1 = [''.join(val1)]
        val2 = val1[0]
        
        if(val2 == u'Ngà' or val2 == u'ngà'):
            if(len(args[0]) < 6):
                return 'Khong tim thay'
            val3 = val[5:]
            val3 = [''.join(val3)]
            Res = DALdsPNH.FindingDsPNH_Ngay(val3[0])
            
        elif(val2 == u'Thá' or val2 == u'thá'):
            if(len(args[0]) < 7):
                return 'Khong tim thay'
            val3 = val[6:]
            val3 = [''.join(val3)]
            Res = DALdsPNH.FindingDsPNH_Thang(val3[0])

        elif(val2 == u'Năm' or val2 == u'năm'):
            if(len(args[0]) < 5):
                return 'Khong tim thay'
            val3 = val[4:]
            val3 = [''.join(val3)]
            Res = DALdsPNH.FindingDsPNH_Nam(val3[0])
        else:
            Res = DALdsPNH.FindingDS_PNH(args[0])

        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsCT_PNH:
    # Get Values
    def GetDSCT_PNH_Key(*args):
        return DALdsCT_PNH.GetDSCT_PNH_Key(args[0])
    
    def GetDSCT_PNH():
        return DALdsCT_PNH.GetDSCT_PNH()

    def GetMaCT_PNH():
        return DALdsCT_PNH.GetMaCT_PNH()

    def GetMaPhieuNhap():
        return DALdsCT_PNH.GetMaPhieuNhap()

    def GetMaMatHang():
        return DALdsCT_PNH.GetMaMatHang()

    # Add Values
    def AddDSCT_PNH(*args):
        # Generate MaCT_PNH
        number = []
        for i in BLLdsCT_PNH.GetMaCT_PNH():
            number.append(int(i[5:]))

        max = int(0)
        for i in number:
            if i > max:
                max = i
        max = max + 1

        mact_pnh = 'CTPNH' + str(max)
        if args[2] == '':
            return 'SLN rong'
        if args[3] == '':
            return 'DGN rong'
        if int(args[2]) <= 0:
            return 'SLN am'
        if int(args[3]) <= 0:
            return 'DGN am'

        DALdsCT_PNH.AddDSCT_PNH(mact_pnh, args[0], args[1], args[2], args[3])

    # Remove Values
    def RemoveDSCT_PNH(*args):
        DALdsCT_PNH.RemoveDSCT_PNH(args[0])

    # Update Values
    def UpdateDSCT_PNH(*args):
        if args[2] == '':
            return 'SLN rong'
        if args[3] == '':
            return 'DGN rong'
        if int(args[2]) <= 0:
            return 'SLN am'
        if int(args[3]) <= 0:
            return 'DGN am'

        DALdsCT_PNH.UpdateDSCT_PNH(args[0], args[1], args[2], args[3])

    # Finding Values
    def FindingDsCT_PNH(*args):
        Res = DALdsCT_PNH.FindingDS_PNH(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsPhieuXH:
    # Get Values
    def GetDSPhieuXH_Key(*args):
        return DALdsPXH.GetDSPhieuXH_Key(args[0])
    
    def GetDSPhieuXH_Key1(*args):
        return DALdsPXH.GetDSPhieuXH_Key1(args[0])
    
    def GetDSPhieuXH():
        return DALdsPXH.GetDSPhieuXH()

    def GetMaPhieuXH():
        return DALdsPXH.GetMaPhieuXH()

    def GetMaDaiLy():
        return DALdsPXH.GetMaDaiLy()

    # Add Values
    def AddDSPhieuXH(*args):
        # Generate MaPhieuXuat
        number = []
        for i in BLLdsPhieuXH.GetMaPhieuXH():
            number.append(int(i[3:]))

        max = int(0)
        for i in number:
            if i > max:
                max = i
        max = max + 1

        mapxh = 'PXH' + str(max)

        if args[0] == '':
            return 'MDL rong'
        if args[1] == '':
            return 'NLP rong'
        
        # Solve datetime 'Dai Ly'
        ntn = list(DALdsDaiLy.GetNgayTiepNhan(args[0]))
        ntn_sosanh = ntn[0][0].date()
        if args[1] < ntn_sosanh:
            return 'Ngay khong hop le'

        DALdsPXH.AddDSPhieuXH(mapxh, args[0], args[1])

    # Remove Values
    def RemoveDSPhieuXH(*args):
        lst = list(args[0])
        new_list = [x for x in lst if x != ' ']
        new_list = [''.join(new_list)]
        if new_list[0] in BLLdsCT_PXH.GetMaPhieuXuat():
            return 'MPX in CT_PXH'
        else:
            DALdsPXH.RemoveDSPhieuXH(args[0])

    # Update Values
    def UpdateDSPhieuXH(*args):
        if args[2] == '':
            return 'NLP rong'
        # Solve datetime
        ntn = list(DALdsDaiLy.GetNgayTiepNhan(args[1]))
        ntn_sosanh = ntn[0][0].date()
        if args[2] < ntn_sosanh:
            return 'Ngay khong hop le'
        
        DALdsPXH.UpdateDSPhieuXH(args[0], args[1], args[2])

    # Finding Values
    def FindingDsPXH(*args):
        val = list(args[0])
        val1 = val[0:3]
        val1 = [''.join(val1)]
        val2 = val1[0]
        
        if(val2 == u'Ngà' or val2 == u'ngà'):
            if(len(args[0]) < 6):
                return 'Khong tim thay'
            val3 = val[5:]
            val3 = [''.join(val3)]
            Res = DALdsPXH.FindingDsPXH_Ngay(val3[0])
            
        elif(val2 == u'Thá' or val2 == u'thá'):
            if(len(args[0]) < 7):
                return 'Khong tim thay'
            val3 = val[6:]
            val3 = [''.join(val3)]
            Res = DALdsPXH.FindingDsPXH_Thang(val3[0])

        elif(val2 == u'Năm' or val2 == u'năm'):
            if(len(args[0]) < 5):
                return 'Khong tim thay'
            val3 = val[4:]
            val3 = [''.join(val3)]
            Res = DALdsPXH.FindingDsPXH_Nam(val3[0])
        else:
            Res = DALdsPXH.FindingDS_PNH(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsCT_PXH:
    # Get Values
    def GetDSCT_PXH_Key(*args):
        return DALdsCT_PXH.GetDSCT_PXH_Key(args[0])
    
    def GetDSCT_PXH():
        return DALdsCT_PXH.GetDSCT_PXH()

    def GetMaCT_PXH():
        return DALdsCT_PXH.GetMaCT_PXH()

    def GetMaPhieuXuat():
        return DALdsCT_PXH.GetMaPhieuXuat()

    def GetMaMatHang():
        return DALdsCT_PXH.GetMaMatHang()

    # Add Values
    def AddDSCT_PXH(*args):
        # Generate MaCT_PXH
        number = []
        for i in BLLdsCT_PXH.GetMaCT_PXH():
            number.append(int(i[5:]))

        max = int(0)
        for i in number:
            if i > max:
                max = i
        max = max + 1

        mact_pxh = 'CTPXH' + str(max)
        if args[2] == '':
            return 'SLX rong'
        if int(args[2]) <= 0:
            return 'SLX am'

        if int(args[2]) > BLLdsMatHang.GetSoLuongTon(args[1]):
            return 'SLX <= SLT'
        
        DALdsCT_PXH.AddDSCT_PXH(mact_pxh, args[0], args[1], args[2])

    # Remove Values
    def RemoveDSCT_PXH(*args):
        DALdsCT_PXH.RemoveDSCT_PXH(args[0])

    # Update Values
    def UpdateDSCT_PXH(*args):
        if args[2] == '':
            return 'SLX rong'
        if int(args[2]) <= 0:
            return 'SLX am'

        DALdsCT_PXH.UpdateDSCT_PXH(args[0], args[1], args[2])

    # Finding Values
    def FindingDsCT_PXH(*args):
        Res = DALdsCT_PXH.FindingDS_PNH(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsBCDS:
    # Get Values
    def GetDSBCDS_Key(*args):
        return DALdsBCDS.GetDSBCDS_Key(args[0])
    
    def GetDSBCDS():
        return DALdsBCDS.GetDSBCDS()

    def GetMaBCDoanhSo():
        return DALdsBCDS.GetMaBCDoanhSo()

    def GetMaDaiLy():
        return DALdsBCDS.GetMaDaiLy()

    # Check the same values
    def Check_BaocaoTrung(*args):
        DsBCDS = DALdsBCDS.GetThang_MaDaiLy(args[1])
        if DsBCDS != 0:
            for i in DsBCDS:
                if(str(i[0]) == str(args[0])):
                    return True
            return False 
        
    # Add Values
    def AddDSBCDS(*args):
        MaBCDS_Max = BLLdsBCDS.GetMaBCDoanhSo()
        number = []
        for i in MaBCDS_Max:
            temp = i[4:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1
        mabcds = 'BCDS' + str(max)
        if BLLdsBCDS.Check_BaocaoTrung(args[0], args[1]):
            return 'Bao cao da ton tai'
        
        DALdsBCDS.AddDSBCDS(mabcds, args[0], args[1], None, None, None)

    # Remove Values
    def RemoveDSBCDS(*args):
        DALdsBCDS.RemoveDSBCDS(args[0])

    # Update Values
    def UpdateDSBCDS(*args):
        if BLLdsBCDS.Check_BaocaoTrung(args[1], args[2]):
            return 'Bao cao trung'
        DALdsBCDS.UpdateDSBCDS(args[0], args[1], args[2], None, None, None)
        
        
    # Finding Values
    def FindingDsBCDS(*args):
        value0 = list(args[0])
        value1 = value0[0:5]
        value2 = value0[6:]
        value1 = [''.join(value1)]
        value2 = [''.join(value2)]
        if(str(value1[0]) == u'tháng' or str(value1[0]) == u'Tháng'):
            Res = DALdsBCDS.FindingDsBCDS_Thang(int(value2[0]))
        else:
            Res = DALdsBCDS.FindingDsBCDS(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsBCCN:
    # Get Values
    def GetDSBCCN_Key(*args):
        return DALdsBCCN.GetDSBCCN_Key(args[0])
    
    def GetDSBCCN():
        return DALdsBCCN.GetDSBCCN()

    def GetMaBCCongNo():
        return DALdsBCCN.GetMaBCCongNo()

    def GetMaDaiLy():
        return DALdsBCCN.GetMaDaiLy()

    # Check the same values
    def Check_BaocaoTrung(*args):
        DsBCCN = DALdsBCCN.GetThang_MaDaiLy(args[1])
        if DsBCCN != 0:
            for i in DsBCCN:
                if(str(i[0]) == str(args[0])):
                    return True
            return False
        
    # Add Values
    def AddDSBCCN(*args):
        MaBCCN_Max = BLLdsBCCN.GetMaBCCongNo()
        number = []
        for i in MaBCCN_Max:
            temp = i[4:]
            number.append(temp)

        number_int = []
        for i in number:
            temp = int(i)
            number_int.append(temp)
        
        max = int(0)
        for i in number_int:
            if i > max:
                max = i
        max = max + 1
        mabccn = 'BCCN' + str(max)
        if BLLdsBCCN.Check_BaocaoTrung(args[0], args[1]):
            return 'Bao cao da ton tai'

        DALdsBCCN.AddDSBCCN(mabccn, args[0], args[1], None, None, None)

    # Remove Values
    def RemoveDSBCDS(*args):
        DALdsBCCN.RemoveDSBCCN(args[0])

    # Update Values
    def UpdateDSBCCN(*args):
        if BLLdsBCCN.Check_BaocaoTrung(args[1], args[2]):
            return 'Bao cao trung'
        DALdsBCCN.UpdateDSBCCN(args[0], args[1], args[2], None, None, None)

    
    # Finding Values
    def FindingDsBCCN(*args):
        value0 = list(args[0])
        value1 = value0[0:5]
        value2 = value0[6:]
        value1 = [''.join(value1)]
        value2 = [''.join(value2)]
        if(str(value1[0]) == u'tháng' or str(value1[0]) == u'Tháng'):
            Res = DALdsBCCN.FindingDsBCCN_Thang(int(value2[0]))
        else:
            Res = DALdsBCCN.FindingDsBCCN(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLdsPTT:
    # Get Values
    def GetDSPTT_Key(*args):
        return DALdsPTT.GetDSPTT_Key(args[0])
    
    def GetDSPTT():
        return DALdsPTT.GetDSPTT()

    def GetMaPTT():
        return DALdsPTT.GetMaPTT()

    def GetMaDaiLy():
        return DALdsPTT.GetMaDaiLy()

    # Add Values
    def AddDSPTT(*args):
        # Generate MaPhieuThuTien
        number = []
        for i in BLLdsPTT.GetMaPTT():
            number.append(int(i[3:]))

        max = int(0)
        for i in number:
            if i > max:
                max = i
        max = max + 1

        maptt = 'PTT' + str(max)
        if args[0] == '':
            return 'MDL rong'
        if args[1] == '':
            return 'NTT rong'
        if args[2] == '':
            return 'STT rong'
        if int(args[2]) <= 0:
            return 'STT am'
        if int(args[2]) > BLLdsDaiLy.GetTienNo(str(args[0])):
            return 'STT > STN'
        
        # Solve datetime
        ntn = list(DALdsDaiLy.GetNgayTiepNhan(args[0]))
        ntn_sosanh = ntn[0][0].date()
        if args[1] < ntn_sosanh:
            return 'Ngay khong hop le'
        DALdsPTT.AddDSPTT(maptt, args[0], args[1], args[2])

    # Remove Values
    def RemoveDSPTT(*args):
        DALdsPTT.RemoveDSPTT(args[0])

    # Update Values
    def UpdateDSPTT(*args):
        if args[3] == '':
            return 'STT rong'
        if int(args[3]) <= 0:
            return 'STT am'
        if int(args[3]) > BLLdsDaiLy.GetTienNo(str(args[1])):
            return 'STT > STN'
        
        # Solve datetime
        ntn = list(DALdsDaiLy.GetNgayTiepNhan(args[1]))
        ntn_sosanh = ntn[0][0].date()
        if args[2] < ntn_sosanh:
            return 'Ngay khong hop le'
        
        DALdsPTT.UpdateDSPTT(args[0], args[1], args[2], int(args[3]))

    # Finding Values
    def FindingDsPTT(*args):
        val = list(args[0])
        val1 = val[0:3]
        val1 = [''.join(val1)]
        val2 = val1[0]
        
        if(val2 == u'Ngà' or val2 == u'ngà'):
            if(len(args[0]) < 6):
                return 'Khong tim thay'
            val3 = val[5:]
            val3 = [''.join(val3)]
            Res = DALdsPTT.FindingDsPTT_Ngay(val3[0])
            
        elif(val2 == u'Thá' or val2 == u'thá'):
            if(len(args[0]) < 7):
                return 'Khong tim thay'
            val3 = val[6:]
            val3 = [''.join(val3)]
            Res = DALdsPTT.FindingDsPTT_Thang(val3[0])

        elif(val2 == u'Năm' or val2 == u'năm'):
            if(len(args[0]) < 5):
                return 'Khong tim thay'
            val3 = val[4:]
            val3 = [''.join(val3)]
            Res = DALdsPTT.FindingDsPTT_Nam(val3[0])
        else:
            Res = DALdsPTT.FindingDsPTT(args[0])
        if(Res == False):
           return 'Khong tim thay'
        F_res = []
        for i in Res:
            F_res.append(i[0])
        return F_res

class BLLThamSo:
    # Get Values
    def GetSDLTDMQ():
        return DALThamSo.GetSDLTDMQ()

    def GetSLDL_TS(*args):
        return DALThamSo.GetSLDL_TS(args[0])

    def GetTLDG():
        return DALThamSo.GetTLDG()
    
    # Update Values
    def UpdateSDLTDMQ(*args):
        DALThamSo.UpdateSDLTDMQ(args[0])

    def UpdateTLDG(*args):
        if(DALThamSo.UpdateTLDG(args[0]) == 'Thay đổi thành công!'):
            return 'Thay đổi thành công!'
        return 'Thay đổi thất bại!'
