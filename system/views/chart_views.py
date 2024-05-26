from datetime import datetime
from flask import request, url_for, Blueprint, redirect

# from system.models import *

bp = Blueprint('chart', __name__, url_prefix='/chart')

@bp.route('/')
def index():
  pass