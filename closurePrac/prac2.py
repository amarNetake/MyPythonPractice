# Closures are just the nested functions whose inner function is passed as a reference which stands in a listening mode

def outerFunc(x):
    def innerFunc(message):
        return message.upper()
    def innerFunc2(message):
        return message.lower()
    if x is True:
        return innerFunc
    else:
        return innerFunc2

importantMessage = outerFunc(True)
notImportantMessage = outerFunc(False)

print(importantMessage("Alert: There is fire in the apartment."))
print(notImportantMessage("Your Parcel Will Arrive in 10 DAYS."))