##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[MyAi AC]
N, M = map(int, input().split())
S = list(input())
T = list(input())

# 差分配列（0/1 だけで管理するので ^ を使う）
diff = [0] * (N + 1)

for _ in range(M):
    l, r = map(int, input().split())
    diff[l-1] ^= 1   # 左端にXOR
    diff[r]   ^= 1   # 右端にXOR

cur = 0
for i in range(N):
    cur ^= diff[i]   # 累積XOR（= 区間フラグ反映）
    if cur:          # 1なら奇数回操作された
        S[i] = T[i]

print(''.join(S))
##################################################################
[MyAi AC]
N, M = map(int, input().split())
S = list(input())
T = list(input())

# 差分配列
diff = [0] * (N + 1)

for _ in range(M):
    l, r = map(int, input().split())
    diff[l-1] += 1
    diff[r] -= 1  # 範囲外処理のため r はそのまま

# 累積和をとって各位置の操作回数を求める
cur = 0
for i in range(N):
    cur += diff[i]
    if cur % 2 == 1:
        S[i] = T[i]

print(''.join(S))
##################################################################
[MyBrain TLE6]
N,M=map(int,input().split())
S=list(input())
T=list(input())
U=[0]*N
for i in range(M):
  l,r=map(int,input().split())
  for j in range(l-1,r):
    U[j]+=1
#print(U)
for k,ui in enumerate(U):
  if ui%2==1:
    S[k]=T[k]
#print(S)
print(''.join(S))
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

