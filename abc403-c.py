##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[my AC]

N,M,Q=map(int,input().split())
A=set()
ALL=set()
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A.add((x-1,y-1))
  elif qr[0]==2:
    x=qr[1]
    ALL.add(x-1)
  else:
    x,y=qr[1],qr[2]
    if x-1 in ALL:
      print('Yes')
    elif (x-1,y-1) in A:
      print('Yes')
    else:
      print('No')


##################################################################
[my TLE3]

N,M,Q=map(int,input().split())
A=set()
ALL=[]
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A.add((x-1,y-1))
  elif qr[0]==2:
    x=qr[1]
    ALL+=[x-1]
  else:
    x,y=qr[1],qr[2]
    if x-1 in ALL:
      print('Yes')
    elif (x-1,y-1) in A:
      print('Yes')
    else:
      print('No')

##################################################################
[my TLE20]

N,M,Q=map(int,input().split())
A=[]

ALL=[]
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A+=[(x-1,y-1)]
  elif qr[0]==2:
    x=qr[1]
    ALL+=[x-1]
  else:
    x,y=qr[1],qr[2]
    if x-1 in ALL:
      print('Yes')
    elif (x-1,y-1) in A:
      print('Yes')
    else:
      print('No')

##################################################################
[my AC]

N,M,Q=map(int,input().split())
A=[]
for i in range(N):
  A+=[set()]
ALL=set()
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A[x-1].add(y-1)
  elif qr[0]==2:
    x=qr[1]
    ALL.add(x-1)
  else:
    x,y=qr[1],qr[2]
    if x-1 in ALL:
      print('Yes')
    elif y-1 in A[x-1]:
      print('Yes')
    else:
      print('No')


##################################################################
[my TLE3]

N,M,Q=map(int,input().split())
A=[]
for i in range(N):
  A+=[set()]
ALL=[]
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A[x-1].add(y-1)
  elif qr[0]==2:
    x=qr[1]
    ALL+=[x-1]
  else:
    x,y=qr[1],qr[2]
    if x-1 in ALL:
      print('Yes')
    elif y-1 in A[x-1]:
      print('Yes')
    else:
      print('No')

##################################################################
[titia]

import sys
input = sys.stdin.readline

N,M,Q=map(int,input().split())
OK=[0]*(N+1)
S=set()

for i in range(Q):
    L=list(map(int,input().split()))
    if L[0]==1:
        x,y=L[1],L[2]
        S.add((x,y))
    elif L[0]==2:
        OK[L[1]]=1
    else:
        x,y=L[1],L[2]
        if OK[x]==1 or (x,y) in S:
            print("Yes")
        else:
            print("No")

##################################################################
[my AC]

N,M,Q=map(int,input().split())
A=[]
for i in range(N):
  A+=[set()]
ALL=set(list(range(M)))
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A[x-1].add(y-1)
  elif qr[0]==2:
    x=qr[1]
    A[x-1]=ALL
  else:
    x,y=qr[1],qr[2]
    if y-1 in A[x-1]:
      print('Yes')
    else:
      print('No')

##################################################################
[my TLE9]

N,M,Q=map(int,input().split())
A=[]
for i in range(N):
  A+=[set()]

for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A[x-1].add(y-1)
  elif qr[0]==2:
    x=qr[1]
    A[x-1]=set(list(range(M)))
  else:
    x,y=qr[1],qr[2]
    if y-1 in A[x-1]:
      print('Yes')
    else:
      print('No')

##################################################################
[my TLE,RE12]

import numpy as np
N,M,Q=map(int,input().split())
A=np.zeros((N,M))
ANS=['No','Yes']
for i in range(Q):
  qr=list(map(int,input().split()))
  if qr[0]==1:
    x,y=qr[1],qr[2]
    A[x-1][y-1]=1
  elif qr[0]==2:
    x=qr[1]
    A[x-1]=1
  else:
    x,y=qr[1],qr[2]
    v=A[x-1][y-1]
    print(ANS[int(v)])
    
##################################################################
