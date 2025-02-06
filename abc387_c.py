#################################################
#################################################
#################################################
#################################################

#################################################
#################################################
#################################################
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

ans=0
for i in range(l,r+1):
  X=list(str(i))
  t=1
  for xi in set(X[1:]):
    if X[0]<=xi:
      t=0
      break
  ans+=t
print(ans)
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

ans=0
for i in range(l,r+1):
  X=list(str(i))
  if X[0]>max(set(X[1:])):
    ans+=1
print(ans)
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

