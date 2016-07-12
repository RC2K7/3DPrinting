from .. import db

class Filaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filament = db.Column(db.String(64), unique=True)
    availability = db.Column(db.Boolean, default=True)