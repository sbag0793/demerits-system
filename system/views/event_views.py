from datetime import datetime
import logging

from flask import Blueprint, render_template, redirect, url_for, request
from system import db
from system.models import Student
from system.forms import RequestStudents
# from system.forms import 

bp = Blueprint('event', __name__, url_prefix='/event')
reason_list = [
  '학급에 봉사함',
  '성실하게 청소함',
  '아침 일찍 등교함',
  '자발적으로 헌혈을 함',
  '발표에 성실하게 참여함',
  '행복을 위해 노력함',
  '꾸준하게 자기계발을 함'
]

@bp.route('/', methods=('GET', 'POST'))
def index():
  form = RequestStudents()
  if request.method == 'POST':
    student_list = Student.query.filter_by(
      grade=form.grade.data,
      Class=form.Class.data
    ).all()
    return render_template('event/event.html', reason_list=reason_list, student_list=student_list, a=form.validate_on_submit())
  else:
    return render_template('event/event.html', reason_list=reason_list, form=form, a=form.validate_on_submit())