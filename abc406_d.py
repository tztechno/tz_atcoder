##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[cgpt fix AC]

h, w, n = map(int, input().split())

H = [set() for _ in range(h)]
W = [set() for _ in range(w)]

for _ in range(n):
    x, y = map(int, input().split())
    H[x - 1].add(y - 1)
    W[y - 1].add(x - 1)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    
    if a == 1:
        print(len(H[b - 1]))
        for y in H[b - 1]:   ###
            W[y].discard(b - 1)  ###
        H[b - 1] = set()
    else:
        print(len(W[b - 1]))
        for x in W[b - 1]:  ###
            H[x].discard(b - 1)  ###
        W[b - 1] = set()
       
##################################################################
[my TLE]
h,w,n=map(int,input().split())

H=[]
for i in range(h):
  H+=[set()]
  
W=[]
for j in range(w):
  W+=[set()]

XY=[]
for i in range(n):
  x,y=map(int,input().split())
  H[x-1].add(y-1)
  W[y-1].add(x-1)

q=int(input())
for i in range(q):
  a,b=map(int,input().split())
  
  if a==1:
    print(len(H[b-1]))
    H[b-1]=set()
    for j in range(w):
      W[j].discard(b-1)
  
  else:
    print(len(W[b-1]))
    W[b-1]=set()
    for j in range(h):
      H[j].discard(b-1)
    
##################################################################
[my TLE,WA]

h,w,n=map(int,input().split())

H=[]
for i in range(h):
  H+=[set()]
  
W=[]
for j in range(w):
  W+=[set()]

XY=[]
for i in range(n):
  x,y=map(int,input().split())
  H[x-1].add(y-1)
  W[y-1].add(x-1)

q=int(input())
for i in range(q):
  a,b=map(int,input().split())
  
  if a==1:
    print(sum(H[b-1]))
    H[b-1]=set()
    for j in range(w):
      W[j].discard(b-1)
  
  else:
    print(sum(W[b-1]))
    W[b-1]=set()
    for j in range(h):
      H[j].discard(b-1)
    
##################################################################
[titia]

### Step-by-step Explanation

1. **Input Reading**:

   ```python
   H,W,N=map(int,input().split())
   ```

   Reads the grid dimensions and the number of marked points.

2. **Initialize Structures**:

   ```python
   HS=[set() for i in range(H+1)]
   WS=[set() for i in range(W+1)]
   ```

   * `HS[x]` stores the set of columns with marked cells in row `x`.
   * `WS[y]` stores the set of rows with marked cells in column `y`.

3. **Read Marked Cells**:

   ```python
   for i in range(N):
       x,y=map(int,input().split())
       HS[x].add(y)
       WS[y].add(x)
   ```

4. **Process Queries**:

   ```python
   Q=int(input())
   for tests in range(Q):
       L=list(map(int,input().split()))
       x=L[1]
       ...
   ```

   For each query:

   * If `L[0] == 1`, remove all marked points in row `x`.
   * Else, remove all marked points in column `x`.
   * In each case, remove the corresponding entries from both `HS` and `WS`.


##################################################################
[titia]

import sys
input = sys.stdin.readline

H,W,N=map(int,input().split())
HS=[set() for i in range(H+1)]
WS=[set() for i in range(W+1)]

for i in range(N):
    x,y=map(int,input().split())
    HS[x].add(y)
    WS[y].add(x)
Q=int(input())

for tests in range(Q):
    L=list(map(int,input().split()))
    x=L[1]
    if L[0]==1:
        ANS=0
        while HS[x]:
            k=HS[x].pop()
            ANS+=1
            WS[k].remove(x)
    else:
        ANS=0
        while WS[x]:
            k=WS[x].pop()
            ANS+=1
            HS[k].remove(x)

    print(ANS)
        
##################################################################
[my TLE,RE]
# ❌ 問題点：NumPyを使っているが意味がない・遅い

import numpy as np
H,W,N=map(int,input().split())
A=np.zeros((H,W))
XY=[]
for i in range(N):
  x,y=map(int,input().split())
  A[x-1][y-1]=1

Q=int(input())
for i in range(Q):
  a,b=map(int,input().split())
  if a==1:
    print(int(A[b-1].sum()))
    A[b-1]=0
  elif a==2:
    print(int(A[:,b-1].sum()))
    A[:,b-1]=0
      
##################################################################
