#ABC248_C
#dice sum
#https://atcoder.jp/contests/abc248/tasks/abc248_c

N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0] * (K + 1) for _ in range(N)]
for j in range(1, M + 1):
    if j > K:
        break
    dp[0][j] = 1

for i in range(1, N):
    for j in range(K + 1):
        for k in range(1, M + 1):
            if j - k < 0:
                break
            dp[i][j] += dp[i - 1][j - k]
            dp[i][j] %= MOD

print(sum(dp[-1]) % MOD)

