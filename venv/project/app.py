from flask import Flask, render_template, url_for, redirect, flash, session, request, g
from models import LoginForm, RegistrationForm, StudentForm, AddStudent
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Student(UserMixin, db.Model):
    admission_number = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(20), nullable=False)
    student_class = db.Column(db.Integer, nullable=False)
    student_division = db.Column(db.String(2), nullable=False)
    attendance_percentage = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Student('{self.student_name}', '{self.student_class}', '{self.student_division}', '{self.attendance_percentage}')"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('search_student'))
        else:
            flash("check email and password is correct")
    return render_template('login.html', form=form)


@app.route('/search_student', methods=['GET', 'POST'])
@login_required
def search_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(student_name=form.student_name.data).first()
        if student:
            return render_template('login_success.html', student=student, form=form)
        else:
            return redirect(url_for('search_student'))
    return render_template('login_success.html', form=form)


@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    # if current_user.is_authenticated:
    #     return redirect(url_for('login'))
    form = AddStudent()
    if form.validate_on_submit():
        student = Student(student_name=form.student_name.data, student_class=form.student_class.data,
                          student_division=form.student_division.data,
                          attendance_percentage=form.attendance_percentage.data)
        db.session.add(student)
        db.session.commit()
        flash(f"successfully added")
        return redirect(url_for('add_student'))
    return render_template('add_student.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f"Your account has been created, Now you can login")
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
