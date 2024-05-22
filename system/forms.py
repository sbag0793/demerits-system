from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length

class StudentForm(FlaskForm):
  # grade = IntegerField('학년', validators=[DataRequired(), NumberRange(min=1, max=3)])
  # Class = IntegerField('반', validators=[DataRequired()])
  # number = IntegerField('번호', validators=[DataRequired()])
  # name = StringField('성명', validators=[DataRequired(), Length(min=1, max=10)])
  grade = IntegerField('학년')
  Class = IntegerField('반')
  number = IntegerField('번호')
  name = StringField('성명')

class TeacherForm(FlaskForm):
  name = StringField('성명', validators=[DataRequired(), Length(min=1, max=10)])
  password = StringField('초기 비밀번호', validators=[DataRequired(), Length(min=8, max=16)])