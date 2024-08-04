def square_nums(nums):
    for item in nums:
        yield(item**2)
    
my_nums= square_nums([1,2,3,4,5])
print("------------------"*4)

print(my_nums)
print("------------------"*4)

for item in my_nums:
    print(item)
print("------------------"*4)

for item in my_nums:   # This loop will print nothing as generator my_nums has gotten exhausted
    print(item)
print("------------------"*4)

my_nums= square_nums([1,2,3,4,5])   # Again got the generator
my_nums = list(my_nums)  #Converted generator into list and now it will not exhaust but you will lose the advantage of generator.
print(my_nums)
print("------------------"*4)
print(my_nums)
print("------------------"*4)
# Generators are space and time efficient as it does not hold heck a lot of values at a time and holds a single value at a time.

# Generators gives you a performance boost in terms of both memory as well as execution time which is noticable when you deal with humongous data 

# Generators does not holds the entire result in the memory. It yields 1 result at a time.