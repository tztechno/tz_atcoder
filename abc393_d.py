##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
[titia]

import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

A=list(range(N+1))
BOX=list(range(N+1))
BOX_INV=list(range(N+1))

for tests in range(Q):
    #print(BOX,BOX_INV)
    L=list(map(int,input().split()))

    if L[0]==1:
        a,b=L[1],L[2]

        A[a]=BOX[b]

    elif L[0]==2:
        a,b=L[1],L[2]

        BOX[a],BOX[b]=BOX[b],BOX[a]

        BOX_INV[BOX[a]]=a
        BOX_INV[BOX[b]]=b

    else:
        a=L[1]
        print(BOX_INV[A[a]])

##################################################################
[my TLE]
import sys
input = sys.stdin.readline

N,Q=map(int,input().split())
from collections import defaultdict,deque,Counter
bird= defaultdict(int)

for i in range(N):
  bird[i+1]=i+1
  
for i in range(Q):
  qr=list(map(int,input().split()))
  
  if qr[0]==1:
    a,b=qr[1],qr[2]
    bird[a]=b
    
  elif qr[0]==2:
    a,b=qr[1],qr[2]
    A=[]
    B=[]
    for j in range(N):
      if bird[j+1]==a:
        A+=[j+1]
      if bird[j+1]==b:
        B+=[j+1]

    for a in A:
      bird[a]=b
    for b in B:
      bird[b]=a

  elif qr[0]==3:
    a=qr[1]
    print(bird[a])
##################################################################
