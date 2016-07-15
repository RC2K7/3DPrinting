from flask import Blueprint, render_template, session, redirect, url_for

blueprint = Blueprint('manage', __name__, url_prefix='/manage')

@blueprint.before_request
def required_priv():
    if 'user' not in session:
        return redirect(url_for('account.login'))
    if not session['user'].role >= 1:
        return redirect(url_for('content.index'))
    pass

@blueprint.route('/')
def index():
    return redirect(url_for('content.index'))
    pass

@blueprint.route('/prints')
def prints():
    if not session['user'].role >= 1:
        return render_template('errors/403.html')

    return render_template('manage/prints.html')
    pass

@blueprint.route('/access')
def access():
    return render_template('manage/access.html')
    pass