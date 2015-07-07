# coding=utf-8
from app import app
from flask import render_template, flash, abort, request
from datetime import datetime
from forms import *
from models import *
import json


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, 
            form.password.data, form.phone_number.data, form.pets.data)
        user.registration_time = datetime.now()
        db.session.add(user)
        db.session.commit()
        return "Регистрация прошла успешна"
    return render_template('registration.html', form=form)


@app.route('/api/users', methods=['POST','GET'])
def api_registration():
    if request.method == 'POST':
        form = RegistrationForm(csrf_enabled=False)
        if form.validate_on_submit():
            user = User(form.username.data, form.email.data, 
                form.password.data, form.phone_number.data, form.pets.data)
            user.registration_time = datetime.now().isoformat()
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('get_user', id=user.id))
        return json.dumps(form.errors)
    else:
        query = User.query
        if request.args.get('email'):
            query = query.filter_by(email=request.args.get('email'))
        if request.args.get('registration_time'):
            query = query.filter_by(registration_time=request.args.get('registration_time'))
        
        users = query.all()
        all_users = []
        for user in users:
            i = {
                'name': user.username,
                'email': user.email,
                'phone_number': user.phone_number,
                'pets': user.pets,
                'registration_time': str(user.registration_time)
            }
            all_users.append(i)
        return json.dumps(all_users)


@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        user_dict = {
        'name': user.username,
        'email': user.email,
        'phone_number': user.phone_number,
        'pets': user.pets,
        'registration_time': str(user.registration_time)
        }
        return json.dumps(user_dict)
    else:
        return abort(404)