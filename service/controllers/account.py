from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from ..auth import Auth
from flask_cas import login_required
from ..forms.accounts import Edit_Profile_Form

blueprint = Blueprint('account', __name__, url_prefix='/account')

@blueprint.before_request
def rquire_login():
    if not ('user' in session or request.path.startswith(url_for('.login'))):
        return render_template('errors/403.html')
    pass

@blueprint.route('/login')
@login_required
def login():
    Auth.attempt();
    return redirect(url_for('content.index'))

@blueprint.route('/logout')
def logout():
    Auth._logout()
    return redirect(url_for('cas.logout', _external=True))

@blueprint.route('/edit')
def edit_profile():
    form = Edit_Profile_Form()
    form.name = session['user'].name
    form.email = session['user'].email
    return render_template('account/edit_profile.html', form=form)