# NOTE: There are 3 types of methods in OOPs
# Regular methods -- Methods associated with an instance. Takes instance as the first/default argument. i.e. func(self,...)

# Class methods -- Method associated with class and not instance. We simply add decorator '@classmethod' to declare it to be a class method.

# Static methods -- Methods inside of class that are neither associated with object instances nor with the class. 
# Static methods DO NOT recieve instance of object or class as first parameter. 

class Employee:
    numOfEmployees = 0
    raiseAmount = 1.04

    # Constructor which also happens to be a Regular method
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first,self.last)
        Employee.numOfEmployees += 1

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

emp1 = Employee("Amar","Netake",3800000)
emp2 = Employee("Arushi","Sharma",2200000)

print("-------------------------------------------------------------------------------------------------")

print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(Employee.raiseAmount)
print("-------------------------------------------------------------------------------------------------")

Employee.setRaiseAmount(1.07) # Calling the class method which will pass class as the first argument.
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(Employee.raiseAmount)
print("-------------------------------------------------------------------------------------------------")

emp1.setRaiseAmount(1.06)  # We can access the class method using object instance also but the default first argument passed will still remain to be class.
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(Employee.raiseAmount)
print("-------------------------------------------------------------------------------------------------")