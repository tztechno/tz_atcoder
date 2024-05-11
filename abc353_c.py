abc353_c.py
##################################################
##################################################
##################################################
##################################################
##################################################
[peri AC]
import bisect
n = int(input())
a = list(map(int, input().split(' ')))
mod = 10 ** 8

big = (n-1) * sum(a)
a.sort()
for i in range(n):
    cur = a[i]
    rest = mod - cur
    pos = bisect.bisect_left(a, rest, lo=i+1)
    count = n - pos
    big -= count * mod
print(big)
##################################################
[sugi AC]
N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
cnt = 0
r = N
for i in range(N):
    r = max(r, i + 1)
    while r - 1 > i and A[r - 1] + A[i] >= 10 ** 8:
        r -= 1

    cnt += N - r

for i in range(N):
    ans += A[i] * (N - 1)

ans -= cnt * 10 ** 8
print(ans)
##################################################
[nishi AC]
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 8
sum_A = sum(A)
A.sort()
cnt = 0
r = N
for i in range(N):
    r = max(r, i + 1)
    while (r - 1 > i and A[r - 1] + A[i] >= mod):
        r -= 1
    cnt += N - r

ans = (sum_A * (N - 1)) - (mod * cnt)

print(ans)
##################################################
[titia AC]
import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

A.sort()

S=[0]
for a in A:
    S.append(S[-1]+a)

ANS=0
ind=n-1
for i in range(n):
    a=A[i]
    while ind>=0 and a+A[ind]>=10**8:
        ind-=1

    #print(ind)
    ANS+=S[-1]-a
    ANS+=a*(n-1)
    if i>ind:
        ANS-=(n-1-ind-1)*(10**8)
    else:
        ANS-=(n-1-ind)*(10**8)

    #print(ANS)

print(ANS//2)
##################################################
[my TLE]
from itertools import product,permutations,combinations,accumulate
from collections import defaultdict,deque,Counter
import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
rem=10**8
B=[]
for a in A:
  B+=[a%rem]
C0=list(combinations(B,2))
ANS=[]
for ci in C0:
  ANS+=[sum(ci)%rem]
ANS.sort()
ANS2=Counter(ANS)
ANS3=0
for a in ANS2:
  ANS3+=a*ANS2[a]
print(ANS3)
##################################################
