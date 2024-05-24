from system import db
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, event
from sqlalchemy.sql.expression import update


# 데이터 입력 시 외래키는 입력 X, 해당하는 객체만 입력
class Event(db.Model):
  id = db.Column(db.Integer)
  positive = db.Column(db.Boolean) #
  negative = db.Column(db.Boolean) #
  score = db.Column(db.Integer, nullable=False) #
  reason = db.Column(db.Text(), nullable=False) #
  teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id', ondelete='CASCADE'))
  teacher = db.relationship('Teacher', backref=db.backref('event_set', cascade='all, delete-orphan')) #
  student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
  student = db.relationship('Student', backref=db.backref('event_set', cascade='all, delete-orphan')) #
  event_date = db.Column(db.DateTime(), nullable=False) #
  __table_args__ = (
    PrimaryKeyConstraint(id),
    {}
  )

class Teacher(db.Model):
  id = db.Column(db.Integer)
  account = db.Column(db.String(62), nullable=False, unique=True)
  password = db.Column(db.String(50))
  point = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(30), nullable=False)
  __table_args__ = (
    PrimaryKeyConstraint(id),
  )

class Student(db.Model):
  id = db.Column(db.Integer)
  grade = db.Column(db.Integer, nullable=False)
  Class = db.Column(db.Integer, nullable=False)
  number = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(30), nullable=False)
  __table_args__ = (
        UniqueConstraint(grade, Class, number),
        PrimaryKeyConstraint(id),
    )

class ScoreBoard(db.Model):
  id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
  p_point = db.Column(db.Integer)
  n_point = db.Column(db.Integer)
  __table_args__ = (
    PrimaryKeyConstraint(id),
    {}
  )

@event.listens_for(Event, 'after_update')
def update_score(mapper, connection, target):
    student = target.student
    if target.positive:
        connection.execute(
            update(ScoreBoard)
            .where(ScoreBoard.id == target.student_id)
            .values(p_point=ScoreBoard.p_point + target.score)
        )
    else:
        connection.execute(
            update(ScoreBoard)
            .where(ScoreBoard.id == target.student_id)
            .values(n_point=ScoreBoard.n_point + target.score)
        )

@event.listens_for(Student, 'after_update')
def create_board(mapper, connection, target):
    # 해당 target.id에 대한 ScoreBoard 레코드가 있는지 확인합니다.
    existing_scoreboard = ScoreBoard.query.get(target.id)
    if not existing_scoreboard:
        # 해당 target.id에 대한 ScoreBoard 레코드가 없으면 새로 생성합니다.
        sb = ScoreBoard(id=target.id)
        db.session.add(sb)
        db.session.commit()