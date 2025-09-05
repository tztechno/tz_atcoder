#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
[triv explain cgpt]

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
