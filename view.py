# coding=utf-8
from app import app
from flask import render_template, flash
from forms import *


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return "Регистрация прошла успешна"

    return render_template('registration.html', form=form)