from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/3 REGINA/skripsi/UNTAR.db'
app.config['SECRET_KEY'] = '9f8b7d6e8a7d4b56a1c9d6b5e4f7d3a2'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'app_route.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# db.init_app(app)

# blueprint for auth routes in our app
from .routes import app_route as app_route_blueprint
app.register_blueprint(app_route_blueprint)

# from flask import *
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# app = Flask(__name__)

# # Konfigurasi database menggunakan SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/3 REGINA/skripsi/UNTAR.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Inisialisasi SQLAlchemy
# db = SQLAlchemy(app)

# # Definisi model untuk tabel USER
# class User(db.Model):
#     __tablename__ = 'USER'
#     id = db.Column('USER_ID', db.Integer, primary_key=True)
#     email = db.Column('EMAIL', db.String(120), unique=True, nullable=False)
#     password = db.Column('PASSWORD', db.String(120), nullable=False)
    
#     def __repr__(self):
#         return f'<User {self.email}>'

# @app.route("/", methods=["POST", "GET"])
# def login():
#     if request.method=="POST":
#         first_name = request.form["first_name"]
#         last_name = request.form["last_name"]
#         # Query untuk mengambil USER_ID berdasarkan EMAIL
#         user = User.query.filter_by(email=first_name).first()

#         if user:
#             user_id = user.id
#         else:
#             user_id = None

#         print(first_name + last_name)
#         print(user_id)
#         return render_template("login.html")
#     else:
#         return render_template("login.html")
