from system import db
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint


# 데이터 입력 시 외래키는 입력 X, 해당하는 객체만 입력
class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  Type = db.Column(db.String(10), nullable=False) #
  score = db.Column(db.Integer, nullable=False) #
  reason = db.Column(db.Text(), nullable=False) #
  teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id', ondelete='CASCADE'))
  teacher = db.relationship('Teacher', backref=db.backref('event_set', cascade='all, delete-orphan'))
  student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
  student = db.relationship('Student', backref=db.backref('event_set', cascade='all, delete-orphan')) #
  event_date = db.Column(db.DateTime(), nullable=False)

class Teacher(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  account = db.Column(db.String(62), nullable=False, unique=True)
  password = db.Column(db.String(50))
  point = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(30), nullable=False)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  grade = db.Column(db.Integer, nullable=False)
  Class = db.Column(db.Integer, nullable=False)
  number = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(30), nullable=False)
  __table_args__ = (
        UniqueConstraint(grade, Class, number),
        {},
    )