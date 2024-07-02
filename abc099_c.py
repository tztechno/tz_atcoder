#abc099_c.py
##############################
##############################
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -10**9
for i in range(1, 2**10):
	total = 0
	for j in range(N):
		count = 0
		for k in range(10):
			if i&(1<<k) and F[j][k] == 1:
				count += 1
		total += P[j][count]
	if total >= ans:
		ans = total
print(ans)
##############################
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -(10 ** 18)
for bit in range(1 << 10):
    if bit.bit_count() == 0:
        continue
    shop_open = [0] * N
    for i in range(N):
        for j in range(10):
            if bit >> j & 1 and F[i][j] == 1:
                shop_open[i] += 1
    X = 0
    for i in range(N):
        X += P[i][shop_open[i]]
    ans = max(ans, X)
print(ans)
##############################
[myans WA,TLE]
N=int(input())
F=[]
for i in range(N):
  F+=[list(map(int,input().split()))]
P=[]
for i in range(N):
  P+=[list(map(int,input().split()))]
import numpy as np
ANS=0
for i in range(1<<11):
  jar=np.array(list(bin(i)[2:].zfill(11))).astype(int)
  SM=0
  for j in range(N):
    sm=(np.array(P[j])*jar).sum()
    SM+=sm
  ANS=max(ANS,SM)
print(ANS)
##############################
