# Getter demonstration

class Employee:
    raise_amount = 1.04  # Class Variable
    empCount = 0  # Class Variable. Each time when we create a new employee we will update this class variable by 1
    def __init__(self,first,last,pay): # We think of __init__() method as the constructor
        self.first=first
        self.last=last
        self.pay=pay

        Employee.empCount += 1

    # Using @property decorator is used as "getter" when we can declare the variables that are dependent and derived from different variables as methods but still can access them as variables.
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'
    
    @property
    def fullName(self):
        return "{} {}".format(self.first,self.last)

emp1 = Employee("Anuj","Kumar",1200000)

print(emp1.first)
print(emp1.fullName) # Accessing fulllName as variable and not as method
print(emp1.email)
print("--------------------------------------------------------------------------------------")

# Now what if we want to change the first name and reflect those changes into email and fullName and also at the same time we know that fullName and email sounds more like a variable and not like a method and hence we want to access it like a variable and not like a method.
emp1.first="Deepak"  # Anuj changed his first name to Deepak
print(emp1.first)
print(emp1.fullName)  # Change can be immediately reflected
print(emp1.email)
print("--------------------------------------------------------------------------------------")

try:
    emp1.fullName = "Manoj Pandey"  # Will throw an error i.e. cant set the attribute. See code2 to see how to resolve
except:
    print("An error occurred...")