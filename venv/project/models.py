from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired, Email, EqualTo
import re


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password'), Length(min=6, max=15)])
    submit = SubmitField('Sign Up')


class StudentForm(FlaskForm):
    student_name = StringField('Student name', validators=[DataRequired()])
    student_class = IntegerField('Class', validators=[DataRequired()])
    student_division = StringField('Division', validators=[DataRequired(), Length(min=1, max=1)])
    submit = SubmitField('Search')


class AddStudent(FlaskForm):
    student_name = StringField('Student name', validators=[DataRequired()])
    student_class = IntegerField('Class', validators=[DataRequired()])
    student_division = StringField('Division', validators=[DataRequired(), Length(min=1, max=1)])
    attendance_percentage = IntegerField('attendance percentage', validators=[DataRequired()])
    submit = SubmitField('Add student')