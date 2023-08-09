
########################################

def pop_left(lst, i):
    return [lst.pop(0) for _ in range(i)]

def pop_right(lst, j):
    return [lst.pop() for _ in range(j)]

########################################

my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)  # インデックス2の要素を取り出す
print(popped_element)  # 出力: 3
print(my_list)  # 出力: [1, 2, 4, 5]

########################################


