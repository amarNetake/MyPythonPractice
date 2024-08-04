import functools

def make_secure(func):

    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if(user['access_level']=='admin'):
            return func(*args,**kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function

@make_secure
def get_password(panel):
    if(panel=='admin'):
        return "1234"
    elif(panel=="billing"):
        return "super_secure_password"

print("------------------------"*4)

user = {"username":"Amar","access_level":"admin"}
print(get_password("billing"))

print("------------------------"*4)

user = {"username":"Yasmin","access_level":"guest"}
print(get_password("billing"))

print("------------------------"*4)
user = {"username":"Ronald","access_level":"admin"}
print(get_password("admin"))