from flask import session
from datetime import datetime

class TemplateGlobals:

    @staticmethod
    def inject_year():
        return dict(year=datetime.now().year)

class TemplateFunctions:

    @staticmethod
    def is_logged_in():
        return 'user' in session

    @staticmethod
    def is_maintainer():
        return session['user'].role >= 1

    @staticmethod
    def is_admin():
        return session['user'].role >= 2

    @staticmethod
    def is_master():
        return session['user'].role >= 3

    @staticmethod
    def get_name():
        return session['user'].name
    
    @staticmethod
    def get_sid():
        return session['user'].sid

class TemplateFilters:
    
    @staticmethod
    def striplines(s):
        return ' '.join(s.splitlines())