##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
DPの基本はforループです！
初心者はまずforループで書くことを覚える
慣れてきたら効率化（累積和など）を学ぶ
特別な理由がない限り、forループを使うのが安全で確実
「dpの計算では、forloopを使うことが基本」という理解は完璧です！✨
##################################################################
[deepseek AC]
MOD = 998244353
N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # 累積和の配列を作成
    prefix = [0] * (K + 2)
    for j in range(K + 1):
        prefix[j + 1] = (prefix[j] + dp[i][j]) % MOD
    
    for j in range(K + 1):
        # kの範囲: max(1, j - (K - M))からmin(M, j)まで
        left = max(0, j - M)
        right = min(j - 1, K)
        if left <= right:
            dp[i + 1][j] = (prefix[right + 1] - prefix[left]) % MOD
        else:
            dp[i + 1][j] = 0

res = sum(dp[N][1:K + 1]) % MOD
print(res)
##################################################################
[rto explain deepseek]
このコードは、動的計画法（DP）を用いて問題を解いています。
具体的には、サイコロをN回振ったときに出目の合計がK以下となる場合の数を求めています。
ただし、サイコロはM面で各面は1からMまでの整数です。

## コードの説明

1. **初期設定**:
   - MOD = 998244353: 答えをこの数で割った余りを求めるため
   - N, M, Kを入力: Nはサイコロを振る回数、Mはサイコロの面数、Kは合計の上限
   - dpテーブルを初期化: dp[i][j] = i回サイコロを振ったときに合計がjとなる場合の数
   - dp[0][0] = 1: 0回振ったときの合計0が初期状態

2. **DPの計算**:
   - 各i回目（0からN-1まで）について
   - 各合計値j（0からKまで）について
   - 各出目k（1からMまで）について
   - もしj+kがK以下なら、dp[i+1][j+k]にdp[i][j]を加算

3. **結果の計算**:
   - N回振ったときの合計値が1からKまでのすべての場合の数の和を求める
   - MODで割った余りを出力

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
