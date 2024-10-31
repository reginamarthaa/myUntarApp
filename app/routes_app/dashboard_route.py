from flask import Blueprint, jsonify, render_template
from flask_login import current_user, login_required
import matplotlib.pyplot as plt
import os
from .. import current_directory
from ..services import dashboard_svc as db_svc

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/')
def dashboard():
    data_hasil = db_svc.getHasilKuesioner()
    data_pertanyaan = db_svc.getDataKuesioner()
    return render_template('dashboard.html', email=current_user.email, data_hasil=data_hasil, data_pertanyaan=data_pertanyaan)

@dashboard_route.route('/get_data/<int:question_id>')
def get_data(question_id):
    data_pertanyaan = db_svc.getDataKuesioner()
    return data_pertanyaan[question_id]