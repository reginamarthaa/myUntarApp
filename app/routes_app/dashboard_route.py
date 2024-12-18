import pickle
from flask import Blueprint, jsonify, logging, render_template, request
from flask_login import current_user, login_required
import matplotlib.pyplot as plt
import os

import numpy as np
from .. import current_directory
from ..services import dashboard_svc as db_svc

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/')
def dashboard():
    nama = getattr(current_user, 'nama', "")
    data_hasil = db_svc.getHasilKuesioner()
    # data_pertanyaan = db_svc.getDataKuesioner()
    data = db_svc.getDataKuesioner('PERTANYAAN_1')
    
    # final_features = [np.array([0.7, 0.7, 0.7, 0.7, 0.7])]
    # model = pickle.load(open('app\svm_model_poly.pkl', 'rb')) # Load the trained model
    # prediction = model.predict(final_features)
    # print(prediction)
    
    data_pertanyaan = {
        "data": []
    }
    for Nilai, Jumlah in data:
        data_pertanyaan["data"].append({"Nilai": Nilai, "Jumlah": Jumlah})
    return render_template('dashboard.html', data_hasil=data_hasil, data_pertanyaan=data_pertanyaan, nama=nama)

@dashboard_route.route('/get_data_pert/<string:NO_PERTANYAAN>')
def get_data_pert(NO_PERTANYAAN):
    data_pertanyaan = db_svc.getDataKuesioner(NO_PERTANYAAN)
    # data1 = data_pertanyaan[NO_PERTANYAAN]
    # data2 = [tuple(float(value) for value in row) for row in data1] # Konversi Row menjadi dict
    print("halo")
    return jsonify(data_pertanyaan)
    # return data

@dashboard_route.route('/get_data', methods = ['GET'])
def get_data():
    try :
        NO_PERTANYAAN = request.args.get('NO_PERTANYAAN', type=str)
        data_pertanyaan = db_svc.getDataKuesioner(NO_PERTANYAAN)
        # data1 = data_pertanyaan[NO_PERTANYAAN]
        # data2 = [tuple(float(value) for value in row) for row in data1] # Konversi Row menjadi dict
        print("halo")
        
        data_pertanyaan_json = {
            "data_pertanyaan": []
        }
        for Nilai, Jumlah in data_pertanyaan:
            data_pertanyaan_json["data_pertanyaan"].append({"Nilai": Nilai, "Jumlah": Jumlah})
        # data_pertanyaan.update({float(result.Nilai): result.Jumlah for result in data_pertanyaan})
        
        return data_pertanyaan_json
        # return data
    except Exception as e:
        print(f"Error: {e}")
        return None