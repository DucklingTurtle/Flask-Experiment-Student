from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class RegistrationFormStudent(FlaskForm):
    student_id = IntegerField("Student ID", validators=[DataRequired(), NumberRange(min=0, max=99999999)])
    name = StringField("Last and First Name", validators=[DataRequired(), Length(min=2, max=20)])
    focus1 = StringField("Field of Focus 1", validators=[DataRequired(), Length(min=2, max=40)])
    focus2 = StringField("Field of Focus 2", validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Enter")