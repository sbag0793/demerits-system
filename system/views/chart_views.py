from datetime import datetime
from flask import request, url_for, Blueprint, redirect, render_template

# from system.models import *

bp = Blueprint('chart', __name__, url_prefix='/chart')

@bp.route('/')
def index():
  return render_template('chart/chart_viewer.html')