user = {'username':'amar','access_level':'guest'}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if(user['access_level']=='admin'):
            return func()
        else:
            return 'No admin permissions for {}.'.format(user['username'])
    return secure_function

# Unsuccessful if we invoke it here
print(get_admin_password())

get_admin_password = make_secure(get_admin_password)

# Successful if we invoke it here
print(get_admin_password())