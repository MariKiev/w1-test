# coding=utf-8
from app import app, db
from flask import render_template, flash, abort, request, jsonify, redirect, url_for
from datetime import datetime
from forms import WebRegistration, ApiRegistration
from models import User

def create_and_save_user(username, email, password, phone_number, pets):
    user = User(username, email, password, phone_number, pets)
    user.registration_time = datetime.now()
    db.session.add(user)
    db.session.commit()
    return user

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = WebRegistration()
    if form.validate_on_submit():
        create_and_save_user(form.username.data, form.email.data, 
            form.password.data, form.phone_number.data, form.pets.data)
        return "Регистрация прошла успешна"
    return render_template('registration.html', form=form)


@app.route('/api/users', methods=['POST','GET'])
def api_registration():
    if request.method == 'POST':
        form = ApiRegistration(csrf_enabled=False)
        if form.validate_on_submit():
            user = create_and_save_user(form.username.data, form.email.data, 
                form.password.data, form.phone_number.data, form.pets.data)
            return redirect(url_for('get_user', id=user.id))
        return jsonify(form.errors)
    else:
        query = User.query
        if request.args.get('email'):
            query = query.filter_by(email=request.args.get('email'))
        if request.args.get('registration_time'):
            query = query.filter_by(registration_time=request.args.get('registration_time'))
        
        users = query.all()
        all_users = []
        for user in users:
            all_users.append(user.to_dictionary())
        return jsonify(results=all_users)


@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return jsonify(user.to_dictionary())
    else:
        return abort(404)