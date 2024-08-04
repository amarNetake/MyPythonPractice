
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
    raise_amount = 1.2

developer1 = Employee("Kartik","Surya",1500000)
developer2 = Developer("Yami","Patel",1500000)

print(developer1.email)
print(developer2.email)
print(developer1.raise_amount)
print(developer2.raise_amount)
print("--------------------------------------------------------------------------------------")
developer1.applyRaise()   # developer1 applied for raise in his salary
# developer1 is an object of Employee class so it will use raise_amount already defined in Employee class to compute applyRaise()

developer2.applyRaise()   # developer2 applied for raise in his salary
# Developer2 is an object of Developer class so it will use raise_amount already defined in developer class to compute the applyRaise() defined in it's base class Employee. as it does not have applyRaise() function defined in Developer class.

print(developer1.pay)
print(developer2.pay)
print("--------------------------------------------------------------------------------------")