# Passing user defined function to map()
nums = [5,10,15,20,25]
print("-----------------"*4)

print("before squaring : {}".format(nums))
def sq(item):
    return item**2

sq_nums = list(map(sq,nums))  # Applying user defined function on each item of list nums
print("after squaring : {}".format(sq_nums))
print("-----------------"*4)

# Passing "lambda function" to map
cube_nums = list(map(lambda x: x**3, nums)) # We defined an (anonymous function)/(lambda function) to which if we pass an item it will cube that item

print(nums)
print(cube_nums)
print("-----------------"*4)

def square(item):
    return item**2

def twice(item):
    return item+item

def cube(item):
    return item**3

li = []
func = [twice,square,cube]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    li.append({i:val})

print(li)
print("-----------------"*4)