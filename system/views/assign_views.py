from flask import Blueprint, url_for, redirect, render_template

bp = Blueprint('assign', __name__, url_prefix='/assign')


@bp.route('/')
def index():
  return render_template('assign/grant.html')