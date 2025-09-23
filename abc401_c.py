

[titia AC]
import sys
input = sys.stdin.readline

mod=10**9

N,K=map(int,input().split())

if N<K:
    print(1)
    exit()

from collections import deque

A=deque([1]*K)
SUM=K

for i in range(N-K+1):
    A.append(SUM)
    SUM+=SUM
    SUM-=A.popleft()
    SUM%=mod

print(A[-1]%mod)
