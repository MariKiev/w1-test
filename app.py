# coding=utf-8
from flask import Flask
from settings import SECRET_KEY, DB_URL
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)


from view import *

if __name__ == '__main__':
    app.run(debug=True)