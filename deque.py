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
