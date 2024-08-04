# -----------------------------------------------REDUCE----------------------------------------------------
# reduce is available in functools module
from functools import reduce

# The reduce(func,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is available in "functools" module.
#
# Working:
# 
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continuestill no more elements are left in the container.
# The final returned result is returned and printed on console.

nums = [2, 4, 6, 8, 10]

cumulated_sum = reduce(lambda x,y: x+y,nums)
print(nums)
print(cumulated_sum)