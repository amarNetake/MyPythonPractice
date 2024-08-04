
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

hello_printer = outer_function("Hello!")
good_bye_printer = outer_function("Bye!")

hello_printer()
good_bye_printer()
hello_printer()
hello_printer()
good_bye_printer()