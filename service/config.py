import random, string, datetime
from simplekv.fs import FilesystemStore

class DefaultConfig():

    # Cache Settings
    STORE = FilesystemStore('/tmp/')

    # CAS Settings
    CAS_SERVER = 'https://weblogon.csusb.edu'
    CAS_AFTER_LOGIN = 'index'
    CAS_AFTER_LOGOUT = 'index'

     # Security Settings
    SECRET_KEY = ''.join(random.SystemRandom().choice(string.printable) for _ in range(32))
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
    SESSION_COOKIE_NAME = 'innovation-lab'
    SESSION_KEY_BITS = 256

    # Template Settings
    JINJA_AUTO_RELOAD = True

    # Upload Settings
    UPLOADS_DEFAULT_DEST = './storage'
    UPLOADED_PRINTS_ALLOW = tuple('stl obj'.split())

    # Tuples Extensions
    PRINTS = tuple('stl obj'.split())

    # Database Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(DefaultConfig):

    # Environment Settings
    DEBUG = True
    TESTING = True

    # Database Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../simple.db'

class ProductionConfig(DefaultConfig):
    pass