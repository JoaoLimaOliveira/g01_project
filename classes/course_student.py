"""
@author: António Brito / Carlos Bragança (2025)
#objective: class CourseStudent
"""""
# Class CourseStudent
from classes.course import Course
from classes.student import Student
# Import the generic class
from classes.gclass import Gclass

class Course_Student(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_semester','_grade','_student_id','_courses_id']
    # Class header title
    header = 'CourseStudent'
    # field description for use in, for example, input form
    des = ['Id','Courses_id','Student_id','Semester','Grade']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, semester, grade,student_id,courses_id,):
        super().__init__()
        # Object attributes
        # Check the course and student referential integrity
        try:
            courses_id = int(courses_id)
            student_id = int(student_id)
        except ValueError:
            print(f"Invalid course_id or student_id: {courses_id}, {student_id}")
            return
        if courses_id in Course.lst:
            if student_id in Student.lst:
                id = Course_Student.get_id(id)
                self._id = id
                self._courses_id = courses_id
                self._student_id = student_id
                self._semester = semester
                self._grade = grade
                # Add the new object to the CourseStudent list
                Course_Student.obj[id] = self
                Course_Student.lst.append(id)
            else:
                print('student ', student_id, ' not found')
        else:
            print('course ', courses_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # course property getter method
    @property
    def courses_id(self):
        return self._courses_id
    # student property getter method
    @property
    def student_id(self):
        return self._student_id
    # semester property getter method
    @property
    def semester(self):
        return self._semester
    # semester property setter method
    @semester.setter
    def semester(self, semester):
        self._semester = semester
    # grade property getter method
    @property
    def grade(self):
        return self._grade
    # grade property setter method
    @grade.setter
    def grade(self, grade):
        self._grade = grade
        