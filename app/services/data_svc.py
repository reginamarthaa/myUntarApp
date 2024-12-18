from ..models import DataKuesioner, Mahasiswa, ProgramStudi
from .. import db
import pyodbc
from .. import connection_string

def getMahasiswa():
    mahasiswa_all = Mahasiswa.query.all()
    return mahasiswa_all

# def getMahasiswadanProdi():
#     # mahasiswa_all = db.session.query(Mahasiswa).join(ProgramStudi, Mahasiswa.program_studi_id == ProgramStudi.program_studi_id).all()
#     # return mahasiswa_all
#     conn = pyodbc.connect(
#         f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
#     cursor = conn.cursor()
#     cursor.execute("EXEC spGetMahasiswadDanProdi @NIM = None, @NAMA = None, @NAMA_FAKULTAS = None, @NAMA_PROGRAM_STUDI = None")
#     mahasiswa_all = cursor.fetchall()
#     return mahasiswa_all

def getMahasiswadanProdiwithParam(nim = '', nama = '', fakultas = '', prodi = ''):
    # mahasiswa_all = db.session.query(Mahasiswa).join(ProgramStudi, Mahasiswa.program_studi_id == ProgramStudi.program_studi_id).all()
    # return mahasiswa_all
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("set nocount on; EXEC spGetMahasiswaDanProdi @NIM = ?, @NAMA = ?, @NAMA_FAKULTAS = ?, @NAMA_PROGRAM_STUDI = ?", (nim, nama, fakultas, prodi))
    mahasiswa_all = cursor.fetchall()
    cursor.close()
    conn.close()
    return mahasiswa_all

def deleteDataKuesionerMahasiswa(nim):
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
        cursor = conn.cursor()
        cursor.execute("EXEC spDeleteDataKuesionerMahasiswa @NIM = ?", (nim))
        conn.commit()
    except pyodbc.Error as e:
        print("Database error:", e)
        return e
    except Exception as e:
        print("Error:", e)
        return e
    finally:
        # Pastikan koneksi selalu ditutup
        conn.close()
    return "Berhasil"