from ..models import DataKuesioner, Mahasiswa, ProgramStudi
from .. import db
import pyodbc

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
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
    cursor = conn.cursor()
    cursor.execute("set nocount on; EXEC spGetMahasiswadDanProdi @NIM = ?, @NAMA = ?, @NAMA_FAKULTAS = ?, @NAMA_PROGRAM_STUDI = ?", (nim, nama, fakultas, prodi))
    mahasiswa_all = cursor.fetchall()
    return mahasiswa_all