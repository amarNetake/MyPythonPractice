def hello_decorator(func):
    def inner1(*args,**kwargs):
        
        print("Before Execution")

        #Getting the returned value
        returned_value=func(*args,**kwargs)
        print("After Execution")

        #Returning the value to the original frame
        return returned_value
    
    return inner1

@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a+b
# Equivalent to sum_two_numbers = hello_decorator(sum_two_numbers)
a, b= 3, 2

# Getting the value through return of the function
print("Sum = ",sum_two_numbers(a, b))