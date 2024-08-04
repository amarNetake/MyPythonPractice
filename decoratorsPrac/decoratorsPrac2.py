user = {"username":"Amar","access_level":"guest"}

def get_admin_password():
    return "1234"

def get_guest_password():
    return None

def secure_function(func):
    if(user['access_level']=='admin'):
        return func
    else:
        return get_guest_password
    
#If we invoke get_admin_password() here it will invoke the get_admin_password() and will give the admin password to us irrespective of the type of user.
print(get_admin_password())
print(get_admin_password())
print(get_admin_password())

#Checking the user's access level when we are defining the function 
get_admin_password = secure_function(get_admin_password) #Below this line only, we can protect to show password only if the user is admin.

# Now every time below if we try to access the get_admin_password() depending on if user had been a guest or an admin it will decide whether to show password or not.

print(get_admin_password())
print(get_admin_password())
print(get_admin_password())

# But this is also what we do not desire as:
# 1) We want to check the user's access level when we call the function and not when we define it.
# 2) Want to make sure irrespective of the location where it will be invoked we want to protect get_admin_password()