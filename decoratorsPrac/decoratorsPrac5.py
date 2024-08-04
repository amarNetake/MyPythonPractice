import functools

def make_secure(func):
    @functools.wraps(func) # This will help to print 'make_secure_function' as output of make_secure_function.__name__ instead of 'secure_function'
    def secure_function():
        if(user['access_level']=='admin'):
            return func()
        else: 
            return f"No admin permission for {user['username']}."
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

# Above code will create a get_admin_password() function and pass it through the decorator like
# def get_admin_password():
#   return "1234"
# get_admin_password=make_secure(get_admin_password)

print("------------------------"*4)

user = {"username":"amar", "access_level":"guest"}
print(get_admin_password())
print("------------------------"*4)

user = {"username":"James","access_level":"admin"}
print(get_admin_password())
print("------------------------"*4)

print(get_admin_password.__name__)
#Will store the internal function as the name if we will NOT use @functools.wraps(func) which is not what we want and documentation attached to get_admin_password will be lost. Hence we use inbuilt decorator @functools.wraps(func) using functools module.
print("------------------------"*4)