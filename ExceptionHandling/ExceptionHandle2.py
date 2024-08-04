# try:
#     statement(s)
# except IndexError:
#     statement(s)
# except ValueError:
#     statement(s)

# Demonstartion of catching specific error and catching multiple errors

def fun(num):
    if(num<5):
        result = num / (num - 4)
    print(f"The result is {result}")

try:
    fun(2)   # Will execute without error
    fun(3)   # Will execute without error
    fun(8)   # Will throw NameError
    fun(1)   # Control will not reach here as after above error it immediately just goes to below except block
    fun(4)   # Would have thrown ZeroDivisionError but control will not reach here as after above error it immediately just goes to below except block
except ZeroDivisionError:
    print(f"Zero Division Error occurred. Please choose a number except 4...")
except NameError:
    print("NameError occurred as object accessed is not initialized or created...")

print("----------------------"*4)
print("************Normal flow of program is protected... Control reached below the point where error occurred!!!************")
print("----------------------"*4)