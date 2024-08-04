
import logging

logging.basicConfig(filename='loggingPrac/logs/loggingPrac2.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info(f'Created an employee {self.fullName} whose email id is: {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullName(self):
        return f'{self.first} {self.last}'


emp_1 = Employee("Amar","Netake")
emp_2 = Employee("Karan","Sinha")
emp_3 = Employee("Yash","Jaypal")