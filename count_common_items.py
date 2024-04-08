def count_common_items(list1, list2):
    # リストをセットに変換して、重複を削除します
    set1 = set(list1)
    set2 = set(list2)
    
    # 2つのセットの共通要素を見つけ、その数を返します
    return sum(min(list1.count(item), list2.count(item)) for item in set1.intersection(set2))

# 例として、2つのリストを作成します
list1 = [1, 2, 3, 4, 4]
list2 = [3, 4, 4, 6, 7]

# 共通項の数を数えます
common_count = count_common_items(list1, list2)
print("共通項の数:", common_count)
