abc362_c.py
################################################
################################################
################################################
################################################
################################################
################################################
[titia]
import sys
input = sys.stdin.readline
N=int(input())
LR=[list(map(int,input().split())) for i in range(N)]
P=0
M=0
for l,r in LR:
    P+=l
    M+=r
if P<=0<=M:
    print("Yes")
else:
    print("No")
    exit()
Q=-P
X=[]
for l,r in LR:
    S=min(r-l,Q)
    X.append(l+S)
    Q-=S
print(*X)
################################################
################################################
[my ans TLE,RE]
import sys
input = sys.stdin.readline
N=int(input())
MIN,MAX=map(int,input().split())
R=[list(range(MIN,MAX+1))]
for i in range(1,N):
  l,r=map(int,input().split())
  MIN+=l
  MAX+=r
  R+=[list(range(l,r+1))]
from itertools import product,permutations,combinations,accumulate
C0=list(product(*R))
if MIN<=0<=MAX:
  print('Yes')
  for ci in C0:
    if sum(ci)==0:
      print(*ci)
      exit()  
else:
  print('No')
################################################
    
        
