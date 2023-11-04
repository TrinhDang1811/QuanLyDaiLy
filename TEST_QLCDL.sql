CREATE DATABASE TEST_QLCDL
GO

USE TEST_QLCDL
GO

SET DATEFORMAT DMY 

-- CREATE TABLES
CREATE TABLE TAIKHOAN
(
	TenTaiKhoan VARCHAR(50) NOT NULL,
	MatKhau		VARCHAR(50) NOT NULL,
	MaQuyen		CHAR(5) NOT NULL
)

CREATE TABLE QUYEN
(
	MaQuyen		CHAR(5) NOT NULL,
	TenQuyen	VARCHAR(20) NOT NULL
)

CREATE TABLE DAILY 
( 
	MaDaiLy			CHAR(10) NOT NULL, 
	TenDaiLy		NVARCHAR(20) NOT NULL, 
	MaLoaiDaiLy		CHAR(10) NOT NULL, 
	DienThoai		VARCHAR(15) NOT NULL,
	DiaChi			NVARCHAR(50) NOT NULL, 
	MaQuan			CHAR(10) NOT NULL, 
	NgayTiepNhan	SMALLDATETIME NOT NULL, 
	SoTienNo		MONEY 
); 

CREATE TABLE LOAIDAILY 
( 
	MaLoaiDaiLy		CHAR(10) NOT NULL, 
	TenLoaiDaiLy	NVARCHAR(20) NOT NULL, 
	SoNoToiDa		MONEY
); 

CREATE TABLE QUAN 
( 
	MaQuan	CHAR(10) NOT NULL, 
	TenQuan NVARCHAR(20) NOT NULL 
); 

CREATE TABLE PHIEUNHAPHANG 
( 
	MaPhieuNhap		CHAR(10) NOT NULL, 
	NgayLapPhieu	SMALLDATETIME NOT NULL, 
	TongTien		MONEY 
); 

CREATE TABLE CT_PNH 
( 
	MaCT_PNH	CHAR(10) NOT NULL, 
	MaPhieuNhap CHAR(10) NOT NULL, 
	MaMatHang	CHAR(10) NOT NULL, 
	SoLuongNhap INT NOT NULL, 
	DonGiaNhap	MONEY NOT NULL, 
	ThanhTien	MONEY 
); 

CREATE TABLE MATHANG 
( 
	MaMatHang	CHAR(10) NOT NULL, 
	TenMatHang	VARCHAR(20) NOT NULL, 
	MaDVT		CHAR(10) NOT NULL, 
	SoLuongTon	INT
); 

CREATE TABLE DVT 
( 
	MaDVT	CHAR(10) NOT NULL, 
	TenDVT	VARCHAR(10) NOT NULL 
); 

CREATE TABLE PHIEUXUATHANG 
(
	MaPhieuXuat		CHAR(10) NOT NULL, 
	MaDaiLy			CHAR(10) NOT NULL, 
	NgayLapPhieu	SMALLDATETIME NOT NULL, 
	TongTien		MONEY 
); 

CREATE TABLE CT_PXH
( 
	MaCT_PXH	CHAR(10) NOT NULL, 
	MaPhieuXuat CHAR(10) NOT NULL, 
	MaMatHang	CHAR(10) NOT NULL, 
	SoLuongXuat INT NOT NULL, 
	DonGiaXuat	MONEY, 
	ThanhTien	MONEY
); 

CREATE TABLE PHIEUTHUTIEN 
(
	MaPhieuThuTien	CHAR(10) NOT NULL, 
	MaDaiLy			CHAR(10) NOT NULL, 
	NgayThuTien		SMALLDATETIME NOT NULL, 
	SoTienThu		MONEY NOT NULL 
); 

CREATE TABLE BAOCAODOANHSO 
( 
	MaBCDoanhSo		CHAR(10) NOT NULL, 
	Thang			TINYINT NOT NULL, 
	MaDaiLy			CHAR(10) NOT NULL, 
	SoPhieuXuat		INT, 
	TongTriGia		MONEY, 
	TyLe			FLOAT  
); 

CREATE TABLE BAOCAOCONGNO
( 
	MaBCCongNo	CHAR(10) NOT NULL, 
	Thang		TINYINT NOT NULL, 
	MaDaiLy		CHAR(10) NOT NULL, 
	NoDau		MONEY, 
	PhatSinh	MONEY, 
	NoCuoi		MONEY  
); 

CREATE TABLE THAMSO
(
	SoDaiLyToiDaMoiQuan INT NOT NULL, 
	TiLeDonGiaBan		FLOAT NOT NULL 
); 

-- TABLES CONSTRAINTS
--TAIKHOAN
ALTER TABLE TAIKHOAN ADD
	CONSTRAINT TK_TenTaiKhoan_PK PRIMARY KEY(TenTaiKhoan),
	CONSTRAINT TK_MaQuyen_FK FOREIGN KEY(MaQuyen) REFERENCES QUYEN(MaQuyen)

--QUYEN
ALTER TABLE QUYEN ADD
	CONSTRAINT Q_MaQuyen_PK PRIMARY KEY(MaQuyen)

--DAILY
ALTER TABLE DAILY ADD 
	CONSTRAINT DL_MaDaiLy_PK PRIMARY KEY(MaDaiLy), 
	CONSTRAINT DL_MaLoaiDaiLy_FK FOREIGN KEY(MaLoaiDaiLy) REFERENCES LOAIDAILY(MaLoaiDaiLy), 
	CONSTRAINT DL_MaQuan_FK FOREIGN KEY(MaQuan) REFERENCES QUAN(MaQuan) 
 
--LOAIDAILY
ALTER TABLE LOAIDAILY ADD 
	CONSTRAINT LDL_MaLoaiDaiLy_PK PRIMARY KEY(MaLoaiDaiLy) 

--QUAN  
ALTER TABLE QUAN ADD 
	CONSTRAINT Q_MaQuan_PK PRIMARY KEY(MaQuan) 

--PHIEUNHAPHANG  
ALTER TABLE PHIEUNHAPHANG ADD 
	CONSTRAINT PNH_MaPhieuNhap_PK PRIMARY KEY(MaPhieuNhap) 

--CT_PNH
ALTER TABLE CT_PNH ADD 
	CONSTRAINT CTPNH_MaCTPNH_PK PRIMARY KEY(MaCT_PNH), 
	CONSTRAINT CTPNH_MaPhieuNhap_FK FOREIGN KEY(MaPhieuNhap) REFERENCES PHIEUNHAPHANG(MaPhieuNhap), 
	CONSTRAINT CTPNH_MaMatHang_FK FOREIGN KEY(MaMatHang) REFERENCES MATHANG(MaMatHang) 

--MATHANG
ALTER TABLE MATHANG ADD 
	CONSTRAINT MH_MaMatHang_PK PRIMARY KEY(MaMatHang), 
	CONSTRAINT MH_MaDVT_FK FOREIGN KEY(MaDVT) REFERENCES DVT(MaDVT) 

--DVT  
ALTER TABLE DVT ADD 
	CONSTRAINT DVT_MaDVT_PK PRIMARY KEY(MaDVT) 

--PHIEUXUATHANG  
ALTER TABLE PHIEUXUATHANG ADD 
	CONSTRAINT PXH_MaPhieuXuat_PK PRIMARY KEY(MaPhieuXuat), 
	CONSTRAINT PXH_MaDaiLy_FK FOREIGN KEY(MaDaiLy) REFERENCES DAILY(MaDaiLy) 

--CT_PXH  
ALTER TABLE CT_PXH ADD 
	CONSTRAINT CTPXH_MaCTPXH_PK PRIMARY KEY(MaCT_PXH), 
	CONSTRAINT CTPXH_MaPhieuXuat_FK FOREIGN KEY(MaPhieuXuat) REFERENCES PHIEUXUATHANG(MaPhieuXuat), 
	CONSTRAINT CTPXH_MaMatHang_FK FOREIGN KEY(MaMatHang) REFERENCES MATHANG(MaMatHang) 

--PHIEUTHUTIEN  
ALTER TABLE PHIEUTHUTIEN ADD 
	CONSTRAINT PTT_MaPhieuThuTien_PK PRIMARY KEY(MaPhieuThuTien), 
	CONSTRAINT PTT_MaDaiLy_FK FOREIGN KEY(MaDaiLy) REFERENCES DAILY(MaDaiLy) 

--BAOCAODOANHSO  
ALTER TABLE BAOCAODOANHSO ADD 
	CONSTRAINT BCDS_MaBCDoanhSo_PK PRIMARY KEY(MaBCDoanhSo), 
	CONSTRAINT BCDS_MaDaiLy_FK FOREIGN KEY(MaDaiLy) REFERENCES DAILY(MaDaiLy) 

--BAOCAOCONGNO
ALTER TABLE BAOCAOCONGNO ADD 
	CONSTRAINT BCCN_MaBCCongNo_PK PRIMARY KEY(MaBCCongNo), 
	CONSTRAINT BCCN_MaDaiLy_FK FOREIGN KEY(MaDaiLy) REFERENCES DAILY(MaDaiLy) 

-- TABLES TRIGGERS, PROCEDURES
CREATE PROC Proc_DangNhap 
@TK varchar(50), 
@MK varchar(50) 
AS  
BEGIN 
	SELECT TenTaiKhoan, TenQuyen FROM TAIKHOAN TK, QUYEN Q  
	WHERE TenTaiKhoan = @TK AND MatKhau = @MK AND TK.MaQuyen = Q.MaQuyen 
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
CREATE TRIGGER CT_PNH_SoLuongTon_Insert
ON CT_PNH
FOR INSERT
AS
BEGIN
	DECLARE @soluongton int
	SELECT @soluongton = SUM(CN.SoLuongNhap) FROM CT_PNH CN, inserted I
	WHERE CN.MaMatHang = I.MaMatHang 
	UPDATE MATHANG SET SoLuongTon = @soluongton
	FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang
END
GO

CREATE TRIGGER CT_PNH_SoLuongTon_Update
ON CT_PNH
FOR UPDATE
AS
IF (UPDATE(SoLuongNhap))
BEGIN
	DECLARE @soluongnhap_moi int, @soluongnhap_cu int, @soluongton int
	SET @soluongnhap_moi = (SELECT SoLuongNhap FROM inserted)
	SET @soluongnhap_cu = (SELECT SoLuongNhap FROM deleted)
	SET @soluongton = (SELECT MH.SoLuongTon FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang)
	BEGIN
		UPDATE MATHANG SET SoLuongTon = @soluongton + (@soluongnhap_moi - @soluongnhap_cu)
		FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang
	END
END
GO

CREATE TRIGGER CT_PNH_SoLuongTon_Delete
ON CT_PNH
FOR DELETE
AS
BEGIN
	DECLARE @soluongnhap int
	SELECT @soluongnhap = D.SoLuongNhap FROM MATHANG MH, deleted D WHERE MH.MaMatHang = D.MaMatHang
	UPDATE MATHANG SET SoLuongTon = SoLuongTon - @soluongnhap
	FROM MATHANG MH, deleted D WHERE MH.MaMatHang = D.MaMatHang
END
GO

CREATE TRIGGER CT_PNH_ThTien_ToTien_Insert_Update
ON CT_PNH
FOR INSERT, UPDATE
AS
IF NOT EXISTS (SELECT * FROM deleted) OR (UPDATE(SoLuongNhap) OR UPDATE(DonGiaNhap))
BEGIN
	DECLARE @soluongnhap int, 
			@dongianhap money,
			@tongthanhtien money,
			@tongtien money,
			@mact_pnh char(10)
	SELECT @soluongnhap = I.SoLuongNhap, @dongianhap = I.DonGiaNhap, @mact_pnh = I.MaCT_PNH
	FROM CT_PNH CN, inserted I
	WHERE CN.MaCT_PNH = I.MaCT_PNH
	UPDATE CT_PNH SET ThanhTien = @dongianhap * @soluongnhap
	WHERE CT_PNH.MaCT_PNH = @mact_pnh

	SELECT @tongthanhtien = SUM(CN.ThanhTien) FROM CT_PNH CN, PHIEUNHAPHANG PNH, inserted I
	WHERE CN.MaPhieuNhap = PNH.MaPhieuNhap AND I.MaPhieuNhap = PNH.MaPhieuNhap
	UPDATE PHIEUNHAPHANG SET TongTien = @tongthanhtien
	FROM inserted I, PHIEUNHAPHANG PNH
	WHERE I.MaPhieuNhap = PNH.MaPhieuNhap
END
GO

CREATE TRIGGER CT_PNH_ThTien_ToTien_Delete
ON CT_PNH
FOR DELETE
AS
BEGIN
	DECLARE @maphieunhap char(10), @tongtien money
	SELECT @maphieunhap = MaPhieuNhap FROM deleted
	SELECT @tongtien = SUM(ThanhTien) FROM CT_PNH CN
	WHERE CN.MaPhieuNhap = @maphieunhap
	UPDATE PHIEUNHAPHANG SET TongTien = @tongtien
	WHERE PHIEUNHAPHANG.MaPhieuNhap = @maphieunhap
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
CREATE TRIGGER CT_PXH_SoLuongTon_Insert
ON CT_PXH
FOR INSERT
AS
BEGIN
	DECLARE @soluongton int, @soluongxuat int
	SET @soluongton = (SELECT MH.SoLuongTon FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang)
	SET @soluongxuat = (SELECT SoLuongXuat FROM inserted)
	IF (@soluongton < @soluongxuat)
	BEGIN
		ROLLBACK TRAN
	END
	ELSE
	BEGIN
		UPDATE MATHANG SET SoLuongTon = @soluongton - @soluongxuat
		FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang
	END
END
GO

CREATE TRIGGER CT_PXH_SoLuongTon_Update
ON CT_PXH
FOR UPDATE
AS
IF (UPDATE(SoLuongXuat))
BEGIN
	DECLARE @allslx int, @soluongton int
	SET @soluongton = (SELECT MH.SoLuongTon FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang)
	SELECT @allslx = SUM(CX.SoLuongXuat) FROM CT_PXH CX, inserted I
	WHERE CX.MaMatHang = I.MaMatHang
	IF (@soluongton < @allslx)
	BEGIN
		ROLLBACK TRAN
	END
	ELSE
	BEGIN
		UPDATE MATHANG SET SoLuongTon = @soluongton - @allslx
		FROM MATHANG MH, inserted I WHERE MH.MaMatHang = I.MaMatHang
	END
END
GO

CREATE TRIGGER CT_PXH_SoLuongTon_Delete
ON CT_PXH
FOR DELETE
AS
BEGIN
	DECLARE @soluongxuat int, @soluongton int
	SELECT @soluongxuat = D.SoLuongXuat, @soluongton = MH.SoLuongTon 
	FROM MATHANG MH, deleted D WHERE MH.MaMatHang = D.MaMatHang
	UPDATE MATHANG SET SoLuongTon = @soluongton + @soluongxuat
	FROM MATHANG MH, deleted D WHERE MH.MaMatHang = D.MaMatHang
END
GO

CREATE TRIGGER CT_PXH_DGX_ThTien_ToTien_Insert_Update
ON CT_PXH
FOR INSERT, UPDATE
AS
IF NOT EXISTS (SELECT * FROM deleted) OR UPDATE(SoLuongXuat)
BEGIN
	DECLARE @soluongxuat int,
			@dongianhap money, 
			@dongiaxuat money,
			@tongtien money,
			@tienno money,
			@tiennotoida money,
			@tyle float,
			@mapxh char(10)

	SELECT @tyle = TiLeDonGiaBan FROM THAMSO
	SELECT @soluongxuat = SoLuongXuat FROM CT_PXH
	SELECT @dongianhap = CN.DonGiaNhap, @mapxh = I.MaPhieuXuat 
	FROM inserted I, CT_PNH CN WHERE CN.MaMatHang = I.MaMatHang
	SET @dongiaxuat = @dongianhap * @tyle
	UPDATE CT_PXH SET CT_PXH.DonGiaXuat = @dongiaxuat, CT_PXH.ThanhTien = @dongiaxuat * @soluongxuat
	FROM inserted I, CT_PXH CX 
	WHERE I.MaMatHang = CX.MaMatHang
	
	SELECT @tongtien = SUM(CX.ThanhTien) FROM CT_PXH CX, inserted I
	WHERE I.MaPhieuXuat = CX.MaPhieuXuat
	UPDATE PHIEUXUATHANG SET TongTien = @tongtien
	FROM inserted I, PHIEUXUATHANG PXH
	WHERE I.MaPhieuXuat = PXH.MaPhieuXuat
END
GO

CREATE TRIGGER CT_PXH_DGX_ThTien_ToTien_Delete
ON CT_PXH
FOR DELETE
AS
BEGIN
	DECLARE @maphieuxuat char(10), @tongtien money
	SELECT @maphieuxuat = MaPhieuXuat FROM deleted
	SELECT @tongtien = SUM(ThanhTien) FROM CT_PXH CX
	WHERE CX.MaPhieuXuat = @maphieuxuat
	UPDATE PHIEUXUATHANG SET TongTien = @tongtien
	WHERE PHIEUXUATHANG.MaPhieuXuat = @maphieuxuat
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
CREATE TRIGGER PhieuXH_SoTienNo_Insert_Update
ON PHIEUXUATHANG
FOR INSERT, UPDATE
AS
IF NOT EXISTS (SELECT * FROM deleted) OR (UPDATE(TongTien))
BEGIN
	DECLARE @tongtienno money

	SELECT @tongtienno = SUM(PXH.TongTien) FROM PHIEUXUATHANG PXH, inserted I
	WHERE PXH.MaDaiLy = I.MaDaiLy
	
	UPDATE DAILY SET SoTienNo = @tongtienno
	FROM DAILY DL, inserted I
	WHERE DL.MaDaiLy = I.MaDaiLy
END
GO

CREATE TRIGGER PhieuXH_SoTienNo_Delete
ON PHIEUXUATHANG
FOR DELETE
AS
BEGIN
	DECLARE @madaily char(10), @tongtien money
	SELECT @tongtien = PXH.TongTien, @madaily = I.MaDaiLy FROM PHIEUXUATHANG PXH, inserted I
	WHERE PXH.MaPhieuXuat = I.MaPhieuXuat
	UPDATE DAILY SET SoTienNo = DAILY.SoTienNo - @tongtien
	WHERE DAILY.MaDaiLy = @madaily
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
CREATE TRIGGER PhieuThuTien_SoTienThu_Insert_Update
ON PHIEUTHUTIEN
FOR INSERT, UPDATE
AS 
IF NOT EXISTS (SELECT * FROM deleted) OR UPDATE(SoTienThu)
BEGIN
	DECLARE @sotienthu money, @sotienno money, @allsothienthu money
	SELECT @sotienthu = I.SoTienThu, @sotienno = DL.SoTienNo FROM inserted I, DAILY DL
	WHERE I.MaDaiLy = DL.MaDaiLy
	IF (@sotienthu > @sotienno)
	BEGIN
		ROLLBACK TRAN
	END
	ELSE
	BEGIN
		UPDATE DAILY SET SoTienNo = @sotienno - @sotienthu
		FROM DAILY DL, inserted I
		WHERE DL.MaDaiLy = I.MaDaiLy
	END
END
GO

CREATE TRIGGER PhieuThuTien_SoTienThu_Delete
ON PHIEUTHUTIEN
FOR DELETE
AS 
BEGIN
	DECLARE @sotienthu_del money, @madl char(10)
	SELECT @sotienthu_del = D.SoTienThu, @madl = D.MaDaiLy
	FROM deleted D, DAILY DL WHERE D.MaDaiLy = DL.MaDaiLy
	UPDATE DAILY SET SoTienNo = SoTienNo + @sotienthu_del
	WHERE DAILY.MaDaiLy = @madl
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
CREATE TRIGGER BCDoanhSo_SPX_TRT_TL
ON BAOCAODOANHSO
FOR INSERT, UPDATE
AS
BEGIN
	DECLARE @thang tinyint,
			@sophieuxuat int,
			@tongtrigia money,
			@all money,
			@tyle float,
			@madaily char(10)

	SELECT @thang = Thang, @madaily = MaDaiLy FROM inserted

	SELECT @sophieuxuat = COUNT(MaPhieuXuat), @tongtrigia = SUM(TongTien) 
	FROM PHIEUXUATHANG PXH
	WHERE PXH.MaDaiLy = @madaily AND MONTH(PXH.NgayLapPhieu) = @thang
	IF (@tongtrigia) IS NULL
	BEGIN
		SET @tongtrigia = 0
	END

	SELECT @all = SUM(TongTien) FROM PHIEUXUATHANG PXH 
	WHERE PXH.MaDaiLy  = @madaily
	IF (@all) IS NULL
	BEGIN
		SET @all = 0
		SET @tyle = 0
	END
	ELSE
	BEGIN
		SET @tyle = @tongtrigia / @all
	END
	UPDATE BAOCAODOANHSO 
	SET SoPhieuXuat = @sophieuxuat, TongTriGia = @tongtrigia, TyLe = (@tyle * 100.0)
	WHERE BAOCAODOANHSO.MaDaiLy = @madaily AND BAOCAODOANHSO.Thang = @thang
END
GO

CREATE TRIGGER BCCongNo_ND_PS_NC
ON BAOCAOCONGNO
FOR INSERT, UPDATE
AS
BEGIN
	DECLARE @nodau money, 
			@phatsinh money, 
			@sotienthu money,
			@madaily char(10),
			@thang tinyint
	SELECT @madaily = I.MaDaiLy, @thang = I.Thang FROM inserted I
	SELECT @nodau = BCCN.NoCuoi FROM BAOCAOCONGNO BCCN, inserted I
	WHERE (I.Thang - 1) = BCCN.Thang AND BCCN.MaDaiLy = I.MaDaiLy
	IF @nodau IS NULL OR NOT EXISTS (SELECT Thang FROM BAOCAOCONGNO WHERE Thang = @thang - 1)
	BEGIN
		SET @nodau = 0
	END
	SELECT @phatsinh = SUM(PXH.TongTien) FROM PHIEUXUATHANG PXH
	WHERE PXH.MaDaiLy = @madaily AND MONTH(PXH.NgayLapPhieu) = @thang
	IF @phatsinh IS NULL
	BEGIN
		SET @phatsinh = 0
	END
	SELECT @sotienthu = SUM(PTT.SoTienThu) FROM PHIEUTHUTIEN PTT
	WHERE PTT.MaDaiLy = @madaily AND MONTH(NgayThuTien) = @thang
	IF @sotienthu IS NULL
	BEGIN
		SET @sotienthu = 0
	END
	UPDATE BAOCAOCONGNO SET NoDau = @nodau, PhatSinh = @phatsinh, NoCuoi = (@nodau + @phatsinh) - @sotienthu
	WHERE BAOCAOCONGNO.MaDaiLy = @madaily AND BAOCAOCONGNO.Thang = @thang
END
GO
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------


INSERT INTO TAIKHOAN VALUES('quantrivien', '123', 1)
INSERT INTO TAIKHOAN VALUES('DaoNguyenNhatMinh', '123', 2)
INSERT INTO TAIKHOAN VALUES('NguyenAnhKiet', '123', 2)
INSERT INTO TAIKHOAN VALUES('NguyenXuandangTrinh', '123', 2)

INSERT INTO QUYEN VALUES(1, 'quantrivien')
INSERT INTO QUYEN VALUES(2, 'nguoidung')

-- TEST CT_PNH
INSERT INTO PHIEUNHAPHANG VALUES ('PNH1', '10/01/2023', NULL)
INSERT INTO PHIEUNHAPHANG VALUES ('PNH2', '07/01/2023', NULL)
INSERT INTO PHIEUNHAPHANG VALUES ('PNH3', '09/01/2023', NULL)
INSERT INTO PHIEUNHAPHANG VALUES ('PNH4', '04/01/2023', NULL)

INSERT INTO DVT VALUES ('DVT1', 'cai')
INSERT INTO DVT VALUES ('DVT2', 'hop')
INSERT INTO DVT VALUES ('DVT3', 'quyen')

INSERT INTO MATHANG VALUES ('MH1', 'Ly Tra', 'DVT1', NULL)
INSERT INTO MATHANG VALUES ('MH2', 'But Chi', 'DVT2', NULL)
INSERT INTO MATHANG VALUES ('MH3', 'Sach Giao Khoa', 'DVT3', NULL)
INSERT INTO MATHANG VALUES ('MH4', 'Sua Ong Tho', 'DVT2', NULL)

INSERT INTO CT_PNH VALUES ('CTPNH1', 'PNH1', 'MH1', 10, 5000, NULL)
INSERT INTO CT_PNH VALUES ('CTPNH2', 'PNH2', 'MH2', 30, 2000, NULL)
INSERT INTO CT_PNH VALUES ('CTPNH3', 'PNH3', 'MH3', 50, 10000, NULL)
INSERT INTO CT_PNH VALUES ('CTPNH4', 'PNH4', 'MH4', 33, 23500, NULL)
INSERT INTO CT_PNH VALUES ('CTPNH5', 'PNH1', 'MH1', 12, 5000, NULL)
INSERT INTO CT_PNH VALUES ('CTPNH6', 'PNH3', 'MH3', 8, 10000, NULL)

-- TEST CT_PXH
INSERT INTO QUAN VALUES('MQ1','Quan 1')
INSERT INTO QUAN VALUES('MQTD','TP. Thu Duc')

INSERT INTO LOAIDAILY VALUES('LDL1', 'Loai 1', 10000000)
INSERT INTO LOAIDAILY VALUES('LDL2', 'Loai 2', 5000000)

INSERT INTO DAILY VALUES('MDL1', 'Dai Ly 1', 'LDL1', '0911936302', 'Khu Pho 6, Ph.Linh Trung, TP.Thu Duc, TP.HCM', 'MQ1', '10/03/2023', NULL)
INSERT INTO DAILY VALUES('MDL3', 'Dai Ly 3', 'LDL1', '0983943362', 'Phu Long, Tan Phu Dong, TP.Sa Dec, Tinh Dong Thap', 'MQTD', '06/02/2023', NULL)
INSERT INTO DAILY VALUES('MDL6', 'Dai Ly 6', 'LDL2', '0919430933', 'Phu Long, Tan Phu Dong, TP.Sa Dec, Tinh Dong Thap', 'MQTD', '12/01/2023', NULL)

INSERT INTO PHIEUXUATHANG VALUES('PXH1', 'MDL1', '11/03/2023', NULL)
INSERT INTO PHIEUXUATHANG VALUES('PXH2', 'MDL3', '08/02/2023', NULL)
INSERT INTO PHIEUXUATHANG VALUES('PXH3', 'MDL6', '15/01/2023', NULL)
INSERT INTO PHIEUXUATHANG VALUES('PXH4', 'MDL1', '18/03/2023', NULL)
INSERT INTO PHIEUXUATHANG VALUES('PXH5', 'MDL1', '23/04/2023', NULL)
INSERT INTO PHIEUXUATHANG VALUES('PXH6', 'MDL3', '08/04/2023', NULL)

INSERT INTO CT_PXH VALUES('CTPXH1', 'PXH1', 'MH1', 7, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH2', 'PXH2', 'MH3', 15, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH3', 'PXH2', 'MH2', 25, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH4', 'PXH3', 'MH4', 11, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH5', 'PXH4', 'MH4', 2, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH6', 'PXH3', 'MH1', 3, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH7', 'PXH5', 'MH4', 7, NULL, NULL)
INSERT INTO CT_PXH VALUES('CTPXH8', 'PXH6', 'MH2', 3, NULL, NULL)

INSERT INTO PHIEUTHUTIEN VALUES('PTT1', 'MDL1', '25/04/2023', 1000)
INSERT INTO PHIEUTHUTIEN VALUES('PTT2', 'MDL3', '18/02/2023', 10000)
INSERT INTO PHIEUTHUTIEN VALUES('PTT3', 'MDL6', '27/01/2023', 12300)
INSERT INTO PHIEUTHUTIEN VALUES('PTT4', 'MDL1', '27/04/2023', 120000)
INSERT INTO PHIEUTHUTIEN VALUES('PTT5', 'MDL1', '28/04/2023', 50000)
INSERT INTO PHIEUTHUTIEN VALUES('PTT6', 'MDL3', '14/04/2023', 12300)

INSERT INTO BAOCAODOANHSO VALUES('BCDS1', 3, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS2', 3, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS3', 3, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS4', 5, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS5', 4, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS6', 5, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS7', 2, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS8', 6, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS9', 6, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS10', 4, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS11', 1, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS12', 6, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS13', 5, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS14', 2, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS15', 2, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAODOANHSO VALUES('BCDS16', 4, 'MDL6', NULL, NULL, NULL)


INSERT INTO BAOCAOCONGNO VALUES('BCCN1', 3, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN2', 4, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN3', 5, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN4', 6, 'MDL1', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN5', 3, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN6', 2, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN7', 4, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN8', 4, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN9', 5, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN10', 2, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN11', 3, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN12', 6, 'MDL6', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN13', 5, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN14', 6, 'MDL3', NULL, NULL, NULL)
INSERT INTO BAOCAOCONGNO VALUES('BCCN15', 1, 'MDL6', NULL, NULL, NULL)

INSERT INTO THAMSO VALUES(4, 1.02)

SELECT * FROM LOAIDAILY
SELECT * FROM PHIEUTHUTIEN
SELECT * FROM MATHANG
SELECT * FROM CT_PXH
SELECT * FROM PHIEUNHAPHANG
SELECT * FROM CT_PNH
SELECT * FROM BAOCAODOANHSO
SELECT * FROM DAILY
SELECT * FROM PHIEUXUATHANG
SELECT * FROM BAOCAOCONGNO
SELECT * FROM THAMSO

SELECT * FROM DAILY WHERE MaDaiLy = 'MDL1'
SELECT * FROM BAOCAOCONGNO WHERE MaDaiLy = 'MDL1'

DELETE FROM CT_PNH WHERE MaCT_PNH = 'CTPNH5'