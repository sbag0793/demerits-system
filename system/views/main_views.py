from flask import Blueprint, render_template, redirect, url_for, request
from system.models import Event

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('POST', 'GET'))
def index():
  event_list = Event.query.all()
  return render_template('main/index.html', event_list=event_list)