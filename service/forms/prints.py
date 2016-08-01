from flask_wtf import Form
from flask_wtf import Form as NoCsrfForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange
from ..models.prints import Print

class Print_Entry(NoCsrfForm):
    file = FileField('File Upload', validators=[DataRequired(), FileRequired(), FileAllowed(['.stl', '.obj'], "STL and OBJ Files Only!")])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)], default=1)
    filament = SelectField('Color Preference', validators=[DataRequired()],
                           choices=[('w', 'White'), ('b', 'Blue'), ('s', 'Silver')])

class Print_Submission(Form):
    prints = FieldList(FormField(Print_Entry), min_entries=1)
    submit = SubmitField('Submit Print')