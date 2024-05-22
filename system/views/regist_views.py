from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('regist', __name__, url_prefix='/regist')


@bp.route('/')
def index():
  return render_template('regist/student_register.html', test='test')
