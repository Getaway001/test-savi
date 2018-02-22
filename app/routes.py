import os

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User,Document
from flask import send_from_directory, current_app 


@app.route('/')
@app.route('/index')
@login_required
def index():
    docs = Document.query.all()
    return render_template('index.html', title='Home', docs=docs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


'''@app.route('/annuaire/<int:year>/<publi_name>.pdf')
def publication(year, publi_name):
    directory = os.path.join('static', 'data', 'yearbooks', str(year))
    fname = "{}.pdf".format(publi_name)
    return send_from_directory(directory, fname)
'''

@app.route('/docs/<publication_name>.pdf')
@login_required
def publication(publication_name):
    directory = os.path.join('static', 'data', 'docs')
    fname = "{}.pdf".format(publication_name)
    return send_from_directory(directory, fname)
#UPLOAD_FOLDER = 'Users/ibrahimadiop/Desktop/microblog-0.5/pdfs/'
