# Khai Báo Thư Viện
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import os
import subprocess
import sys

from DTO import *
from BLL import *



# Cài Đặt Các Thư Viện Cần Thiết
def install(package):
    subprocess.check_call([sys.executable,"-m", "pip", "install", package])

TK = TaiKhoan()
TKBLL = TaiKhoanBLL()

class Account:
    KTTK = []

# Định Nghĩa Treeview Widget
class edit_treeview(ttk.Treeview):
            def __init__(self, master, **kw):
                super().__init__(master, **kw)
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

def GUI():
    # Trang Đăng Nhập
    def LogInPage(*args):
        LogIn_Window = tk.Tk()
        LogIn_Window.title('TRANG ĐĂNG NHẬP')

        w, h = (LogIn_Window.winfo_screenwidth()) / 2, (LogIn_Window.winfo_screenheight()/2)

        LogIn_Window.geometry('800x400+%d+%d' % (w - 400, h - 200))
        LogIn_Window.resizable(False, False)

        # Chuyển Đến Trang Chính
        def Switch_to_MainPage():
            LogIn_Window.destroy()
            MainPage()

        # Nút Đăng Nhập
        def DangNhapBtn():
            TK.TenTaiKhoan = WinEtr1.get()
            TK.MatKhau = WinEtr2.get()
            KTTK = TKBLL.KiemTraTK(TK.TenTaiKhoan, TK.MatKhau)
            if KTTK == 'Chua Nhap Tai Khoan':
                messagebox.showerror(title=u'Lỗi', message=u'Chưa Nhập Tài Khoản')
            elif KTTK == 'Chua Nhap Mat Khau':
                messagebox.showerror(title=u'Lỗi', message=u'Chưa Nhập Mật Khẩu')
            elif KTTK == 'Tai Khoan Hoac Mat Khau Khong Chinh Xac':
                messagebox.showerror(title=u'Lỗi', message=u'Tài Khoản Hoặc Mật Khẩu Không Chính Xác')
            else:
                messagebox.showinfo(title=u'Thông Báo', message=u'Đăng Nhập Thành Công')
                Account.KTTK.append(KTTK)
                Switch_to_MainPage()

        # Trỏ Vào 'Tài Khoản' Entry Widget
        def Etr1In(e):
            WinEtr1.delete(0, 'end')

        # Trỏ Ra 'Tài Khoản' Entry Widget
        def Etr1Out(e):
            if WinEtr1.get() == '':
                WinEtr1.insert(0, u'Tài Khoản')

        # Trỏ Vào 'Mật Khẩu' Entry Widget
        def Etr2In(e):
            WinEtr2.delete(0, 'end')
            WinEtr2.config(show='*')

        # Trỏ Ra 'Mật Khẩu' Entry Widget
        def Etr2Out(e):
            if WinEtr2.get() == '':
                WinEtr2.insert(0, u'Mật Khẩu')

        # Nhấn Enter Sau Khi Nhập 'Mật Khẩu' Entry Widget
        def Prs_Etr(e):
            DangNhapBtn()

        # Hình Nền Cho Trang Đăng Nhập
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "TrangDangNhap.png"
        file=abs_file_path+current_file
        trangdangnhap_photo = Image.open(file)
        LogIn_Window.Img = ImageTk.PhotoImage(trangdangnhap_photo)
        tk.Label(LogIn_Window, image=LogIn_Window.Img).pack(fill='both', expand=True)

        # Logo UIT Trên Trang Đăng Nhập
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "UITLogo.png"
        file=abs_file_path+current_file
        logo_photo = Image.open(file)
        LogIn_Window.Lg = ImageTk.PhotoImage(logo_photo)
        tk.Label(LogIn_Window, image=LogIn_Window.Lg).place(x=90, y=30)

        # Tạo Các Label Widget
        tk.Label(LogIn_Window,
                 text=u'Chào mừng đến với phần mềm',
                 font='Times 16',
                 fg='#D6D6D6',
                 bg='#1971B0').place(x=55, y=195)

        tk.Label(LogIn_Window,
                 text=u'Quản Lý Các Đại Lý',
                 font='Times 16',
                 fg='#D6D6D6',
                 bg='#1971B0').place(x=137, y=225)

        tk.Label(LogIn_Window,
                 text=u'Phát triển bởi Nhóm 23',
                 font='Times 10',
                 fg='#D6D6D6',
                 bg='#1971B0').place(x=185, y=350)

        tk.Label(LogIn_Window,
                 text=u'Đăng Nhập Vào Tài Khoản Của Bạn',
                 font='Times 18 bold',
                 fg='#1971B0',
                 bg='#EEEEEE').place(x=375, y=50)

        tk.Label(LogIn_Window,
                 text=u'Được hỗ trợ từ cô Đỗ Thị Thanh Tuyền',
                 font='Times 10',
                 fg='#858585',
                 bg='#EEEEEE').place(x=350, y=350)

        # Tạo Các Entry Widget
        WinEtr1 = tk.Entry(LogIn_Window, width=36, font='Times 16', bd=0)
        WinEtr1.place(x=390, y=144)
        WinEtr1.insert(0, u'Tài Khoản')
        WinEtr1.bind('<FocusIn>', Etr1In)
        WinEtr1.bind('<FocusOut>', Etr1Out)

        WinEtr2 = tk.Entry(LogIn_Window, width=36, font='Times 16', bd=0)
        WinEtr2.place(x=390, y=204)
        WinEtr2.insert(0, u'Mật Khẩu')
        WinEtr2.bind('<FocusIn>', Etr2In)
        WinEtr2.bind('<FocusOut>', Etr2Out)
        WinEtr2.bind('<Return>', Prs_Etr)

        # Tạo Các Button Widget
        tk.Button(LogIn_Window,
                  text=u'Đăng Nhập',
                  font='Times 16',
                  bg='#1971B0',
                  fg='White',
                  width=15,
                  command=DangNhapBtn).place(x=460, y=270)
        
        LogIn_Window.mainloop()

    # Trang Chính
    def MainPage():
        Main_Window = tk.Tk()
        Main_Window.title('TRANG CHÍNH')

        w, h = Main_Window.winfo_screenwidth(), Main_Window.winfo_screenheight()

        Main_Window.geometry('1280x720+%d+%d' % ((w/2) - 640, (h/2) - 360))
        Main_Window.resizable(False, False)

        # Nút Đổi Mật Khẩu
        def ChangePassWord():
            ChangePass_Win = tk.Tk()
            ChangePass_Win.title(u"Đổi mật khẩu")
            w, h = ChangePass_Win.winfo_screenwidth(), ChangePass_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            ChangePass_Win.geometry('500x260+%d+%d' % (sw, sh))
            def ChangePass(userName, newPass, verifyPass):
                Res = TaiKhoanBLL.ChangePassword(userName, newPass, verifyPass)
                if Res == False:
                    messagebox.showerror("Thông báo!!!", "Đổi mật khẩu thất bại do mật khẩu xác nhận không khớp!!!")
                else:
                    messagebox.showinfo("Thông báo!!!", "Đổi mật khẩu thành công!!! Đăng xuất để dùng mật khẩu mới!!!")
                    ChangePass_Win.destroy()

            ChangeFrm1 = tk.Frame(ChangePass_Win, width=500, height=50, bg="#3c8bec")
            ChangeFrm1.grid(row=0, column=0)
            ChangeFrm2 = tk.Frame(ChangePass_Win, width=500, height=450, bg="white")
            ChangeFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            ChangeFrm1lb = tk.Label(ChangeFrm1,
                                    width=22,
                                    text=u"ĐỔI MẬT KHẨU",
                                    fg="white",
                                    bg="#3c8bec",
                                    font=("Consolas", 15),
                                    anchor='w')
            ChangeFrm1lb.place(x=165, y=10)

            ChangeFrm2lb1 = tk.Label(ChangeFrm2,
                                     width=22,
                                     text=u"Tên tài khoản     :",
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     anchor='w')
            ChangeFrm2lb1.place(x=0, y=0)
            
            ChangeFrm2lb2 = tk.Label(ChangeFrm2,
                                     width=22,
                                     text=u"Mật khẩu mới      :",
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     anchor='w')
            ChangeFrm2lb2.place(x=0, y=60)
            
            ChangeFrm2lb3 = tk.Label(ChangeFrm2,
                                     width=22,
                                     text=u"Nhập lại mật khẩu :",
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     anchor='w')
            ChangeFrm2lb3.place(x=0, y=110)
            
            ChangeFrm2lb4 = tk.Label(ChangeFrm2,  #Set tên tài khoản
                                     width=22,
                                     text=Account.KTTK[0][0][0],
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     anchor='w')
            ChangeFrm2lb4.place(x=250, y=2)

            # Tạo Các Entry Widget
            ChangeFrm2et1 = tk.Entry(ChangeFrm2,
                                     width=22,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15))
            
            ChangeFrm2et2 = tk.Entry(ChangeFrm2,
                                     width=22,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15))

            ChangeFrm2et1.place(x=250, y=60)
            ChangeFrm2et2.place(x=250, y=110)

            # Tao Các Button Widget
            SelectedBtn1 = tk.Button(ChangeFrm2,
                                     width=18,
                                     text=u"Lưu",
                                     font='Times 16',
                                     bg='#3c8bec',
                                     fg='White',
                                     command=lambda: ChangePass(Account.KTTK[0][0][0], ChangeFrm2et1.get(), ChangeFrm2et2.get()))
            SelectedBtn1.place(x=10, y=160)
            SelectedBtn2 = tk.Button(ChangeFrm2,
                                     width=18,
                                     text=u"Thoát",
                                     font='Times 16',
                                     bg='#3c8bec',
                                     fg='White',
                                     command=ChangePass_Win.destroy)
            SelectedBtn2.place(x=260, y=160)

        # Chuyển Về Trang Chính
        def Switch_to_LogInPage():

            Main_Window.destroy()
            Account.KTTK.clear()
            LogInPage()

        # Nút In Phếu BCDS
        def Export_BCDS():
            data = {u'Mã BC doanh số': [],
                    u'Tháng':[],
                    u'Mã đại lý':[],
                    u'Số phiếu xuất':[],
                    u'Tổng trị giá':[],
                    u'Tỷ lệ':[]}
            for i in treeview.get_children():
                data[u'Mã BC doanh số'].append(treeview.item(i)['values'][0])
                data[u'Tháng'].append(treeview.item(i)['values'][1])
                data[u'Mã đại lý'].append(treeview.item(i)['values'][2])
                data[u'Số phiếu xuất'].append(treeview.item(i)['values'][3])
                data[u'Tổng trị giá'].append(treeview.item(i)['values'][4])
                data[u'Tỷ lệ'].append(treeview.item(i)['values'][5])
            df_BCDS = pd.DataFrame(data, columns=[u'Mã BC doanh số', u'Tháng', u'Mã đại lý', u'Só phiếu xuất', u'Tổng trị giá', u'Tỷ lệ'])
            file = asksaveasfilename(defaultextension=".xlsx")
            excel_writer = pd.ExcelWriter(file)
            df_BCDS.to_excel(excel_writer, index=False)
            excel_writer.close()

            messagebox.showinfo(u'Thông báo', u'Xuất bản báo cáo doanh số thành công.')

        # Nút In Phiếu BCCN
        def Export_BCCN():
            data = {u'Mã BC công nợ': [],
                    u'Tháng': [],
                    u'Mã đại lý': [],
                    u'Nợ đầu': [],
                    u'Phát sinh': [],
                    u'Nợ cuối': []}
            for i in treeview.get_children():
                data[u'Mã BC công nợ'].append(treeview.item(i)['values'][0])
                data[u'Tháng'].append(treeview.item(i)['values'][1])
                data[u'Mã đại lý'].append(treeview.item(i)['values'][2])
                data[u'Nợ đầu'].append(treeview.item(i)['values'][3])
                data[u'Phát sinh'].append(treeview.item(i)['values'][4])
                data[u'Nợ cuối'].append(treeview.item(i)['values'][5])
            df_BCCN = pd.DataFrame(data, columns=[u'Mã BC công nợ', u'Tháng', u'Mã đại lý', u'Nợ đầu', u'Phát sinh', u'Nợ cuối'])
            file = asksaveasfilename(defaultextension=".xlsx")
            excel_writer = pd.ExcelWriter(file)
            df_BCCN.to_excel(excel_writer, sheet_name='BCCN')
            excel_writer.close()

            messagebox.showinfo(u'Thông báo', u'Xuất bản báo cáo công nợ thành công.')

        # Các Hàm Thêm
        def AddDaiLy():
            AddDaiLy_Win = tk.Tk()
            AddDaiLy_Win.title(u"Thêm đại lý")
            w, h = AddDaiLy_Win.winfo_screenwidth(), AddDaiLy_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            AddDaiLy_Win.geometry('500x410+%d+%d' % (sw, sh))

            maldl = BLLdsDaiLy.GetMaLDL_dsLDL()
            maquan = BLLdsDaiLy.GetMaQuan_dsQuan()
            maldl_combobox = StringVar()
            maquan_combobox = StringVar()

            # Nút Thêm
            def Addnewdl():
                TenDaiLy = str(AddFrm2entry2.get())
                MaLoaiDL = str(AddFrm2entry3.get())
                Dienthoai = str(AddFrm2entry4.get())
                Diachi = str(AddFrm2entry5.get())
                Maquan = str(AddFrm2entry6.get())
                Ngaytiepnhan = AddFrm2entry7.get_date()
                
                GUIflag = BLLdsDaiLy.AddDSDaiLy(TenDaiLy, MaLoaiDL, Dienthoai, Diachi, Maquan, Ngaytiepnhan)
                if GUIflag == 'TDL rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đại lý không được để trống.')
                elif GUIflag == 'DT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Điện thoại không được để trống.')
                elif GUIflag == 'DC rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Địa chỉ không được để trống.')
                elif GUIflag == 'NTN rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày tiếp nhận không được để trống.')
                elif GUIflag == 'TDL dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đại lý quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'DT dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Điện thoại quá dài. Tối đa 15 ký tự.')
                elif GUIflag == 'DC dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Địa chỉ quá dài. Tối đa 50 ký tự.')
                elif GUIflag == 'SDLTQ toi da':
                    messagebox.showerror(u'Lỗi !!!', u'Số đại lý trong quận đã đạt giới hạn tối đa, xin vui lòng nhập lại '
                                                    u'hoặc thay đổi số đại lý tối đa trong mỗi quận.')
                elif GUIflag == 'SDT trung':
                    messagebox.showerror(u'Lỗi !!!', u'Số điện thoại đã tồn tại '
                                                    u'xin vui lòng nhập lại số điện thoại khác.')
                elif GUIflag == 'DC trung':
                    messagebox.showerror(u'Lỗi !!!', u'Địa chỉ đã tồn tại '
                                                    u'xin vui lòng nhập lại địa chỉ khác.')
                elif GUIflag == 'TDL trung':
                    messagebox.showerror(u'Lỗi !!!', u'Tên đại lý đã tồn tại '
                                                    u'xin vui lòng nhập tên đại lý khác.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công đại lý mới.')
                    Prs_Etr('f')
                    AddDaiLy_Win.destroy()

            AddFrm1 = tk.Frame(AddDaiLy_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)
            AddFrm2 = tk.Frame(AddDaiLy_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"THÊM ĐẠI LÝ MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=175, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên đại lý:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb4 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã loại đại lý :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb4.place(x=0, y=60)

            AddFrm2lb4 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Điện thoại :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb4.place(x=0, y=110)

            AddFrm2lb5 = tk.Label(AddFrm2,
                                  width=22,
                                  text="Địa chỉ :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb5.place(x=0, y=160)

            AddFrm2lb6 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã quận :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb6.place(x=0, y=210)

            AddFrm2lb7 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày tiếp nhận:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb7.place(x=0, y=260)

            # Tạo Entry Widget
            AddFrm2entry2 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo ComboBox Widget
            AddFrm2entry3 = ttk.Combobox(AddFrm2,
                                         textvariable=maldl_combobox,
                                         font=("bold", 16),
                                         state='readonly')

            # Tuple For Combobox Values
            maldl_tuple = ()
            for i in maldl:
                maldl_tuple += (i,)

            AddFrm2entry3['values'] = maldl_tuple
            AddFrm2entry3.current(0)

            AddFrm2entry3.place(x=200, y= 60)

            # Tạo Các Entry Widget
            AddFrm2entry4 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry4.place(x=200, y=110)

            AddFrm2entry5 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry5.place(x=200, y=160)

            # Tạo ComboBox Widget
            AddFrm2entry6 = ttk.Combobox(AddFrm2,
                                         textvariable=maquan_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # Tuple For Combobox Values
            maquan_tuple = ()
            for i in maquan:
                maquan_tuple += (i,)

            AddFrm2entry6['values'] = maquan_tuple
            AddFrm2entry6.current(0)
            AddFrm2entry6.place(x=200, y=210)

            # Tạo DateEntry Widget
            AddFrm2entry7 = DateEntry(AddFrm2,
                                    width=40,
                                    day=0, 
                                    month=1, 
                                    year=2023,
                                    bd=1,
                                    state='readonly',
                                    date_pattern='mm/dd/y')
            AddFrm2entry7.place(x=200, y=265)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewdl)
            AddFrm2Btn1.place(x=10, y=310)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=AddDaiLy_Win.destroy)
            AddFrm2Btn2.place(x=260, y=310)

        def AddLoaiDaiLy():
            LoaiDL_Add_Win = tk.Tk()
            LoaiDL_Add_Win.title(u"Thêm Loại đại lý")
            w, h = LoaiDL_Add_Win.winfo_screenwidth(), LoaiDL_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            LoaiDL_Add_Win.geometry('500x210+%d+%d' % (sw, sh))

            # Nút Thêm
            def Addnewldl():
                TenLoaiDaiLy = str(AddFrm2entry2.get())
                SoNoToida = str(AddFrm2entry3.get())

                GUIflag = BLLdsLoaiDaiLy.AddDSLoaiDL(TenLoaiDaiLy, SoNoToida)
                if GUIflag == 'TLDL rong':
                    messagebox.showwarning(u'Cảnh báo !!!', 'Tên loại đại lý không được để trống.')
                elif GUIflag == 'TLDL khong hop le':
                    messagebox.showwarning(u'Cảnh báo !!!', 'Tên loại đại lý không hợp lệ.')
                elif GUIflag == 'SNTD rong':
                    messagebox.showwarning(u'Cảnh báo !!!', 'Số nợ tối đa không được để trống.')
                elif GUIflag == 'TLDL dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên loại đại lý quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'STN am':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số nợ tối đa phải >= 0.')
                elif GUIflag == 'TLDL trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên loại đại lý đã tồn tại, vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công loại đại lý mới.')
                    Prs_Etr('f')
                    LoaiDL_Add_Win.destroy()

            AddFrm1 = tk.Frame(LoaiDL_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(LoaiDL_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Ta Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1, 
                                 width=22,
                                 text=u"THÊM LOẠI ĐẠI LÝ MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=150, y=10)
        
            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên loại đại lý:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)
            
            AddFrm2lb3 = tk.Label(AddFrm2, 
                                  width=22,
                                  text=u"Số nợ tối đa   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            # Tạo Các Entry Widget
            AddFrm2entry2 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry2.place(x=200, y=2)

            AddFrm2entry3 = tk.Entry(AddFrm2, 
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry3.place(x=200, y=60)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text="Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewldl)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2, 
                                    width=18, 
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=LoaiDL_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def AddQuan():
            Quan_Add_Win = tk.Tk()
            Quan_Add_Win.title(u"Thêm quận")
            w, h = Quan_Add_Win.winfo_screenwidth(), Quan_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            Quan_Add_Win.geometry('500x160+%d+%d' % (sw, sh))

            # Nút Thêm
            def Addnewquan():
                Tenquan = str(AddFrm2entry2.get())
                GUIflag = BLLdsQuan.AddDSQuan(Tenquan)
                if GUIflag == 'TQ rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên quận không được để trống.')
                elif GUIflag == 'TQ dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên quận quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'TQ trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên quận đã tồn tại, vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công quận mới.')
                    Prs_Etr('f')
                    Quan_Add_Win.destroy()

            AddFrm1 = tk.Frame(Quan_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(Quan_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"THÊM QUẬN MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=175, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên quận",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y= 0)

            # Tạo Entry Widget
            AddFrm2entry2 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewquan)
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Quan_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def AddMatHang():
            MatHang_Add_Win = tk.Tk()
            MatHang_Add_Win.title(u"Thêm mặt hàng")
            w, h = MatHang_Add_Win.winfo_screenwidth(), MatHang_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            MatHang_Add_Win.geometry('500x210+%d+%d' % (sw, sh))

            mamh = BLLdsMatHang.GetDVT_dsDVT()
            mamathang_combobox = StringVar()

            # Nút Thêm
            def Addnewmh():
                TenMH = str(AddFrm2entry2.get())
                MaDVT = str(AddFrm2entry3.get())

                GUIflag = BLLdsMatHang.AddDSMatHang(TenMH, MaDVT)
                if GUIflag == 'TMH rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên mặt hàng không được để trống.')
                elif GUIflag == 'TMH dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên mặt hàng quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'TenMH trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên mặt hàng đã tồn tại, xin vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công mặt hàng mới')
                    Prs_Etr('f')
                    MatHang_Add_Win.destroy()

            AddFrm1 = tk.Frame(MatHang_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(MatHang_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=23,
                                 text=u"THÊM MẶT HÀNG MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=145, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên mặt hàng  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đơn vị tính:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            # Tạo Entry Widget
            AddFrm2entry2 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo ComboBox Widget
            AddFrm2entry3 = ttk.Combobox(AddFrm2,
                                         textvariable=mamathang_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # Tuple For Combobox Values
            mamh_tuple = ()
            for i in mamh:
                mamh_tuple += (i,)

            AddFrm2entry3['values'] = mamh_tuple
            AddFrm2entry3.current(0)

            AddFrm2entry3.place(x=200, y= 60)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewmh)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=MatHang_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def AddDonviTinh():
            DVT_Add_Win = tk.Tk()
            DVT_Add_Win.title(u"Thêm đơn vị tính mới")
            w, h = DVT_Add_Win.winfo_screenwidth(), DVT_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            DVT_Add_Win.geometry('500x160+%d+%d' % (sw, sh))
            # Nút Thêm
            def Addnewdvt():
                TenDVT = str(AddFrm2entry2.get())

                GUIflag = BLLdsDVT.AddDSDVT(TenDVT)
                if GUIflag == 'TDVT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đơn vị tính không được để trống.')
                elif GUIflag == 'TDVT dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đơn vị tính quá dài. Tối đa 10 ký tự.')
                elif GUIflag == 'TenDVT trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đơn vị tính đã tồn tại, vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công đơn vị tính mới.')
                    Prs_Etr('f')
                    DVT_Add_Win.destroy()

            AddFrm1 = tk.Frame(DVT_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(DVT_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"THÊM ĐƠN VỊ TÍNH MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=150, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên đơn vị tính:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            # Tạo Entry Widget
            AddFrm2entry2 = tk.Entry(AddFrm2,
                                    width=23,
                                    fg="black",
                                    bg="white",
                                    font=("Consolas", 15),
                                    bd=1)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo Các Button Wisget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewdvt)
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=DVT_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def AddDsBCDS():
            BCDS_ADD_WIN = tk.Tk()
            BCDS_ADD_WIN.title(u"Thêm báo cáo doanh số tháng")
            w, h = BCDS_ADD_WIN.winfo_screenwidth(), BCDS_ADD_WIN.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            BCDS_ADD_WIN.geometry('500x210+%d+%d' % (sw, sh))

            madl = BLLdsDaiLy.GetMaDaiLy()
            thang_combobox = StringVar()
            madl_combobox = StringVar()

            # Nút Thêm
            def Addnewbcds():
                Thang = str(AddFrm2entry1.get())
                MaDL = str(AddFrm2entry2.get())

                GUIFlag = BLLdsBCDS.AddDSBCDS(Thang, MaDL)
                if GUIFlag == 'Bao cao da ton tai':
                    messagebox.showerror(u'Thông báo', u'Đã tồn tại báo cáo, thêm mới báo cáo thất bại.') 
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công báo cáo doanh số mới.') 
                    Prs_Etr('f')
                    BCDS_ADD_WIN.destroy()

            AddFrm1 = tk.Frame(BCDS_ADD_WIN, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(BCDS_ADD_WIN, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"THÊM BÁO CÁO DOANH SỐ MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=80, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tháng:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            # Tạo ComboBox Widget
            AddFrm2entry1=ttk.Combobox(AddFrm2,
                                    textvariable=thang_combobox,
                                    font=("bold", 16),
                                    state='readonly')

            # Tuple For Combobox Values
            thang_tuple = ()
            for i in range(1, 13):
                thang_tuple += (i,)

            AddFrm2entry1['values'] = thang_tuple
            AddFrm2entry1.current(0)

            AddFrm2entry1.place(x=200, y= 2)

            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                    textvariable=madl_combobox,
                                    font=("bold", 16),
                                    state='readonly')

            # Tuple For Combobox Values
            madl_tuple = ()
            for i in madl:
                madl_tuple += (i,)

            AddFrm2entry2['values'] = madl_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 60)

            # Tạo Label Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewbcds)
            AddFrm2Btn1.place(x=10, y=110)

            # Tạo Button Widget
            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=BCDS_ADD_WIN.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def AddDsBCCN():
            BCCN_ADD_WIN = tk.Tk()
            BCCN_ADD_WIN.title(u"Thêm báo cáo công nợ tháng")
            w, h = BCCN_ADD_WIN.winfo_screenwidth(), BCCN_ADD_WIN.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            BCCN_ADD_WIN.geometry('500x210+%d+%d' % (sw, sh))

            madl = BLLdsDaiLy.GetMaDaiLy()
            thang_combobox=StringVar()
            madl_combobox=StringVar()

            # Nút Thêm
            def Addnewbccn():
                Thang = str(AddFrm2entry2.get())
                MaDL = str(AddFrm2entry3.get())

                GUIFlag = BLLdsBCCN.AddDSBCCN(Thang, MaDL)
                if GUIFlag == 'Bao cao da ton tai':
                    messagebox.showerror(u'Thông báo', u'Báo cáo đã tồn tại, thêm mới báo cáo thất bại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công báo cáo công nợ mới.')
                    Prs_Etr('f')
                    BCCN_ADD_WIN.destroy()

            AddFrm1 = tk.Frame(BCCN_ADD_WIN, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(BCCN_ADD_WIN, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"THÊM BÁO CÁO CÔNG NỢ MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=80, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tháng:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            # Tạo ComboBox Widget
            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         textvariable=thang_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # Tuple For Combobox Values
            thang_tuple = ()
            for i in range(1, 13):
                thang_tuple += (i,)

            AddFrm2entry2['values'] = thang_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 2)

            AddFrm2entry3 = ttk.Combobox(AddFrm2,
                                    textvariable=madl_combobox,
                                    font=("bold", 16),
                                    state='readonly')

            # Tuple For Combobox Values
            madl_tuple = ()
            for i in madl:
                madl_tuple += (i,)

            AddFrm2entry3['values'] = madl_tuple
            AddFrm2entry3.current(0)

            AddFrm2entry3.place(x=200, y= 60)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Addnewbccn)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=BCCN_ADD_WIN.destroy)
            AddFrm2Btn2.place(x=260, y=110)
        
        def AddPhieuNhapHang():
            PhieuNH_Add_Win = tk.Tk()
            PhieuNH_Add_Win.title(u"Thêm phiếu nhập hàng")
            w, h = PhieuNH_Add_Win.winfo_screenwidth(), PhieuNH_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            PhieuNH_Add_Win.geometry('500x160+%d+%d' % (sw, sh))

            # Nút Thêm
            def Addnewpnh():
                NgayLapPhieu = AddFrm2entry2.get_date()

                GUIflag = BLLdsPhieuNH.AddDSPhieuNH(NgayLapPhieu)
                if GUIflag == 'NLP rong':
                    messagebox.showwarning(u'Cảnh báo !!!', 'Ngày lập phiếu không được để trống.')
                elif GUIflag == 'MPN dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Mã phiếu nhập quá dài. Tối đa 10 ký tự.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công phiếu nhập hàng mới.')
                    Prs_Etr('f')
                    PhieuNH_Add_Win.destroy()

            AddFrm1 = tk.Frame(PhieuNH_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(PhieuNH_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"THÊM PHIẾU NHẬP HÀNG MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=145, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày lập phiếu:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            # Tạo DataEntry Widget
            AddFrm2entry2 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      state='readonly',
                                      date_pattern='mm/dd/y')
            AddFrm2entry2.place(x=200, y=2)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=Addnewpnh)
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=PhieuNH_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def AddPhieuXuatHang():
            PhieuXH_Add_Win = tk.Tk()
            PhieuXH_Add_Win.title(u"Thêm phiếu xuất hàng")
            w, h = PhieuXH_Add_Win.winfo_screenwidth(), PhieuXH_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            PhieuXH_Add_Win.geometry('500x210+%d+%d' % (sw, sh))

            # Nút Thêm
            def Addnewpxh():
                NgayLapPhieu = AddFrm2entry3.get_date()

                GUIflag = BLLdsPhieuXH.AddDSPhieuXH(MaDaiLy.get(), NgayLapPhieu)
                if GUIflag == 'MDL rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Chưa có Đại Lý nào trong hệ thống. '
                                                            u'Vui lòng thêm Đại Lý trước.')
                elif GUIflag == 'NLP rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày lập phiếu không được để trống.')
                elif GUIflag == 'Ngay khong hop le':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày lập phiếu phải lớn hơn ngày tiếp nhận đại lý.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công phiếu xuất hàng mới')
                    Prs_Etr('f')
                    PhieuXH_Add_Win.destroy()

            AddFrm1 = tk.Frame(PhieuXH_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(PhieuXH_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"THÊM PHIẾU XUẤT HÀNG MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=145, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày lập phiếu:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            MaDaiLy = StringVar(AddFrm2)

            # Tạo ComboBox Widget
            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         font=("Consolas", 15),
                                         state='readonly',
                                         textvariable=MaDaiLy,
                                         width=23)
            lst = list()
            for i in BLLdsDaiLy.GetMaDaiLy():
                lst.append(i)
            AddFrm2entry2['values'] = lst
            AddFrm2entry2.current(0)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo DataEntry Widget
            AddFrm2entry3 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      state='readonly',
                                      date_pattern='mm/dd/y')
            AddFrm2entry3.place(x=200, y=60)

            # Tạo Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=Addnewpxh)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=PhieuXH_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def AddPhieuThuTien():
            AddPTT_Add_Win = tk.Tk()
            AddPTT_Add_Win.title(u"Thêm phiếu thu tiền")
            w, h = AddPTT_Add_Win.winfo_screenwidth(), AddPTT_Add_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            AddPTT_Add_Win.geometry('500x260+%d+%d' % (sw, sh))

            # Nút Thêm
            def Addnewptt():
                NgayThuTien = AddFrm2entry3.get_date()
                SoTienThu = str(AddFrm2entry4.get())
                GUIflag = BLLdsPTT.AddDSPTT(MaDaiLy.get(), NgayThuTien, SoTienThu)
                if GUIflag == 'MDL rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Chưa có Đại Lý nào trong hệ thống. '
                                                            u'Vui lòng thêm Đại Lý trước.')
                elif GUIflag == 'NTT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày thu tiền không được để trống.')
                elif GUIflag == 'STT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu không được để trống.')
                elif GUIflag == 'STT am':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu phải > 0.')
                elif GUIflag == 'STT > STN':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu phải <= Số tiền nợ của Đại Lý.')
                elif GUIflag =='Ngay khong hop le':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày thu tiền phải lớn hơn ngày tiếp nhận đại lý.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã thêm thành công phiếu thu tiền mới')
                    Prs_Etr('f')
                    AddPTT_Add_Win.destroy()

            AddFrm1 = tk.Frame(AddPTT_Add_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(AddPTT_Add_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            # Tạo Các Label Widget
            AddFrm1lb = tk.Label(AddFrm1,
                                 width=25,
                                 text=u"THÊM PHIẾU THU TIỀN MỚI",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=110, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày thu tiền:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            AddFrm2lb4 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Số tiền thu  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb4.place(x=0, y=110)

            MaDaiLy = StringVar(AddFrm2)

            # Tạo ComboBox Widget
            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         font=("Consolas", 15),
                                         state='readonly',
                                         textvariable=MaDaiLy,
                                         width=23)
            lst = list()
            for i in BLLdsDaiLy.GetMaDaiLy():
                lst.append(i)
            AddFrm2entry2['values'] = lst
            AddFrm2entry2.current(0)
            AddFrm2entry2.place(x=200, y=2)

            # Tạo DataEntry Widget
            AddFrm2entry3 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      state='readonly',
                                      date_pattern='mm/dd/y')
            AddFrm2entry3.place(x=200, y=60)

            # Tạo Entry Widget
            AddFrm2entry4 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry4.place(x=200, y=110)

            # Tạo Các Button Widget
            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=22,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=Addnewptt)
            AddFrm2Btn1.place(x=10, y=160)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=22,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='white',
                                    command=AddPTT_Add_Win.destroy)
            AddFrm2Btn2.place(x=260, y=160)

        # Các Hàm Cập Nhật
        def UpdateDaiLy(MaDaiLy):
            
            selectedItem = treeview.selection()[0]
            tendldefault=str(treeview.item(selectedItem)['values'][1])
            sdtdefault=str(treeview.item(selectedItem)['values'][3])
            dcdefault=str(treeview.item(selectedItem)['values'][4])
            ntndefault=(treeview.item(selectedItem)['values'][6])

            DaiLy_Update_Win = tk.Tk()
            DaiLy_Update_Win.title(u"Cập nhật đại lý")
            w, h = DaiLy_Update_Win.winfo_screenwidth(), DaiLy_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            DaiLy_Update_Win.geometry('500x410+%d+%d' % (sw, sh))

            Maldl = DALdsLoaiDaiLy.GetMaLoaiDL()
            Maquan = DALdsQuan.GetMaQuan()
            maldl_combobox = StringVar()
            maquan_combobox = StringVar()

            def UpdateDL():
                TenDaiLy = str(AddFrm2entry1.get())
                Maloaidaily = str(AddFrm2entry2.get())
                Dienthoai = str(AddFrm2entry3.get())
                Diachi = str(AddFrm2entry4.get())
                Maquan = str(AddFrm2entry5.get())
                Ngaytiepnhan = AddFrm2entry6.get_date()
                
                GUIflag = BLLdsDaiLy.UpdateDSDaiLy(MaDaiLy, TenDaiLy, Maloaidaily, Dienthoai, Diachi, Maquan, Ngaytiepnhan)
                if GUIflag == 'TDL dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đại lý quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'DT dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Điện thoại quá dài. Tối đa 15 ký tự.')
                elif GUIflag == 'DC dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Địa chỉ quá dài. Tối đa 50 ký tự.')
                elif GUIflag == 'SDLTQ toi da':
                    messagebox.showerror(u'Lỗi !!!', u'Số đại lý trong quận đã đạt giới hạn tối đa, xin vui lòng nhập lại '
                                                    u'hoặc thay đổi số đại lý tối đa trong mỗi quận.')
                elif GUIflag == 'SDT trung':
                    messagebox.showerror(u'Lỗi !!!', 'Số điện thoại đã tồn tại.'
                                                    'xin vui lòng nhập lại.')
                elif GUIflag == 'DC trung':
                    messagebox.showerror(u'Lỗi !!!', 'Địa chỉ đã tồn tại '
                                                    'xin vui lòng nhập lại.')
                elif GUIflag == 'TDL trung':
                    messagebox.showerror(u'Lỗi !!!', 'Tên đại lý đã tồn tại trong quận.'
                                                    'xin vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật đại lý thành công.')
                    Prs_Etr('f')
                    DaiLy_Update_Win.destroy()

            AddFrm1 = tk.Frame(DaiLy_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(DaiLy_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"CẬP NHẬT ĐẠI LÝ",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=175, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên đại lý:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y=0)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã loại đại lý:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y= 60)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Điện thoại:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=110)

            AddFrm2lb4 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Địa chỉ:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb4.place(x=0, y= 160)

            AddFrm2lb5 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã quận:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb5.place(x=0, y=210)

            AddFrm2lb6 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày tiếp nhận:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb6.place(x=0, y= 260)

            AddFrm2entry1 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry1.insert(tk.END,tendldefault)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         textvariable=maldl_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            maldl_tuple = ()
            for i in Maldl:
                maldl_tuple += (i,)

            AddFrm2entry2['values'] = maldl_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 60)

            AddFrm2entry3 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry3.insert(tk.END, sdtdefault)
            AddFrm2entry3.place(x=200, y=110)

            AddFrm2entry4 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry4.insert(tk.END, dcdefault)
            AddFrm2entry4.place(x=200, y=160)

            AddFrm2entry5 = ttk.Combobox(AddFrm2,
                                         textvariable=maquan_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            maquan_tuple = ()
            for i in Maquan:
                maquan_tuple += (i,)

            AddFrm2entry5['values'] = maquan_tuple
            AddFrm2entry5.current(0)

            AddFrm2entry5.place(x=200, y= 210)

            AddFrm2entry6 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      date_pattern='mm/dd/y')
            AddFrm2entry6.delete(0, tk.END)
            AddFrm2entry6.insert(0, ntndefault)
            AddFrm2entry6.place(x=200, y=260)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=UpdateDL)
            AddFrm2Btn1.place(x=10, y=310)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=DaiLy_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=310)

        def UpdateLoaiDaiLy(Maloaidaily):
            LoaiDaiLy_Update_Win = tk.Tk()
            LoaiDaiLy_Update_Win.title(u"Cập nhật loại đại lý")
            w, h = LoaiDaiLy_Update_Win.winfo_screenwidth(), LoaiDaiLy_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            LoaiDaiLy_Update_Win.geometry('500x210+%d+%d' % (sw, sh))

            selectedItem = treeview.selection()[0]
            tenldldefault = str(treeview.item(selectedItem)['values'][1])
            sonotoida = int(treeview.item(selectedItem)['values'][2])

            def Updateldl():
                TenLoaiDaiLy = str(AddFrm2entry1.get())
                SoNoToida = str(AddFrm2entry2.get())

                GUIflag = BLLdsLoaiDaiLy.UpdateDSLoaiDL(Maloaidaily, TenLoaiDaiLy, SoNoToida)
                if GUIflag == 'TLDL rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên loại đại lý không được để trống.')
                elif GUIflag == 'SNTD rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số nợ tối đa không được để trống.')
                elif GUIflag == 'TLDL dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên loại đại lý quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'SNTD am':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số nợ tối đa phải >= 0.')
                elif GUIflag == 'TLDL trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên loại đại lý đã tồn tại, vui lòng nhập lại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật loại đại lý thành công.')
                    Prs_Etr('f')
                    LoaiDaiLy_Update_Win.destroy()

            AddFrm1 = tk.Frame(LoaiDaiLy_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(LoaiDaiLy_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"CẬP NHẬT LOẠI ĐẠI LÝ",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=150, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên loại đại lý:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y= 0)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Số nợ tối đa   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y= 60)

            AddFrm2entry1 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry1.insert(tk.END, tenldldefault)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry2.insert(tk.END, sonotoida)
            AddFrm2entry2.place(x=200, y=60)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Updateldl)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=LoaiDaiLy_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def UpdateQuan(Maquan):
            Quan_Update_Win = tk.Tk()
            Quan_Update_Win.title(u"Cập nhật quận")
            w, h = Quan_Update_Win.winfo_screenwidth(), Quan_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            Quan_Update_Win.geometry('500x160+%d+%d' % (sw, sh))

            selectedItem = treeview.selection()[0]
            tenquandefault = str(treeview.item(selectedItem)['values'][1])
            
            def Updatequan(Maquan):
                Tenquan = str(AddFrm2entry1.get())

                GUIflag = BLLdsQuan.UpdateDSQuan(Maquan, Tenquan)
                if GUIflag == 'TQ dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên quận quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'TQ trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên quận đã tồn tại.')
                elif GUIflag == 'K cập nhật':
                    messagebox.showinfo(u'Thông báo', u'Không cập nhật lại quận.')
                    Quan_Update_Win.destroy()
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật quận thành công.')
                    Prs_Etr('f')
                    Quan_Update_Win.destroy()

            AddFrm1 = tk.Frame(Quan_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(Quan_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"CẬP NHẬT QUẬN",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=175, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên quận",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=0)

            AddFrm2entry1 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry1.insert(tk.END, tenquandefault)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=lambda: Updatequan(Maquan))
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Quan_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def UpdateMatHang(MaMH):
            MatHang_Update_Win = tk.Tk()
            MatHang_Update_Win.title(u"Cập nhật mặt hàng")
            w, h = MatHang_Update_Win.winfo_screenwidth(), MatHang_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            MatHang_Update_Win.geometry('500x210+%d+%d' % (sw, sh))

            MaDVT = DALdsDVT.GetMaDVT()
            madvt_combobox = StringVar()
            
            selectedItem = treeview.selection()[0]
            tenmhdefault=str(treeview.item(selectedItem)['values'][1])

            def Updatemh(MaMH):
                TenMH = str(AddFrm2entry1.get())
                MaDVT = str(AddFrm2entry2.get())

                GUIflag = BLLdsMatHang.UpdateDSMatHang(MaMH, TenMH, MaDVT)
                if GUIflag == 'TMH dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên mặt hàng quá dài. Tối đa 20 ký tự.')
                elif GUIflag == 'TenMH trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên mặt hàng đã tồn tại, xin vui lòng nhập lại.')
                elif GUIflag == 'K cập nhật':
                    messagebox.showinfo(u'Thông báo', u'Không cập nhật lại mặt hàng.')
                    MatHang_Update_Win.destroy()
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật mặt hàng thành công.')
                    Prs_Etr('f')
                    MatHang_Update_Win.destroy()

            AddFrm1 = tk.Frame(MatHang_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(MatHang_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"CẬP NHẬT MẶT HÀNG",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=165, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                 width=22,
                                 text=u"Tên mặt hàng  :",
                                 fg="black",
                                 bg="white",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm2lb2.place(x=0, y=2)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đơn vị tính:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            AddFrm2entry1 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry1.insert(tk.END, tenmhdefault)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         textvariable=madvt_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            madvt_tuple = ()
            for i in MaDVT:
                madvt_tuple += (i,)

            AddFrm2entry2['values'] = madvt_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 60)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=lambda: Updatemh(MaMH))
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=MatHang_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def UpdateDVT(MaDVT):
            DVT_Update_Win = tk.Tk()
            DVT_Update_Win.title(u"Cập nhật đơn vị tính")
            w, h = DVT_Update_Win.winfo_screenwidth(), DVT_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            DVT_Update_Win.geometry('500x160+%d+%d' % (sw, sh))

            selectedItem = treeview.selection()[0]
            tendvtdefault=str(treeview.item(selectedItem)['values'][1])

            def Updatedvt(MaDVT):
                TenDVT = str(AddFrm2entry1.get())

                GUIflag = BLLdsDVT.UpdateDSDVT(MaDVT, TenDVT)
                if GUIflag == 'TDVT dai':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đơn vị tính quá dài. Tối đa 10 ký tự.')
                elif GUIflag == 'TenDVT trung':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Tên đơn vị tính đã tồn tại, vui lòng nhập lại.')
                elif GUIflag == 'K cập nhật':
                    messagebox.showinfo(u'Thông báo', u'Không có cập nhật lại đơn vị tính.')
                    DVT_Update_Win.destroy()
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật đơn vị tính thành công.')
                    Prs_Etr('f')
                    DVT_Update_Win.destroy()

            AddFrm1 = tk.Frame(DVT_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(DVT_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=22,
                                 text=u"CẬP NHẬT ĐƠN VỊ TÍNH",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=150, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tên đơn vị tính:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y=0)

            AddFrm2entry1 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry1.insert(tk.END, tendvtdefault)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=lambda: Updatedvt(MaDVT))
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=DVT_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def UpdateDsBCDS(maBCDS):
            Update_BCDS_WIN = tk.Tk()

            Update_BCDS_WIN.title(u"Cập nhật báo cáo doanh số")
            w, h = Update_BCDS_WIN.winfo_screenwidth(), Update_BCDS_WIN.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            Update_BCDS_WIN.geometry('500x210+%d+%d' % (sw, sh))

            madl = BLLdsDaiLy.GetMaDaiLy()
            thang_combobox=StringVar()
            madl_combobox=StringVar()

            def Updatect_pnh():
                Thang = str(AddFrm2entry1.get())
                MaDL = str(AddFrm2entry2.get())

                GUIFlag = BLLdsBCDS.UpdateDSBCDS(maBCDS, Thang, MaDL)
                if GUIFlag == 'Bao cao trung':
                    messagebox.showerror(u'Thông báo', u'Báo cáo bị trùng, cập nhật thất bại.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật thành công báo cáo doanh số.')
                    Prs_Etr('f')
                    Update_BCDS_WIN.destroy()

            AddFrm1 = tk.Frame(Update_BCDS_WIN, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(Update_BCDS_WIN, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"CẬP NHẬT BÁO CÁO DOANH SỐ THÁNG",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=80, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tháng:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y=0)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=60)

            AddFrm2entry1 = ttk.Combobox(AddFrm2,
                                         textvariable=thang_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            thang_tuple = ()
            for i in range(1, 13):
                thang_tuple += (i,)

            AddFrm2entry1['values'] = thang_tuple
            AddFrm2entry1.current(0)

            AddFrm2entry1.place(x=200, y= 2)

            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         textvariable=madl_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            madl_tuple = ()
            for i in madl:
                madl_tuple += (i,)

            AddFrm2entry2['values'] = madl_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 60)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Updatect_pnh)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Update_BCDS_WIN.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def UpdateDsBCCN(maBCCN):
            Update_BCCN_WIN = tk.Tk()
            Update_BCCN_WIN.title(u"Cập nhật báo cáo doanh số")
            w, h = Update_BCCN_WIN.winfo_screenwidth(), Update_BCCN_WIN.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            Update_BCCN_WIN.geometry('500x210+%d+%d' % (sw, sh))

            madl = BLLdsDaiLy.GetMaDaiLy()
            thang_combobox=StringVar()
            madl_combobox=StringVar()

            def Updatect_pnh():
                Thang = str(AddFrm2entry1.get())
                MaDL = str(AddFrm2entry2.get())

                GUIFlag = BLLdsBCCN.UpdateDSBCCN(maBCCN, Thang, MaDL)
                if GUIFlag == 'Bao cao trung':
                    messagebox.showerror(u'Thông báo', u'Báo cáo trùng, cập nhật báo cáo thất bại.')
                else:   
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật thành công báo cáo công nợ.')
                    Prs_Etr('f')
                    Update_BCCN_WIN.destroy()

            AddFrm1 = tk.Frame(Update_BCCN_WIN, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(Update_BCCN_WIN, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"CẬP NHẬT BÁO CÁO CÔNG NỢ THÁNG",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=80, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Tháng:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y=0)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý   :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=60)

            AddFrm2entry1 = ttk.Combobox(AddFrm2,
                                         textvariable=thang_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            thang_tuple = ()
            for i in range(1, 13):
                thang_tuple += (i,)

            AddFrm2entry1['values'] = thang_tuple
            AddFrm2entry1.current(0)

            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                         textvariable=madl_combobox,
                                         font=("bold", 16),
                                         state='readonly')
            # tuple for combobox values
            madl_tuple = ()
            for i in madl:
                madl_tuple += (i,)

            AddFrm2entry2['values'] = madl_tuple
            AddFrm2entry2.current(0)

            AddFrm2entry2.place(x=200, y= 60)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thêm",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Updatect_pnh)
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Update_BCCN_WIN.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def UpdatePhieuNhapHang(MaPhieuNhap):
            PhieuNhapHang_Update_Win = tk.Tk()
            PhieuNhapHang_Update_Win.title(u"Cập nhật phiếu nhập hàng")
            w, h = PhieuNhapHang_Update_Win.winfo_screenwidth(), PhieuNhapHang_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            PhieuNhapHang_Update_Win.geometry('500x160+%d+%d' % (sw, sh))

            Select = treeview.selection()[0]
            NLP_Old = treeview.item(Select)['values'][1]

            def Updatepnh():
                NgayLapPhieu = AddFrm2entry1.get_date()

                GUIflag = BLLdsPhieuNH.UpdateDSPhieuNH(MaPhieuNhap, NgayLapPhieu)
                if GUIflag == 'NLP rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày lập phiếu không được để trống.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật phiếu nhập hàng thành công.')
                    Prs_Etr('f')
                    PhieuNhapHang_Update_Win.destroy()

            AddFrm1 = tk.Frame(PhieuNhapHang_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(PhieuNhapHang_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"CẬP NHẬT PHIẾU NHẬP HÀNG",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=130, y=10)

            AddFrm2lb1 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày lập phiếu:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb1.place(x=0, y=0)

            AddFrm2entry1 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      date_pattern='mm/dd/y')
            AddFrm2entry1.delete(0, tk.END)
            AddFrm2entry1.insert(0, NLP_Old)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=Updatepnh)
            AddFrm2Btn1.place(x=10, y=60)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=PhieuNhapHang_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=60)

        def UpdatePhieuXuatHang(MaPhieuXuat):
            PhieuXuatHang_Update_Win = tk.Tk()
            PhieuXuatHang_Update_Win.title(u"Cập nhật phiếu xuất hàng")
            w, h = PhieuXuatHang_Update_Win.winfo_screenwidth(), PhieuXuatHang_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            PhieuXuatHang_Update_Win.geometry('500x210+%d+%d' % (sw, sh))

            Select = treeview.selection()[0]
            MaDaiLy_Old = treeview.item(Select)['values'][1]
            NLP_Old = treeview.item(Select)['values'][2]

            def Updatepxh(MaPXH):
                NgayLapPhieu = AddFrm2entry2.get_date()

                GUIflag = BLLdsPhieuXH.UpdateDSPhieuXH(MaPXH, AddFrm2entry1.get(), NgayLapPhieu)
                if GUIflag == 'NLP rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày lập phiếu không được để trống.')
                elif GUIflag == 'Ngay khong hop le':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày lập phiếu phải lớn hơn ngày tiếp nhận đại lý.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật phiếu xuất hàng thành công.')
                    Prs_Etr('f')
                    PhieuXuatHang_Update_Win.destroy()

            AddFrm1 = tk.Frame(PhieuXuatHang_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(PhieuXuatHang_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=33,
                                 text=u"CẬP NHẬT PHIẾU XUẤT HÀNG",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=135, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=2)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày lập phiếu:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            MaDaiLy = StringVar()
            Lst = list()
            for i in BLLdsDaiLy.GetMaDaiLy():
                Lst.append(i)

            AddFrm2entry1 = ttk.Combobox(AddFrm2,
                                         font=("Consolas", 15),
                                         state='readonly',
                                         textvariable=MaDaiLy,
                                         values=Lst,
                                         width=23)
            AddFrm2entry1.set(MaDaiLy_Old)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      date_pattern='mm/dd/y')
            AddFrm2entry2.delete(0, tk.END)
            AddFrm2entry2.insert(0, NLP_Old)
            AddFrm2entry2.place(x=200, y=60)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=lambda: Updatepxh(MaPhieuXuat))
            AddFrm2Btn1.place(x=10, y=110)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=PhieuXuatHang_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=110)

        def UpdatePhieuThuTien(MaPhieuThuTien):
            PhieuThuTien_Update_Win = tk.Tk()
            PhieuThuTien_Update_Win.title(u"Cập nhật phiếu thu tiền")
            w, h = PhieuThuTien_Update_Win.winfo_screenwidth(), PhieuThuTien_Update_Win.winfo_screenheight()
            sw, sh = (w / 2) - 400, (h / 2) - 200
            PhieuThuTien_Update_Win.geometry('500x260+%d+%d' % (sw, sh))

            Select = treeview.selection()[0]
            MaDaiLy_Old = treeview.item(Select)['values'][1]
            NgayThuTien_Old = treeview.item(Select)['values'][2]
            SoTienThu_Old = treeview.item(Select)['values'][3]

            def Updateptt(MaPTT):
                NgayThuTien = AddFrm2entry2.get_date()
                SoTienThu = float(AddFrm2entry3.get())

                GUIflag = BLLdsPTT.UpdateDSPTT(MaPTT, AddFrm2entry1.get(), NgayThuTien, SoTienThu)
                if GUIflag == 'NTT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày thu tiền không được để trống.')
                elif GUIflag == 'STT rong':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu không được để trống.')
                elif GUIflag == 'STT am':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu phải > 0.')
                elif GUIflag == 'STT > STN':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Số tiền thu phải <= Số tiền nợ.')
                elif GUIflag == 'Ngay khong hop le':
                    messagebox.showwarning(u'Cảnh báo !!!', u'Ngày thu tiền phải lớn hơn ngày tiếp nhận đại lý.')
                else:
                    messagebox.showinfo(u'Thông báo', u'Đã cập nhật phiếu thu tiền thành công.')
                    Prs_Etr('f')
                    PhieuThuTien_Update_Win.destroy()

            AddFrm1 = tk.Frame(PhieuThuTien_Update_Win, width=500, height=50, bg="#3c8bec")
            AddFrm1.grid(row=0, column=0)

            AddFrm2 = tk.Frame(PhieuThuTien_Update_Win, width=500, height=450, bg="white")
            AddFrm2.grid(row=1, column=0)

            AddFrm1lb = tk.Label(AddFrm1,
                                 width=25,
                                 text=u"CẬP NHẬT PHIẾU THU TIỀN",
                                 fg="white",
                                 bg="#3c8bec",
                                 font=("Consolas", 15),
                                 anchor='w')
            AddFrm1lb.place(x=100, y=10)

            AddFrm2lb2 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Mã đại lý  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb2.place(x=0, y=2)

            AddFrm2lb3 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Ngày thu tiền:",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb3.place(x=0, y=60)

            AddFrm2lb4 = tk.Label(AddFrm2,
                                  width=22,
                                  text=u"Số tiền thu  :",
                                  fg="black",
                                  bg="white",
                                  font=("Consolas", 15),
                                  anchor='w')
            AddFrm2lb4.place(x=0, y=110)

            MaDaiLy = StringVar()
            Lst = list()
            for i in BLLdsDaiLy.GetMaDaiLy():
                Lst.append(i)

            AddFrm2entry1 = ttk.Combobox(AddFrm2,
                                         textvariable=MaDaiLy,
                                         font=("Consolas", 15),
                                         state='readonly',
                                         values=Lst,
                                         width=23)
            AddFrm2entry1.set(MaDaiLy_Old)
            AddFrm2entry1.place(x=200, y=2)

            AddFrm2entry2 = DateEntry(AddFrm2,
                                      width=40,
                                      day=0,
                                      month=1,
                                      year=2023,
                                      bd=1,
                                      state='readonly',
                                      date_pattern='mm/dd/y')
            AddFrm2entry2.insert(0, tk.END)
            AddFrm2entry2.insert(0, NgayThuTien_Old)
            AddFrm2entry2.place(x=200, y=60)

            AddFrm2entry3 = tk.Entry(AddFrm2,
                                     width=23,
                                     fg="black",
                                     bg="white",
                                     font=("Consolas", 15),
                                     bd=1)
            AddFrm2entry3.insert('end', SoTienThu_Old)
            AddFrm2entry3.place(x=200, y=110)

            AddFrm2Btn1 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Cập nhật",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=lambda: Updateptt(MaPhieuThuTien))
            AddFrm2Btn1.place(x=10, y=160)

            AddFrm2Btn2 = tk.Button(AddFrm2,
                                    width=18,
                                    text=u"Thoát",
                                    font='Times 16',
                                    bg='#3c8bec',
                                    fg='White',
                                    command=PhieuThuTien_Update_Win.destroy)
            AddFrm2Btn2.place(x=260, y=160)

        # Bind The Single Click On MainPage
        def on_single_click(event):
            single_region = treeview.identify_region(event.x, event.y)
            Choice = category.get()
            if single_region == 'cell':
                Main_Window_Button8.config(state=tk.DISABLED)
                Main_Window_Button9.config(state=tk.ACTIVE)
                Main_Window_Button10.config(state=tk.ACTIVE)
                if Choice in (u'DANH SÁCH PHIẾU NHẬP HÀNG', u'DANH SÁCH PHIẾU XUẤT HÀNG'):
                    rel_path = "IMAGE\\"
                    abs_file_path = os.path.join(script_dir, rel_path)
                    current_file = "detail.png"
                    file=abs_file_path+current_file
                    detail_photo = Image.open(file)
                    detail_image = detail_photo.resize((35, 35), Image.LANCZOS)
                    Main_Window.detail_img = ImageTk.PhotoImage(detail_image)
                    Main_Window_Button5.config(text=u'  CHI TIẾT PHIẾU  ', width=275, image=Main_Window.detail_img, bd=0, borderwidth=0, compound='left', command=Show_Detail_Note)
                    Main_Window_Button5.place(x=0, y=576)

            elif single_region == 'nothing':
                for i in treeview.selection():
                    treeview.selection_remove(i)
                Main_Window_Button8.config(state=tk.ACTIVE)
                Main_Window_Button9.config(state=tk.DISABLED)
                Main_Window_Button10.config(state=tk.DISABLED)
                if(category.get() in (u'DANH SÁCH BÁO CÁO DOANH SỐ',u'DANH SÁCH BÁO CÁO CÔNG NỢ')):
                    pass
                else:
                    Main_Window_Button5.place_forget()
            else:
                return

        # Custom The Treeview Font Size And Row Height
        Config = ttk.Style()
        Config.configure("Custom.Treeview", highlightthickness=0, bd=0, font=('Times', 13), rowheight=40) # Modify the font of the body
        Config.configure("Custom.Treeview.Heading", font=('Times', 13, 'bold')) # Modify the font of the headings
        Config.layout("Custom.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # Hiển Thị Các Widget
        def Show():
            # Show Widgets
            Main_Window_Combobox_Ds.place(x=281, y=72)
            Main_Window_Entry.place(x=896, y=72)
            Main_Window_Button7.place(x=1209, y=72)
            Main_Window_Button8['state'] = tk.ACTIVE
            Main_Window_Button8.place(x=281, y=648)
            Main_Window_Button9['state'] = tk.DISABLED
            Main_Window_Button9.place(x=640, y=648)
            Main_Window_Button10['state'] = tk.DISABLED
            Main_Window_Button10.place(x=998, y=648)

        # Các Danh Sách Quản Lý - ComboBox
        def CasDs():   
            Main_Window_Button.config(fg='black', bg='white')
            Main_Window_Button2.config(fg='white', bg='#3c8bec')
            Main_Window_Button3.config(fg='white', bg='#3c8bec')
            Main_Window_Button4.config(fg='white', bg='#3c8bec')
            Main_Window_Button5.place_forget()

            Main_Window_Entry1.place_forget()
            Main_Window_Entry2.place_forget()
            Show()
            Main_Window_Combobox_Ds.config(values=[u'DANH SÁCH ĐẠI LÝ',
                                                   u'DANH SÁCH LOẠI ĐẠI LÝ',
                                                   u'DANH SÁCH QUẬN',
                                                   u'DANH SÁCH MẶT HÀNG',
                                                   u'DANH SÁCH ĐƠN VỊ TÍNH'])
            Main_Window_Combobox_Ds.current(0)
            Default_Treeview(category.get())
            Main_Window_Combobox_Ds.bind('<<ComboboxSelected>>', Prs_Etr)
            Main_Window_Button8.config(command=Add)

        # Các Danh Sách Phiếu - ComboBox
        def Show_Note():
            Main_Window_Button.config(fg='white', bg='#3c8bec')
            Main_Window_Button2.config(fg='black', bg='white')
            Main_Window_Button3.config(fg='white', bg='#3c8bec')
            Main_Window_Button4.config(fg='white', bg='#3c8bec')
            Main_Window_Button5.place_forget()

            Main_Window_Entry.place_forget()
            Main_Window_Entry1.place_forget()
            Main_Window_Entry2.place(x=896, y=72)

            Show()
            Main_Window_Combobox_Ds.config(values=[u'DANH SÁCH PHIẾU NHẬP HÀNG',
                                                   u'DANH SÁCH PHIẾU XUẤT HÀNG',
                                                   u'DANH SÁCH PHIẾU THU TIỀN'])
            Main_Window_Combobox_Ds.current(0)
            Default_Treeview(category.get())
            Main_Window_Combobox_Ds.bind('<<ComboboxSelected>>', Prs_Etr)

        # Nút In Phiếu BÁO CÁO
        def Export_Report():
            if(str(Main_Window_Combobox_Ds.get()) == u'DANH SÁCH BÁO CÁO DOANH SỐ'):
                Export_BCDS()
            elif(str(Main_Window_Combobox_Ds.get()) == u'DANH SÁCH BÁO CÁO CÔNG NỢ'):
                Export_BCCN()

        # Các Danh Sách Báo Cáo - ComboBox
        def Show_Report():

            Main_Window_Button.config(fg='white', bg='#3c8bec')
            Main_Window_Button2.config(fg='white', bg='#3c8bec')
            Main_Window_Button3.config(fg='black', bg='white')
            Main_Window_Button4.config(fg='white', bg='#3c8bec')
            
            Main_Window_Entry.place_forget()
            Main_Window_Entry2.place_forget()
            Main_Window_Entry1.place(x=896, y=72)
           
            rel_path = "IMAGE\\"
            abs_file_path = os.path.join(script_dir, rel_path)
            current_file = "excel.png"
            file=abs_file_path+current_file
            export_photo = Image.open(file)
            export_image = export_photo.resize((35, 35), Image.LANCZOS)
            Main_Window.export_img = ImageTk.PhotoImage(export_image)
            Main_Window_Button5.config(text=u'  XUẤT BÁO CÁO  ', width=275, bd=0, borderwidth=0, image=Main_Window.export_img, compound='left')
            Main_Window_Button5.place(x=0, y=576)
            Show()
            Main_Window_Combobox_Ds.config(values=[u'DANH SÁCH BÁO CÁO DOANH SỐ',
                                                   u'DANH SÁCH BÁO CÁO CÔNG NỢ'])
            Main_Window_Combobox_Ds.current(0)
            Default_Treeview(category.get())
            Main_Window_Combobox_Ds.bind('<<ComboboxSelected>>', Prs_Etr)
            Main_Window_Button8.config(command=Add)
            Main_Window_Button5.config(command=Export_Report)

        # Nút Xem Chi Tiết Phiếu Nhập - Xuất Hàng
        def Show_Detail_Note():

            Detail_Note_Win = tk.Toplevel(Main_Window)
            Detail_Note_Win.title(u'DANH SÁCH CÁC PHIẾU CHI TIẾT')
            Detail_Note_Win.resizable(False, False)
            w = (Detail_Note_Win.winfo_screenwidth() / 2) - 500
            h = (Detail_Note_Win.winfo_screenheight() / 2) - 300
            Detail_Note_Win.geometry('1000x600+%d+%d' % (w, h))
            Detail_Note_Win.grab_set()

            def Upt_Detail_Note_Treeview():
                for i in Detail_Note_Treeview.get_children():
                    Detail_Note_Treeview.delete(i)

                if category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    for i in BLLdsCT_PNH.GetDSCT_PNH_Key(Key):
                        Detail_Note_Treeview.insert('', 'end', iid=i[0],
                                                    values=(
                                                    str(i[0]), str(i[1]), str(i[2]), str(i[3]),
                                                    str(i[4]).replace('.0000', ''), str(i[5]).replace('.0000', '')))
                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    for i in BLLdsCT_PXH.GetDSCT_PXH_Key(Key):
                        Detail_Note_Treeview.insert('', 'end', iid=i[0],
                                                    values=(
                                                    str(i[0]), str(i[1]), str(i[2]), str(i[3]),
                                                    str(i[4]).replace('.0000', ''), str(i[5]).replace('.0000', '')))

            def Detail_Note_on_single_click(event):
                single_region = Detail_Note_Treeview.identify_region(event.x, event.y)
                if single_region == 'cell':
                    Detail_Note_Btn1.config(state=tk.DISABLED)
                    Detail_Note_Btn2.config(state=tk.ACTIVE)
                    Detail_Note_Btn3.config(state=tk.ACTIVE)

                elif single_region == 'nothing':
                    for i in Detail_Note_Treeview.selection():
                        Detail_Note_Treeview.selection_remove(i)
                    Detail_Note_Btn1.config(state=tk.ACTIVE)
                    Detail_Note_Btn2.config(state=tk.DISABLED)
                    Detail_Note_Btn3.config(state=tk.DISABLED)

                else:
                    return

            def Add_Detail_Note():
                if category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    AddCT_PNH_Add_Win = tk.Toplevel(Detail_Note_Win)
                    AddCT_PNH_Add_Win.title(u'Thêm chi tiết phiếu nhập hàng.')
                    w = (AddCT_PNH_Add_Win.winfo_screenwidth() / 2) - 400
                    h = (AddCT_PNH_Add_Win.winfo_screenheight() / 2) - 200
                    AddCT_PNH_Add_Win.geometry('500x260+%d+%d' % (w, h))

                    def Addnewct_pnh():
                        MaPhieuNhap = treeview.selection()[0].replace(' ', '')
                        SoLuongNhap = str(AddFrm2entry4.get())
                        DonGiaNhap = str(AddFrm2entry5.get())

                        GUIflag = BLLdsCT_PNH.AddDSCT_PNH(MaPhieuNhap, AddFrm2entry3.get(), SoLuongNhap, DonGiaNhap)
                        if GUIflag == 'SLN rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Số lượng nhập không được để trống.')
                        elif GUIflag == 'DGN rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Đơn giá nhập không được để trống.')
                        elif GUIflag == 'SLN am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Số lượng nhập phải > 0.')
                        elif GUIflag == 'DGN am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Đơn giá nhập phải > 0.')
                        else:
                            messagebox.showinfo(u'Thông báo', u'Đã thêm thành công chi tiết phiếu nhập hàng mới.')
                            Upt_Detail_Note_Treeview()
                            AddCT_PNH_Add_Win.destroy()

                    AddFrm1 = tk.Frame(AddCT_PNH_Add_Win, width=500, height=50, bg="#3c8bec")
                    AddFrm1.grid(row=0, column=0)

                    AddFrm2 = tk.Frame(AddCT_PNH_Add_Win, width=500, height=450, bg="white")
                    AddFrm2.grid(row=1, column=0)

                    AddFrm1lb = tk.Label(AddFrm1,
                                         width=35,
                                         text=u"THÊM CHI TIẾT PHIẾU NHẬP HÀNG MỚI",
                                         fg="white",
                                         bg="#3c8bec",
                                         font=("Consolas", 15),
                                         anchor='w')
                    AddFrm1lb.place(x=80, y=10)

                    AddFrm2lb3 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Mã mặt hàng   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb3.place(x=0, y=0)

                    AddFrm2lb4 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Số lượng nhập   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb4.place(x=0, y=60)

                    AddFrm2lb5 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Đơn giá nhập   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb5.place(x=0, y=110)

                    MaMatHang = StringVar()
                    Lst1 = list()
                    for i in BLLdsCT_PNH.GetMaMatHang():
                        Lst1.append(i)

                    AddFrm2entry3 = ttk.Combobox(AddFrm2,
                                                 font=("Consolas", 15),
                                                 state='readonly',
                                                 textvariable=MaMatHang,
                                                 values=Lst1,
                                                 width=21)
                    
                    AddFrm2entry3.current(0)
                    AddFrm2entry3.place(x=200, y=2)

                    AddFrm2entry4 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry4.place(x=200, y=60)

                    AddFrm2entry5 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry5.place(x=200, y=110)

                    AddFrm2Btn1 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thêm",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=Addnewct_pnh)
                    AddFrm2Btn1.place(x=10, y=160)

                    AddFrm2Btn2 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thoát",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=AddCT_PNH_Add_Win.destroy)
                    AddFrm2Btn2.place(x=260, y=160)

                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    AddCT_PXH_Add_Win = tk.Toplevel(Detail_Note_Win)
                    AddCT_PXH_Add_Win.title(u"Thêm chi tiết phiếu xuất hàng")
                    w, h = AddCT_PXH_Add_Win.winfo_screenwidth(), AddCT_PXH_Add_Win.winfo_screenheight()
                    sw, sh = (w / 2) - 400, (h / 2) - 200
                    AddCT_PXH_Add_Win.geometry('500x210+%d+%d' % (sw, sh))

                    def Addnewct_pxh():
                        MaPhieuXuat = treeview.selection()[0].replace(' ', '')
                        SoLuongXuat = str(AddFrm2entry4.get())

                        GUIflag = BLLdsCT_PXH.AddDSCT_PXH(MaPhieuXuat, AddFrm2entry3.get(), SoLuongXuat)
                        if GUIflag == 'SLX rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Số lượng xuất không được để trống.')
                        elif GUIflag == 'SLX am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Số lượng xuất phải > 0.')
                        elif GUIflag == 'SLX <= SLT':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Số lượng xuất phải <= Số lượng tồn.')
                        else:
                            messagebox.showinfo(u'Thông báo', u'Đã thêm thành công chi tiết phiếu xuất hàng mới.')
                            Upt_Detail_Note_Treeview()
                            AddCT_PXH_Add_Win.destroy()

                    AddFrm1 = tk.Frame(AddCT_PXH_Add_Win, width=500, height=50, bg="#3c8bec")
                    AddFrm1.grid(row=0, column=0)

                    AddFrm2 = tk.Frame(AddCT_PXH_Add_Win, width=500, height=450, bg="white")
                    AddFrm2.grid(row=1, column=0)

                    AddFrm1lb = tk.Label(AddFrm1,
                                         width=33,
                                         text=u"THÊM CHI TIẾT PHIẾU XUẤT HÀNG MỚI",
                                         fg="white",
                                         bg="#3c8bec",
                                         font=("Consolas", 15),
                                         anchor='w')
                    AddFrm1lb.place(x=80, y=10)

                    AddFrm2lb3 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Mã mặt hàng   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb3.place(x=0, y=0)

                    AddFrm2lb4 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Số lượng xuất   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb4.place(x=0, y=60)

                    MaMatHang = StringVar()
                    Lst1 = list()
                    for i in BLLdsMatHang.GetMaMatHang():
                        Lst1.append(i)

                    AddFrm2entry3 = ttk.Combobox(AddFrm2,
                                                 font=("Consolas", 15),
                                                 state='readonly',
                                                 textvariable=MaMatHang,
                                                 values=Lst1,
                                                 width=21)
                    AddFrm2entry3.current(0)
                    AddFrm2entry3.place(x=200, y=2)

                    AddFrm2entry4 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry4.place(x=200, y=60)

                    AddFrm2Btn1 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thêm",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=Addnewct_pxh)
                    AddFrm2Btn1.place(x=10, y=110)

                    AddFrm2Btn2 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thoát",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=AddCT_PXH_Add_Win.destroy)
                    AddFrm2Btn2.place(x=260, y=110)

            def Delete_Detail_Note():
                Select = Detail_Note_Treeview.selection()[0]
                if category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    BLLdsCT_PNH.RemoveDSCT_PNH(Select)
                    messagebox.showinfo(u'Thông báo!', u'Đã xoá thành công chi tiết phiếu nhập hàng.')
                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    BLLdsCT_PXH.RemoveDSCT_PXH(Select)
                    messagebox.showinfo(u'Thông báo!', u'Đã xoá thành công chi tiết phiếu xuất hàng.')
                Upt_Detail_Note_Treeview()

            def Update_Detail_Note():
                Select = Detail_Note_Treeview.selection()[0]
                if category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    CT_PNH_Update_Win = tk.Toplevel(Detail_Note_Win)
                    CT_PNH_Update_Win.title(u"Cập nhật chi tiết phiếu nhập hàng")
                    w, h = CT_PNH_Update_Win.winfo_screenwidth(), CT_PNH_Update_Win.winfo_screenheight()
                    sw, sh = (w / 2) - 400, (h / 2) - 200
                    CT_PNH_Update_Win.geometry('500x260+%d+%d' % (sw, sh))

                    MaMatHang_Old = Detail_Note_Treeview.item(Select)['values'][2].replace(' ', '')
                    SoLuongNhap_Old = Detail_Note_Treeview.item(Select)['values'][3]
                    DonGiaNhap_Old = Detail_Note_Treeview.item(Select)['values'][4]

                    def Updatect_pnh():
                        SoLuongNhap = str(AddFrm2entry3.get())
                        DonGiaNhap = str(AddFrm2entry4.get())

                        GUIflag = BLLdsCT_PNH.UpdateDSCT_PNH(Select, AddFrm2entry2.get(), SoLuongNhap, DonGiaNhap)
                        if GUIflag == 'SLN rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Số lượng nhập không được để trống.')
                        elif GUIflag == 'DGN rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Đơn giá nhập không được để trống.')
                        elif GUIflag == 'SLN am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Số lượng nhập phải > 0.')
                        elif GUIflag == 'DGN am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Đơn giá nhập phải > 0.')
                        else:
                            messagebox.showinfo(u'Thông báo', u'Đã cập nhật thành công chi tiết phiếu nhập hàng.')
                            Upt_Detail_Note_Treeview()
                            CT_PNH_Update_Win.destroy()

                    AddFrm1 = tk.Frame(CT_PNH_Update_Win, width=500, height=50, bg="#3c8bec")
                    AddFrm1.grid(row=0, column=0)

                    AddFrm2 = tk.Frame(CT_PNH_Update_Win, width=500, height=450, bg="white")
                    AddFrm2.grid(row=1, column=0)

                    AddFrm1lb = tk.Label(AddFrm1,
                                         width=33,
                                         text=u"CẬP NHẬT CHI TIẾT PHIẾU NHẬP HÀNG",
                                         fg="white",
                                         bg="#3c8bec",
                                         font=("Consolas", 15),
                                         anchor='w')
                    AddFrm1lb.place(x=75, y=10)

                    AddFrm2lb2 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Mã mặt hàng   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb2.place(x=0, y=0)

                    AddFrm2lb3 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Số lượng nhập   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb3.place(x=0, y=60)

                    AddFrm2lb4 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Đơn giá nhập   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb4.place(x=0, y=110)

                    MaMatHang = StringVar()
                    Lst = list()
                    for i in BLLdsMatHang.GetMaMatHang():
                        Lst.append(i)

                    AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                                 font=("Consolas", 15),
                                                 state='readonly',
                                                 textvariable=MaMatHang,
                                                 values=Lst,
                                                 width=23)
                    AddFrm2entry2.set(MaMatHang_Old)
                    AddFrm2entry2.place(x=200, y=2)

                    AddFrm2entry3 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry3.insert('end', SoLuongNhap_Old)
                    AddFrm2entry3.place(x=200, y=60)

                    AddFrm2entry4 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry4.insert('end', DonGiaNhap_Old)
                    AddFrm2entry4.place(x=200, y=110)

                    AddFrm2Btn1 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Cập nhật",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=Updatect_pnh)
                    AddFrm2Btn1.place(x=10, y=160)

                    AddFrm2Btn2 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thoát",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=CT_PNH_Update_Win.destroy)
                    AddFrm2Btn2.place(x=260, y=160)

                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    CT_PXH_Update_Win = tk.Toplevel(Detail_Note_Win)
                    CT_PXH_Update_Win.title(u"Cập nhật chi tiết phiếu xuất hàng")
                    w, h = CT_PXH_Update_Win.winfo_screenwidth(), CT_PXH_Update_Win.winfo_screenheight()
                    sw, sh = (w / 2) - 400, (h / 2) - 200
                    CT_PXH_Update_Win.geometry('500x210+%d+%d' % (sw, sh))

                    MaMatHang_Old = Detail_Note_Treeview.item(Select)['values'][2].replace(' ', '')
                    SoLuongXuat_Old = Detail_Note_Treeview.item(Select)['values'][3]

                    def Updatect_pxh():
                        SoLuongXuat = str(AddFrm2entry3.get())

                        GUIflag = BLLdsCT_PXH.UpdateDSCT_PXH(Select, AddFrm2entry2.get(), SoLuongXuat)

                        if GUIflag == 'SLX rong':
                            messagebox.showwarning(u'Cảnh báo !!!', 'Số lượng xuất không được để trống.')
                        elif GUIflag == 'SLX am':
                            messagebox.showwarning(u'Cảnh báo !!!', u'Số lượng xuất phải > 0.')
                        else:
                            messagebox.showinfo(u'Thông báo', u'Đã cập nhật thành công chi tiết phiếu xuất hàng.')
                            Upt_Detail_Note_Treeview()
                            CT_PXH_Update_Win.destroy()

                    AddFrm1 = tk.Frame(CT_PXH_Update_Win, width=500, height=50, bg="#3c8bec")
                    AddFrm1.grid(row=0, column=0)

                    AddFrm2 = tk.Frame(CT_PXH_Update_Win, width=500, height=450, bg="white")
                    AddFrm2.grid(row=1, column=0)

                    AddFrm1lb = tk.Label(AddFrm1,
                                         width=33,
                                         text=u"CẬP NHẬT CHI TIẾT PHIẾU XUẤT HÀNG",
                                         fg="white",
                                         bg="#3c8bec",
                                         font=("Consolas", 15),
                                         anchor='w')
                    AddFrm1lb.place(x=80, y=10)

                    AddFrm2lb2 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Mã mặt hàng   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb2.place(x=0, y=0)

                    AddFrm2lb3 = tk.Label(AddFrm2,
                                          width=22,
                                          text=u"Số lượng xuất   :",
                                          fg="black",
                                          bg="white",
                                          font=("Consolas", 15),
                                          anchor='w')
                    AddFrm2lb3.place(x=0, y=60)

                    MaMatHang = StringVar()
                    Lst = list()
                    for i in BLLdsMatHang.GetMaMatHang():
                        Lst.append(i)

                    AddFrm2entry2 = ttk.Combobox(AddFrm2,
                                                 font=("Consolas", 15),
                                                 state='readonly',
                                                 textvariable=MaMatHang,
                                                 values=Lst,
                                                 width=23)
                    AddFrm2entry2.set(MaMatHang_Old)
                    AddFrm2entry2.place(x=200, y=2)

                    AddFrm2entry3 = tk.Entry(AddFrm2,
                                             width=23,
                                             fg="black",
                                             bg="white",
                                             font=("Consolas", 15),
                                             bd=1)
                    AddFrm2entry3.insert('end', SoLuongXuat_Old)
                    AddFrm2entry3.place(x=200, y=60)

                    AddFrm2Btn1 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Cập nhật",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=Updatect_pxh)
                    AddFrm2Btn1.place(x=10, y=110)

                    AddFrm2Btn2 = tk.Button(AddFrm2,
                                            width=18,
                                            text=u"Thoát",
                                            font='Times 16',
                                            bg='#3c8bec',
                                            fg='White',
                                            command=CT_PXH_Update_Win.destroy)
                    AddFrm2Btn2.place(x=260, y=110)

            Detail_Note_Frm1 = tk.Frame(Detail_Note_Win,
                                        bg='#3c8bec',
                                        height=100)
            Detail_Note_Frm1.pack(fill='both', expand=1)

            Detail_Note_Lb = tk.Label(Detail_Note_Frm1,
                                      width=35,
                                      text=u'',
                                      fg='white',
                                      bg='#3c8bec',
                                      font=('bold', 20, 'italic'),
                                      anchor='w')
            Detail_Note_Lb.place(x=10, y=10)

            # Tìm mục
            def Prs_Finding_CacDS_Detail(e):
                Finding_Detail_Note()

            def EtrIn3(e):
                Detail_Note_Etr.delete(0, 'end')

            def EtrOut3(e):
                if Detail_Note_Etr.get() == '':
                    Detail_Note_Etr.insert(0, u'Tìm kiếm')

            def Update_Object_Founded_Detail_Treeview(args):
                if (args != []):
                    selections = []
                    for i in args:
                        for child in Detail_Note_Treeview.get_children():
                            if (i == str(Detail_Note_Treeview.item(child)["values"][0])):
                                selections.append(child)
                    for i in Detail_Note_Treeview.get_children():
                        if i not in selections:
                            Detail_Note_Treeview.delete(i)

            def Finding_Detail_Note():
                entered_detail_note = Detail_Note_Etr.get()
                if(category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG'):
                    GUIFlag = BLLdsCT_PNH.FindingDsCT_PNH(entered_detail_note)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy chi tiếp nhập cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy chi tiết nhập cần tìm!!!")
                        Update_Object_Founded_Detail_Treeview(GUIFlag)
                elif(category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG'):
                    GUIFlag = BLLdsCT_PXH.FindingDsCT_PXH(entered_detail_note)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy chi tiết xuất cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy chi tiết xuất cần tìm!!!")
                        Update_Object_Founded_Detail_Treeview(GUIFlag)

            # Tìm kiếm
            rel_path = "IMAGE\\"
            abs_file_path = os.path.join(script_dir, rel_path)
            current_file = "Search.png"
            file=abs_file_path+current_file
            find_photo = Image.open(file)
            find_image = find_photo.resize((30, 25), Image.LANCZOS)
            Detail_Note_Win.find_img = ImageTk.PhotoImage(find_image)

            Detail_Note_Btn = tk.Button(Detail_Note_Frm1,
                                        fg="white",
                                        bg="#e2e2e2",
                                        bd=0,
                                        image=Detail_Note_Win.find_img,
                                        highlightbackground="#e2e2e2",
                                        command=Finding_Detail_Note)
            Detail_Note_Btn.image = Detail_Note_Win.find_img
            Detail_Note_Btn.place(x=915, y=60)

            Detail_Note_Etr = tk.Entry(Detail_Note_Frm1,
                                       width=25,
                                       bg='white',
                                       fg='black',
                                       font=('bold', 16),
                                       textvariable=data_finding)
            Detail_Note_Etr.place(x=600, y=60)

            Detail_Note_Etr.insert(0, u'Tìm kiếm')
            Detail_Note_Etr.bind('<FocusIn>', EtrIn3)
            Detail_Note_Etr.bind('<FocusOut>', EtrOut3)
            Detail_Note_Etr.bind('<Return>', Prs_Finding_CacDS_Detail)
    
            Detail_Note_Frm2 = tk.Frame(Detail_Note_Win,
                                        bg='#e2e2e2',
                                        height=500)
            Detail_Note_Frm2.pack(fill='both', expand=1)

            # Thêm
            rel_path = "IMAGE\\"
            abs_file_path = os.path.join(script_dir, rel_path)
            current_file = "Add_button.png"
            file=abs_file_path+current_file
            add_button_photo = Image.open(file)
            add_button_image = add_button_photo.resize((200, 50), Image.LANCZOS)
            Detail_Note_Win.add_button_img = ImageTk.PhotoImage(add_button_image)
            Detail_Note_Btn1 = tk.Button(Detail_Note_Frm2,
                                        #  width=17,
                                        #  text=u'THÊM',
                                         fg='black',
                                         bg='#e2e2e2',
                                         bd=0,
                                         borderwidth=0,
                                        #  font=('bold', 16),
                                         state=tk.NORMAL,
                                         image=Detail_Note_Win.add_button_img,
                                         highlightbackground='white',
                                        #  anchor='center')
                                         command=Add_Detail_Note
                                        )
            Detail_Note_Btn1.image=Detail_Note_Win.add_button_img
            Detail_Note_Btn1.place(x=120, y=440)

            # Xóa
            rel_path = "IMAGE\\"
            abs_file_path = os.path.join(script_dir, rel_path)
            current_file = "Delete_button.png"
            file=abs_file_path+current_file
            delete_button_photo = Image.open(file)
            delete_button_image = delete_button_photo.resize((200, 50), Image.LANCZOS)
            Detail_Note_Win.delete_button_img = ImageTk.PhotoImage(delete_button_image)
            Detail_Note_Btn2 = tk.Button(Detail_Note_Frm2,
                                        #  width=17,
                                        #  text=u'XÓA',
                                         fg='black',
                                         bg='#e2e2e2',
                                         bd=0,
                                         borderwidth=0,
                                        #  font=('bold', 16),
                                         state=tk.DISABLED,
                                        #  anchor='center',
                                         image=Detail_Note_Win.delete_button_img,
                                         highlightbackground='white',
                                         command=Delete_Detail_Note)
            Detail_Note_Btn2.image=Detail_Note_Win.delete_button_img
            Detail_Note_Btn2.place(x=420, y=440)

            # Cập nhật
            rel_path = "IMAGE\\"
            abs_file_path = os.path.join(script_dir, rel_path)
            current_file = "Update_button.png"
            file=abs_file_path+current_file
            update_button_photo = Image.open(file)
            update_button_image = update_button_photo.resize((200, 50), Image.LANCZOS)
            Detail_Note_Win.update_button_img = ImageTk.PhotoImage(update_button_image)
            Detail_Note_Btn3 = tk.Button(Detail_Note_Frm2,
                                        #  width=17,
                                        #  text=u'CẬP NHẬT',
                                         fg='black',
                                         bg='#e2e2e2',
                                         bd=0,
                                         borderwidth=0,
                                        #  font=('bold', 16),
                                         state=tk.DISABLED,
                                        #  anchor='center',
                                         image=Detail_Note_Win.update_button_img,
                                         highlightbackground='white',
                                         command=Update_Detail_Note)
            Detail_Note_Btn3.image=Detail_Note_Win.update_button_img
            Detail_Note_Btn3.place(x=720, y=440)

            column_names = ("NULL1", "NULL2", "NULL3", "NULL4", "NULL5", "NULL6")
            Detail_Note_Treeview = edit_treeview(Detail_Note_Frm2,
                                                 columns=column_names,
                                                 height=10,
                                                 style="Custom.Treeview")

            y_scrollbar1 = Scrollbar(Detail_Note_Frm2,
                                    orient=VERTICAL,
                                    command=Detail_Note_Treeview.yview)
            y_scrollbar1.place(x=980, y=5, height=424)

            Detail_Note_Treeview.heading("NULL1", text="NULL")
            Detail_Note_Treeview.heading("NULL2", text="NULL")
            Detail_Note_Treeview.heading("NULL3", text="NULL")
            Detail_Note_Treeview.heading("NULL4", text="NULL")
            Detail_Note_Treeview.heading("NULL5", text="NULL")
            Detail_Note_Treeview.heading("NULL6", text="NULL")
            Detail_Note_Treeview['show'] = 'headings'

            note_treeview_size = int(163)
            Detail_Note_Treeview.column("NULL1", width=note_treeview_size)
            Detail_Note_Treeview.column("NULL2", width=note_treeview_size)
            Detail_Note_Treeview.column("NULL3", width=note_treeview_size)
            Detail_Note_Treeview.column("NULL4", width=note_treeview_size)
            Detail_Note_Treeview.column("NULL5", width=note_treeview_size)
            Detail_Note_Treeview.column("NULL6", width=note_treeview_size)

            Key = treeview.selection()[0].replace(' ', '')

            if category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                Detail_Note_Lb.config(text=u'DANH SÁCH CHI TIẾT PHIẾU NHẬP HÀNG')

                Detail_Note_Treeview.heading("#1", text=u"Mã chi tiết phiếu nhập hàng")
                Detail_Note_Treeview.heading("#2", text=u"Mã phiếu nhập")
                Detail_Note_Treeview.heading("#3", text=u"Mã mặt hàng")
                Detail_Note_Treeview.heading("#4", text=u"Số lượng nhập")
                Detail_Note_Treeview.heading("#5", text=u"Đơn giá nhập")
                Detail_Note_Treeview.heading("#6", text=u"Thành tiền")

                treeview_column_width = int(163)

                Detail_Note_Treeview.column("NULL1", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL2", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL3", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL4", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL5", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL6", width=treeview_column_width)

                for i in BLLdsCT_PNH.GetDSCT_PNH_Key(Key):
                    Detail_Note_Treeview.insert('', 'end', iid=i[0],
                                                values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]),
                                                        str(i[4]).replace('.0000', ''), str(i[5]).replace('.0000', '')))

            elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                Detail_Note_Lb.config(text=u'DANH SÁCH CHI TIẾT PHIẾU XUẤT HÀNG')

                Detail_Note_Treeview.heading("#1", text=u"Mã chi tiết phiếu xuất hàng")
                Detail_Note_Treeview.heading("#2", text=u"Mã phiếu xuất")
                Detail_Note_Treeview.heading("#3", text=u"Mã mặt hàng")
                Detail_Note_Treeview.heading("#4", text=u"Số lượng xuất")
                Detail_Note_Treeview.heading("#5", text=u"Đơn giá xuất")
                Detail_Note_Treeview.heading("#6", text=u"Thành tiền")

                treeview_column_width = int(163)

                Detail_Note_Treeview.column("NULL1", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL2", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL3", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL4", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL5", width=treeview_column_width)
                Detail_Note_Treeview.column("NULL6", width=treeview_column_width)

                for i in BLLdsCT_PXH.GetDSCT_PXH_Key(Key):
                    Detail_Note_Treeview.insert('', 'end', iid=i[0],
                                                values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]),
                                                        str(i[4]).replace('.0000', ''), str(i[5]).replace('.0000', '')))

            Detail_Note_Treeview.config(yscrollcommand=y_scrollbar1.set)
            Detail_Note_Treeview.place(x=5, y=5)
            Detail_Note_Win.bind("<ButtonRelease-1>", Detail_Note_on_single_click)

        # Load Treeview With Default Values
        def Default_Treeview(key):
            for i in treeview.get_children():
                treeview.delete(i)

            if key == u'DANH SÁCH ĐẠI LÝ':
                Main_Window_Label.config(text=u'DANH SÁCH ĐẠI LÝ')
                treeview.heading("#1", text=u"Mã đại lý")
                treeview.heading("#2", text=u"Tên đại lý")
                treeview.heading("#3", text=u"Mã loại đại lý")
                treeview.heading("#4", text=u"Điện thoại")
                treeview.heading("#5", text=u"Địa chỉ")
                treeview.heading("#6", text=u"Mã quận")
                treeview.heading("#7", text=u"Ngày tiếp nhận")
                treeview.heading("#8", text=u"Số tiền nợ")

                treeview.column("NULL1", width=90, minwidth=80)
                treeview.column("NULL2", width=100, minwidth=90)
                treeview.column("NULL3", width=123, minwidth=100)
                treeview.column("NULL4", width=100, minwidth=90)
                treeview.column("NULL5", width=200, minwidth=180)
                treeview.column("NULL6", width=90, minwidth=80)
                treeview.column("NULL7", width=123, minwidth=100)
                treeview.column("NULL8", width=100, minwidth=90)
                for i in BLLdsDaiLy.GetDSDaiLy():
                    treeview.insert('', 'end', iid=i[0], values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]),
                                                                 str(i[4]), str(i[5]), str(i[6]), i[7]))

            elif key == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                Main_Window_Label.config(text=u'DANH SÁCH PHIẾU NHẬP HÀNG')
                treeview.heading("#1", text=u"Mã phiếu nhập")
                treeview.heading("#2", text=u"Ngày lập phiếu")
                treeview.heading("#3", text=u"Tổng tiền")

                treeview.column("NULL1", width=330)
                treeview.column("NULL2", width=330)
                treeview.column("NULL3", width=330)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsPhieuNH.GetDSPhieuNH():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2])))

            elif key == U'DANH SÁCH BÁO CÁO DOANH SỐ':
                Main_Window_Label.config(text=u'DANH SÁCH BÁO CÁO DOANH SỐ')
                treeview.heading("#1", text=u"Mã báo cáo doanh số")
                treeview.heading("#2", text=u"Tháng")
                treeview.heading("#3", text=u"Mã đại lý")
                treeview.heading("#4", text=u"Số phiếu xuất")
                treeview.heading("#5", text=u"Tổng trị giá")
                treeview.heading("#6", text=u"Tỷ lệ")

                treeview.column("NULL1", width=180)
                treeview.column("NULL2", width=165)
                treeview.column("NULL3", width=165)
                treeview.column("NULL4", width=165)
                treeview.column("NULL5", width=165)
                treeview.column("NULL6", width=165)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsBCDS.GetDSBCDS():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5])))

        # Update The Treeview Data (Rows)
        def Prs_Etr(e):
            key = category.get()
            for i in treeview.get_children():
                treeview.delete(i)

            if key == u'DANH SÁCH ĐẠI LÝ':
                Default_Treeview(key)

            elif key == u'DANH SÁCH LOẠI ĐẠI LÝ':
                Main_Window_Label.config(text=u'DANH SÁCH LOẠI ĐẠI LÝ')
                treeview.heading("#1", text=u"Mã loại đại lý")
                treeview.heading("#2", text=u"Tên loại đại lý")
                treeview.heading("#3", text=u"Số nợ tối đa")
                
                treeview.column("NULL1", width=330)
                treeview.column("NULL2", width=330)
                treeview.column("NULL3", width=330)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsLoaiDaiLy.GetDSLoaiDL():
                    treeview.insert("", 'end', iid=i[0], values=(str(i[0]), str(i[1]), int(i[2])))

            elif key == u'DANH SÁCH QUẬN':
                Main_Window_Label.config(text=u'DANH SÁCH QUẬN')
                treeview.heading("#1", text=u"Mã quận")
                treeview.heading("#2", text=u"Tên quận")

                treeview.column("NULL1", width=495)
                treeview.column("NULL2", width=495)
                treeview.column("NULL3", width=0, minwidth=0)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsQuan.GetDSQuan():
                    treeview.insert("", 'end', iid=i[0], values=(str(i[0]), str(i[1])))

            elif key == u'DANH SÁCH MẶT HÀNG':
                Main_Window_Label.config(text=u'DANH SÁCH MẶT HÀNG')
                treeview.heading("#1", text=u"Mã mặt hàng")
                treeview.heading("#2", text=u"Tên mặt hàng")
                treeview.heading("#3", text=u"Mã đơn vị tính")
                treeview.heading("#4", text=u"Số hàng tồn")

                treeview.column("NULL1", width=247)
                treeview.column("NULL2", width=247)
                treeview.column("NULL3", width=247)
                treeview.column("NULL4", width=247)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsMatHang.GetDSMatHang():
                    treeview.insert('', 'end', iid=i[0], values=(str(i[0]), str(i[1]), str(i[2]), str(i[3])))

            elif key == u'DANH SÁCH ĐƠN VỊ TÍNH':
                Main_Window_Label.config(text=u'DANH SÁCH ĐƠN VỊ TÍNH')
                treeview.heading("#1", text=u"Mã đơn vị tính")
                treeview.heading("#2", text=u"Tên đơn vị tính")

                treeview.column("NULL1", width=495)
                treeview.column("NULL2", width=495)
                treeview.column("NULL3", width=0, minwidth=0)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsDVT.GetDSDVT():
                    treeview.insert("", 'end', iid=i[0], values=(str(i[0]), str(i[1])))

            elif key == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                Main_Window_Label.config(text=u'DANH SÁCH PHIẾU NHẬP HÀNG')
                treeview.heading("#1", text=u"Mã phiếu nhập")
                treeview.heading("#2", text=u"Ngày lập phiếu")
                treeview.heading("#3", text=u"Tổng tiền")

                treeview.column("NULL1", width=330)
                treeview.column("NULL2", width=330)
                treeview.column("NULL3", width=330)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsPhieuNH.GetDSPhieuNH():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2])))

            elif key == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                Main_Window_Label.config(text=u'DANH SÁCH PHIẾU XUẤT HÀNG')
                treeview.heading("#1", text=u"Mã phiếu xuất")
                treeview.heading("#2", text=u"Mã đại lý")
                treeview.heading("#3", text=u"Ngày lập phiếu")
                treeview.heading("#4", text=u"Tổng tiền")

                treeview.column("NULL1", width=330)
                treeview.column("NULL2", width=330)
                treeview.column("NULL3", width=330)
                treeview.column("NULL4", width=0, minwidth=0)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsPhieuXH.GetDSPhieuXH():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2]), str(i[3])))

            elif key == u'DANH SÁCH PHIẾU THU TIỀN':
                Main_Window_Label.config(text=u'DANH SÁCH PHIẾU THU TIỀN')
                treeview.heading("#1", text=u"Mã phiếu thu tiền")
                treeview.heading("#2", text=u"Mã đại lý")
                treeview.heading("#3", text=u"Ngày thu tiền")
                treeview.heading("#4", text=u"Số tiền thu")

                treeview.column("NULL1", width=248)
                treeview.column("NULL2", width=248)
                treeview.column("NULL3", width=248)
                treeview.column("NULL4", width=248)
                treeview.column("NULL5", width=0, minwidth=0)
                treeview.column("NULL6", width=0, minwidth=0)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsPTT.GetDSPTT():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2]), str(i[3])))

            elif key == u'DANH SÁCH BÁO CÁO DOANH SỐ':
                Main_Window_Label.config(text=u'DANH SÁCH BÁO CÁO DOANH SỐ')
                treeview.heading("#1", text=u"Mã báo cáo doanh số")
                treeview.heading("#2", text=u"Tháng")
                treeview.heading("#3", text=u"Mã đại lý")
                treeview.heading("#4", text=u"Số phiếu xuất")
                treeview.heading("#5", text=u"Tổng trị giá")
                treeview.heading("#6", text=u"Tỷ lệ")
        
                treeview.column("NULL1", width=180)
                treeview.column("NULL2", width=163)
                treeview.column("NULL3", width=163)
                treeview.column("NULL4", width=163)
                treeview.column("NULL5", width=163)
                treeview.column("NULL6", width=163)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsBCDS.GetDSBCDS():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5])))

            elif key == u'DANH SÁCH BÁO CÁO CÔNG NỢ':
                Main_Window_Label.config(text=u'DANH SÁCH BÁO CÁO CÔNG NỢ')
                treeview.heading("#1", text=u"Mã báo cáo công nợ")
                treeview.heading("#2", text=u"Tháng")
                treeview.heading("#3", text=u"Mã đại lý")
                treeview.heading("#4", text=u"Nợ đầu")
                treeview.heading("#5", text=u"Phát sinh")
                treeview.heading("#6", text=u"Nợ cuối")
                
                treeview.column("NULL1", width=180)
                treeview.column("NULL2", width=163)
                treeview.column("NULL3", width=163)
                treeview.column("NULL4", width=163)
                treeview.column("NULL5", width=163)
                treeview.column("NULL6", width=163)
                treeview.column("NULL7", width=0, minwidth=0)
                treeview.column("NULL8", width=0, minwidth=0)
                for i in BLLdsBCCN.GetDSBCCN():
                    treeview.insert("", 'end', iid=i[0],
                                    values=(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5])))

        # Nút Xem Quy Định
        def show_regular():
            Main_Window_Button4.config(fg='black', bg='white')
            Regular_Win = Toplevel()
            Regular_Win.title('CÁC QUY ĐỊNH')
            sw, sh = (w / 2) - 400, (h / 2) - 200
            Regular_Win.geometry('500x250+%d+%d' % (sw, sh))

            def Change():
                Regular_Win_entry1.config(state=tk.NORMAL)
                Regular_Win_entry2.config(state=tk.NORMAL)


            def Save():
                BLLThamSo.UpdateSDLTDMQ(float(Regular_Win_entry1.get()))
                BLLThamSo.UpdateTLDG(float(Regular_Win_entry2.get()))

                Regular_Win_entry1.config(state=tk.DISABLED)
                Regular_Win_entry2.config(state=tk.DISABLED)

            def Exit():
                Main_Window_Button4.config(fg='white', bg='#3c8bec')
                Regular_Win.destroy()
            Regular_Win_Frm0=tk.Frame(Regular_Win,
                                    width=500,
                                    height=70,
                                    bg='#3c8bec')
            Regular_Win_Frm0.place(x=0, y=0)
            Regular_Win_label=tk.Label(Regular_Win_Frm0,width=25, text=u'CÁC QUY ĐỊNH', fg='white', bg='#3c8bec', font=('bold', 20), anchor='center')
            Regular_Win_label.place(x=40, y=10)
            Regular_Win_Frm1=tk.LabelFrame(Regular_Win,
                                            text=u'CÁC QUY ĐỊNH',
                                            width=500,
                                            height=180,
                                            bg='white')
            Regular_Win_Frm1.place(x=0, y=70)
            Regular_Win_label1=tk.Label(Regular_Win_Frm1,width=25, text=u'Số đại lý tối đa mỗi quận: ', fg='black', bg='white', font=('bold', 15), anchor='w')
            Regular_Win_label2=tk.Label(Regular_Win_Frm1,width=25, text=u'Tỷ lệ đơn giá nhập/ xuất: ', fg='black', bg='white', font=('bold', 15), anchor='w')
            Regular_Win_label1.place(x=0,y=0)
            Regular_Win_label2.place(x=0, y=50)

            Regular_Win_entry1=tk.Entry(Regular_Win_Frm1,width=10, fg='black', bg='white', font=('bold', 15), state=tk.NORMAL)
            Regular_Win_entry2=tk.Entry(Regular_Win_Frm1,width=10, fg='black', bg='white', font=('bold', 15), state=tk.NORMAL)
            Regular_Win_entry1.place(x=330, y=0)
            Regular_Win_entry2.place(x=330, y=50)       

            Regular_Win_entry1.delete(0, 'end')
            Regular_Win_entry2.delete(0, 'end')


            # Hiện số lượng đại lý tối đa trong quận
            Val1 = BLLThamSo.GetSDLTDMQ()
            Regular_Win_entry1.config(state=tk.NORMAL)
            Regular_Win_entry1.delete(0, 'end')
            Regular_Win_entry1.insert(0, Val1)
            Regular_Win_entry1.config(state=tk.DISABLED)

            # Hiện tỷ suất nhập xuất
            Val2 = BLLThamSo.GetTLDG()
            Regular_Win_entry2.config(state=tk.NORMAL)
            Regular_Win_entry2.delete(0, 'end')
            Regular_Win_entry2.insert(0, Val2)
            Regular_Win_entry2.config(state=tk.DISABLED)

            Regular_Win_button1=tk.Button(Regular_Win_Frm1,width=10, text=u'THAY ĐỔI', font='Times 16', bg='#3c8bec', fg='White', command=Change)
            Regular_Win_button2=tk.Button(Regular_Win_Frm1,width=10, text=u'LƯU', font='Times 16', bg='#3c8bec', fg='White', command=Save)
            Regular_Win_button3=tk.Button(Regular_Win_Frm1,width=10, text=u'QUAY VỀ', font='Times 16', bg='#3c8bec', fg='White', command=Exit)
            Regular_Win_button1.place(x=30, y=100)
            Regular_Win_button2.place(x=180, y=100)
            Regular_Win_button3.place(x=330, y=100)

        # Bind The 'Search' Entry Widget
        def EtrIn(e):
            Main_Window_Entry.delete(0, 'end')

        def EtrOut(e):
            if Main_Window_Entry.get() == '':
                Main_Window_Entry.insert(0, u'Tìm kiếm')

        def EtrIn1(e):
                Main_Window_Entry1.delete(0, 'end')

        def EtrOut1(e):
            if Main_Window_Entry1.get() == '':
                Main_Window_Entry1.insert(0, u'Tìm tháng: tháng + số')

        def EtrIn2(e):
                Main_Window_Entry2.delete(0, 'end')

        def EtrOut2(e):
            if Main_Window_Entry2.get() == '':
                Main_Window_Entry2.insert(0, u'Thời gian: tháng/ngày/năm + số')

        # Kích Hoạt Hoặc Vô Hiệu 3 Nút Thêm, Xoá, Cập Nhật
        def Default_Button():
            Main_Window_Button8['state'] = tk.DISABLED
            Main_Window_Button9['state'] = tk.DISABLED
            Main_Window_Button10['state'] = tk.DISABLED

        # Thêm Mục
        def Add():
            if(category.get() == ''):
                messagebox.showerror("Thông báo!!!", "Chưa chọn xem các danh sách!!!")
            else:
                if(str(category.get()) == u'DANH SÁCH ĐẠI LÝ'):
                    AddDaiLy()
                elif(str(category.get()) == u'DANH SÁCH LOẠI ĐẠI LÝ'):
                    AddLoaiDaiLy()
                elif(str(category.get()) == u'DANH SÁCH QUẬN'):
                    AddQuan()
                elif(str(category.get()) == u'DANH SÁCH MẶT HÀNG'):
                    AddMatHang()
                elif(str(category.get()) == u'DANH SÁCH ĐƠN VỊ TÍNH'):
                    AddDonviTinh()
                elif(str(category.get()) == u'DANH SÁCH BÁO CÁO DOANH SỐ'):
                    AddDsBCDS()
                elif(str(category.get()) == u'DANH SÁCH BÁO CÁO CÔNG NỢ'):
                    AddDsBCCN()
                elif category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    AddPhieuNhapHang()
                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    AddPhieuXuatHang()
                elif category.get() == u'DANH SÁCH PHIẾU THU TIỀN':
                    AddPhieuThuTien()

        # Xóa Mục
        def Delete():
            Choice = str(category.get())
            selected = treeview.selection()
            selected1 = list(selected)
        
            if(selected1 == []):
                messagebox.showerror('Thông báo!!!', 'Chưa chọn mục để xóa!!!')
            else:
                if (Choice == u'DANH SÁCH ĐẠI LÝ'):  # Xóa đại lý
                    GUIflag = BLLdsDaiLy.RemoveDSDaiLy(selected1[0])
                    if GUIflag == 'MDL in PTT':
                        messagebox.showerror(u'Lỗi !!!', u'Mã đại lý đang tồn tại trong phiếu thu tiền. Xoá thất bại.')
                    elif GUIflag == 'MDL in PXH':
                        messagebox.showerror(u'Lỗi !!!', u'Mã đại lý đang tồn tại trong phiếu xuất hàng. Xoá thất bại.')
                    elif GUIflag == 'MDL in BCDS':
                        messagebox.showerror(u'Lỗi !!!', u'Mã đại lý đang tồn tại trong báo cáo doanh số. Xoá thất bại.')
                    elif GUIflag == 'MDL in BCCN':
                        messagebox.showerror(u'Lỗi !!!', u'Mã đại lý đang tồn tại trong báo cáo công nợ. Xoá thất bại.')
                    else:
                        treeview.delete(selected1[0])
                        messagebox.showinfo(u"Thông báo!", u"Đã xóa đại lý thành công.")

                elif (Choice == u'DANH SÁCH LOẠI ĐẠI LÝ'):  # Xóa loại đại lý
                    GUIflag = BLLdsLoaiDaiLy.RemoveDSLoaiDL(selected1[0])
                    if GUIflag == 'MLDL in DAILY':
                        messagebox.showerror(u'Lỗi !!!', u'Mã loại đại lý đang tồn tại trong DANH SÁCH ĐẠI LÝ. Xoá thất bại.')
                    else:
                        treeview.delete(selected1[0])
                        messagebox.showinfo(u"Thông báo!", u"Đã xóa loại đại lý thành công.")

                elif (Choice == u'DANH SÁCH QUẬN'):  # Xóa quận
                    GUIflag = BLLdsQuan.RemoveDSQuan(selected1[0])
                    if GUIflag == 'MQ in DAILY':
                        messagebox.showerror(u'Lỗi !!!', u'Mã quận đang tồn tại trong DANH SÁCH ĐẠI LÝ. Xoá thất bại.')
                    else:
                        treeview.delete(selected1[0])
                        messagebox.showinfo(u"Thông báo!", u"Đã xóa quận thành công.")

                elif (Choice == u'DANH SÁCH MẶT HÀNG'):  # Xóa mặt hàng
                    GUIflag = BLLdsMatHang.RemoveDSMatHang(selected1[0])
                    if GUIflag == 'MMH in CT_PNH':
                        messagebox.showerror(u'Lỗi !!!', u'Mã mặt hàng đang tồn tại trong chi tiết phiếu nhập hàng. Xoá thất bại.')
                    elif GUIflag == 'MMH in CT_PXH':
                        messagebox.showerror(u'Lỗi !!!', u'Mã mặt hàng đang tồn tại trong chi tiết phiếu xuất hàng. Xoá thất bại.')
                    else:
                        treeview.delete(selected1[0])
                        messagebox.showinfo(u"Thông báo!", u"Đã xóa mặt hàng thành công.")

                elif (Choice == u'DANH SÁCH ĐƠN VỊ TÍNH'):  # Xóa đơn vị tính
                    GUIflag = BLLdsDVT.RemoveDSDVT(selected1[0])
                    if GUIflag == 'MDVT in MATHANG':
                        messagebox.showerror(u'Lỗi !!!', u'Mã đơn vị tính đang tồn tại trong DANH SÁCH MẶT HÀNG. Xoá thất bại.')
                    else:
                        treeview.delete(selected1[0])
                        messagebox.showinfo(u"Thông báo!", u"Đã xóa đơn vị tính thành công.")

                elif (Choice == u'DANH SÁCH BÁO CÁO DOANH SỐ'):
                    BLLdsBCDS.RemoveDSBCDS(selected1[0])
                    treeview.delete(selected1[0])
                    messagebox.showinfo(u'Thông báo!', u'Đã xoá báo cáo doanh số tháng thành công.')

                elif (Choice == u'DANH SÁCH BÁO CÁO CÔNG NỢ'):
                    BLLdsBCCN.RemoveDSBCDS(selected1[0])
                    treeview.delete(selected1[0])
                    messagebox.showinfo(u'Thông báo!', u'Đã xoá báo cáo công nợ tháng thành công.')

                elif Choice == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    GUIflag = BLLdsPhieuNH.RemoveDSPhieuNH(selected[0])
                    if GUIflag == 'MPN in CT_PNH':
                        messagebox.showerror(u'Lỗi !!!', u'Mã phiếu nhập đang tồn tại trong CHI TIẾT PHIẾU NHẬP HÀNG. '
                                                         u'Xoá thất bại.')
                    else:
                        treeview.delete(selected[0])
                        messagebox.showinfo(u'Thông báo!', u'Đã xoá phiếu nhập hàng thành công.')

                elif Choice == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    GUIflag = BLLdsPhieuXH.RemoveDSPhieuXH(selected[0])
                    if GUIflag == 'MPX in CT_PXH':
                        messagebox.showerror(u'Lỗi !!!', u'Mã phiếu xuất đang tồn tại trong CHI TIẾT PHIẾU XUẤT HÀNG. '
                                                         u'Xoá thất bại.')
                    else:
                        treeview.delete(selected[0])
                        messagebox.showinfo(u'Thông báo!', u'Đã xoá phiếu xuất hàng thành công.')

                elif Choice == u'DANH SÁCH PHIẾU THU TIỀN':
                    BLLdsPTT.RemoveDSPTT(selected[0])
                    treeview.delete(selected[0])
                    messagebox.showinfo(u'Thông báo!', u'Đã xoá phiếu thu tiền thành công.')

        # Sửa Mục
        def Update():
            chosen = treeview.selection()
            selected = list(chosen)
            if(selected == []):
                messagebox.showerror("Thông báo!!!", "Chưa chọn mục cần cập nhật!!!")
            else:
                if(str(category.get()) == u'DANH SÁCH ĐẠI LÝ'):
                    UpdateDaiLy(selected[0])
                elif(str(category.get()) == u'DANH SÁCH LOẠI ĐẠI LÝ'):
                    UpdateLoaiDaiLy(selected[0])
                elif(str(category.get()) == u'DANH SÁCH QUẬN'):
                    UpdateQuan(selected[0])
                elif(str(category.get()) == u'DANH SÁCH MẶT HÀNG'):
                    UpdateMatHang(selected[0])
                elif(str(category.get()) == u'DANH SÁCH ĐƠN VỊ TÍNH'):
                    UpdateDVT(selected[0])
                elif(str(category.get()) == u'DANH SÁCH BÁO CÁO DOANH SỐ'):
                    UpdateDsBCDS(selected[0])
                elif(str(category.get()) == u'DANH SÁCH BÁO CÁO CÔNG NỢ'):
                    UpdateDsBCCN(selected[0])
                elif category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG':
                    UpdatePhieuNhapHang(selected[0])
                elif category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG':
                    UpdatePhieuXuatHang(selected[0])
                elif category.get() == u'DANH SÁCH PHIẾU THU TIỀN':
                    UpdatePhieuThuTien(selected[0])

        # Tìm mục
        # Highlight Object
        def Prs_Finding_CacDS(e):
            Finding_CacDS()

        def Update_Object_Founded_Treeview(args):
            if (args != []):
                selections = []
                for i in args:
                    for child in treeview.get_children():
                        if (i == str(treeview.item(child)["values"][0])):
                            selections.append(child)
                for i in treeview.get_children():
                    if i not in selections:
                        treeview.delete(i)

        def Finding_CacDS():
            entered = Main_Window_Entry.get()
            entered_report = Main_Window_Entry1.get()
            entered_bill = Main_Window_Entry2.get()
            if(entered == ''):
                messagebox.showerror("Thông báo!!!", "Chưa nhập dữ liệu tìm kiếm!!!")
            else:
                if(category.get() == u'DANH SÁCH ĐẠI LÝ'):
                    GUIFlag = BLLdsDaiLy.FindingDsDaiLy(entered)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy đại lý cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy đại lý cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH LOẠI ĐẠI LÝ'):
                    GUIFlag = BLLdsLoaiDaiLy.FindingDsLoaiDaiLy(entered)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy loại đại lý cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy đại loại đại lý cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH MẶT HÀNG'):
                    GUIFlag = BLLdsMatHang.FindingDsMatHang(entered)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy mặt hàng cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy mặt hàng cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH QUẬN'):
                    GUIFlag = BLLdsQuan.FindingDsQuan(entered)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy quận cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy quận cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH ĐƠN VỊ TÍNH'):
                    GUIFlag = BLLdsDVT.FindingDsDVT(entered)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy đơn vị tính cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy đơn vị tính cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)
                
                elif(category.get() == u'DANH SÁCH BÁO CÁO DOANH SỐ'):
                    GUIFlag = BLLdsBCDS.FindingDsBCDS(entered_report)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy báo cáo cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy báo cáo cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH BÁO CÁO CÔNG NỢ'):
                    GUIFlag = BLLdsBCCN.FindingDsBCCN(entered_report)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy báo cáo cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy báo cáo cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH PHIẾU NHẬP HÀNG'):
                    GUIFlag = BLLdsPhieuNH.FindingDsPNH(entered_bill)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy phiếu nhập hàng cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy phiếu nhập hàng cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH PHIẾU XUẤT HÀNG'):
                    GUIFlag = BLLdsPhieuXH.FindingDsPXH(entered_bill)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy phiếu xuất cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy phiếu xuất cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

                elif(category.get() == u'DANH SÁCH PHIẾU THU TIỀN'):
                    GUIFlag = BLLdsPTT.FindingDsPTT(entered_bill)
                    if(GUIFlag == u'Khong tim thay'):
                        messagebox.showerror("Thông báo!!!", "Không tìm thấy phiếu thu tiền cần tìm!!!")
                    else:
                        messagebox.showinfo("Thông báo!!!", "Đã tìm thấy phiếu thu tiền cần tìm!!!")
                        Update_Object_Founded_Treeview(GUIFlag)

        data_finding = StringVar()
        data_finding1 = StringVar()
        data_finding2 = StringVar()
        category = StringVar()

        # Create Frames 
        MainWindow_Frm1 = tk.Frame(Main_Window,
                                   width=280,
                                   height=720,
                                   bg = '#3c8bec',
                                   borderwidth=3)
        MainWindow_Frm1.place(x=0, y=0)

        MainWindow_Frm2 = tk.Frame(Main_Window,
                                   width=1000,
                                   height=120,
                                   bg = '#e2e2e2',
                                   borderwidth=3)
        MainWindow_Frm2.place(x=281, y=0)
        
        MainWindow_Frm3 = tk.Frame(Main_Window,
                                   width=280,
                                   height=120,
                                   bg = 'white',
                                   highlightbackground='white',
                                   borderwidth=3)
        MainWindow_Frm3.place(x=0, y=0)

        # Create Label
        # Label hiện tên danh sách/ mục
        Main_Window_Label = tk.Label(Main_Window,
                                     width=30,
                                     text=u'QUẢN LÝ CÁC ĐẠI LÝ',
                                     fg='black',
                                     bg='#e2e2e2',
                                     font=('bold', 20, 'italic'),
                                     anchor='w')
        Main_Window_Label.place(x=294, y=7)

        # Create Button
        # Các danh sách
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "list_icon.png"
        file=abs_file_path+current_file
        list_photo = Image.open(file)
        list_image = list_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.list_img = ImageTk.PhotoImage(list_image)
  
        Main_Window_Button = tk.Button(Main_Window,
                                       width=275,
                                       text='  XEM DANH SÁCH',
                                       image=Main_Window.list_img,
                                       fg='white',
                                       bg='#3c8bec',
                                       font=('bold', 18),
                                       borderwidth=0, 
                                       compound='left',
                                       command=CasDs)
        Main_Window_Button.place(x=0, y=144)

        # Xem Phiếu
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "bill.png"
        file = abs_file_path + current_file
        bill_photo = Image.open(file)
        bill_image = bill_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.bill_img = ImageTk.PhotoImage(bill_image)

        Main_Window_Button2 = tk.Button(Main_Window,
                                        width=275,
                                        text='  XEM PHIẾU         ',
                                        image=Main_Window.bill_img,
                                        fg='white',
                                        bg='#3c8bec',
                                        font=('bold', 18),
                                        borderwidth=0,
                                        compound='left',
                                        command=Show_Note)
        Main_Window_Button2.place(x=0, y=216)

        # Báo cáo
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "business-report.png"
        file=abs_file_path+current_file
        report_photo = Image.open(file)
        report_image = report_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.report_img = ImageTk.PhotoImage(report_image)
        Main_Window_Button3 = tk.Button(Main_Window,
                                        width=275,
                                        text='  BÁO CÁO            ',
                                        image=Main_Window.report_img,
                                        fg='white',
                                        bg='#3c8bec',
                                        font=('bold', 18),
                                        borderwidth=0,
                                        compound='left',
                                        command=Show_Report)
        Main_Window_Button3.place(x=0, y=288)

        # Qui định
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "regular.png"
        file=abs_file_path+current_file
        regular_photo = Image.open(file)
        regular_image = regular_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.regular_img = ImageTk.PhotoImage(regular_image)
        Main_Window_Button4 = tk.Button(Main_Window,
                                        width=275,
                                        text='  QUY ĐỊNH           ',
                                        image=Main_Window.regular_img,
                                        fg='white',
                                        bg='#3c8bec',
                                        font=('bold', 18),
                                        borderwidth=0,
                                        compound='left',
                                        command=show_regular)
        Main_Window_Button4.place(x=0, y=360)

        # Xem chi tiết phiếu
        Main_Window_Button5 = tk.Button(Main_Window,
                                        width=275,
                                        text=u'XEM CHI TIẾT PHIẾU',
                                        fg='white',
                                        bg='#3c8bec',
                                        font=('bold', 18),
                                        command=Show_Detail_Note)

        # Đăng xuất
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "logout.png"
        file = abs_file_path + current_file
        logout_photo = Image.open(file)
        logout_image = logout_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.logout_img = ImageTk.PhotoImage(logout_image)
        Main_Window_Button6 = tk.Button(Main_Window,
                                        width=275,
                                        text='  ĐĂNG XUẤT       ',
                                        image=Main_Window.logout_img,
                                        fg='white',
                                        bg='#3c8bec',
                                        font=('bold', 18),
                                        borderwidth=0,
                                        compound='left',
                                        command=Switch_to_LogInPage)
        Main_Window_Button6.place(x=0, y=648)

        # Tìm kiếm
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "Search.png"
        file=abs_file_path+current_file
        find_photo = Image.open(file)
        find_image = find_photo.resize((30, 30), Image.LANCZOS)
        Main_Window.find_img = ImageTk.PhotoImage(find_image)

        Main_Window_Button7 = tk.Button(Main_Window,
                                        fg="white",
                                        bg="#e2e2e2",
                                        bd=0,
                                        image=Main_Window.find_img,
                                        highlightbackground="#e2e2e2",
                                        command=Finding_CacDS)
        Main_Window_Button7.image = Main_Window.find_img

        # Thêm
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "Add_button.png"
        file=abs_file_path+current_file
        add_button_photo = Image.open(file)
        add_button_image = add_button_photo.resize((275, 50), Image.LANCZOS)
        Main_Window.add_button_img = ImageTk.PhotoImage(add_button_image)

        Main_Window_Button8 = tk.Button(Main_Window,
                                        fg='black',
                                        bg='#e2e2e2',
                                        bd=0,
                                        borderwidth=0,
                                        image=Main_Window.add_button_img,
                                        highlightbackground="white",
                                        command=Add)
        Main_Window_Button8.image = Main_Window.add_button_img

        # Xóa
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "Delete_button.png"
        file=abs_file_path+current_file
        delete_button_photo = Image.open(file)
        delete_button_image = delete_button_photo.resize((275, 50), Image.LANCZOS)
        Main_Window.delete_button_img = ImageTk.PhotoImage(delete_button_image)

        Main_Window_Button9 = tk.Button(Main_Window,
                                        fg='black',
                                        bg='#e2e2e2',
                                        bd=0,
                                        borderwidth=0,
                                        image=Main_Window.delete_button_img,
                                        highlightbackground="white",
                                        command=Delete)
        
        Main_Window_Button9.image = Main_Window.delete_button_img

        # Cập nhật
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "Update_button.png"
        file=abs_file_path+current_file
        update_button_photo = Image.open(file)
        update_button_image = update_button_photo.resize((275, 50), Image.LANCZOS)
        Main_Window.update_button_img = ImageTk.PhotoImage(update_button_image)

        Main_Window_Button10 = tk.Button(Main_Window,
                                         fg='black',
                                         bg='#e2e2e2',
                                         bd=0,
                                         borderwidth=0,
                                         image=Main_Window.update_button_img,
                                         highlightbackground="white",
                                         command=Update)

        Main_Window_Button10.image = Main_Window.update_button_img

        # Đổi mật khẩu
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "change_password.png"
        file=abs_file_path+current_file
        changepasss_button_photo = Image.open(file)
        uchangepass_button_image = changepasss_button_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.changepass_button_img = ImageTk.PhotoImage(uchangepass_button_image)
        Main_Window_Button11 = tk.Button(MainWindow_Frm3,
                                         text=u"  Đổi mật khẩu       ",
                                         width=265,
                                         fg="black",
                                         bg="white",
                                         font=("bold", 18),
                                         image=Main_Window.changepass_button_img,
                                         highlightbackground="white",
                                         bd=0,
                                         borderwidth=0,
                                         compound='left',
                                         command=ChangePassWord)
        Main_Window_Button11.place(x=0, y=60)

        # Create Entry
        Main_Window_Entry = tk.Entry(Main_Window,
                                     width=20,
                                     bg='white',
                                     fg='black',
                                     font=('bold',20),
                                     textvariable=data_finding)

        Main_Window_Entry.insert(0, u'Tìm kiếm')
        Main_Window_Entry.bind('<FocusIn>', EtrIn)
        Main_Window_Entry.bind('<FocusOut>', EtrOut)
        Main_Window_Entry.bind('<Return>', Prs_Finding_CacDS)

        # Entry for 'Báo cáo'
        Main_Window_Entry1 = tk.Entry(Main_Window,
                                      width=20,
                                      bg='white',
                                      fg='black',
                                      font=('bold',20),
                                      textvariable=data_finding1)

        Main_Window_Entry1.insert(0, u'Tìm tháng: tháng + số')
        Main_Window_Entry1.bind('<FocusIn>', EtrIn1)
        Main_Window_Entry1.bind('<FocusOut>', EtrOut1)
        Main_Window_Entry1.bind('<Return>', Prs_Finding_CacDS)

        # Entry for 'Phiếu'
        Main_Window_Entry2 = tk.Entry(Main_Window,
                                      width=20,
                                      bg='white',
                                      fg='black',
                                      font=('bold',20),
                                      textvariable=data_finding2)

        Main_Window_Entry2.insert(0, u'Thời gian: tháng/ngày/năm + số')
        Main_Window_Entry2.bind('<FocusIn>', EtrIn2)
        Main_Window_Entry2.bind('<FocusOut>', EtrOut2)
        Main_Window_Entry2.bind('<Return>', Prs_Finding_CacDS)

        # Treeview
        column_names = ("NULL1", "NULL2", "NULL3", "NULL4", "NULL5", "NULL6", "NULL7", "NULL8")
        treeview = edit_treeview(Main_Window, columns=column_names, height=12, style="Custom.Treeview")

        y_scrollbar = Scrollbar(Main_Window, orient=VERTICAL, command=treeview.yview)
        y_scrollbar.place(x=1260, y=122, height=505)

        treeview.heading("NULL1", text="NULL")
        treeview.heading("NULL2", text="NULL")
        treeview.heading("NULL3", text="NULL")
        treeview.heading("NULL4", text="NULL")
        treeview.heading("NULL5", text="NULL")
        treeview.heading("NULL6", text="NULL")
        treeview.heading("NULL7", text="NULL")
        treeview.heading("NULL8", text="NULL")
        treeview['show'] = 'headings'

        treeview.column("NULL1", width=330)
        treeview.column("NULL2", width=330)
        treeview.column("NULL3", width=330)
        treeview.column("NULL4", width=0, minwidth=0)
        treeview.column("NULL5", width=0, minwidth=0)
        treeview.column("NULL6", width=0, minwidth=0)
        treeview.column("NULL7", width=0, minwidth=0)
        treeview.column("NULL8", width=0, minwidth=0)

        treeview.config(yscrollcommand=y_scrollbar.set)
        treeview.place(x=281, y=122)

        Main_Window_Combobox_Ds = ttk.Combobox(Main_Window,
                                               width=30,
                                               textvariable=category,
                                               font=("bold", 15),
                                               state='readonly')
        
        Main_Window_Combobox_Ds['values'] = ('DANH SÁCH ĐẠI LÝ',
                                             'DANH SÁCH LOẠI ĐẠI LÝ',
                                             'DANH SÁCH QUẬN',
                                             'DANH SÁCH MẶT HÀNG',
                                             'DANH SÁCH ĐƠN VỊ TÍNH')

        Main_Window_Combobox_Ds.current(0)
        Main_Window_Combobox_Ds.bind('<<ComboboxSelected>>', Prs_Etr)
        Default_Button()
        Main_Window.bind("<ButtonRelease-1>", on_single_click)
        
        # Show User
        rel_path = "IMAGE\\"
        abs_file_path = os.path.join(script_dir, rel_path)
        current_file = "account.png"
        file=abs_file_path+current_file
        user_photo = Image.open(file)
        user_image = user_photo.resize((35, 35), Image.LANCZOS)
        Main_Window.user_img = ImageTk.PhotoImage(user_image)

        user_name = '  ' + str(Account.KTTK[0][0][0]) + '        '
        Main_Window_Label2 = tk.Label(MainWindow_Frm3,
                                      width=265,
                                      text=user_name,
                                      image=Main_Window.user_img,
                                      fg='black',
                                      bg='white',
                                      font=('bold', 18, 'italic'),
                                      compound='left')
        Main_Window_Label2.place(x=0, y=0)

        Main_Window.mainloop()
        
    LogInPage()
    
if __name__ == "__main__":
    install('pyodbc')
    install('pandas')
    install('tkcalendar')
    install('xlsxwriter')
    install('pillow')

    import tkcalendar
    from tkcalendar import DateEntry
    from PIL import Image, ImageTk 
    import pandas as pd
    import xlsxwriter
    from pandas import ExcelWriter

    GUI()