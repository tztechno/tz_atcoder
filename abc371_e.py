
abc371_e.py
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
N=int(input())
A=[int(i) for i in input().split()]
X=[[-1] for i in range(N+1)]
B=[(N*(N+1))//2 for i in range(N+1)]
for i,a in enumerate(A):
    X[a].append(i)
for a in range(N+1):
    X[a].append(N)

for a in range(N+1):
    for j in range(len(X[a])-1):
        d=X[a][j+1]-X[a][j]
        B[a]-=((d)*(d-1))//2
print(sum(B))

##################################################################
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

MAE=[-1]*(N+10)
ANS=0
for i in range(N):
    a=A[i]
    mae=MAE[a]

    ANS+=(i-mae)*(N-i)

    MAE[a]=i

print(ANS)
##################################################################
import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
from math import inf, sqrt, gcd
from heapq import heappush, heappop, heapify, heapreplace
from itertools import accumulate
from functools import lru_cache

input = lambda: sys.stdin.readline().rstrip("\r\n")
ii = lambda: int(input())
mii = lambda: map(int, input().split())
moii = lambda: map(lambda num: int(num) - 1, input().split())
lmii = lambda: list(map(int, input().split()))
tmii = lambda: tuple(map(int, input().split()))
mfi = lambda: map(float, input().split())
lmfi = lambda: list(map(float, input().split()))

def solve():
    n = ii()
    a = lmii()
    pre = [0] * (n + 1)
    res = s = 0
    for i, x in enumerate(a):
        s -= pre[x]
        pre[x] = i + 1
        s += pre[x]
        res += s
    print(res)
    return


if __name__ == '__main__':
    T = 1
    for _ in range(T):
        solve()
##################################################################
N = int(input())
A = list(map(int, input().split()))

last_occurrence = [0] * (N + 1)
total = 0

for i in range(1, N + 1):
    a_i = A[i - 1]
    contribution = (i - last_occurrence[a_i]) * (N - i + 1)
    total += contribution
    last_occurrence[a_i] = i

print(total)

##################################################################
N = int(input())
Integers = list(map(int, input().split()))

def cumulative_sum(num):
    return num * (num + 1) // 2

Num_Pos = {}

for i, A in enumerate(Integers):
    if A not in Num_Pos:
        Num_Pos[A] = [-1, i]
    else:
        Num_Pos[A].append(i)
for A in Num_Pos.keys():
    Num_Pos[A].append(len(Integers))

allArrayNum = len(Num_Pos.keys()) * cumulative_sum(N)

complimentArrayNum = 0
for Positions in Num_Pos.values():
    for i in range(len(Positions)-1):
        complimentArrayNum += cumulative_sum((Positions[i+1] -1) - Positions[i])

print(allArrayNum - complimentArrayNum)
##################################################################
ans = acc = 0
N = int(input())
R = [-1]*(N+1)
for L, a in enumerate(map(int, input().split())):
    acc += L-R[a]
    ans += acc
    R[a] = L
print(ans)
##################################################################
