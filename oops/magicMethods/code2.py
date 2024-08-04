
class Employee:
    raise_amount = 1.04  # Class Variable
    empCount = 0  # Each time when we create a new employee we will update this class variable by 1.
    def __init__(self,first,last,pay):   # We can think of __init__() method as the constructor
        self.first=first  # Instance variable
        self.last=last    # Instance variable
        self.pay=pay      # Instance variable
        self.email = f"{self.first}.{self.last}@company.com"   # Instance variable
        Employee.empCount += 1

    def getFullName(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return "Employee({},{},{})".format(self.first,self.last,self.pay)

emp1 = Employee("Amar","Netake",2500000)
print(emp1) # This will invoke  __repr__ automatically and give much better object structure that can be directly used to generate a new object of that type.

