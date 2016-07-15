from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from ..auth import Auth
from flask_cas import login_required
from ..forms.accounts import Edit_Profile_Form
from .. import db

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

@blueprint.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    form = Edit_Profile_Form()

    if form.validate_on_submit():
        session['user'].name = form.name.data
        session['user'].email = form.email.data

        db.session.merge(session['user'])
        db.session.commit()

        flash('Profile Has Been Updated')
        return redirect(url_for('content.index'))

    else:
        if form.errors.items():
            for field, errors in form.errors.items():
                for error in errors:
                    flash(getattr(form, field).label.text + ' - ' + error)

    form.populate_form()
    return render_template('account/edit_profile.html', form=form)