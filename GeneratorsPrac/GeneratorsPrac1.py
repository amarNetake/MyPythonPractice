# Without Generators
def square_nums(nums):
    result = []
    for item in nums:
        result.append(item**2)
    return result

my_nums = square_nums([1,2,3,4,5])

print(my_nums)