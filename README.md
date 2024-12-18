# Set up Web

## Deskripsi
Proyek ini adalah sebuah aplikasi berbasis web yang dibangun menggunakan Flask sebagai framework backend. Aplikasi ini dirancang untuk memanfaatkan SQL Server sebagai basis data.

## Persyaratan Sistem
1. **Python 3.8 atau lebih baru**
2. **SQL Server**
3. **SSMS (SQL Server Management Studio)** untuk manajemen basis data
4. **Virtual Environment (optional)** untuk mengelola dependensi Python
5. **Git** untuk manajemen versi

## Instalasi dan Pengaturan

### 1. Clone Repository
```bash
git clone https://github.com/reginamarthaa/myUntarApp
cd myUntarApp
```

### 2. Buat dan Aktifkan Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate # Untuk Mac/Linux
venv\Scripts\activate   # Untuk Windows
```

### 3. Instalasi Dependensi
Pastikan Anda berada di direktori proyek, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Database
1. Pastikan SQL Server sudah berjalan.
2. Impor schema database atau jalankan script yang disediakan di folder `database`.
3. Sesuaikan konfigurasi koneksi database di file `.env`:
```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
DB_PORT=1433
```

### 5. Menjalankan Aplikasi
Jalankan server Flask menggunakan perintah berikut:
```bash
flask run.py
```
Aplikasi akan berjalan di [http://localhost:5000](http://localhost:5000).

## Script SQL
Jalankan script SQL yang terdapat pada folder script dengan urutan sebagai berikut:
1 Script Table.sql
2 Script spInsertDataKuesionerMahasiswa.sql
3 Script spInsertDataMahasiswa.sql
4 Scipt spGetMahasiswaDanProdi.sql
5 spGetDataKuesioner.sql
6 Script spGetHasilKuesioner.sql
7 Script spDeleteDataKuesionerMahasiswa.sql

---

Terima kasih telah menggunakan proyek ini! Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk menghubungi saya melalui issue di GitHub.
