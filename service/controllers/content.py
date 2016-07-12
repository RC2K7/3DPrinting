from flask import Blueprint, render_template, redirect, session, url_for
from flask_cas import login_required
from ..auth import Auth

blueprint = Blueprint('content', __name__)

@blueprint.route('/')
def index():
    return render_template('content/index.html')

@blueprint.route('/info')
def info():
    return render_template('errors/under_construction.html')