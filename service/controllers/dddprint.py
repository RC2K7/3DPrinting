from flask import Blueprint, render_template, session, redirect, url_for, flash
from ..forms.prints import Print_Submission
from ..models.prints import Print

blueprint = Blueprint('3dprint', __name__, url_prefix='/account/3dprint')

@blueprint.before_request
def required_login():
    if not 'user' in session:
        return redirect(url_for('account.login'))
    pass

@blueprint.route('/request', methods=['GET', 'POST'])
def request():
    form = Print_Submission()

    if form.validate_on_submit():
        flash("Validated", "alert")
    else:
        flash("Failed", "alert")

    if len(form.prints) == 0:
        form.prints = [Print()]

    return render_template('3dprint/request.html', form=form)

@blueprint.route('/view')
def view():
    return render_template('errors/under_construction.html')
    pass