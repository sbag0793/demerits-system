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
    student = Student(grade=form.grade.data, Class=form.Class.data, number=form.number.data, name=form.name.data)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('register.index'), code=302)
  student_list = Student.query.order_by(Student.id.desc()).all()
  return render_template('register/student_register.html', form=form, student_list=student_list)