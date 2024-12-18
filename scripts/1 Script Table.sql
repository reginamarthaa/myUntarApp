CREATE TABLE AKUN (
	AKUN_ID BIGINT PRIMARY KEY IDENTITY(1,1),
	EMAIL VARCHAR(50) NOT NULL UNIQUE,
	NAMA VARCHAR(50) NOT NULL,
	PASSWORD VARCHAR(200) NOT NULL
);

CREATE TABLE PROGRAM_STUDI (
	PROGRAM_STUDI_ID VARCHAR(10) PRIMARY KEY NOT NULL,
	NAMA_FAKULTAS VARCHAR(50) NOT NULL,
	NAMA_PROGRAM_STUDI VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE MAHASISWA (
	NIM VARCHAR(10) PRIMARY KEY NOT NULL,
	NAMA VARCHAR(50) NOT NULL,
	EMAIL VARCHAR(50),
	PROGRAM_STUDI_ID VARCHAR(10) NOT NULL,
);

CREATE TABLE DATA_KUESIONER (
	NIM VARCHAR(10) PRIMARY KEY NOT NULL,
	PERTANYAAN_1 DECIMAL(3, 2) NOT NULL,
	PERTANYAAN_2 DECIMAL(3, 2) NOT NULL,
	PERTANYAAN_3 DECIMAL(3, 2) NOT NULL,
	PERTANYAAN_4 DECIMAL(3, 2) NOT NULL,
	PERTANYAAN_5 DECIMAL(3, 2) NOT NULL,
	HASIL INT
);

ALTER TABLE MAHASISWA
ADD CONSTRAINT fk_mahasiswa_prodi
FOREIGN KEY (PROGRAM_STUDI_ID) REFERENCES PROGRAM_STUDI(PROGRAM_STUDI_ID);

INSERT INTO PROGRAM_STUDI (PROGRAM_STUDI_ID, NAMA_FAKULTAS, NAMA_PROGRAM_STUDI)
VALUES ('FEB_MB', 'Fakultas Ekonomi dan Bisnis', 'Manajemen Bisnis'),
('FEB_AB', 'Fakultas Ekonomi dan Bisnis', 'Akuntansi Bisnis'),
('FH_H', 'Fakultas Hukum', 'Hukum'),
('FT_TM', 'Fakultas Teknik', 'Teknik Mesin'),
('FT_TE', 'Fakultas Teknik', 'Teknik Elektro'),
('FT_TI', 'Fakultas Teknik', 'Teknik Industri'),
('FT_A', 'Fakultas Teknik', 'Arsitektur'),
('FT_TS', 'Fakultas Teknik', 'Teknik Sipil'),
('FT_PWK', 'Fakultas Teknik', 'Perencanaan Wilayah dan Kota'),
('FK_K', 'Fakultas Kedokteran', 'Kedokteran'),
('FP_P', 'Fakultas Psikologi', 'Psikologi'),
('FTI_TI', 'Fakultas Teknologi Informasi', 'Teknik Informatika'),
('FTI_SI', 'Fakultas Teknologi Informasi', 'Sistem Informasi'),
('FSRD_DI', 'Fakultas Seni Rupa dan Desain', 'Desain Interior'),
('FSRD_DKV', 'Fakultas Seni Rupa dan Desain', 'Desain Komunikasi Visual'),
('FIK_IK', 'Fakultas Ilmu Komunikasi', 'Ilmu Komunikasi');