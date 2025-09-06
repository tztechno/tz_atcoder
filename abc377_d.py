#####################################################
例題：「Lはループで小さくし、Rはminで小さくする」手法を使う典型的な問題をいくつか紹介します。

## 練習問題 1: 包含関係を扱う問題

### 問題
長さMの数列とN個の区間が与えられる。各位置lから始まる区間で、すべての与えられた区間と交差するものの個数を求めよ。

```python
def solve():
    N, M = map(int, input().split())
    P = [10**9] * (M+2)
    
    for _ in range(N):
        l, r = map(int, input().split())
        P[l] = min(P[l], r)
    
    R = M + 1
    ans = 0
    for L in range(M, 0, -1):
        R = min(R, P[L])
        # LからR-1までが条件を満たす
        ans += max(0, R - L)
    
    print(ans)

# テストケース
test_input = ["3 5", "1 3", "2 4", "3 5"]
```

## 練習問題 2: 最小値の伝播

### 問題
各位置iに値A[i]がある。各位置lから始まる連続部分列で、最大値が閾値K以下である最長の長さを求めよ。

```python
def solve_min_max():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 右から左へ処理して最小の「悪い」位置を見つける
    P = [N] * (N+2)  # P[i]: iから見て最初にA[j] > Kとなるj
    
    for i in range(N-1, -1, -1):
        if A[i] > K:
            P[i] = i
        else:
            P[i] = P[i+1] if i+1 < N else N
    
    R = N
    result = []
    for L in range(N-1, -1, -1):
        R = min(R, P[L])
        max_length = R - L
        result.append(max_length)
    
    result.reverse()
    print(*result)

# テストケース: N=5, K=3, A=[1,4,2,5,3]
```

## 練習問題 3: 貪欲な区間スケジューリング

### 問題
N個の仕事があり、各仕事は時間[L_i, R_i]で行われる。重ならないように選べる仕事の最大数を求めよ。

```python
def interval_scheduling():
    N = int(input())
    intervals = []
    max_r = 0
    for _ in range(N):
        l, r = map(int, input().split())
        intervals.append((l, r))
        max_r = max(max_r, r)
    
    # 各開始時間に対する最小終了時間
    P = [10**9] * (max_r+2)
    for l, r in intervals:
        P[l] = min(P[l], r)
    
    # 右から左へ処理
    R = max_r + 1
    count = 0
    current_time = max_r + 1
    
    for L in range(max_r, 0, -1):
        if P[L] < 10**9:  # この開始時間の仕事が存在
            if P[L] < current_time:  # 重ならない
                count += 1
                current_time = L
            else:
                # より早く終わる仕事を選ぶ
                if P[L] < R:
                    R = P[L]
        else:
            R = min(R, current_time)
    
    print(count)

# テストケース
test_intervals = [(1,3), (2,5), (4,6), (5,7)]
```

## 練習問題 4: 水位問題

### 問題
各位置iの高さH[i]が与えられる。各位置から右に見て、水位が下がらない最長の連続区間の長さを求めよ。

```python
def water_level():
    N = int(input())
    H = list(map(int, input().split()))
    
    # P[i]: iから右へ見て最初にH[j] < H[j-1]となる位置
    P = [N] * (N+2)
    
    for i in range(N-2, -1, -1):
        if H[i+1] < H[i]:
            P[i] = i+1
        else:
            P[i] = P[i+1]
    
    R = N
    result = []
    for L in range(N-1, -1, -1):
        R = min(R, P[L])
        length = R - L
        result.append(length)
    
    result.reverse()
    print(*result)

# テストケース: H = [1,2,3,2,1,4,3]
```

## 解き方のコツ

1. **逆方向処理**: 右から左へループ
2. **最小値伝播**: `R = min(R, P[L])`で制約を伝える
3. **連続性の利用**: 現在の状態を1変数で管理
4. **問題変換**: 求めたいものを「全区間数 - 条件を満たさない区間数」と考える

#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
[triv] 理解の核心部分
Lはループで小さくし、Rはminで小さくする
R = M+1 #右端から見る
ans = 0
for L in range(M, 0, -1):#L:1-M：L毎に空白区間をカウント
    R = min(R, P[L])#RはP[L]とは無関係の変数で、徐々に小さくなり、右側から見てminを取ることで「より大きく探している」
    ans += R - L
    print(L,R,P[L])
#####################################################
[triv explain cgpt] 理解不能

P = [inf] * (M+1)
for _ in range(N):
    l, r = map(int, input().split())
    P[l] = min(P[l], r)

* 区間 `[l, r]` が `N` 本与えられる。
* それぞれの始点 `l` に対して、最も右端が小さい `r` を記録する。
* つまり **始点ごとに最短の区間を残す**。

R = M+1
ans = 0
for L in range(M, 0, -1):
    R = min(R, P[L])   # L を左端とした区間の最小右端を反映
    ans += R - L       # [L, R) の長さを加算

* `L` を右から左へ（`M` から 1 へ）動かす。
* その時点での「到達可能な最小右端」を `R` として更新。
* 各 `L` ごとに **右端が `R` 未満の区間**の数を数えている。

### 何を数えているか？

* このコードは **長さ M の整数区間のうち、与えられた N 区間に含まれる「良い区間」の個数**を数えています。
* 各 `L` に対して、取りうる右端は `L+1, L+2, …, R-1` まで。
* よって `R - L - 1` 通りの区間が作れる。
* それを全部足すと `ans`。

[triv]
N, M = map(int, input().split())
inf = float("inf")
P = [inf] * (M+1)
for _ in range(N):
    l, r = map(int, input().split())
    P[l] = min(P[l], r)

R = M+1
ans = 0
for L in range(M, 0, -1):
    R = min(R, P[L])
    ans += R - L

print(ans)

#####################################################
[hello]
from sortedcontainers import SortedList

N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]

LR.sort()
SL = SortedList()

for i in range(N):
  SL.add(LR[i][1])
idx = 0
ans = 0

for i in range(1, M+1):
  while idx < N and SL and LR[idx][0] < i:
    SL.discard(LR[idx][1])
    idx += 1
  if SL:
    ans += SL[0] - i
  else:
    ans += M-i+1

print(ans)
#####################################################
[yta]
N, M = list(map(int, input().split()))

LR = [[] for _ in range(N)]
for i in range(N):
    LR[i] = list(map(int, input().split()))
sections = sorted(LR)

rcnt = [0] * (M + 1)
rlist = [[] for _ in range(M + 1)]

for l, r in sections:
    rlist[l].append(r)
    rcnt[r] += 1

ans = 0
r = 1
for l in range(1, M + 1):
    while r <= M and rcnt[r] == 0:
        r += 1
    ans += r - l
    #print(l, r, r - l, ans)

    for curr in rlist[l]:
        rcnt[curr] -= 1

print(ans)

#####################################################
[aki]
n, m = map(int, input().split())
c = [0] * m
for _ in range(n):
    l, r = map(int, input().split())
    c[r - 1] = max(c[r - 1], l)
for i in range(m - 1):
    c[i + 1] = max(c[i], c[i + 1])
print(sum([i - c[i] + 1 for i in range(m)]))
#####################################################
[triv]
N, M = map(int, input().split())
inf = float("inf")
P = [inf] * (M+1)
for _ in range(N):
    l, r = map(int, input().split())
    P[l] = min(P[l], r)

R = M+1
ans = 0
for L in range(M, 0, -1):
    R = min(R, P[L])
    ans += R - L

print(ans)
#####################################################
[my TLE21]
import sys
input = sys.stdin.readline
N,m=map(int,input().split())
M=list(range(1,m+1))
R=[]
for i in range(N):
  l,r=map(int,input().split())
  R+=[(l,r)]
T=[]
for i in range(1,m+1):
  for j in range(i,m+1):
    t=0
    for ri in R:
      if ri[0]>=i and ri[1]<=j: #ijが安全包含される
        t=1
        break
    if t==0: #どれにも完全包含されない
      T+=[(i,j)]
print(len(set(T)))
#print(set(T))
#####################################################
[titia]
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
LR=[list(map(int,input().split())) for i in range(N)]
LIST=[[] for i in range(M+2)]
for l,r in LR:
    LIST[l].append(r)
ANS=0
MIN=M+1
for i in range(M,0,-1):
    for r in LIST[i]:
        MIN=min(MIN,r)
    ANS+=MIN-i
    #print(i,MIN,ANS)
print(ANS)
#####################################################
