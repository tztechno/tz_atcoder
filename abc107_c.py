abc107_c.py
############################################################
############################################################
N,K = list(map(int,input().split()))
x = list(map(int,input().split()))
ans = float("inf")
for i in range(N-K+1):
    m = min(x[i],0)
    M = max(x[i+K-1],0)
    dist = min(abs(m)*2+abs(M),abs(M)*2+abs(m))
    ans = min(ans,dist)
print(ans)
############################################################
N,K=map(int,input().split())
C=list(map(int,input().split()))
import bisect
x=bisect.bisect_right(C,0)
#最初左に行く場合
if x>=K:
    ANS=-(C[x-K])
else:
    ANS=10**10
for i in range(1,min(x+1,K+1)):
    if x-i+K-1>=N:
        continue
    elif ANS>=C[x-i+K-1]-2*C[x-i]:
        ANS=C[x-i+K-1]-2*C[x-i]
CC=[None]*N
for i in range(N):
    CC[i]=-C[i]
CC.reverse()
x=bisect.bisect_right(CC,0)
if x>=K:
    if ANS>-(CC[x-K]):
        ANS=-(CC[x-K])
for i in range(1,min(x+1,K)):
    if x-i+K-1>=N:
        continue
    elif ANS>=CC[x-i+K-1]-2*CC[x-i]:
        ANS=CC[x-i+K-1]-2*CC[x-i]
print(ANS)
############################################################
[my RE]
N,K=map(int,input().split())
X=list(map(int,input().split()))
M=[]
P=[]
for x in X:
  if x>=0:
    P+=[x]
  else:
    M+=[-x]
M.sort()
P.sort()
if len(M)==0:
  print(P[K-1])
  exit()
if len(P)==0:
  print(M[K-1])
  exit()
ANS=[]
for i in range(1,len(M)):
  j=K-i
  ANS+=[min(M[i-1]*2+P[j-1],M[i-1]+P[j-1]*2)]
print(min(ANS))
############################################################
