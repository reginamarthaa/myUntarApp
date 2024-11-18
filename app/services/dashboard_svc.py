from decimal import Decimal
import re
import sqlite3 as sql
import pyodbc
from flask import jsonify
from .. import connection_string

def getHasilKuesioner():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("EXEC spGetHasilKuesioner")
    hasil = cursor.fetchall()

    if hasil:
        data = {
            'Hasil': 'Label'
        }
        data.update({str(result.Label): result.Jumlah for result in hasil})
    else:
        data = {}

    cursor.close()
    conn.close()
    return data

def getDataKuesioner(no_pertanyaan):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("EXEC spGetDataKuesioner @PERTANYAAN = ?", (no_pertanyaan))
    hasil = cursor.fetchall()

    # if hasil:
    #     data = {
    #         'Hasil': 'Label'
    #     }
    #     data.update({float(result.Nilai): result.Jumlah for result in hasil})
    # else:
    #     data = {}
    
    cursor.close()
    conn.close()
    return hasil