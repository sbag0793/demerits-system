from system import db
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, event
from sqlalchemy.sql.expression import update, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.Boolean, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text(), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id', ondelete='CASCADE'))
    teacher = db.relationship('Teacher', backref=db.backref('event_set', cascade='all, delete-orphan'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
    student = db.relationship('Student', backref=db.backref('event_set', cascade='all, delete-orphan'))
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
    )


class ScoreBoard(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    p_point = db.Column(db.Integer, default=0)
    n_point = db.Column(db.Integer, default=0)


@event.listens_for(Event, 'after_insert')
def update_score(mapper, connection, target):
    if target._type:
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


@event.listens_for(Student, 'after_insert')
def create_board(mapper, connection, target):
    try:
        connection.execute(
            insert(ScoreBoard).values(id=target.id)
        )
    except IntegrityError:
        # Ignore if the scoreboard already exists
        pass