from app import app,db
from datetime import datetime
from app.models import *


# add admin & users
user=User(id=1,username='admin',fullname='admin',position='admin',email='admin@admin')
user.set_password('admin')
db.session.add(user)

user=User(id=2,username='kanishk',fullname='kanishk',position='ceo',email='kani@kani')
user.set_password('admin')
db.session.add(user)

user=User(id=3,username='karan',fullname='karan',position='cto',email='karan@karan')
user.set_password('admin')
db.session.add(user)

'''
interview=Interview(id=1,title='fmeeting',date=datetime(2018,2,15),startTime=10,endTime=14,duration=4, studentEmail='c@d', bookerEmail='e@f')
db.session.add(interview)
'''

# add students
student=Student(id=1, studentName='stu1', email='stu1@stu1')
db.session.add(student)

student=Student(id=2, studentName='stu2', email='stu2@stu2')
db.session.add(student)

student=Student(id=3, studentName='stu3', email='stu3@stu3')
db.session.add(student)


db.session.commit()