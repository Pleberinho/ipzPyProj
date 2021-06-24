from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length


class EmployeeForm(FlaskForm):
    name = StringField('Імя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Прізвище', validators=[DataRequired(), Length(max=50)])
    middle_name = StringField('По-батькові', validators=[DataRequired(), Length(max=50)])
    address = StringField('Адреса', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(max=50)])
    phone = IntegerField('Номер телефону',
                         validators=[DataRequired(), NumberRange(min=-9223372036854775808, max=9223372036854775807)])
    salary = IntegerField('Зарплата',
                          validators=[DataRequired(), NumberRange(min=-9223372036854775808, max=9223372036854775807)])
    category = SelectField('Посада', validators=[DataRequired()],
                           choices=[
                               (1, "Trainee"),
                               (2, "Junior"),
                               (3, "Middle"),
                               (4, "Senior")]
                           )
    submit = SubmitField('Застосувати')
