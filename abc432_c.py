

###############################################
###############################################
###############################################
[titia]
import sys
input = sys.stdin.readline

N,X,Y=map(int,input().split())
A=list(map(int,input().split()))

A.sort()

MAX=Y*A[0]
k=Y-X
ANS=0

for a in A:
    MIN=X*a
    YS=(MAX-MIN)//k
    XS=a-YS

    if XS>=0 and YS>=0 and XS*X+YS*Y==MAX:
        ANS+=YS
    else:
        print(-1)
        exit()
###############################################
###############################################
###############################################
[tuc]
N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
x=[0]
for i in range(1,N):
    a=A[i]
    if Y*(A[0]-a)%(Y-X)!=0:
        print(-1)
        exit()
    xi=Y*(a-A[0])//(Y-X)
    x.append(xi)
m=min(x)
if m<0:
    for i in range(N):
        x[i]+=-m
ans=0
for i in range(N):
    if x[i]>A[i]:
        print(-1)
        exit()
    ans+=A[i]-x[i]
print(ans)
###############################################
###############################################
###############################################
###############################################
[shige]
N, X, Y = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
W = A[0] * Y
D = Y - X
for i in range(N):
    if (W - A[i]*X) % D != 0:
        print(-1)
        exit()
    if (W - A[i]*X) < 0 or (W - A[i]*X) > A[i] * (Y - X):
        print(-1)
        exit()
ans = 0
for i in range(N):
    ans += (W - A[i]*X) // D
print(ans)
###############################################
###############################################
[WA2]
N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
R=A[0]*Y
ans=0
for ai in A:
  qi = (R-ai*X)//(Y-X)
  pi = ai-qi
  ans+=qi
  if qi<0 or pi<0:
    print(-1)
    exit()
  #print(f"ai={ai}: pi={pi}, qi={qi}")
  #print(f"pi+qi={pi+qi}, pi*X+qi*Y={pi*X + qi*Y}")
print(ans)
###############################################
[TLE8,WA2]
N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
MX=A[0]*Y
MN=A[-1]*X
D=Y-X
#print(MX,MN)
ANS=[]
for R in range(MX,MN-1,-D):
  ans=0
  for ai in A:
    qi = (R-ai*X)//(Y-X)
    pi = ai-qi
    if qi>=0 and pi>=0:
      ans+=qi
  ANS+=[ans]
if len(ANS)==0:
  print(-1)
else:
  print(max(ANS))


###############################################
[TLE7,WA2]
N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
MX=A[0]*Y
MN=A[-1]*X
D=Y-X
#print(MX,MN)
ANS=[]
for R in range(MX,MN-1,-D):
  ans=0
  for ai in A:
    qi = (R-ai*X)//(Y-X)
    pi = ai-qi
    if qi<0 or pi<0:
      break
    ans+=qi
  ANS+=[ans]
if len(ANS)==0:
  print(-1)
else:
  print(max(ANS))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################

