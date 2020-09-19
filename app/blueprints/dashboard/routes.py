from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user

from app import db
from . import bp


@bp.route('/')
def dashboard():
    latest_translations = current_user.get_latest_translations(15)
    return render_template('dashboard/dashboard.html', latest_translations=latest_translations, user=current_user)
