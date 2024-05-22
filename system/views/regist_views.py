from flask import Blueprint, render_template, redirect, url_for
from system.forms import StudentForm, TeacherForm

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/')
def index():
  form = StudentForm()
  return render_template('register/student_register.html', form=form)