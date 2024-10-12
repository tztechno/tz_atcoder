#############################################


#############################################


#############################################


#############################################


#############################################


#############################################


#############################################


#############################################


#############################################


import sys
input = sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))

if sum(A)<=M:
    print("infinite")
    exit()

OK=0
NG=10**10


while NG>OK+1:
    mid=(OK+NG)//2

    score=0
    for a in A:
        score+=min(a,mid)

    if score<=M:
        OK=mid
    else:
        NG=mid

print(OK)


#############################################
[my WA]

from bisect import bisect_left,bisect_right,bisect
from collections import defaultdict,deque,Counter

N,M=map(int,input().split())
A=list(map(int,input().split()))

A.sort()
B=[0]
for a in A:
  B+=[B[-1]+a]

amin=min(A)
amax=max(A)
s=amin
bl=bisect_left(A,s)
T=B[bl]+s*(N-bl)
S=[s]
P=set()

while T!=M:
  #print(T,M,s)
  if (T,s) not in P:
    P.add((T,s))
  else:
    break
  
  if T<M:
    s2=(s+amax)//2
    bl2=bisect_left(A,s2)
    T=B[bl2]+s2*(N-bl2)
    s=s2
    if T<M:
      S+=[s2]

  elif T>M:
    s2=(s+amin)//2
    bl2=bisect_left(A,s2)
    T=B[bl2]+s2*(N-bl2)
    s=s2
    if T<M:
      S+=[s2]
      
if sum(A)<=M:
  print('infinite')
else:
  print(max(S))

#############################################
[my TLE]

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
B=[0]
for a in A:
  B+=[B[-1]+a]
from bisect import bisect_left,bisect_right,bisect
amin=min(A)
amax=max(A)
for s in range(amin,amax+1):
  bl=bisect_left(A,s)
  T=B[bl]+s*(N-bl)
  if T>M:
    print(s-1)
    exit()
print('infinite')

#############################################
