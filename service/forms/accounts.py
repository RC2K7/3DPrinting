from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Email, DataRequired

from flask import session

class Edit_Profile_Form(Form):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Save")

    def populate_form(self):
        self.name.process_data(session['user'].name)
        self.email.process_data(session['user'].email)