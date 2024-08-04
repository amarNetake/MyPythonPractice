# Raising standard exception

try:
    raise NameError("Hi There")  # Raise Error
except NameError:
    print("An Exception")
    #raise # To determine whether the exception was raised or not

print("---------------------"*4)

print("Normal flow of program sustained...")
print("---------------------"*4)