# The filter method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a sequence true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, dictionaries, or containers of any iterators.
# Returns: An iterator that is already filtered.

sequence = ['g','e','e','j','k','s','p','a','r','i']
vowels = ['a','e','i','o','u']
consonants = []
li = filter(lambda x:x not in vowels, sequence)
item = next(li,None)
while(item is not None):
    consonants.append(item)
    item = next(li,None)
print(consonants)
print("-----------------"*4)

nums = [2, 7, 0, 12, 6, 3, 8, 9, 2344, 46, 23, 6, 23, 3, 7, 78, 34, 92, 56]

def is_greater(num):
    return num>10

li = filter(is_greater,nums)
gr_than_10=[]
item = next(li,None)
while(item is not None):
    gr_than_10.append(item)
    item = next(li,None)

print(gr_than_10)
print("-----------------"*4)

seq = [0, 4, 2, 10, 6, 8, 12]

# Result that only contains odd numbers of seq
odds = filter(lambda x: x%2 != 0, seq)
print(f"odd numbers in seq:{list(odds)}")
# Result that only contains even numbers of seq
evens = filter(lambda x: x%2 == 0, seq)
print(f"even numbers in seq:{list(evens)}")
print("-----------------"*4)