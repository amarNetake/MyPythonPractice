
class Employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= f'{self.first}.{self.last}@company.com'

    def getFullName(self):
        return "{} {}".format(self.first,self.last)
    def applyRaise(self):
        self.pay = self.pay * self.raise_amount
    
class Developer(Employee):
    raise_amount = 1.2
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_Emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_Emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_Emp(self):
        for emp in self.employees:
            print(emp.getFullName(),end=" # ")

developer1 = Developer("Kartik","Surya",1500000,"Python")
developer2 = Developer("Yami","Patel",1500000,"Java")
developer3 = Developer("Jayesh","Singh",1800000,'Python')
developer4 = Developer("Raghav","Negi",1600000,"Java")
developer5 = Developer("Monica","Sharma",1100000,"Python")
developer6 = Developer("Aradhya","Trivedi",1000000,"Java")

manager1 = Manager("Amar","Netake",3800000,[developer1,developer4,developer5])
manager2 = Manager("Yashasvi","Sinha",2700000,[developer3])
print("----------------------------------------------------------------------------------------------")

manager1.print_Emp()
print()
manager2.print_Emp()
print()
print("----------------------------------------------------------------------------------------------")

manager1.add_Emp(developer6)
manager2.add_Emp(developer5)
manager1.print_Emp()
print()
manager2.print_Emp()
print()
print("----------------------------------------------------------------------------------------------")

manager1.remove_Emp(developer1)
manager1.print_Emp()
print()
manager2.print_Emp()
print()
print("----------------------------------------------------------------------------------------------")

print(isinstance(manager1,Manager))
print(isinstance(manager1,Employee))
print(isinstance(manager1,Developer))
print("----------------------------------------------------------------------------------------------")

print(issubclass(Developer,Manager))
print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))
print(issubclass(Manager,Employee))
print(issubclass(Employee,Employee))
print(issubclass(Employee,Manager))
print(issubclass(Employee,Developer))
print("----------------------------------------------------------------------------------------------")