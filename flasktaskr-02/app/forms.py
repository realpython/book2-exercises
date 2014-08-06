# forms.py

from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, \
    SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class AddTaskForm(Form):
    task_id = IntegerField('Priority')
    name = TextField('Task Name', validators=[DataRequired()])
    due_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y'
    )
    priority = SelectField(
        'Priority',
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
            ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
        ]
    )
    status = IntegerField('Status')


class RegisterForm(Form):
    name = TextField(
        'Username',
        validators=[DataRequired(),
        Length(min=6, max=25)]
    )
    email = TextField(
        'Email',
        validators=[DataRequired(),
        Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(),
        Length(min=6, max=40)])
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password',
        message='Passwords must match')]
    )


class LoginForm(Form):
    name = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
