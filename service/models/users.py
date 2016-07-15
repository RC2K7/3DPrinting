from .. import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(9), unique=True, index=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False, default=0)
    name = db.Column(db.String(70))
    email = db.Column(db.String(247), unique=True)

    role = db.relationship('Roles', lazy='joined')

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name=None):
        self.name = name