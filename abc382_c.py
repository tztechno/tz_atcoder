#############################################


#############################################
#############################################
#############################################
#############################################
#############################################

N,M=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
Amin=[A[0]]
Aidx=[0]
for i in range(1,N):
    if Amin[-1]>A[i]:
        Amin.append(A[i])
        Aidx.append(i)

for b in B:
    if Amin[0]<=b:
        print(1)
        continue
    ng=0
    ok=len(Amin)
    while(abs(ng-ok)>1):
        mid=(ok+ng)//2
        if Amin[mid]<=b:
            ok=mid
        else:
            ng=mid
    if ok==len(Amin):
        print(-1)
    else:
        print(Aidx[ok]+1)

#############################################
[cannot understand]

import sys
input = sys.stdin.readline
from bisect import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

LIST=[]
now=1<<31

for i in range(N):
    if now>A[i]:
        LIST.append((A[i],i+1))
        now=A[i]

LIST.append((-1,-1,))
LIST.reverse()
ANS=[]

for i in range(M):
    x=B[i]
    k=bisect(LIST,(x,1<<30))
    ANS.append(LIST[k-1][1])

print(*ANS)

#############################################
[myTLE]

import sys
input = sys.stdin.readline
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
W=[]
for j in range(M):
  W+=[-1]
#print(W)
for j in range(M):
  for i in range(N):
    if A[i]<=B[j] and W[j]==-1:
      W[j]=i+1
for w in W:
  print(w)
#############################################

