
from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
cnt = defaultdict(deque)

from collections import deque
d = deque([1, 2, 3, 4, 5])
d.rotate(1)

import sys
input = sys.stdin.readline
S=input().strip()#改行除く
#S=input()[0:-1]#改行除く

sys.setrecursionlimit(10**8)
from math import gcd,sqrt,log,exp,inf,pi,nan
from itertools import product,permutations,combinations,accumulate
from itertools import groupby, zip_longest
from more_itertools import set_partitions

from bisect import insort, bisect_left, bisect_right
from sortedcontainers import SortedList, SortedSet, SortedDict
sl = SortedList([0, L])

from heapq import heappush,heappop,heapify,heappushpop,heapreplace,merge,nlargest,nsmallest
import networkx as nx

from functools import lru_cache
@lru_cache(maxsize=None)



from atcoder.segtree import SegTree
from atcoder.fenwicktree import FenwickTree
from atcoder.dsu import DSU
from atcoder.maxflow import MFGraph
from atcoder.scc import SCCGraph


------------------------------------------------
for i in range(1 << K):
    for j in range(K):  # 修正点
        if (i >> j) & 1 == 0:  # 修正点
            
------------------------------------------------
for i in range(1<<(N*2)):
    for j in range(2*N):
        if i & (1<<j) != 0:

整数 i のビット表現の中で、j 番目のビットが立っている（つまり1である）かどうかを判定しています。            
------------------------------------------------
for i in range(1 << K):
    bit_string = bin(i)[2:].zfill(K)  # ビット列を K 桁に拡張
    for j, b in enumerate(bit_string):
        if b == '0':
------------------------------------------------
OK=0
NG=10**10
while NG > OK + 1:
    mid = (OK + NG) // 2
    if score <= M:
        OK = mid
    else:
        NG = mid

------------------------------------------------
def f(a, b):
    return a*a*a-b*b*b
N=int(input())
for w in range(1,1000000):
    ok=1
    ng=int(1e9)
    while (ng-ok)>1:
        m=(ok+ng)//2
        if(f(w+m,m)<=N): ok=m
        else: ng=m
    if(f(ok+w,ok)==N):
        print(ok+w,ok)
        exit()
print(-1)
------------------------------------------------

from operator import itemgetter
from decimal import Decimal


INF = float("INF")
FourNb=[(-1,0),(1,0),(0,1),(0,-1)]
cursol=dict(zip('UDRL',FourNb))
alp=[chr(ord('a')+i) for i in range(26)]

input_data = '''
6
6 2 5 3 1 4
'''
lines = input_data.strip().splitlines()
N = int(lines[0])
A = list(map(int, lines[1].split()))

N = int(input())
A = list(map(int,input().split()))

t,k,*a=map(int,input().split())

query = tuple(map(lambda x: int(x)-1, input().split()))


file_path = "/kaggle/input/my-atcoder/ahc042_in/0000.txt"
with open(file_path, 'r') as file:
    content = file.readlines()  # 各行をリストとして取得
array_2d = np.array([list(map(int, line.split())) for line in content[1:]])


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
