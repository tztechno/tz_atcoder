from bisect import bisect_left

# ソートされたリスト
lst = [1, 3, 5, 7, 9]

# 指定した値を挿入するべき位置（左側）のインデックスを取得
index = bisect_left(lst, 4)
print(index)  # 出力結果: 2

# インデックスを使用して挿入操作を行う場合
lst.insert(index, 4)
print(lst)  # 出力結果: [1, 3, 4, 5, 7, 9]
