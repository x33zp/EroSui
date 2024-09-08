#!/usr/bin/python3
"""Index"""
from flask import render_template, request, flash
from web_flask.views import app_views
from flask_login import login_required, current_user
from models.note import Note
from models import storage

@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def status():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            new_note.save()
            flash('Note added!', category='success')
        
    return render_template('home.html', user=current_user)
