# coding=utf-8
from flask import Flask
from settings import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


from view import *

if __name__ == '__main__':
    app.run(debug=True)