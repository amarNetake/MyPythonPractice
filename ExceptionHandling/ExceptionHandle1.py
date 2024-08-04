
A = [10,20,30]
# List index out of range exception which we caught and this helped to keep the regular flow of the program running.
try:
    print(f"Second element in A is {A[1]}")

    # Throws error since there are only 3 elements in an array
    print(f"Third element in A is {A[3]}")
except:
    print("An error occurred...You tried to access list index out of range...")

print("The control reached below the point where error occurred!!! Hurray")

try:
    print(3/0) 
except:
    print("Error occurred...")

print("Hi! I am Amar")

