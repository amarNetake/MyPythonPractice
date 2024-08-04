import logging

# We have 5 standard logging levels:
# 1. DEBUG : Detailed information, typically of interest only when diagnosing problems.
# 2. INFO : Confirmation that things are working as expected.
# 3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future(e.g., disk space  low). The software is still working as expected.

# 4. ERROR : Due to a more serious problem, the software has not been able to perform certain function.
# 5. CRITICAL : A serious error, indicating that the program itself may be unable to continue running.

# Default level of logging is WARNING. What this means is it will capture everything that is a WARNING or above. So by default it will log WARNING, ERROR and CRITICAL which means by default it will ignore DEBUG and INFO log statements.

logging.basicConfig(filename='loggingPrac/logs/loggingPrac1.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') 
# different formats are available in : https://docs.python.org/3/library/logging.html#logrecord-attributes
# logging.DEBUG is a constant with value 10 
# logging.INFO is a constant with value 20 
# logging.WARNING is a constant with value 30 
# logging.ERROR is a constant with value 40 
# logging.CRITICAL is a constant with value 50 

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

num_1 = 20
num_2 = 10

add_result = add(num_1,num_2)
logging.debug(f'{num_1} + {num_2} = {add_result}')  # Since default logging level is WARNING(i.e. will log anything WARNING and higher) it will not log anything.

subtract_result = subtract(num_1,num_2)
logging.debug(f'{num_1} - {num_2} = {subtract_result}')  # Since default logging level is WARNING(i.e. will log anything WARNING and higher) it will not log anything.

multiply_result = multiply(num_1,num_2)
logging.debug(f'{num_1} * {num_2} = {multiply_result}') # Since default logging level is WARNING(i.e. will log anything WARNING and higher) it will not log anything.

divide_result = divide(num_1,num_2)
logging.debug(f'{num_1} / {num_2} = {divide_result}')  # Since default logging level is WARNING(i.e. will log anything WARNING and higher) it will not log anything.

