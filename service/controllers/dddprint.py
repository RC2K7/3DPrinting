from flask import Blueprint, render_template, session, redirect, url_for
from ..forms.prints import Print_Submission

blueprint = Blueprint('3dprint', __name__, url_prefix='/account/3dprint')

@blueprint.before_request
def required_login():
    if not 'user' in session:
        return redirect(url_for('account.login'))
    pass

@blueprint.route('/request', methods=['GET', 'POST'])
def request():
    # if request.method == 'POST':
    #     file = request.files.get('file')
    #     if not file:
    #         flash('Fill All Marked Fields')
    #     else:
    #         try:
    #             filename = prints.save(request.files['file'])
    #         except UploadNotAllowed:
    #             flash('Upload Not Allowed')
    #         else:
    #             flash('Completed Uploading... {}'.format(filename))
    #     return redirect(url_for('content.index'))
    form = Print_Submission()
    return render_template('3dprint/request.html', form=form)

@blueprint.route('/view')
def view():
    return render_template('errors/under_construction.html')
    pass