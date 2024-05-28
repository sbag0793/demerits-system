from flask import Blueprint, render_template, redirect, url_for, request
from system.models import Event

bp = Blueprint('main', __name__, url_prefix='/')

reason_list = [
  '학급에 봉사함',
  '성실하게 청소함',
  '아침 일찍 등교함',
  '자발적으로 헌혈을 함',
  '발표에 성실하게 참여함',
  '행복을 위해 노력함',
  '꾸준하게 자기계발을 함'
]


@bp.route('/', methods=('POST', 'GET'))
def index():
  event_list = list(reversed(Event.query.all()))
  return render_template('main/index.html', event_list=event_list, reason_list=reason_list)