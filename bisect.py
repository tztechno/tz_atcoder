from bisect import bisect_left, bisect_right

# Sorted list of numbers
numbers = [1, 3, 5, 7, 9]

# Using bisect_left
position = bisect_left(numbers, 6)
print(position)  # Output: 3

# Using bisect_right
position = bisect_right(numbers, 6)
print(position)  # Output: 3

# Inserting an element into the list
number = 6
position = bisect_right(numbers, number)
numbers.insert(position, number)
print(numbers)  # Output: [1, 3, 5, 6, 7, 9]
