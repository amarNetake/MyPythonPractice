# Without Generators
def square_nums(nums):
    for item in nums:
        yield(item**2)

my_nums = square_nums([1,2,3,4,5])

print("--------------------"*4)
print(my_nums)
print("--------------------"*4)
print(next(my_nums,None))
print(next(my_nums,None))
print(next(my_nums,None))
print(next(my_nums,None))
print(next(my_nums,None))
print(next(my_nums,None))   # Generator got exhausted
print(next(my_nums,None))   # Generator got exhausted
print("--------------------"*4)

# Generators does not hold the entire result in the memory. It yields 1 result at a time.


