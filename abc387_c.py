#################################################

#################################################

#################################################

#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

def judge(x):
  X=list(str(x))
  t=int(X[0])
  S=set(X[1:])
  if t>int(max(S)):
    return 1
  else:
    return 0

ans=0
for i in range(l,r+1):
  ans+=judge(i)
print(ans)
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

from collections import defaultdict,deque,Counter

def judge(x):
  X=list(str(x))
  C=Counter(X)
  mx=max(C.keys())
  if C[mx]==1 and X[0]==str(mx):
    return 1
  else:
    return 0

ans=0
for i in range(l,r+1):
  ans+=judge(i)
print(ans)
#################################################

