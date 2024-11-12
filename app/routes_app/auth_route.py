from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from app.models import Akun

auth_route = Blueprint('auth_route', __name__)

@auth_route.route('/login')
def login():
    return render_template('login.html')

@auth_route.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Akun.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_route.login')) # if the user doesn't exist or password is wrong, reload the page
    
    user = Akun.query.filter_by(email=email).first()

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)

    return redirect(url_for('dashboard_route.dashboard'))

@auth_route.route('/signup')
def signup():
    return render_template('signup.html')

@auth_route.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    nama = request.form.get('name')
    password = request.form.get('password')

    user = Akun.query.filter_by(email=email).first()
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email sudah terdaftar')
        return redirect(url_for('auth_route.signup'))
    
     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Akun(email=email, nama=nama, password=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth_route.login'))

@auth_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_route.login'))