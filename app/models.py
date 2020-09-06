from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    fullname = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    position = db.Column(db.String(64), nullable=False)
    email=db.Column(db.String(64), nullable=False, unique=True)
    interviews = db.relationship('Interview', backref='booker', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    studentName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    interviews = db.relationship('Interview', backref='student', lazy='dynamic')

    def __repr__(self):
        return f'Student {self.studentName}'


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(64), nullable=False, unique=True)
    date = db.Column(db.DateTime, nullable=False)
    startTime = db.Column(db.Integer, nullable=False)
    endTime = db.Column(db.Integer, nullable=False)  # should be calculated with startTime and duration
    duration = db.Column(db.Integer, nullable=False)
    studentEmail = db.Column(db.String(64), db.ForeignKey('student.email'))
    bookerEmail = db.Column(db.String(64), db.ForeignKey('user.email'))

    def __repr__(self):
        return f'Interview {self.id} for {self.id} last for {self.duration}'