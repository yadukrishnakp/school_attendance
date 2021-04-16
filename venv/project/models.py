from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired, Email, EqualTo
import re


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('Login')

    def password_validation(self, password):
        if re.search('[0-9]', password) is None:
            raise ValidationError('Make sure your password has a number in it')
        if re.search('[A-Z]', password) is None:
            raise ValidationError('Make sure your password has a capital letter in it')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=6, max=15)])
    submit = SubmitField('Sign Up')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken.Please choose different one')
    #
    # def validate_email(self, email):
    #     email = User.query.filter_by(email=email.data).first()
    #     if email:
    #         raise ValidationError('That email is taken.Please choose different one')
