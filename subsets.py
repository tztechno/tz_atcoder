from itertools import chain, combinations

def enumerate_subsets(s):
    # 元の集合の要素をリスト化
    elements = list(s)
    n = len(elements)
    # 空集合を含むために range(n + 1) としている
    for r in range(n + 1):
        # itertools.combinations を使って r 個の要素からなる部分集合を列挙
        for subset in combinations(elements, r):
            yield set(subset)

# テスト用の集合
my_set = {1, 2, 3}
# 部分集合を列挙
for subset in enumerate_subsets(my_set):
    print(subset)
