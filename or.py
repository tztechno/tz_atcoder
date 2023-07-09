list1 = [1, 1, 0, 0]
list2 = [0, 0, 1, 1]

result = [x or y for x, y in zip(list1, list2)]
print(result)
