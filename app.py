#!usr/bin/python

from flask import Flask, g, render_template, redirect, url_for, flash
from flask.ext.login import LoginManager

import models
import forms

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key ='hard to guess'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
         return None


@app.before_request()
def before_request():
    #connect to database before each request
    g.db =models.DATABASE
    g.db.connect()


@app.after_request
def after_request():
    #close the database after each request
    g.db.close()
    return response


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("you are registered", "success")
        models.User.create_User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return 'Hey'


if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
        username="Larrisa",
        email="larrisa@gmail.com",
        password='password',
        admin=True
    )

    app.run(debug=DEBUG, port=PORT, host=HOST)