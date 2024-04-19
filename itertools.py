#######################################################

from itertools import permutations
n,a,b,c,d=map(int,input().split())
counts = {'A': a, 'B': b, 'C': c, 'D': d}
chars = []
for char, count in counts.items():
    chars.extend([char] * count)
#print(chars)
perms = permutations(chars)

#######################################################

from itertools import groupby

data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5)]

# Sort the data by the key (optional, but groups should be consecutive)
sorted_data = sorted(data, key=lambda x: x[0])

# Use groupby to group elements by the first element of each tuple
grouped_data = {key: list(group) for key, group in groupby(sorted_data, key=lambda x: x[0])}

print(grouped_data)

#######################################################

from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b']

# Use zip_longest to combine lists, filling missing values with None
result = list(zip_longest(list1, list2, fillvalue=None))

print(result)

#######################################################
