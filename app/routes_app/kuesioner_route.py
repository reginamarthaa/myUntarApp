import pickle
from flask import Blueprint, json, jsonify, render_template, request
from flask_login import login_required
import numpy as np
from ..services import kuesioner_svc as kue_svc


kuesioner_route = Blueprint('kuesioner_route', __name__)

@kuesioner_route.route('/predict')
@login_required
def predict():
    class_entry_relations = kue_svc.getDDLValue()

    default_classes = sorted(class_entry_relations.keys())
    default_values = class_entry_relations[default_classes[0]]

    return render_template('kuesioner.html',
                       fakultas=default_classes,
                       prodi=default_values)

from flask import jsonify

@kuesioner_route.route('/predict_input', methods=['POST', 'GET'])
@login_required
def predict_post():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x3 = request.form.get('x3')
    x4 = request.form.get('x4')
    x5 = request.form.get('x5')
    final_features = [np.array([x1, x2, x3, x4, x5])]

    # Load model dan prediksi
    model = pickle.load(open('app/metode/svm_model_poly_1.pkl', 'rb'))
    prediction = model.predict(final_features)

    # Ambil data lainnya
    selected_class = request.form.get('fakultas')
    selected_entry = request.form.get('prodi')
    nama = request.form.get('nama')
    email = request.form.get('email')

    # Simpan data ke database
    prodi_id = kue_svc.getIdbyProdi(selected_entry)
    nim = kue_svc.extract_numbers(email)
    kue_svc.insertData(nim, nama, email, prodi_id, x1, x2, x3, x4, x5, prediction)

    print(prediction[0])
    if prediction[0] == 0 :
        result = "Tertarik"
    elif prediction[0] == 1 :
        result = "Ragu-ragu"
    elif prediction[0] == 2 :
        result = "Tidak Tertarik"
    else :
        result = "Tidak termasuk ke dalam kelas manapun"    

    # Kembalikan respons JSON dengan hasil klasifikasi
    return jsonify({"success": True, "classification" : result, "nim" : nim}), 200

    # return render_template('kuesioner.html', prediction_text='Predicted Species: {}'.format(prediction)) # Render the predicted result

@kuesioner_route.route('/prodi', methods=['POST'])
@login_required
def get_prodi():
    fakultas = request.form['fakultas']
    prodii = kue_svc.getProdibyFakultas(fakultas)
    return json.dumps(prodii)

@kuesioner_route.route('/_update_dropdown')
@login_required
def update_dropdown():

    # the value of the first dropdown (selected by the user)
    selected_class = request.args.get('selected_class', type=str)

    # get values for the second dropdown
    updated_values = kue_svc.getDDLValue()[selected_class]

    # create the value sin the dropdown as a html string
    html_string_selected = ''
    for entry in updated_values:
        html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)

    return jsonify(html_string_selected=html_string_selected)

@kuesioner_route.route('/_process_data')
@login_required
def process_data():
    selected_class = request.args.get('selected_class', type=str)
    selected_entry = request.args.get('selected_entry', type=str)

    # process the two selected values here and return the response; here we just create a dummy string
    
    return jsonify(random_text="You selected the car brand: {} and the model: {}.".format(selected_class, selected_entry))
