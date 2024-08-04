user = {"username":"Amar", "access_level":"guest"}

def get_admin_password():
    return "1234"

print(get_admin_password()) # However we do not want the password to be accessed rightaway and should be accessed only if access_level is admin

# So we want to get the get_admin_password() function secured, so that no matter when and where this function get's invoked it should be first checking the access_level of the user and depending on that it should decide whether to display the password or not.

# This below code block will work but again in future we can still access the admin password by simply invoking the function.
if(user["access_level"]=='admin'):
    print(get_admin_password())

print(get_admin_password())  #This will still invoke the admin password irrespecive of the type of user as the function is still insecure.

#We are looking to wrap the get_admin_password() method to a outer function which should automatically invoked first if we try to access the get_admin_password() and that function should make sure that if the user is admin then only return or display the password. 