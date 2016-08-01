from .. import db

class Print(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    file = db.Column(db.String(50))
    quantity = db.Column(db.Integer())
    filament = db.Column(db.Integer(), db.ForeignKey('filaments.id'))