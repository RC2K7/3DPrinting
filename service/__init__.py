from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_cas import CAS
from flask_uploads import UploadSet, configure_uploads
from flask_kvsession import KVSessionExtension
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

db = SQLAlchemy()
cas = CAS()
prints = UploadSet()
session = KVSessionExtension()
csrf = CsrfProtect()
bootstrap = Bootstrap()

def create_app(config):
    app = Flask(
        __name__.split('.')[0],
        static_url_path='',
        static_folder='../public',
        template_folder='frontend/templates'
    )

    app.config.from_object(config)

    register_blueprints(app)
    register_errorhandlers(app)
    register_extensions(app)
    register_template_functions(app)

    return app

def register_blueprints(app):
    from . import controllers

    for name in dir(controllers):
        if not name.startswith("__"):
            app.register_blueprint(getattr(controllers, name).blueprint)

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{}.html'.format(error_code)), error_code

    for errcode in [403, 404]:
        app.errorhandler(errcode)(render_error)

def register_extensions(app):
    csrf.init_app(app)
    session.init_app(app, app.config["STORE"])
    db.init_app(app)
    cas.init_app(app, '/cas')
    prints = UploadSet(name='prints', extensions=['stl', 'obj'])
    configure_uploads(app, (prints))
    bootstrap.init_app(app)

def register_template_functions(app):
    from . import template

    # TODO: Implement this in a sane manner
    for name in dir(template.TemplateGlobals):
        if not name.startswith("__"):
            app.context_processor(getattr(template.TemplateGlobals, name))

    for name in dir(template.TemplateFunctions):
        if not name.startswith("__"):
            app.add_template_global(getattr(template.TemplateFunctions, name))

    for name in dir(template.TemplateFilters):
        if not name.startswith("__"):
            app.add_template_filter(getattr(template.TemplateFilters, name))