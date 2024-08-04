# So after 'self' if we want we can specify what other arguments we want to accept.

class Employee:
    def __init__(self,first,last,pay):
        self.first=first # NOTE: We can name instance variables anything i.e. self.fname=first would also work but we generally prefer the prior approach 
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

    def getFullName(self):  # An instance is always passed as one and first argument by default in python so do not forget to add 'self' as the first argument.
        return '{} {}'.format(self.first,self.last)
    
# When we create methods within the class they recieve the instance as the first argument automatically and by convention "we should  call the instance 'self'. "

emp1 = Employee("Amar","Netake",2500000) # So instance is passed automatically and "need not" mention the instance name as first argument
emp2 = Employee("Karan","Singh",1400000) 

#NOTE: first, last, pay, email are instance variables and are specific to each instance
print("-----------------"*5)
print(emp1.pay)
print(emp1.email)
print(emp1.getFullName())

print("-----------------"*5)

print(emp2.pay)
print(emp2.email)
print(emp2.getFullName())
print("-----------------"*5)
