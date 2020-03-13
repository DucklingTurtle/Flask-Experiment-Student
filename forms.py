from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange


class RegistrationFormStudent(FlaskForm):
    name = StringField("Last and First Name", validators=[DataRequired(), Length(min=2, max=20)])
    focus1 = SelectField("Focus 1", choices=[("AP", "American Politics"), ("CP", "Comparative Politics"),
                                             ("IR", "International Relations"), ("MT", "Methodology"), ("TH", "Political Theory")])
    focus2 = SelectField("Focus 2", choices=[("AP", "American Politics"), ("CP", "Comparative Politics"),
                                             ("IR", "International Relations"), ("MT", "Methodology"),
                                             ("TH", "Political Theory")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Enter")


class RegistrationFormTeacher(FlaskForm):
    name = StringField("Last and First Name", validators=[DataRequired(), Length(min=2, max=20)])
    focus1 = SelectField("Focus 1", choices=[("AP", "American Politics"), ("CP", "Comparative Politics"),
                                             ("IR", "International Relations"), ("MT", "Methodology"), ("TH", "Political Theory")])
    focus2 = SelectField("Focus 2", choices=[("AP", "American Politics"), ("CP", "Comparative Politics"),
                                           ("IR", "International Relations"), ("MT", "Methodology"),
                                           ("TH", "Political Theory")])

    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Enter")