abc359_d.py
#################################################
#################################################
#################################################
[mizu]
M=998244353
n,k=map(int,input().split())
m=(1<<k)-1
s=[f"{i:0{k}b}"for i in range(1<<k)]
s=[int(i,2)for i in s if i!=i[::-1]]
d=[0]*2**k
S=input()
T,S=S[:k],S[k:]
t=[""]
for i in T:
    if i=="A":i="0"
    elif i=="B":i="1"
    else:i="01"
    t=[j+_ for j in t for _ in i]
for i in t:d[int(i,2)]+=1
for _ in S:
    p=[0]*2**k
    if _=="A":
        for i in s:p[i*2&m]+=d[i]
    elif _=="B":
        for i in s:p[(i*2&m)|1]+=d[i]
    else:
        for i in s:p[(i*2&m)|1]+=d[i];p[i*2&m]+=d[i]
    d=[i%M for i in p]
print(sum(d[i]for i in s)%M)
#################################################
[titia]
import sys
input = sys.stdin.readline

mod=998244353

N,K=map(int,input().split())
S=input().strip()

MAX=(1<<K)-1

SET=set()
for i in range(1<<K):
    SX=bin(i)[2:].zfill(K)
    #print(SX)
    if SX==SX[::-1]:
        SET.add(i)

DP=[0]*(1<<K)

if S[0]=="A":
    DP[0]=1
elif S[0]=="B":
    DP[1]=1
else:
    DP[0]=1
    DP[1]=1
for i in range(1,len(S)):
    #print(DP)
    s=S[i]
    NDP=[0]*(1<<K)
    for j in range(1<<K):
        if s=="A" or s=="?":
            NDP[(j*2) & MAX]=(NDP[(j*2) & MAX]+DP[j])%mod
        if s=="B" or s=="?":
            NDP[(j*2+1)& MAX]=(NDP[(j*2+1) & MAX]+DP[j])%mod

    DP=NDP

    if i>=K-1:
        #print(i)
        for j in SET:
            DP[j]=0

print(sum(DP)%mod)
        
        
#################################################
[my TLE]
from itertools import product,permutations,combinations,accumulate

N,K=map(int,input().split())
S=list(input())
mod=998244353

P=[]
for i in range(N):
  if S[i]=='?':
    P+=[i]

C=list(product(['A','B'],repeat=len(P)))

def judge2(N,K,S):
  T=1
  for i in range(N-K):
    si=S[i:i+K]
    t=0
    for j in range(K):
      if si[j]!=si[K-j-1]:
        t=1
        break
    if t==0:#回文
      T=0
      break
  return T #順列に対してT>0ならば+1
  
ANS=0
for ci in C:
  S2=S
  for p,cii in zip(P,ci):
    S2[p]=cii
  #print(S2)
  ans=judge2(N,K,S2)
  ANS+=ans
  #print(ans,S2)
print(ANS%mod)
#################################################
