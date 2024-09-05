#!/usr/bin/python3
"""Index"""
from flask import render_template, request, flash
from web_flask.auth import app_auth


@app_auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    return render_template('login.html', boolean=True)


@app_auth.route('/logout', strict_slashes=False)
def logout():
    return "Logout"


@app_auth.route('/sign-up', methods=['GET', 'POST'], strict_slashes=False)
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2 and len(password1) > 6:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 chars.', category='error')
        else:
            flash('Account created.', category='success')

    return render_template('sign_up.html')
