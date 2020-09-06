from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app import db
import sqlite3


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))





@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = BookinterviewForm()
    if form.validate_on_submit():

        # check time collision
        interviewcollisions = Interview.query.filter_by(
            date=datetime.combine(form.date.data, datetime.min.time())).filter_by(studentEmail=form.students.data).all()
        print(len(interviewcollisions))
        for interviewcollision in interviewcollisions:
            # [a, b] overlaps with [x, y] iff b > x and a < y
            if (form.startTime.data < interviewcollision.endTime and (
                    form.startTime.data + form.duration.data) > interviewcollision.startTime):
                flash(
                    f'The time from {interviewcollision.startTime} to {interviewcollision.endTime} is already booked')
                return redirect(url_for('book'))


        endTime = form.startTime.data + form.duration.data

        interview = Interview(title=form.title.data, date=form.date.data, startTime=form.startTime.data, endTime=endTime, duration=form.duration.data, studentEmail=form.students.data, bookerEmail=form.interviewee.data)
        db.session.add(interview)

        db.session.commit()

        flash('Interview Scheduling success!')
        return redirect(url_for('index'))
    return render_template('book.html', title='Schedule Interviews', form=form)




@app.route('/interviewbooker')
def interviewbooker():
    interviews = Interview.query.order_by(Interview.date).all()

    interviewreturns = []
    for interview in interviews:
        interviewreturn = dict()
        interviewreturn['title'] = interview.title
        interviewreturn['studentEmail'] = Student.query.filter_by(email=interview.studentEmail).first().email
        interviewreturn['bookerEmail'] = User.query.filter_by(email=interview.bookerEmail).first().email
        interviewreturn['date'] = interview.date.date()
        interviewreturn['time'] = f'{interview.startTime} to {interview.endTime}'
        interviewreturns.append(interviewreturn)
    return render_template('interviewbooker.html', interviews=interviewreturns)



@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditinterviewForm()
    if form.validate_on_submit():

        # check time collision
        interviewcollisions = Interview.query.filter_by(
            date=datetime.combine(form.date.data, datetime.min.time())).filter_by(studentEmail=form.students.data).all()
        print(len(interviewcollisions))
        for interviewcollision in interviewcollisions:
            # [a, b] overlaps with [x, y] iff b > x and a < y
            if (form.startTime.data < interviewcollision.endTime and (
                    form.startTime.data + form.duration.data) > interviewcollision.startTime):
                flash(
                    f'The time from {interviewcollision.startTime} to {interviewcollision.endTime} is already booked')
                return redirect(url_for('book'))


        endTime = form.startTime.data + form.duration.data

        interview=Interview.query.filter_by(bookerEmail=form.interviewee.data).first()

        interview.title=form.title.data
        interview.date=form.date.data
        interview.startTime=form.startTime.data
        interview.endTime=endTime
        interview.duration=form.duration.data
        interview.studentEmail=form.students.data
        interview.bookerEmail=form.interviewee.data

        db.session.commit()

        flash('Interview Update success!')
        return redirect(url_for('index'))
    return render_template('edit.html', title='Update Interviews', form=form)