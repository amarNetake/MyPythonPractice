import numpy as np

nums = [1,2,3]

for item in nums:
    print(item)

if('__iter__' in dir(list)):
    print("list is an iterable...")

if('__iter__' in dir(dict)):
    print("Dictionary is an iterable...")

if('__iter__' in dir(str)):
    print("String is an iterable...")

if('__iter__' in dir(tuple)):
    print("tuple is an iterable...")

if('__iter__' in dir(np.array)):
    print("Numpy array is an iterable...")
















