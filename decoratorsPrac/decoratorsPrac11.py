
def display_info(func):
    def inner():
        print(f"Executing {func.__name__} function")
        func()
        print(f"Finished {func.__name__} Execution")
    return inner

def printer():
    print("Hello World!")

print("---------------------------"*4)

printer()
print("---------------------------"*4)

printer = display_info(printer)
printer()
print("---------------------------"*4)

func2= display_info(printer)
func2()
print("---------------------------"*4)

func3= display_info(func2)
func3()
print("---------------------------"*4)