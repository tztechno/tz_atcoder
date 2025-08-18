##################################################################
長さNの整数列A=(A1​,A2​,…,AN​)が与えられます。
あなたの目的は、以下の操作を繰り返し行うことにより、
Aのすべての長さLの連続部分列についてその総和がMの倍数であるようにすることです。
1≤i≤Nなる整数iを選び、Ai​の値を1増やす。
目的を達成するまでの操作回数として考えられる最小値を求めてください。
---------------------------------------
input is given as
N, M, L = map(int, input().split())
A = list(map(int, input().split()))
これに続くpythonコードを作る
##################################################################
sample input
4 5 3
4 2 1 3
--------
answer
4
##################################################################
7 10 4
7 0 9 1 6 4 2
--------------
10
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[CGPT WA]
N, M, L = map(int, input().split())
A = list(map(int, input().split()))

# 最初の区間和
S1 = sum(A[:L])

# L周期ごとにクラス分け
groups = [[] for _ in range(L)]
for i in range(N):
    groups[i % L].append(A[i])

# 各グループごとに「揃える候補余り」ごとのコストを計算
costs = []
for g in groups:
    group_cost = {}
    for r in range(M):
        c = 0
        for x in g:
            need = (r - (x % M)) % M
            c += need
        group_cost[r] = c
    costs.append(group_cost)

# 最小コスト探索
# ただし sum_r (選んだr * group_size) ≡ S1 (mod M) が成り立つ必要あり
from math import inf

dp = { (0, 0): 0 }  # (group_index, total_mod) -> min_cost

for idx, g in enumerate(groups):
    new_dp = {}
    for (i, mod), val in dp.items():
        for r, c in costs[idx].items():
            new_mod = (mod + r * len(g)) % M
            key = (i+1, new_mod)
            new_dp[key] = min(new_dp.get(key, inf), val + c)
    dp = new_dp

# 最終的に total_mod ≡ S1 (mod M) でなければならない
answer = dp.get((L, S1 % M), -1)

print(answer)

##################################################################
[GPTOSS AC]
import sys

INF = 10**18

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    N = next(it)
    M = next(it)
    L = next(it)
    A = [next(it) for _ in range(N)]

    # 1. prefixes
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i + 1] = pref[i] + A[i]

    # 2. c array
    W = N - L + 1            # number of windows
    c = [0] * W
    for k in range(W):
        s = pref[k + L] - pref[k]          # sum of window k (0‑based)
        c[k] = (-s) % M                   # cj

    # 3. d array
    d = [0] * (N)          # only indices 0 .. N-L-1 are used
    for k in range(N - L):
        d[k] = (c[k + 1] - c[k]) % M

    # 4. offsets for every position
    # positions are 0‑based
    offset = [0] * N
    for start in range(L):
        pos = start
        off = 0
        while pos < N:
            offset[pos] = off
            if pos + L < N:
                off = (off + d[pos]) % M
            pos += L

    # 5. contributions for each class
    contr = []              # list of lists
    for start in range(L):
        offs = []
        pos = start
        while pos < N:
            offs.append(offset[pos])
            pos += L
        # compute contribution for all a in 0..M-1
        arr = [0] * M
        for a in range(M):
            s = 0
            for off in offs:
                s += (a + off) % M
            arr[a] = s
        contr.append(arr)

    # 6. DP
    dp = [INF] * M
    dp[0] = 0
    for arr in contr:
        new = [INF] * M
        for r in range(M):
            if dp[r] == INF:
                continue
            base = dp[r]
            for a in range(M):
                nr = (r + a) % M
                val = base + arr[a]
                if val < new[nr]:
                    new[nr] = val
        dp = new

    ans = dp[c[0]]          # c1 = c[0]
    print(ans)

if __name__ == "__main__":
    solve()
##################################################################
[loop]
INF = 10**18

N, M, L = map(int, input().split())
A = list(map(int, input().split()))

cnt = [[0] * M for _ in range(L)]

for i in range(L):
    for j in range(M):
        for k in range(i, N, L):
            cnt[i][j] += (j - A[k]) % M

dp = [[INF] * M for _ in range(L + 1)]
dp[0][0] = 0

for i in range(L):
    for j in range(M):
        for k in range(M):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + cnt[i][(j - k) % M])

print(dp[L][0])

##################################################################
[ryu]
N, M, L = map(int, input().split())
A = list(map(int, input().split()))
INF = int(1e20)

cost = [[0]*M for _ in range(L)]

for i in range(N):
    for j in range(M):
        nj = (A[i] + j) % M
        cost[i%L][nj] += j

dp = [INF]*M
dp[0] = 0

for i in range(L):
    old = dp[:]
    dp = [INF]*M
    for j in range(M):
        for k in range(M):
            nk = (j+k) % M
            dp[nk] = min(dp[nk], old[j] + cost[i][k])

print(dp[0])
##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M,L=map(int,input().split())

A=list(map(int,input().split()))

X=[[0]*M for i in range(L)]

for i in range(N):
    k=i%L

    for j in range(M):
        X[k][(A[i]+j)%M]+=j

DP=[1<<60]*M
DP[0]=0

for i in range(len(X)):
    NDP=[1<<60]*M

    L=X[i]
    for j in range(M):
        for k in range(M):
            NDP[(j+k)%M]=min(NDP[(j+k)%M],DP[j]+L[k])

    DP=NDP

print(DP[0])
##################################################################
[MyAi AC]
N, M, L = map(int, input().split())
A = list(map(int, input().split()))

groups = [[] for _ in range(L)]
for i in range(N):
    groups[i % L].append(A[i])

class_costs = []
for g in groups:
    costs = []
    for x in range(M):
        cost = 0
        for a in g:
            cost += (x - a) % M
        costs.append((x, cost))
    class_costs.append(costs)

INF = 10**18
dp = [INF] * M
dp[0] = 0

for i in range(L):
    newdp = [INF] * M
    for mod in range(M):
        if dp[mod] == INF:
            continue
        for val, cost in class_costs[i]:
            new_mod = (mod + val) % M
            newdp[new_mod] = min(newdp[new_mod], dp[mod] + cost)
    dp = newdp

print(dp[0])
##################################################################
