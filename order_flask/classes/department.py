# Class Customer_login
# Import the generic class
from classes.gclass import Gclass

class Department(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_department_name','_dep_building']
    # Class header title
    header = 'Department'
    # field description for use in, for example, input form
    des = ['Id','Name','Building']
    # Constructor: Called when an object is instantieated
    def __init__(self,id,department_name,dep_building):
        super().__init__()
        # Object attributes
        id = Department.get_id(id)
        self._id = id
        self._department_name = department_name
        self._dep_building = dep_building
        # Add the new object to the Customer's list
        Department.obj[id] = self
        Department.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def department_name(self):
        return self._name
    # name property setter method
    @department_name.setter
    def department_name(self, name):
        self._name = name
    # address property getter method
    @property
    def dep_building(self):
        return self._dep_building
    # address property setter method
    @dep_building.setter
    def dep_building(self, building):
        self._dep_building = building