from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, PasswordField, BooleanField, FormField, DateTimeField, HiddenField, RadioField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo

data_required_msg = '데이터를 작성해주십시오.'
class StudentForm(FlaskForm):
  grade = IntegerField('학년', validators=[DataRequired(message=data_required_msg), NumberRange(min=1, max=3)])
  Class = IntegerField('반', validators=[DataRequired(message=data_required_msg)])
  number = IntegerField('번호', validators=[DataRequired(message=data_required_msg)])
  name = StringField('성명', validators=[DataRequired(message=data_required_msg)])
  # grade = IntegerField('학년')
  # Class = IntegerField('반')
  # number = IntegerField('번호')
  # name = StringField('성명')

class TeacherForm(FlaskForm):
  account = StringField('로그인 ID', validators=[DataRequired(message=data_required_msg), Length(min=4, max=10, message='ID는 4자 이상, 10자 이하로 작성해주십시오')])
  password1 = PasswordField('비밀번호', validators=[DataRequired(message=data_required_msg), Length(min=8, max=16, message='비밀번호는 8자 이상, 16자 이하로 작성해주십시오'), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
  password2 = PasswordField('비밀번호확인', validators=[DataRequired(message=data_required_msg)])
  point = IntegerField('초기포인트', validators=[DataRequired(message=data_required_msg), NumberRange(min=0, max=100, message='초기포인트는 0 이상 100 이하로 설정하십시오.')])
  name = StringField('성명', validators=[DataRequired(message=data_required_msg)])

class RequestStudents(FlaskForm):
  grade = IntegerField('학년', validators=[DataRequired(message=data_required_msg), NumberRange(min=1, max=3)])
  Class = IntegerField('반', validators=[DataRequired(message=data_required_msg)])

class GrantScore(FlaskForm):
  type = RadioField('Type', choices=[('True', '상점'), ('False', '벌점')], validators=[DataRequired(message=data_required_msg)])
  score = IntegerField('점수', validators=[DataRequired(message=data_required_msg)])
  reason = SelectField('Reason', choices=[], validators=[DataRequired(message=data_required_msg)])
  teacherId = HiddenField('Teacher', validators=[DataRequired(message=data_required_msg)])
  studentIds = HiddenField('Student', validators=[DataRequired(message=data_required_msg)])
  event_date = DateTimeField('날짜')