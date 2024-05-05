from sqlalchemy import func, desc, select, and_
from db_struct import Grade, Teacher, Student, Group, Subject
from seed import session

def select_1():
    return (
    session.query(
        Student.name.label('student_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade'),
        Student.id
    )
    .join(Grade, Student.id == Grade.student_id)
    .group_by(Student.id, Student.name, Student.id)
    .order_by(func.avg(Grade.grade).desc())
    .limit(5)
    .all()
)
  
def select_2(subject_id=1):
    return (session.query(
        Student.name.label('student_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade'),
        Subject.name.label("subject_name")
    )
    .join(Grade, Student.id == Grade.student_id)
    .join(Subject, Grade.subject_id == Subject.id )
    .filter(Grade.subject_id == subject_id)
    .group_by(Student.id, Student.name, Subject.id, Subject.name)
    .order_by(func.avg(Grade.grade).desc())
    .limit(1)
    .all()
    )

def select_3(subject_id=1):
    return ( session.query(
        Group.name.label('group_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade'),
    )
    .join(Student, Group.id == Student.group_id)
    .join(Grade, Student.id == Grade.student_id )
    .filter(Grade.subject_id == subject_id)
    .group_by(Group.name, Group.id)
    .order_by(Group.name)
    .all()
    )

def select_4():
    return(session.query(
        func.round(func.avg(Grade.grade), 2).label('average_grade'),
    )
    .order_by(func.avg(Grade.grade).desc())
    .all()
    )

def select_5(teacher_id=1):
    return (session.query(Subject.name.label("Subject_name"))
    .filter(Subject.teacher_id == teacher_id)
    .all()
    )

def select_6(group_id=1):
    return(session.query(Student.name.label("Students"))
    .filter(Student.group_id == group_id)
    .all())

def select_7(group_id=1):
    return(session.query(Subject.name.label('subject'), Grade.grade.label('grades'))
    .join(Grade, Subject.id == Grade.subject_id)
    .join(Student, Grade.student_id == Student.id)
    .filter(Student.group_id == group_id)
    .group_by(Subject.id, Grade.grade)
    .all())

def select_8():
    return(session.query(Teacher.name.label('teacher_name'),
    func.round(func.avg(Grade.grade), 2).label('average_grade'))
    .join(Subject, Teacher.id == Subject.teacher_id)
    .join(Grade, Subject.id == Grade.subject_id)
    .group_by(Teacher.id, Teacher.name)
    .all())

def select_9(student_id=1):
    return(session.query(Subject.name.label('subjects'))
    .join(Grade, Subject.id == Grade.subject_id)
    .join(Student, Grade.student_id == Student.id)
    .filter(Grade.subject_id == student_id)
    .distinct()
    .all())

def select_10(student_id=1, teacher_id=1):
    return(session.query(Subject.name.label('subject'))
    .join(Grade, Subject.id == Grade.subject_id)
    .join(Student, Grade.student_id == Student.id)
    .filter(and_(Student.id == student_id, Subject.teacher_id == teacher_id))
    .distinct()
    .all())
