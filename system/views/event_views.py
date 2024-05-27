from datetime import datetime
import logging

from flask import Blueprint, render_template, redirect, url_for, request
from system import db
from system.models import Student, Event, Teacher
from system.forms import RequestStudents, GrantScore
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
  # 학생 검색
  if request.method == 'POST' and 'requestStudents' in request.form:
    error_list = form.errors
    student_list = Student.query.filter_by(
      grade=form.grade.data,
      Class=form.Class.data
    ).all()
    return render_template('event/event.html', reason_list=reason_list, student_list=student_list, error_list=error_list)
  # 이벤트 생성
  elif request.method == 'POST' and 'grantScore' in request.form:
    error_list = form.errors
    form = GrantScore()
    event = Event(
      _type = bool(form.type.data),
      score = form.score.data,
      reason = int(form.reason.data),
      teacher = Teacher.query.get(form.teacher.data),
      student = Student.query.get(form.student.data),
      event_date = datetime.now()
    )
    db.session.add(event)
    db.session.commit()
    return redirect(url_for('event.index'))
  # GET 요청
  else:
    error_list = []
    return render_template('event/event.html', reason_list=reason_list, form=form, a=form.validate_on_submit(), error_list=error_list)