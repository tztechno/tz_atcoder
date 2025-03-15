##################################################
[some]

N, M = map(int, input().split())
n, m = 0, 0
B = list(map(int, input().split()))
W = list(map(int, input().split()))
B.sort()
W.sort()
value = 0
while B and B[-1] >= 0:
    value += B.pop()
    n += 1

while W and W[-1] >= 0:
    if n == m:
        if B and W[-1] + B[-1] >= 0:
            value += W.pop() + B.pop()
            n += 1
            m += 1
        else:
            break
    else:
        value += W.pop()
        m += 1
print(value)
##################################################
[nata]

#累積和でMAX_W[i] = 白i個以下選ぶときの最大値

N,M = map(int,input().split())

B = list(map(int,input().split()))
W = list(map(int,input().split()))
B.sort(reverse=True)
W.sort(reverse=True)

SUM_W = [0]*(M+1)
for i in range(M):
  SUM_W[i+1] = SUM_W[i] + W[i]

MAX_W = [0]*(M+1)
for i in range(M):
  MAX_W[i+1] = max(MAX_W[i] , SUM_W[i+1])

SUM_B = [0]*(N+1)
for i in range(N):
  SUM_B[i+1] = SUM_B[i] + B[i]

ANS = (-1)*10**18
for i in range(N+1):
  if i <= M:
    ANS = max(ANS,SUM_B[i]+MAX_W[i])
  else:
    ANS = max(ANS,SUM_B[i]+MAX_W[-1])

print(ANS)
##################################################
[saturn]

n,m = map(int,input().split())
A = [*map(int,input().split())]
B = [*map(int,input().split())]
A.sort(reverse=True)
B.sort(reverse=True)
if (m < n):
    B += [0]*(n-m)
ans = 0
ta,tb,mb = 0,0,0
for i in range(n):
    ta += A[i]
    tb += B[i]
    mb = max(mb,tb)
    ans = max(ans,ta+mb)
print(ans)
##################################################
[titia]

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
B=list(map(int,input().split()))
W=list(map(int,input().split()))


B.sort(reverse=True)
W.sort(reverse=True)

SB=[0]
for b in B:
    SB.append(SB[-1]+b)

SW=[0]
for w in W:
    SW.append(SW[-1]+w)


for i in range(1,len(SW)):
    SW[i]=max(SW[i-1],SW[i])

while len(SW)<len(SB):
    SW.append(SW[-1])

ANS=0

for i in range(len(SB)):
    ANS=max(ANS,SB[i]+SW[i])

print(ANS)

##################################################
[cgpt AC]

N, M = map(int, input().split())
B = sorted(map(int, input().split()), reverse=True)
W = sorted(map(int, input().split()), reverse=True)

B3 = [0] * (N + 1)
W3 = [0] * (M + 1)

for i in range(N):
    B3[i + 1] = B3[i] + B[i]

for i in range(M):
    W3[i + 1] = W3[i] + W[i]

W_max = [0] * (M + 1)
W_max[0] = W3[0]
for i in range(1, M + 1):
    W_max[i] = max(W_max[i - 1], W3[i])

ANS = 0
for i in range(1, N + 1):
    ANS = max(ANS, B3[i] + W_max[min(i, M)])

print(ANS)
##################################################
