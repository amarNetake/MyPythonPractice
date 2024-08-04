# Raising user defined exception

print("-----------------------"*4)

class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def printException(self):
        print(f"User Defined Exception : {self.msg}")

try:
    raise Accident("Crash between 2 cars...")
except Accident as ac:
    ac.printException()

print("-----------------------"*4)

print("****************Normal flow of program sustained****************")
print("-----------------------"*4)