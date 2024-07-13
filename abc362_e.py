abc362_e.py
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
[titia]
import sys
input = sys.stdin.readline
from collections import Counter
mod=998244353
N=int(input())
A=list(map(int,input().split()))
ANS=[0]*(N+1)
ANS[1]=N
D=Counter()
# (length, next_number,dif) : number
for i in range(1,N):
    #print(D)
    ND=Counter()
    for j in range(i):
        ND[2,A[i]+(A[i]-A[j]),A[i]-A[j]]+=1
    for leng,next_number,dif in D:
        if A[i]==next_number:
            ND[leng+1,next_number+dif,dif]+=D[leng,next_number,dif]
    for leng,next_number,dif in ND:
        D[leng,next_number,dif]=(D[leng,next_number,dif]+ND[leng,next_number,dif])%mod
for leng,next_number,dif in D:
    ANS[leng]=(ANS[leng]+D[leng,next_number,dif])%mod
print(*ANS[1:])
################################################
################################################
[myans TLE]
import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
from itertools import product,permutations,combinations,accumulate
def part(A,m):
  C0=list(combinations(A,m))
  t=0
  for ci in C0:
    s=set()
    for i in range(m-1):
      s.add(ci[i]-ci[i+1])
    if len(s)==1:
      t+=1
  return t
ANS=[N]
for j in range(2,N+1):
  ANS+=[part(A,j)]
print(*ANS)
################################################
