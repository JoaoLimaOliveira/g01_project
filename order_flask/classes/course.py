"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Order
"""""
# Class CustomerOrder
from classes.department import Department
# Import the generic class
from classes.gclass import Gclass

class Course(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_course_name', '_credits', '_departments_id']
    # Class header title
    header = 'Course'
    # field description for use in, for example, input form
    des = ['Id','Name', 'Credits','Departments_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, course_name, credits, departments_id):
        super().__init__()
        # Object attributes
        # Check the customer referential integrity
        try:
            departments_id = int(departments_id)
        except ValueError:
            print(f"Invalid departments_id: {departments_id}")
            return
        if departments_id in Department.lst:
            id = Course.get_id(id)
            self._id = id
            self._course_name = course_name
            self._credits = int(credits)
            self._departments_id = departments_id
            # Add the new object to the Order list
            Course.obj[id] = self
            Course.lst.append(id)
        else:
            print('Department ', departments_id, ' not found')
    # Object properties
    # code property getter method
    @property
    def id(self):
        return self._id
    # date property getter method
    @property
    def course_name(self):
        return self._course_name
    # date property setter method
    @course_name.setter
    def course_name(self, name):
        self._department_name = name
    @property
    def credits(self):
        return self._credits
    # date property setter method
    @credits.setter
    def credits(self, credits):
        self._credits = int(credits)
    # customer property getter method
    @property
    def departments_id(self):
        return self._departments_id
    # customer property setter method
    @departments_id.setter
    def departments_id(self, departments_id):
        if departments_id in Department.lst:
            self._departments_id = departments_id
        else:
            print('Department ', departments_id, ' not found')    
            