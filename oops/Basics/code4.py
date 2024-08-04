class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= f"{first}.{last}@gmail.com"
    
    def getFullName(self):
        return "{} {}".format(self.first,self.last)
    
# When we create methods within a class they recieve the instance as the first argument automatically and by convention "we should" call the instance 'self'
emp1 = Employee("Amar","Netake",2500000) # So instance is passed automatically and "need not" mention the instance name as first argument
emp2 = Employee("Karan","Singh",1400000)

print(emp2.getFullName())
print(Employee.getFullName(emp2))

# emp1.getFullName() is same as Employee.getFullName(emp1)
x=13
print(id(x))
y=13
print(id(y))
#NOTE: first, last, pay, email are instance variables and are specific to each instance
x=15
print(id(x))
print(id(y))