# Python object oriented programming

# Smallest class code without an error
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

# Both emp1 and emp2 are unique instances of Employee class
print(emp1)
print(emp2)


# -----------------------------------------------------------------------------------------------------------
# NOTE: Following way of doing things is not the best practice of instantiating instance variables.
#       Instance variables contains data that is unique to each instance of a class.
emp1.first = 'Amar'
emp1.last = 'Netake'
emp1.email = 'amarnetake@gmail.com'
emp1.salary = 2500000

emp2.first = "Jayesh"
emp2.last = "Sinha"
emp2.email = 'jayesh.sinha@gmail.com'
emp2.age = 14

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.salary)

print("---------------------------"*3)

print(emp2.first)
print(emp2.last)
print(emp2.email)
print(emp2.age)

print("---------------------------"*3)
print(dir(emp1)) # you will find email, first, last and salary here as it's attributes of object emp1

print("---------------------------"*3)
print(dir(emp2)) # you will find email, first, last and age here as it's attributes of object emp2
print("---------------------------"*3)
# Here all are instance variables but it is not a good way to make instance variables.