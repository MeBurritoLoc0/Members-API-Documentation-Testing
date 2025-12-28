from application.extensions import db
from datetime import date

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(255), nullable=False)
