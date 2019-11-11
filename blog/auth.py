from flask import Blueprint, url_for, render_template, redirect, request, flash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None:
            flash('wrong username '+login_form.username.data)
            return redirect(url_for('auth.login'))
        elif not check_password_hash(user.password, login_form.password.data):
            flash('wrong password')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=login_form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        password = register_form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            return redirect(url_for('auth.login'))

        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('auth/register.html', form=register_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


