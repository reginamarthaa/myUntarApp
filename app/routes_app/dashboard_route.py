from flask import Blueprint, render_template
from flask_login import current_user, login_required


dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', email=current_user.email)
