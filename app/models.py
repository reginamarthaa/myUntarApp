# from app import db
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model, UserMixin):
#     __tablename__ = 'USER'
    
#     USER_ID = db.Column(db.Integer, primary_key=True)
#     EMAIL = db.Column(db.String(150), unique=True, nullable=False)
#     PASSWORD = db.Column(db.String(150), nullable=False)

#     # Method untuk set password dengan hassh
#     def set_password(self, password):
#         self.PASSWORD = generate_password_hash(password)

#     # Method untuk check password
#     def check_password(self, password):
#         return check_password_hash(self.PASSWORD, password)

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'USER'
    id = db.Column('USER_ID', db.Integer, primary_key=True)
    email = db.Column('EMAIL', db.String(120), unique=True, nullable=False)
    password = db.Column('PASSWORD', db.String(120), nullable=False)
    