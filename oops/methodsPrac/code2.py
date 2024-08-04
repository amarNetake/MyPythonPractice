# Class methods can be used as the alternative constructors.

class Employee:
    empCount = 0
    raiseAmount = 1.04

    # Constructor which also happens to be a Regular method
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first,self.last)
        Employee.empCount += 1

    # Regular method
    def getFullName(self):
        return f"{self.first} {self.last}"

    # Regular method
    def applyRaise(self):
        self.pay = self.pay * self.raiseAmount
    
    #Class Method
    @classmethod
    def setRaiseAmount(cls,newRaise):
        cls.raiseAmount=newRaise  # cls.raiseAmount inside the class method is equivalent to writing Employee.raiseAmount outside of class

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

emp1 = Employee("Amar","Netake",4800000)
emp2 = Employee("Arushi","Sinha",3000000)
print("----------------------------------------------------------------------------------------------------")

print(emp1.email)
print(emp2.email)
print(Employee.empCount)
print("----------------------------------------------------------------------------------------------------")
# Suppose we are also getting new employee details in string format separated by '#' so we need to make another type of constructor  which will take this input format and create an instance object catching all the details.
emp3 = Employee.fromString("Suresh#Jain#1200000")
emp4 = Employee.fromString("Hari#Singh#800000")
print(emp3.email)
print(emp4.email)
print(Employee.empCount)
print("----------------------------------------------------------------------------------------------------")

# Suppose we are also getting new employee details in string format separated by '@' and in order with first pay then last name then first name. So, we need to make another type of constructor which will take this input format and create an instance object catching all the details.
emp5 = Employee.fromStringRev("1050000@Bansal@Karan")
emp6 = Employee.fromStringRev("650000@Kumari@Yashasvi")
print(emp5.email)
print(emp6.email)
print(Employee.empCount)
print("----------------------------------------------------------------------------------------------------")