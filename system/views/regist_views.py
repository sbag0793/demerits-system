from datetime import datetime
import logging

from flask import Blueprint, render_template, redirect, url_for, request
from system import db
from system.forms import StudentForm, TeacherForm
from system.models import Student, Teacher

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/')
def index():
  return redirect(url_for('register.student'))

@bp.route('/student', methods=('GET', 'POST'))
def student():
  form = StudentForm()
  student_list = Student.query.order_by(Student.id.desc()).all()

  if request.method == 'POST' and form.validate_on_submit():
    student = Student(grade=form.grade.data, Class=form.Class.data, number=form.number.data, name=form.name.data)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('register.student'))
  return render_template('register/student_register.html', form=form, student_list=student_list)

@bp.route('/teacher', methods=('GET', 'POST'))
def teacher():
  form = TeacherForm()
  if Teacher.query.all():
    teacher_list = Student.query.order_by(Teacher.id.desc()).all()
  else:
    teacher_list = []

  if request.method == 'POST' and form.validate_on_submit():
    teacher = Teacher(id=form.id.data, name=form.name.data, password=form.password.data, point=form.point.data)
    db.session.add(teacher)
    db.session.commit()
    return redirect(url_for('register.teacher'))
  return render_template('register/teacher_register.html', form=form, teacher_list=teacher_list)