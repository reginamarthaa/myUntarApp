from decimal import Decimal
import re
import sqlite3 as sql
import pyodbc
from flask import jsonify

from ..models import ProgramStudi

def getProdi():
    prodi_all = ProgramStudi.query.all()
    # return jsonify([prodi.serialize() for prodi in prodi_all])
    return prodi_all

def getProdibyFakultas(fakultas):
    prodi_all = ProgramStudi.query.filter_by(nama_fakultas=fakultas).all()
    # return jsonify([prodi.serialize() for prodi in prodi_all])
    return prodi_all

def getIdbyProdi(prodi):
    prodi = ProgramStudi.query.filter_by(nama_prodi=prodi).first()
    return prodi.prodi_id

def getDDLValue():
    # Create an empty dictionary
    all_prodi = getProdi()
    myDict = {}
    for p in all_prodi:
    
        key = p.nama_fakultas

        # Select all car models that belong to a car brand
        f = ProgramStudi.query.filter_by(nama_fakultas=key).all()
    
        # build the structure (lst_c) that includes the names of the car models that belong to the car brand
        list_prodi = []
        for p in f:
            list_prodi.append( p.nama_prodi )
        myDict[key] = list_prodi
    
    class_entry_relations = myDict
                        
    return class_entry_relations

def insertData(nim, nama, email, program_studi_id, x1, x2, x3, x4, x5, hasil):
    # conn = pyodbc.connect(
    #     f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
    # cursor = conn.cursor()
    # cursor.execute("EXEC spGetMahasiswaDanProdi @NIM = ?, @NAMA = ?, @EMAIL = ?, @PROGRAM_STUDI_ID = ?, @PERTANYAAN_1 = ?, @PERTANYAAN_2 = ?, @PERTANYAAN_3 = ?, @PERTANYAAN_4 = ?, @PERTANYAAN_5 = ?, @HASIL = ?", 
    #                (nim, nama, email, program_studi_id, str(final_features[0]), str(final_features[1]),str(final_features[2]),str(final_features[3]),str(final_features[4]), hasil))
    # conn.commit()
    # cursor.close()
    # conn.close()
    try:
        # Membuat koneksi ke database
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=02-05-0446-0223;'
            'DATABASE=UNTAR;'
            'UID=regina;'
            'PWD=sa'
        )
        # x1 = final_features[0][0]
        # x2 = final_features[0][1]
        # x3 = final_features[0][2]
        # x4 = final_features[0][3]
        # x5 = final_features[0][4]
        hasill = int(hasil.item())
        x1 = Decimal(x1)
        x2 = Decimal(x2)
        x3 = Decimal(x3)
        x4 = Decimal(x4)
        x5 = Decimal(x5)
        # query = "EXEC spGetMahasiswaDanProdi @NIM = ?, @NAMA = ?, @EMAIL = ?, @PROGRAM_STUDI_ID = ?, @PERTANYAAN_1 = ?, @PERTANYAAN_2 = ?, @PERTANYAAN_3 = ?, @PERTANYAAN_4 = ?, @PERTANYAAN_5 = ?, @HASIL = ?"
        # data = [(
        # with conn.cursor() as cursor:
        #     cursor.execute(
        #         "EXEC spGetMahasiswaDanProdi @NIM = ?, @NAMA = ?, @EMAIL = ?, @PROGRAM_STUDI_ID = ?, @PERTANYAAN_1 = ?, @PERTANYAAN_2 = ?, @PERTANYAAN_3 = ?, @PERTANYAAN_4 = ?, @PERTANYAAN_5 = ?, @HASIL = ?",
        #         (nim, nama, email, program_studi_id, 
        #          x1, x2, x3, 
        #          x4, x5, hasill)
        #     )
        cursor = conn.cursor()
        cursor.execute("EXEC spInsertDataMahasiswa @NIM = ?, @NAMA = ?, @EMAIL = ?, @PROGRAM_STUDI_ID = ?", (nim, nama, email, program_studi_id))
        conn.commit()

        cursor.execute("EXEC spInsertDataKuesionerMahasiswa @NIM = ?, @PERTANYAAN_1 = ?, @PERTANYAAN_2 = ?, @PERTANYAAN_3 = ?, @PERTANYAAN_4 = ?, @PERTANYAAN_5 = ?, @HASIL = ?", 
                   (nim, x1, x2, x3, x4, x5, hasill))
        conn.commit()
        
        # Commit perubahan
        # conn.commit()
    
    except pyodbc.Error as e:
        print("Database error:", e)
    except Exception as e:
        print("Error:", e)
    
    finally:
        # Pastikan koneksi selalu ditutup
        conn.close()

def extract_numbers(email):
    # Mencari angka di dalam string menggunakan regex
    result = re.search(r'\d+', email)
    return result.group() if result else None