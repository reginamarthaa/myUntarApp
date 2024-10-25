import sqlite3 as sql

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

# def getProdi(fakultas):
#     con = sql.connect("C:/3 REGINA/skripsi/UNTAR.db")
#     cur = con.cursor()
#     cur.execute("select PRODI_ID, NAMA_PRODI, NAMA_FAKULTAS from PRODI where NAMA_FAKULTAS =?", (fakultas))
#     prodi = cur.fetchall()
#     con.close()
#     return prodi

# def getProdi():
#     con = sql.connect("C:/3 REGINA/skripsi/UNTAR.db")
#     cur = con.cursor()
#     cur.execute("select PRODI_ID, NAMA_PRODI, NAMA_FAKULTAS from PRODI")
#     prodi = cur.fetchall()
#     con.close()
#     return prodi

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