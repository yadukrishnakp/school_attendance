from flask import Flask, render_template, url_for, redirect
from models import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('home.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        return redirect('/register')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
