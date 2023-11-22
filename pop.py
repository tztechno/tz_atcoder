
########################################

右から取る:
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()
print(popped_element)  # 最後の要素が取り出され、出力される
print(my_list)  # [1, 2, 3, 4]

左から取る:
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(0)
print(popped_element)  # 最初の要素が取り出され、出力される
print(my_list)  # [2, 3, 4, 5]

右から取る:
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(-1)
print(popped_element)  # 最後の要素が取り出され、出力される
print(my_list)  # [1, 2, 3, 4]

左に足す:
my_list = [2, 3, 4, 5]
my_list.insert(0, 1)  # 最初に要素を挿入する
print(my_list)  # [1, 2, 3, 4, 5]

右に足す:
my_list = [1, 2, 3, 4]
my_list.append(5)  # 末尾に要素を追加する
print(my_list)  # [1, 2, 3, 4, 5]

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


