######################################################
s = input()
t = input()
ls = len(s)
lt = len(t)
dp = [[0] * (lt+1) for _ in range(ls+1)] 
for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            p = 1
        else:
            p = 0
        dp[i+1][j+1] = max(dp[i][j]+p,dp[i][j+1],dp[i+1][j])
print(dp[-1][-1])
######################################################
s = input()
t = input()
dp = [[0]*(len(s)) for i in range(len(t))] 
for i in range(len(t)):
    for j in range(len(s)):
        if i == 0 and s[j] == t[i]:dp[i][j] = 1
        elif s[j] == t[i]:
            if j == 0:dp[i][j]=1
            else:dp[i][j] = max(dp[i-1][j-1]+1,dp[i][j-1],dp[i-1][j])
        else:
            if j == 0:dp[i][j] = dp[i-1][j]
            elif i == 0:dp[i][j] = dp[i][j-1]
            else:dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])
######################################################
S=input()
T=input()
N=len(S)
M=len(T)
dp=[[0 for j in range(M+1)]for i in range(N+1)]
for i in range(N):
    for j in range(M):
        dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j]+int(S[i]==T[j]))
print(dp[N][M])
######################################################
