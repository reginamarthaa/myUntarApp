import os
import time
import pandas as pd
from flask import Blueprint, flash, redirect, render_template, request, url_for
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

algoritma_route = Blueprint('algoritma_route', __name__)

# ALLOWED_EXTENSIONS = {'csv', 'txt', 'xlsx'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def kmeans_clustering(data_latih):
    X = data_latih

    kmeans = KMeans(n_clusters=3, random_state=20)
    labels = kmeans.fit_predict(X)

    Y = labels

    data_berlabel = data_latih
    data_berlabel["label"] = Y
    silhouette_avg = silhouette_score(X, Y)
    print(silhouette_avg)
    return data_berlabel 

def svm_classification(data_latih):
    X = data_latih[['mempelajari perkembangan teknologi dalam dunia usaha',
                'Penerapan teknologi dalam usaha',
                'Terlibat dalam kewirausahaan berbasis teknologi',
                'keinginan memberikan dampak dari bisnis menggunakan teknologi ',
                'ketertarikan untuk menjalankan bisnis berbasis teknologi']]
    y = data_latih['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    kernel = 'poly'
    c = 10
    
    svm_model = SVC(kernel=kernel, C = c)
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test)
    
    akurasi = accuracy_score(y_test, y_pred)
    print(f"Akurasi kernel {kernel}, C = {c} : {akurasi}")

    hasil = classification_report(y_test, y_pred)
    print(hasil)
    print("\n")


@algoritma_route.route('/algoritma')
def algoritma():

    return render_template('algoritma.html')

@algoritma_route.route('/algoritma_pelatihan', methods=['POST'])
def algoritma_pelatihan():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    
    if file and file.filename.endswith('.csv'):
        # Membaca file CSV menggunakan Pandas
        data = pd.read_csv(file)

        data_kmeans = kmeans_clustering(data)
        svm_classification(data_kmeans)


        return f"<h1>File berhasil diupload</h1><p>Data:</p>{data_kmeans.to_html()}"
    else:
        return "Invalid file format. Please upload a CSV file."
