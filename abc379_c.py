#################################################################

#################################################################

#################################################################

#################################################################

#################################################################

#################################################################
N, M = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))
XA = list(zip(X,A))
XA.sort()
X, A = zip(*XA)
    
full = N*(N+1)//2

def check():
    if X[0] != 1:
        return False
    cnt = 0
    for i in range(M-1):
        cnt += A[i]
        if cnt < X[i+1] - 1:
            return False
    return True

if sum(A) == N:
    cnt = 0
    for i in range(M):
        full -= A[i]*X[i]
    if check(): print(full)
    else:print(-1)
else:
    print(-1)




#################################################################
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
X=list(map(int,input().split()))
A=list(map(int,input().split()))

LIST=[(X[i],A[i]) for i in range(M)]
LIST.sort()

X=[]
A=[]
for i in range(M):
    X.append(LIST[i][0])
    A.append(LIST[i][1])

if sum(A)!=N:
    print(-1)
    exit()

if X[0]!=1:
    print(-1)
    exit()

ANS=0
for i in range(M):
    now=X[i]

    if i==M-1:
        nec=N+1
    else:
        nec=X[i+1]

    if A[i]<nec-now:
        print(-1)
        exit()

    k=nec-now
    ANS+=k*(k-1)//2
    ANS+=(A[i]-k)*(nec-now)

    if i+1<M:
        A[i+1]+=A[i]-k

print(ANS)
    

#################################################################
[my ans WA19]

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
X=list(map(int,input().split()))
A=list(map(int,input().split()))

T=[]
X+=[N+1]
for i in range(1,M+1):
  T+=[X[i]-1-X[i-1]]

for ai,ti in zip(A,T):
  if ai!=ti+1:
    print(-1)
    exit()
else:
  ans=0
  for ai in A:
    ans+=ai*(ai-1)//2
print(ans)
  
#################################################################

