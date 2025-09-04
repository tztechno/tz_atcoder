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

##################################################################
[rto]
MOD = 998244353
N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
  for j in range(K + 1):
    for k in range(1, M + 1):
      if j + k <= K:
        dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD
res = sum(dp[N][1:]) % MOD
print(res)
##################################################################
[wata]
n,m,k=map(int,input().split())
mod=998244353
dp=[[0]*(k) for _ in range(n)]
for i in range(m):
  dp[0][i]=1
#print(dp)
for i in range(1,n):
  for j in range(k):
    for l in range(max(0,j-m),j):
      #print(1)
      dp[i][j]+=dp[i-1][l]%mod
ans=0
for i in range(k):
  ans+=dp[-1][i]%mod
print(ans%mod)
##################################################################
[titia]
N,M,K= map(int,input().split())
mod=998244353
DP=[0]*(K+1)
DP[0]=1
for i in range(N):
    NDP=[0]*(K+1)
    for j in range(K+1):
        for k in range(1,M+1):
            if j+k>K:
                continue
            NDP[j+k]+=DP[j]
            #NDP[j+k]%=mod #無い方が早い
    DP=NDP
print(sum(DP)%mod)
##################################################################
[mybrain TLE]
n,m,k= map(int, input().split())
import itertools
M=list(range(1,m+1))
t=0
for v in itertools.product(M, repeat=n):
    if sum(v)<=k:
      t+=1
print(t%998244353)
##################################################################
[mybrain TLE]
from itertools import product,permutations,combinations,accumulate
n,m,k=map(int,input().split())
M=list(range(1,m+1))
C=list(product(M,repeat=n))
D=[]
for c in C:
  s=sum(c)
  D+=[s] 
mod=998244353
t=0
for d in D:
  if d<=k:
    t+=1
print(t%mod)
##################################################################
