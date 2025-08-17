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

##################################################################
[baro]
N, M = map(int, input().split())
S = [input(), input()]
order = [0] * (N + 1)
for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    order[L] += 1
    order[R + 1] -= 1

for i in range(N):
    order[i + 1] += order[i]
    order[i] %= 2

ans = []
for i in range(N):
    ans.append(S[order[i]][i])

ans = "".join(ans)
print(ans)
##################################################################
[omon]
N, M = map(int, input().split())
S = input()
T = input()

cum = [0] * (N+1)

for _ in range(M):
    L, R = map(int, input().split())
    cum[L-1] += 1
    cum[R] -= 1

for i in range(N):
    cum[i+1] += cum[i]

ans = [S[i] if cum[i] % 2 == 0 else T[i] for i in range(N)]

print("".join(ans))
##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
S=input().strip()
T=input().strip()

X=[0]*(N+1)

for i in range(M):
    x,y=map(int,input().split())
    X[x-1]^=1
    X[y]^=1

for i in range(1,N+1):
    X[i]^=X[i-1]

#print(X)

ANS=[]

for i in range(N):
    if X[i]==0:
        ANS.append(S[i])
    else:
        ANS.append(T[i])

print("".join(ANS))
##################################################################
[MyAi AC]
N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

flip = [0] * (N + 1)  

for _ in range(M):
    l, r = map(int, input().split())
    flip[l-1] ^= 1
    flip[r] ^= 1

ans = []
cur = 0
for i in range(N):
    cur ^= flip[i]  
    if cur == 0:
        ans.append(S[i])
    else:
        ans.append(T[i])

print("".join(ans))

##################################################################

