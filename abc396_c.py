##################################################

##################################################

##################################################

##################################################

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
