#!/usr/bin/python3
"""Index"""
from flask import render_template, request, flash, redirect, url_for
from web_flask.auth import app_auth
from models.user import User
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@app_auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = storage.get(User, email)

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('app_views.status'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)


@app_auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    return redirect(url_for('app_auth.login'))


@app_auth.route('/sign-up', methods=['GET', 'POST'], strict_slashes=False)
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = storage.get(User, email)

        if user:
            flash('Email already exists.', category='error')
        elif password1 != password2 and len(password1) > 6:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 chars.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            new_user.save()
            flash('Account created.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('app_views.status'))

    return render_template('sign_up.html', user=current_user)
