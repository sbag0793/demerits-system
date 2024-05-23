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

  # POST 요청
  if request.method == 'POST' and form.validate_on_submit():
    student = Student(
      grade=form.grade.data,
      Class=form.Class.data,
      number=form.number.data,
      name=form.name.data
      )
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('register.student'))
  # 오류 반환
  elif not form.validate_on_submit():
    error_list = form.errors
    form = StudentForm()
    return render_template('register/student_register.html', form=form, student_list=student_list, error_list=error_list)
  # GET 요청
  else:
    return render_template('register/student_register.html', form=form, student_list=student_list)

@bp.route('/teacher', methods=('GET', 'POST'))
def teacher():
  form = TeacherForm()
  teacher_list = Teacher.query.order_by(Teacher.id.desc()).all()

  # POST 요청
  if request.method == 'POST' and form.validate_on_submit():
    teacher = Teacher(
      account=form.account.data,
      password=form.password1.data,
      point=form.point.data,
      name=form.name.data
      )
    db.session.add(teacher)
    db.session.commit()
    return redirect(url_for('register.teacher'))
  # 오류 반환
  elif not form.validate_on_submit():
    error_list = form.errors
    form = TeacherForm()
    return render_template('register/teacher_register.html', form=form, teacher_list=teacher_list, error_list=error_list)
  # GET 요청
  else:
    return render_template('register/teacher_register.html', form=form, teacher_list=teacher_list)