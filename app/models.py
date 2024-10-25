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

class Akun(UserMixin, db.Model):
    __tablename__ = 'AKUN'
    id = db.Column('AKUN_ID', db.Integer, primary_key=True)
    email = db.Column('EMAIL', db.String(120), unique=True, nullable=False)
    nama = db.Column('NAMA', db.String(120), unique=True, nullable=False)
    password = db.Column('PASSWORD', db.String(120), nullable=False)

    def serialize(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'nama' : self.nama,
            'password' : self.password
        }

class ProgramStudi(db.Model):
    __tablename__ = 'PROGRAM_STUDI'
    prodi_id = db.Column('PROGRAM_STUDI_ID', db.String(10), primary_key=True)
    nama_prodi = db.Column('NAMA_PROGRAM_STUDI', db.String(120), unique=True, nullable=False)
    nama_fakultas = db.Column('NAMA_FAKULTAS', db.String(120), nullable=False)

    # mahasiswa = db.relationship('Mahasiswa', back_populates='program_studi', lazy=True)

    def serialize(self):
        return {
            'prodi_id' : self.prodi_id,
            'nama_prodi' : self.nama_prodi,
            'nama_fakultas' : self.nama_fakultas
        }

class Mahasiswa(db.Model):
    __tablename__ = 'MAHASISWA'  # Nama tabel di database

    NIM = db.Column(db.String(10), primary_key=True, nullable=False)  # Kolom NIM sebagai primary key
    NAMA = db.Column(db.String(50), nullable=False)  # Kolom NAMA
    EMAIL = db.Column(db.String(50))  # Kolom EMAIL
    PROGRAM_STUDI_ID = db.Column(db.String(10), db.ForeignKey('program_studi.program_studi_id'), nullable=False)

    # program_studi = db.relationship('ProgramStudi', back_populates='mahasiswa', lazy=True)

    def serialize(self):
        return {
            'nim' : self.NIM,
            'nama' : self.NAMA,
            'email' : self.EMAIL,
            'prodi_id' : self.PROGRAM_STUDI_ID
        }
    
class DataKuesioner(db.Model):
    __tablename__ = 'DATA_KUESIONER'  # Nama tabel di database

    NIM = db.Column(db.String(10), primary_key=True, nullable=False)  # Kolom NIM sebagai primary key
    PERTANYAAN_1 = db.Column(db.Numeric(3, 2), nullable=False)  # Kolom PERTANYAAN_1
    PERTANYAAN_2 = db.Column(db.Numeric(3, 2), nullable=False)  # Kolom PERTANYAAN_2
    PERTANYAAN_3 = db.Column(db.Numeric(3, 2), nullable=False)  # Kolom PERTANYAAN_3
    PERTANYAAN_4 = db.Column(db.Numeric(3, 2), nullable=False)  # Kolom PERTANYAAN_4
    PERTANYAAN_5 = db.Column(db.Numeric(3, 2), nullable=False)  # Kolom PERTANYAAN_5
    HASIL = db.Column(db.Integer)  # Kolom HASIL


    