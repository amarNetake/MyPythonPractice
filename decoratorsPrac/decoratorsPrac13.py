import functools

def display_info(func):
    @functools.wraps(func)
    def inner():
        print(f"Executing {func.__name__} function.")
        func()
        print(f"Finished {func.__name__} Execution")
    return inner

@display_info
def printer():
    print("Hello World!")

print("---------------------------"*4)

printer()
print("---------------------------"*4)

printer = display_info(printer)
printer()
print("---------------------------"*4)

func2=display_info(printer)
func2()
print("---------------------------"*4)