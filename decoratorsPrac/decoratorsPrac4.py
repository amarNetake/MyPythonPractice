
def make_secure(func):
    def secure_function():
        if(user['access_level']=='admin'):
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

# Above code will create a get_admin_password() function and pass it through the decorator like 
# def get_admin_password():
#     return "1234"
# get_admin_password = make_secure(get_admin_password)
# 
print("------------------------"*4)

user = {'username':'amar','access_level':'admin'}
print(get_admin_password())

print("------------------------"*4)

user = {"username":"Samir", "access_level":"guest"}
print(get_admin_password())

print("------------------------"*4)

print(get_admin_password.__name__)
# Will store the internal function as the name which is not what we want and documentation attached to get_admin_password will be lost.

print("------------------------"*4)

# @intro_decorator
# def hello_decorator():
#     print("My name is Amar")
# 
# """ Above code is equivalent to """
# def hello_decorator():
#     print("My name is Amar")
# hello_decorator=intro_decorator(hello_decorator)
#
#
# Note: you have to define a intro_decorator() function as well