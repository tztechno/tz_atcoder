##################################################################
長さNの整数列A=(A1​,A2​,…,AN​)が与えられます。
あなたの目的は、以下の操作を繰り返し行うことにより、Aのすべての長さLの連続部分列についてその総和がMの倍数であるようにすることです。
1≤i≤Nなる整数iを選び、Ai​の値を1増やす。
目的を達成するまでの操作回数として考えられる最小値を求めてください。
##################################################################
4 5 3
4 2 1 3
--------
4
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
