##################################################

##################################################

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
