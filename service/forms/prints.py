from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, FieldList, FormField
from wtforms.fields import FileField
from wtforms.validators import DataRequired, NumberRange

class Print_Entry(Form):
    file = FileField('File Upload', validators=[DataRequired()])
    color = SelectField('Color Preference', validators=[DataRequired()], choices=[('w', 'White'), ('b', 'Blue'), ('s', 'Silver')])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])

class Print_Submission(Form):
    prints = FieldList(FormField(Print_Entry), 'Prints', min_entries=1)
    submit = SubmitField('Submit Print')