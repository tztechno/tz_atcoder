##############################################

from collections import deque

左から取る (popleft()):
my_deque = deque([1, 2, 3, 4, 5])
popped_element = my_deque.popleft()
print(popped_element)  # 最初の要素が取り出され、出力される
print(my_deque)  # deque([2, 3, 4, 5])

右から取る (pop()):
my_deque = deque([1, 2, 3, 4, 5])
popped_element = my_deque.pop()
print(popped_element)  # 最後の要素が取り出され、出力される
print(my_deque)  # deque([1, 2, 3, 4])

左に足す (appendleft()):
my_deque = deque([2, 3, 4, 5])
my_deque.appendleft(1)  # 最初に要素を追加する
print(my_deque)  # deque([1, 2, 3, 4, 5])

右に足す (append()):
my_deque = deque([1, 2, 3, 4])
my_deque.append(5)  # 末尾に要素を追加する
print(my_deque)  # deque([1, 2, 3, 4, 5])

##############################################

from collections import deque

# 空の deque の作成
my_deque = deque()

# 要素の追加
my_deque.append(1)           # deque([1])
my_deque.appendleft(2)       # deque([2, 1])

# 要素の削除
value = my_deque.pop()       # value = 1, deque([2])
value = my_deque.popleft()   # value = 2, deque([])

# 要素の参照
value = my_deque[0]          # value = 2

# deque の長さ
length = len(my_deque)       # length = 0

# deque の反転
reversed_deque = my_deque.copy()
reversed_deque.reverse()     # deque([], [1, 2])

##############################################

from collections import deque
Ni=deque(range(1,n+1))
print(Ni)

##############################################
