# First-class functions allow us to treat functions like any other object.

# So, for example, we can pass functions as arguments to another function. We can return functions and we can assign functions to variables. Now, closures allow us to take advantage of first-class functions, and return an inner function that remembers and has access to variables local to the scope in which they were created.

# Closure is just the nested function whose inner function is passed as a reference which stands in listening mode.
def raiseToPower(n):
    def innerFunc(x):
        return x**n
    return innerFunc

findSquare = raiseToPower(2)
findCube = raiseToPower(3)

print(f"The square of 12 is {findSquare(12)}.")
print("The square of 7 is {}.".format(findSquare(7)))
print(f"The cube of 3 is {findCube(3)}.")
print("The cube of 5 is {}.".format(findCube(5)))