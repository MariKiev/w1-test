# coding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from flask_wtf.html5 import EmailField
from wtforms_components import PhoneNumberField
from wtforms.validators import DataRequired, Length, EqualTo


class BaseForm(Form):
    username = StringField(u'Имя', validators=[
        DataRequired(message=u'Заполнение данного поля обязательно'), 
        Length(min=1, max=20, message=u'Заполнение данного поля обязательно')
        ])
    email = EmailField('Email', validators=[
        DataRequired(message=u'Заполнение данного поля обязательно')
        ])
    phone_number = StringField(u'Номер телефона',validators=[
        DataRequired(message=u'Заполнение данного поля обязательно'),
        Length(min=10, max=13, message=u'Введите корректный номер телефона')
        ])
    pets = BooleanField(u'Домашние животные')


class WebRegistration(BaseForm):
    password = PasswordField(u'Пароль', validators=[
        DataRequired(message=u'Заполнение данного поля обязательно'), 
        Length(min=6, max=15, message=u'Введите не менее 6 символов'), 
        EqualTo('check_password', message=u'Пароли не совпадают')
        ])
    check_password = PasswordField(u'Подтверждение пароля', validators=[
        DataRequired(message=u'Заполнение данного поля обязательно')
        ])

class ApiRegistration(BaseForm):
    password = PasswordField(u'Пароль', validators=[
        DataRequired(message=u'Заполнение данного поля обязательно'), 
        Length(min=6, max=15, message=u'Введите не менее 6 символов')
        ])

