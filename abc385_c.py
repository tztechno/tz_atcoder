
###############################################
'''
N棟のビルが等間隔に一列に並んでいます。
手前からi番目のビルの高さはHiです。
あなたは次の条件をともに満たすようにいくつかのビルを選んで電飾で飾ろうとしています。
* 選んだビルたちは高さが等しい
* 選んだビルたちは等間隔に並んでいる
最大でいくつのビルを選ぶことができますか？　
'''
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[my cgpt AC]
N=int(input())
H=list(map(int,input().split()))
from collections import defaultdict,deque,Counter
cnt = defaultdict(list)
H2=sorted(set(H))
for i,h in enumerate(H):
  cnt[h].append(i)
MAX=1
for h in H2:
  lst=cnt[h]
  k=len(lst)
  if k<=MAX:
    continue
  DP=[]
  for i in range(k):
    DP+=[defaultdict(int)]
  for j in range(k):
    for i in range(j):
      d=lst[j]-lst[i]
      DP[j][d]=max(DP[j][d],DP[i][d]+1)
      MAX=max(MAX,DP[j][d]+1)
print(MAX)
      
###############################################
[cgpt]　私の理解

ans = 1
for h, idxs in pos.items():
    k = len(idxs)
    if k <= ans:  # すでにこれより大きい答えがあるなら飛ばす
        continue

各高さの例数（各ビル）分のdictを準備して、
各ビルから見て、数列はどうなるか記録する
自分を終点と考えた時、幅と数列の長さ 
２次元に見えるだけで、１次元のdict、
dictが複数情報を持つ

    dp = [defaultdict(int) for _ in range(k)]
    # dp[j][d] = 長さ（idxs[i], idxs[j]) が公差 d の等差数列

    for j in range(k):後ろから
        for i in range(j):ひとつ前を仮定する
            d = idxs[j] - idxs[i]
            dp[j][d] = max(dp[j][d], dp[i][d] + 1)

これはdictへ結果の入力になっている

            ans = max(ans, dp[j][d] + 1)  # +1 で長さに換算

print(ans)

###############################################
[cgpt AC]

from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))

# 高さごとに出現位置を集める
pos = defaultdict(list)
for i, h in enumerate(H):
    pos[h].append(i)

ans = 1
for h, idxs in pos.items():
    k = len(idxs)
    if k <= ans:  # すでにこれより大きい答えがあるなら飛ばす
        continue

    dp = [defaultdict(int) for _ in range(k)]
    # dp[j][d] = 長さ（idxs[i], idxs[j]) が公差 d の等差数列

    for j in range(k):
        for i in range(j):
            d = idxs[j] - idxs[i]
            dp[j][d] = max(dp[j][d], dp[i][d] + 1)
            ans = max(ans, dp[j][d] + 1)  # +1 で長さに換算

print(ans)

###############################################
###############################################
###############################################
[titia]
import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

ANS=1
for i in range(n):
    for j in range(1,n):
        now=i
        score=0
        while True:
            if now<n and A[now]==A[i]:
                score+=1
            else:
                break
            now+=j

        ANS=max(ANS,score)

print(ANS)

###############################################
[my tita AC]

N=int(input())
H=list(map(int,input().split()))
ANS=1
for i in range(N):#start
  for j in range(1,N):#width
    now=i#右の先端
    count=0
    while True:
      if now<N and H[now]==H[i]:
        now+=j
        count+=1
      else:
        break
    ANS=max(ANS,count)
print(ANS)

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
