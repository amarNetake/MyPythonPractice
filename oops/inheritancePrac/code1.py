
class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first 
        self.last=last
        self.pay=pay
        self.email = f"{self.first}.{self.last}@company.com"
    
    def getFullName(self):
        return "{} {}".format(self.first,self.last)
    def applyRaise(self):
        self.pay = self.pay * self.raise_amount

class Developer(Employee):
    pass

developer1 = Developer("Kartik","Surya",1500000) # Since Developer class does not have __init__() method so it follows following order for lookup: current class -> Base class1 -> Base Class2 -> ... -> Built-in class
developer2 = Developer("Yami","Patel",1500000)

print(developer1.email)
print(developer2.email)
print("--------------------------------------------------------------------------------------")
developer1.applyRaise() # developer1 applied for raise in his pay
print(developer1.pay)
print(developer2.pay)
print(developer1.raise_amount)  # developer1 does not have instance variable raise_amount-> developer1 does not have class variable raise_amount hence it will use base class's class variable raise_amount
print(developer2.raise_amount)
print("--------------------------------------------------------------------------------------")
# print(help(developer1))
# Order of resolving is first it will look in current class then if not present then in super class then if not present then that super class's super class and so on and at the end to the built-in