from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    confirmed_password = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(64))
    pets = db.Column(db.Boolean, default=False)
    registration_time = db.Column(db.DateTime)

    def __init__(self, username, email, password, phone_number, pets):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.phone_number = phone_number
        self.pets = pets

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)