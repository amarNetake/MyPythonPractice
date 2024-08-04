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

    def __str__(self):
        return "{} ; {}".format(self.getFullName(),self.email)

    def __combinedPay__(self,other):
        return self.pay + other.pay

emp1 = Employee("Amar","Netake",3800000)
emp2 = Employee("Arushi","Sinha",2500000)
print("-----------------------------------------------------------------------------------")

print(emp1) # Now this will instead invoke __str__() default
print("-----------------------------------------------------------------------------------")

print(emp1.__repr__())
print(emp1.__str__())
print(emp1.__combinedPay__(emp2))
print("-----------------------------------------------------------------------------------")