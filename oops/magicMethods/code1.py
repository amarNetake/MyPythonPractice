# Special/Magic methods: These methods helps us to emulate some built-in behaviours  in python and also it's how we implement operator overloading

# Example of operator overloading
print(1 + 2) # Prints 3
print('1' + '2') # Prints 12

class Employee:
    raise_amount = 1.04  # Class Variable
    empCount = 0  # Each time when we create a new employee we will update this class variable by 1.
    def __init__(self,first,last,pay):   # We can think of __init__() method as the constructor
        self.first=first
        self.last=last
        self.pay=pay
        self.email = f"{self.first}.{self.last}@company.com"
        Employee.empCount += 1

emp1 = Employee("Amar","Netake",2500000)
print(emp1) # This will print some weird thing that is not much meaningful and utilized only will get to know the classs of this object

# So we can use a special method __repr__() that is invoked automatically when you print the object and is more meaningful and can be directly used to create object.
# See Code2 for demo of magic methods

