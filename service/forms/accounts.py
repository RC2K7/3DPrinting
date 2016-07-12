from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Email, DataRequired

class Edit_Profile_Form(Form):
    name = StringField("First Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Save")