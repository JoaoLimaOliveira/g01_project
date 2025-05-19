"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Student
"""""
# Class Student
# Import the generic class
from classes.gclass import Gclass

class Student(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_student_name','_student_major','_student_email']
    # Class header title
    header = 'Student'
    # field description for use in, for example, input form
    des = ['Id','Name','Major','Email']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, student_name, student_major, student_email):
        super().__init__()
        # Object attributes
        id = Student.get_id(id)
        self._id = id
        self._student_name = student_name
        self._student_major = student_major
        self._student_email = student_email
        # Add the new object to the Student list
        Student.obj[id] = self
        Student.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def student_name(self):
        return self._student_name
    # major property getter method
    @property
    def student_major(self):
        return self._student_major
    # major property setter method
    @student_major.setter
    def student_major(self, major):
        self._student_major = major
    # email property getter method
    @property
    def student_email(self):
        return self._student_email
    # email property setter method
    @student_email.setter
    def student_email(self, email):
        self._student_email = email
