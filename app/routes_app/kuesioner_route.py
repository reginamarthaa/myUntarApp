import pickle
from flask import Blueprint, json, jsonify, render_template, request
import numpy as np
from ..services import kuesioner_svc as kue_svc


kuesioner_route = Blueprint('kuesioner_route', __name__)

@kuesioner_route.route('/predict')
def predict():
    class_entry_relations = kue_svc.getDDLValue()

    default_classes = sorted(class_entry_relations.keys())
    default_values = class_entry_relations[default_classes[0]]

    return render_template('kuesioner.html',
                       fakultas=default_classes,
                       prodi=default_values)

@kuesioner_route.route('/predict_input', methods=['POST', 'GET'])
def predict_post():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x3 = request.form.get('x3')
    x4 = request.form.get('x4')
    x5 = request.form.get('x5')
    # init_features = [float(x) for x in request.form.values()]
    final_features = [np.array([x1, x2, x3, x4, x5])]
    model = pickle.load(open('app\svm_model_poly.pkl', 'rb')) # Load the trained model
    prediction = model.predict(final_features) # Make a prediction

    selected_class = request.form.get('fakultas')
    selected_entry = request.form.get('prodi')
    nama = request.form.get('nama')
    email = request.form.get('email')
    print(selected_class)
    print(selected_entry)
    print(nama)

    prodi_id = kue_svc.getIdbyProdi(selected_entry)
    nim = kue_svc.extract_numbers(email)
    kue_svc.insertData(nim, nama, email, prodi_id, x1, x2, x3, x4, x5, prediction)
    return render_template('kuesioner.html', prediction_text='Predicted Species: {}'.format(prediction)) # Render the predicted result

@kuesioner_route.route('/prodi', methods=['POST'])
def get_prodi():
    fakultas = request.form['fakultas']
    prodii = kue_svc.getProdibyFakultas(fakultas)
    return json.dumps(prodii)

@kuesioner_route.route('/_update_dropdown')
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
def process_data():
    selected_class = request.args.get('selected_class', type=str)
    selected_entry = request.args.get('selected_entry', type=str)

    # process the two selected values here and return the response; here we just create a dummy string
    
    return jsonify(random_text="You selected the car brand: {} and the model: {}.".format(selected_class, selected_entry))
