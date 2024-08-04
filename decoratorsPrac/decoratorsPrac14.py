
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f"wrapper function executed before {original_function.__name__}...")
        original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran...")

@decorator_function
def display_my_info(name,age):
    print(f"My name is {name} and I am {age} years old.")

print("--------------------------"*4)

display()
print("--------------------------"*4)

display_my_info("Amar",25)
print("--------------------------"*4)

display_my_info("Kartik",37)
print("--------------------------"*4)