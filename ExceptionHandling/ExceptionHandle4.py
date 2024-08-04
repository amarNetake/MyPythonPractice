# DEMONSTRATION OF FINALLY BLOCK :-

# try:
#     # Some code
# except:
#     # optional block
#     # Handling of exception (if required)
# else:
#     # Execute if no exception
# finally:
#     # Some code .....(always executed)

# Python provides a keyword 'finally', which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exception.

# No exception raised in try block
try:
    k=5//0  # Raises divide by zero exception
    print(k)
# handles zeroDivision exception
except ZeroDivisionError:
    print("Can't divide by zero...")
finally:
    # this block is always executed
    # regardless of exception generation.
    print("This is always executed...")

print("******************NORMAL FLOW OF PROGRAM CONTINUES******************")