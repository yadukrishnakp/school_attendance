from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import re


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('Login')

    def password_validation(self, password):
        if re.search('[0-9]', password) is None:
            raise ValidationError('Make sure your password has a number in it')
        elif re.search('[A-Z]', password) is None:
            raise ValidationError('Make sure your password has a capital letter in it')
        else:
            raise ValidationError("Your password seems fine")
