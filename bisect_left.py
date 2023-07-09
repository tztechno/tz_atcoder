from bisect import bisect_left

my_list = [1, 3, 5, 7, 9]

# 4 を挿入するべきインデックスを求める
index = bisect_left(my_list, 4)
print(index)  # 出力: 2

# 6 を挿入するべきインデックスを求める
index = bisect_left(my_list, 6)
print(index)  # 出力: 3

# 10 を挿入するべきインデックスを求める
index = bisect_left(my_list, 10)
print(index)  # 出力: 5
