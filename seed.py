from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_struct import Student, Group, Teacher, Subject, Grade, DATABASE_URL
from random import randint

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20


fake = Faker()


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=fake.word()) for _ in range(NUMBER_GROUPS)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range (NUMBER_TEACHERS)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(),teacher_id = randint(1, NUMBER_TEACHERS)) for _ in range(NUMBER_SUBJECTS)] 
session.add_all(subjects)
session.commit()

students = []
for _ in range(NUMBER_STUDENTS):
    student = Student(name=fake.name(), group_id = randint(1, NUMBER_GROUPS))
    session.add(student)
    session.commit()
    students.append(student)

for student in students:
    for _ in range(NUMBER_GRADES):
        grade = randint(1,100)
        date= fake.date_this_year()
        subject_id = randint(1, NUMBER_SUBJECTS)
        grade = Grade(student_id = student.id, subject_id = subject_id, grade = grade, date = date)
        session.add(grade)


session.commit()
