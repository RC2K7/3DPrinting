from .. import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(9), unique=True)
    role = db.Column(db.Integer)
    name = db.Column(db.String(70))
    email = db.Column(db.String(247), unique=True)
