from decimal import Decimal
import re
import sqlite3 as sql
import pyodbc
from flask import jsonify

def getHasilKuesioner():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
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

def getDataKuesioner():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={'02-05-0446-0223'};DATABASE={'UNTAR'};UID={'regina'};PWD={'sa'}')
    cursor = conn.cursor()
    cursor.execute("EXEC spGetDataKuesioner")
    hasil = cursor.fetchall()
    cursor.close()
    conn.close()
    return hasil