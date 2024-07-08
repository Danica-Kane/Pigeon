# IMPORTS 
import os
import uuid
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from wtforms import FileField

from website import DB_NAME
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# LOGIN PAGE 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Login form - compare user inputs to database
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
        
    return render_template("login.html", user=current_user)


# LOGOUT ROUTE - REDIRECT TO LOGIN PAGE
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# SIGN UP PAGE 

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Sign up form 
    if request.method == "POST":
        # get data from form 
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #profile_pic = request.files["profile_pic"]
        
        #picName = str(uuid.uuid1()) + os.path.splitext(profile_pic.filename)[1]
        #profile_pic.save(os.path.join("/Users/danicakane/Downloads/Pigeon/website/static/images", picName))
        
        # security / form requrirements and errors 
        user = User.query.filter_by(email = email).first()
        if user:
            flash('An account with this email already exists', category='error')
            return redirect(url_for('auth.sign_up'))   
        if len(email) < 4:
                flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2'))#profile_pic=picName
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='succsess')
            # Redirect to home page if successful
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)