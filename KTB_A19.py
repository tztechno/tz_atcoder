#######################################################

#stpete AC 
N,WL=map(int,input().split())
W=[0]
V=[0]
for i in range(N):
  w,v=map(int,input().split())
  W+=[w]
  V+=[v]
DP=[]
for i in range(N+1):
  DP+=[[0]*(WL+1)]
 
for i in range(1,N+1):
  for j in range(WL+1):
    if j-W[i]>=0:
      DP[i][j]=max(DP[i-1][j],DP[i-1][j-W[i]]+V[i])
    else:
      DP[i][j]=DP[i-1][j]
print(DP[N][WL])

#######################################################

#stpete TLE13/25

import numpy as np

N,w = map(int,input().split())
W=[]
V=[]
for i in range(N):
    wi,vi = list(map(int,input().split()))
    W+=[wi]
    V+=[vi]

DPWV=[]
for i in range(1<<N):
    DPWV+=[[]]

normal_mapping={'0':0,'1':1}
reverse_mapping={0:'0',1:'1'}

for i in range(1<<N):
    bi=list(bin(i)[2:].zfill(N))
    B=[]
    for bii in bi:
        B+=[normal_mapping[bii]]
    DPWV[i]=((np.array(W)*np.array(B)).sum(),(np.array(V)*np.array(B)).sum())

maxv=0
for dp in DPWV:
    if dp[0]<=w:
        maxv=max(maxv,dp[1])
print(maxv)

#######################################################
