
import sys
input = sys.stdin.readline
#S=input().strip()#改行除く
#S=input()[0:-1]#改行除く

sys.setrecursionlimit(10**8)
from math import gcd,sqrt,log,exp,inf,pi,nan
from itertools import product,permutations,combinations,accumulate
from itertools import groupby, zip_longest
from bisect import bisect_left,bisect_right,bisect
from heapq import heappush,heappop,heapify,heappushpop,heapreplace,merge,nlargest,nsmallest
import networkx as nx



from atcoder.segtree import SegTree
from atcoder.fenwicktree import FenwickTree
from atcoder.dsu import DSU



from operator import itemgetter
from decimal import Decimal

from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
cnt = defaultdict(deque)


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
