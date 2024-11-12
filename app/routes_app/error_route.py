from flask import Blueprint, Flask, render_template
from app import app, db

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html', error=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template('500.html', error=str(e)), 500