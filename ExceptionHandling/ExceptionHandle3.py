# Demonstration of Try-Except-Else block

# In python you can also use else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

def func(a, b):
    try:
        c = (a+b)/(a-b)
    except ZeroDivisionError:
        print("ZeroDivisionError occurred...")
    else:
        print(c)  # Else block gets executed every time when try block successfully executes without any error.
    
# Driver program to test above function
print("-------------------"*4)

func(2.0,3.0)
print("-------------------"*4)

func(3.0,3.0)
print("-------------------"*4)

print("Normal flow of program remains intact... Yeeeyyyy")
print("-------------------"*4)    

