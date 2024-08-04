# Class Variables: Class Variables are the variables that are shared by all the instances of the class. Class variable will be "SHARED" and the "SAME" for each instance.

# Instance Variables: Instance variables are the variables that are specific to each instance. Instance variables are unique for each instance

# Class variables should be the variables that can be shared by all the instances and not sensitive.
class Employee:
    raise_amount = 1.04  # Class Variable
    empCount = 0         # Class Variable
    def __init__(self,first,last,pay):  # We can think of __init__() method as the constructor
        self.first=first   # first is the instance variable
        self.last=last     # last is the instance variable
        self.pay=pay       # pay is the instance variable
        self.email= f'{first}.{last}@gmail.com'   # email is the instance variable
        Employee.empCount += 1
    
    def getFullName(self):
        return "{} {}".format(self.first,self.last)
    
    def applyRaise(self):
        # self.raise_amount - accessing the raise_amount through object which invoked this message
        # Employee.raise_amount - Accessing the raise_amount class variable.
        # Higher priority is to instance variable of the instance if instance variable also exist with same name if not then the self.raise_amount will access the class variable.
        self.pay = (self.pay * self.raise_amount)
        return self.pay
        # As long as object instance that is pointed by self does not have raise_amount as instance variable it will use the class variable's value and as soon as that instance variable is created specific to that object it will give more priority to that.

    def numOfEmployees(self):
        #NOTE: Here self.empCount would return the same value as Employee.empCount until we create instance variable for object pointed by self explicitly which we do not want here.
        return self.empCount

emp1 = Employee("Amar","Netake",2500000)
emp2 = Employee("Karan","Singh",1400000)
print("-----------------------------------------------------------------------------------------------------------------")
print(emp1.__dict__)   # This will give the dictionary of all the instance variables of emp1 as keys and the corresponding values associated with emp1 as values
print("-----------------------------------------------------------------------------------------------------------------")
print(Employee.__dict__)  # Here you can find the class variable as one of the key value pair

# NOTE: Every instance object first once we try to access any variable look for it's instance variable and if it does not exist then will refer to class variable
# NOTE: We can create instance variable for any instance object at any place in the code.
# NOTE: 2 objects of same class can have different number of instance variables and also may have different names if we create the variables outside the class for those instances.
print("-----------------------------------------------------------------------------------------------------------------")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("salary of emp1 = {}".format(emp1.applyRaise()))
print("salary of emp2 = {}".format(emp2.applyRaise()))
print("-----------------------------------------------------------------------------------------------------------------")
Employee.raise_amount=1.07 # We are updating the class variable and so whoever object that does not have same named instance variable will use this value as raise_amount
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("salary of emp1 = {}".format(emp1.applyRaise()))
print("salary of emp2 = {}".format(emp2.applyRaise()))
print("-----------------------------------------------------------------------------------------------------------------")
emp1.raise_amount=1.05 # NOTE: Here we are not setting/accessing the class variable but instead we created an instance variable named raise_amount specific to emp1.
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)
print(emp2.__dict__)
print("-----------------------------------------------------------------------------------------------------------------")
Employee.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount) # Since above we created an instance variable 'raise_amount' for emp1 it will not access class variable
print(emp2.raise_amount) # emp2 has no instance variable named 'raise_amount' hence it will look for class variable named raise_amount
print("-----------------------------------------------------------------------------------------------------------------")
print(emp1.numOfEmployees())
print(emp2.numOfEmployees())
print(Employee.numOfEmployees(emp1))  # Equivalent to emp1.numOfEmployees()
print(Employee.numOfEmployees(emp2))  # Equivalent to emp2.numOfEmployees()
print(Employee.empCount)