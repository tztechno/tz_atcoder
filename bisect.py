
####################################################

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

####################################################

from bisect import bisect_left

# ソートされたリスト
lst = [1, 3, 5, 7, 9]

# 指定した値を挿入するべき位置（左側）のインデックスを取得
index = bisect_left(lst, 4)
print(index)  # 出力結果: 2

# インデックスを使用して挿入操作を行う場合
lst.insert(index, 4)
print(lst)  # 出力結果: [1, 3, 4, 5, 7, 9]


####################################################

from bisect import bisect

# ソートされたリスト
my_list = [1, 3, 3, 6, 7, 8, 12]

# 二分探索で挿入ポイントを見つける
# bisect_left: 要素が既に存在する場合、その要素の左側の挿入ポイントを返す
# bisect_right: 要素が既に存在する場合、その要素の右側の挿入ポイントを返す
# ここでは bisect_left を使用しています
insert_point = bisect(my_list, 5)

print("挿入ポイント:", insert_point)

####################################################
