# coding=utf-8
from app import app
from flask import render_template, flash
from forms import *
from models import *


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, 
            form.password.data, form.phone_number.data, form.pets.data)
            
        db.session.add(user)
        db.session.commit()
        return "Регистрация прошла успешна"
    return render_template('registration.html', form=form)