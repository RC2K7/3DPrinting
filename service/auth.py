from flask import session
from .models.users import Users
from . import cas, db

class Auth:

    @classmethod
    def attempt(cls):
        if cas.username:
            user = Users.query.filter_by(sid=cas.username).first()
            if not user:
                user = Users()
                user.sid = cas.username
                db.session.add(user)
                db.session.commit()
                user = Users.query.filter_by(sid=cas.username).first()
        if user:
            cls._login(user)
            return  True
        return False
    
    @staticmethod
    def _login(user):
        if user:
            session['user'] = user

    @staticmethod
    def _logout():
        session.destroy()