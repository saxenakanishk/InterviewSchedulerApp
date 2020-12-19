from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, \
    SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_login import current_user
from app.models import *
import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class BookinterviewForm(FlaskForm):
    title = StringField('Interview title', validators=[DataRequired()])
    students = StringField('Student email', validators=[DataRequired()])
    interviewee= StringField('Interviewers Email', validators=[DataRequired()] )
    date = DateField('Choose date', format="%m/%d/%Y", validators=[DataRequired()])
    startTime = SelectField('Choose starting time(in 24hr expression)', coerce=int,
                            choices=[(i, i) for i in range(7, 20)])
    duration = SelectField('Choose duration of the interview(in hours)', coerce=int,
                           choices=[(i, i) for i in range(1, 6)])


    submit = SubmitField('Book')

    def validate_title(self, title):
        interview = Interview.query.filter_by(title=self.title.data).first()
        if interview is not None:  # username exist
            raise ValidationError('Please use another interview title.')

    def validate_students(self, students):
        s = Student.query.filter_by(email=self.students.data).first()
        if s is None:
            raise ValidationError("Email id is not present in the database")

    def validate_interviewee(self, interviewee):
        i = User.query.filter_by(email=self.interviewee.data).first()
        if i is None:
            raise ValidationError("Email id is not present in the database")

    def validate_date(self, date):
        if self.date.data < datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')




class EditinterviewForm(FlaskForm):
    title = StringField('Interview title', validators=[DataRequired()])
    students = StringField('Student email', validators=[DataRequired()])
    interviewee= StringField('Interviewers Email', validators=[DataRequired()] )
    date = DateField('Choose date', format="%m/%d/%Y", validators=[DataRequired()])
    startTime = SelectField('Choose starting time(in 24hr expression)', coerce=int,
                            choices=[(i, i) for i in range(9, 19)])
    duration = SelectField('Choose duration of the interview(in hours)', coerce=int,
                           choices=[(i, i) for i in range(1, 6)])


    submit = SubmitField('Edit')

    '''
    def validate_title(self, title):
        interview = Interview.query.filter_by(title=self.title.data).first()
        if interview is not None:  # username exist
            raise ValidationError('Please use another interview title.')
    '''

    def validate_students(self, students):
        s = Student.query.filter_by(email=self.students.data).first()
        if s is None:
            raise ValidationError("Email id is not present in the database")

    def validate_interviewee(self, interviewee):
        i = User.query.filter_by(email=self.interviewee.data).first()
        if i is None:
            raise ValidationError("Email id is not present in the database")

    def validate_date(self, date):
        if self.date.data < datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')