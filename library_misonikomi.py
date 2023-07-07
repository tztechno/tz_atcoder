import sys
import heapq
import math
from itertools import accumulate, product, permutations, groupby
from collections import deque, Counter, defaultdict
from sys import stdin
 
 
int1 = lambda x: int(x) - 1
sti = lambda: stdin.readline()[:-1]                 # S = sti()     (S: string)
ii = lambda: int(sti())                             # N = ii()      (N: int)
mi = lambda: map(int, stdin.readline().split())     # N, M = mi()   (N: int, M: int)
li = lambda: list(mi())                             # A = li()      (A: list (1×?), A[i]: int)
mai = lambda n: [li() for i in range(n)]            # A = mai(N)    (A: matrix (N×?), A[i]: list (1×?), A[i][j]: int)
mi1 = lambda: map(int1, stdin.readline().split())   # N, M = mi()   (Subtract 1 for each variable.)
li1 = lambda: list(mi1())                           # A = li()      (Subtract 1 for each variable.)
mai1 = lambda n: [li1() for i in range(n)]          # A = mai(N)    (Subtract 1 for each variable.)
mis = lambda: map(str, stdin.readline().split())    # S, T = mis()  (S: string, T: string)
lis = lambda: list(mis())                           # S = lis()     (S: list (1×?), S[i]: string)
mais = lambda n: [lis() for i in range(n)]          # S = mais(N)   (S: matrix (N×?), S[i]: list (1×?), S[i][j]: string)
 
