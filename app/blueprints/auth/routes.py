from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.models import User
from . import bp
from .forms import LoginForm, RegistrationForm


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('You have successfully registered', 'success')
        return redirect(url_for('home.index'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Email address not found', 'error')
            return redirect(url_for('auth.login'))
        if not user.check_password(form.password.data):
            flash('Invalid password', 'error')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        flash('You have successfully logged in')

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out')

    return redirect(url_for('home.index'))


@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Email address not found')
            return redirect(url_for('auth.forgot_password'))
        flash('An email sent to you with recover link')
        return redirect(url_for('auth.login'))

    return render_template('auth/forgot_password.html', title='Forgot Password', form=form)
