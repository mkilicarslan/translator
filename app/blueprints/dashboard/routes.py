from flask import render_template, flash, redirect, url_for, request
from app import db
from . import bp


@bp.route('/')
def dashboard():
    return render_template('dashboard/dashboard.html')
