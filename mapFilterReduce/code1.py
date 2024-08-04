# map: Applying one function to entire iterable.

nums = ["2","46","613","8754"]

# Now let's say we want to convert all items in nums to integer. for loop won't be ideal for such small task. So we will use map function

print("-----------------"*4)

print("Type of each item in nums list is {}.".format(type(nums[2])))
nums = map(int, nums)  # Returns a map object with each item of list nums converted to int
print("-----------------"*4)

print("Type of object returned by map function is {}.".format(nums))  #It returns a map object so we need to convert it to list.
print("-----------------"*4)

nums = list(nums) # Converted the map object to list format
print("Type of each item in nums list is {}.".format(type(nums[2])))
print("-----------------"*4)