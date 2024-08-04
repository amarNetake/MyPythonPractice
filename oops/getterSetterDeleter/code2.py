
# Setter demonstration

class Employee:
    raise_amount = 1.04   # Class Variable
    empCount = 0          # Class Variable. Each time when we create a new employee we will update this class variable by 1.
    def __init__(self,first,last,pay):
        self.first=first 
        self.last=last
        self.pay=pay
        Employee.empCount +=1

    # getter
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    #getter
    @property
    def fullName(self):
        return "{} {}".format(self.first,self.last)

    #Setter
    @fullName.setter
    def fullName(self,name):
        first, last=name.split(' ')
        self.first=first
        self.last=last

    #Deleter
    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first=None
        self.last=None

emp1 = Employee("Anuj","Kumar",3800000)

print(emp1.first)
print(emp1.fullName)   # Accessing fullName as a variable and not as a method
print(emp1.email)

print("--------------------------------------------------------------------------------------")

# Now what if we want to change the first name and reflect those changes into email and fullName and also at the same time we know that fullName and email sounds more like a variable and not like a method and hence we want to access it like a variable and not like a method.
emp1.first="Deepak"  # Anuj changed his first name to Deepak
print(emp1.first)
print(emp1.fullName)  # Change can be immediately reflected
print(emp1.email)
print("--------------------------------------------------------------------------------------")

emp1.fullName = "Manoj Pandey"

print(emp1.first)
print(emp1.fullName)
print(emp1.email)
print("--------------------------------------------------------------------------------------")

del emp1.fullName
print(emp1.first)
print(emp1.last)
print(emp1.fullName)
print(emp1.email)
print("--------------------------------------------------------------------------------------")