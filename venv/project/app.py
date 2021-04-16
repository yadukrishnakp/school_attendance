from flask import Flask, render_template, url_for, redirect

from models import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('home.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
