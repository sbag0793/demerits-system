from datetime import datetime
import logging

from flask import Blueprint, render_template, redirect, url_for, request
from system import db
from system.forms import StudentForm, TeacherForm
from system.models import Student, Teacher

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/', methods=('GET', 'POST'))
def index():
  form = StudentForm()
  if request.method == 'POST' and form.validate_on_submit():
    student = Student(grade=form.grade.data, Class=form.Class.data, number=form.number.data)
    # db.session.add(student)
    # db.session.commit()
    form = StudentForm()
    return render_template('register/student_register.html', form=form)
  return render_template('register/student_register.html', tag=4, form=form)