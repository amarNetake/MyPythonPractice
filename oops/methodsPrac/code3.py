# Static methods are just like regular functions inside of the class and is not associated with object instances nor with classes.
# It neither recieves object instance nor class as default first argument.
# The function that has logical connection to an employee class but is not dependent on object instance or class should be static.

class Employee:
    empCount = 0
    raiseAmount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first,self.last)
        Employee.empCount += 1

    # Regular Method
    def getFullName(self):
        return "{} {}".format(self.first,self.last)
    
    #Regular Method
    def applyRaise(self):
        self.pay = self.pay * self.raiseAmount

    # class method used as an alternative constructor to create an instance of an object
    @classmethod
    def fromString(cls,empStr):
        first, last, pay = empStr.split('#')
        return cls(first,last,pay)  # Same as Employee(first,last,pay) so will invoke __init__() and return an employee object instance

    # class method used as an alternative constructor to create an instance of an object
    @classmethod
    def fromStringRev(cls,revEmpStr):
        pay, last, first=revEmpStr.split('@')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if(day%7==5 or day%7==6):
            return False
        else:
            return True

emp1 = Employee("Amar", "Netake", 4800000)
emp2 = Employee("Arushi","Sinha",1900000)

import datetime
day = datetime.datetime.today().weekday() # 0->Monday; 1->Tuesday; ... ;6->Sunday
print(Employee.is_workday(day))