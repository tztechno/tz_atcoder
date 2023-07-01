
def merge_sort(data, lt=lambda x,y: x < y):
  
    # stable sort
    n = len(data)
    res = data.copy()
    if (n - 1).bit_length() & 1:
        data, res = res, data
    width = 1
    while width < n:
        tmp = 0
        for i in range(0, n, 2*width):
            l = i
            r = mid = min(n, i + width)
            end = min(n, i + 2*width)
            while l < mid and r < end:
                if lt(data[r], data[l]):
                    res[tmp] = data[r]
                    r += 1
                else:
                    res[tmp] = data[l]
                    l += 1
                tmp += 1
            while l < mid:
                res[tmp] = data[l]
                l += 1
                tmp += 1
            while r < end:
                res[tmp] = data[r]
                r += 1
                tmp += 1
        data, res = res, data
        width *= 2



'''

The given code implements the merge sort algorithm, 
which is a sorting algorithm that uses the divide-and-conquer approach. 
Merge sort has an average and worst-case time complexity of O(n log n), 
where n is the number of elements in the input list.

The merge_sort function takes two parameters: data and lt.

data: It represents the input list to be sorted.
lt: It is an optional parameter that specifies the comparison function 
used to determine the order of elements. By default, it uses the less-than operator (<) to compare elements.
The function begins by creating a copy of the input list data and 
assigning it to the res variable. This is done to avoid modifying the original input list.

The next step determines the number of iterations required for the sorting process. 
It checks if the highest bit of (n - 1).bit_length() is set. 
If it is, it swaps the data and res variables. 
This is an optimization technique to reduce the number of data copies during merging.

The sorting process starts with a width of 1. 
It doubles the width with each iteration until it reaches a value greater than or equal to the length of the input list n.

Inside the main loop, it iterates over the input list data in strides of 2*width. 
For each iteration, it divides the list into two sublists: data[l:mid] and data[mid:end]. 
The variables l, r, and mid keep track of the indices for the sublists. 
The variable end ensures that the indices do not go out of bounds.

Within the inner loop, it compares the elements from the sublists using the provided comparison function lt. 
If the comparison evaluates to True, it assigns the element from the second sublist (data[r]) 
to the res list at index tmp. Otherwise, it assigns the element from the first sublist (data[l]). 
The loop continues until either l reaches mid or r reaches end. This ensures that all elements 
from both sublists are merged into the res list.

After merging the sublists, it checks if there are any remaining elements in either sublist. 
If so, it copies the remaining elements to the res list.

Finally, it swaps the data and res variables, and doubles the width for the next iteration.

The process continues until the width is greater than or equal to the length of the input list n. At this point, 
the data list contains the sorted elements, and the function returns the sorted list.

Note: The code assumes that the input list data contains comparable elements 
that can be ordered using the provided comparison function lt.

'''
