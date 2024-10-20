from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

app_route = Blueprint('app_route', __name__)

@app_route.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', email=current_user.email)

@app_route.route('/login')
def login():
    return render_template('login.html')

@app_route.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    user = User.query.filter_by(email=email).first()

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)

    return redirect(url_for('app_route.dashboard'))

@app_route.route('/signup')
def signup():
    return render_template('signup.html')

@app_route.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('app_route.signup'))
        # return redirect(url_for('app_route.login'))
    
     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, password=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('app_route.login'))

@app_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app_route.login'))