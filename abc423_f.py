###############################################
32bit 整数に収まらない場合でも大丈夫
N種類、Y年間、M種大量発生
大量発生する年が何回あるか
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[nani]
from math import gcd, comb

def popcount(x):
    return bin(x).count("1")

N, M, Y = map(int, input().split())

A = list(map(int, input().split()))

binom = {}

ans = 0
for mask in range(1 << N):
    count = popcount(mask)
    if count < M:
        continue
    lcm = 1
    for i in range(N):
        if (mask >> i) & 1:
            lcm = lcm * A[i] // gcd(lcm, A[i])
            if lcm > Y:
                break
    else:
        if (count, M) not in binom:
            binom[count, M] = comb(count, M)

        ans += (-1 if (count - M) & 1 else 1) * (Y // lcm) * binom[count, M]

print(ans)

###############################################
[was]
n, m, y = map(lambda s_: int(s_), input().split())
a = tuple(map(lambda s_: int(s_), input().split()))

from math import lcm

n2 = 1 << n
ls = [1]
for ai in a:
    ls += [lcm(e, ai) for e in ls]

f = [y // l for l in ls]
# print(ls)
# print(f)
for i in range(n):
    for bit in range(n2):
        if bit >> i & 1:
            f[bit ^ 1 << i] -= f[bit]
# print(f)
ans = sum(c for bit, c in enumerate(f) if bit.bit_count() == m)
print(ans)





###############################################
[coin]
n,m,y = [int(t) for t in input().split()]
a = [int(t) for t in input().split()]
from math import lcm

g = [1]*(1<<n)
for i in range(n): g[1<<i] = a[i]
for b in range(n):
    for mask in range(1<<n):
        if (mask>>b)&1 == 0:
            t = mask + (1<<b)
            if g[t] > y: continue
            g[t] = lcm(g[t],g[mask])

x = [y//e for e in g]
for b in range(n):
    for mask in range(1<<n):
        if (mask>>b)&1 == 0:
            t = mask + (1<<b)
            x[mask] -= x[t]

S = sum(x[e] for e in range(1<<n) if e.bit_count() == m)
print(S)
###############################################
[titia]
import sys
input = sys.stdin.readline

N=100
Combi=[[] for i in range(N+1)]
Combi[0]=[1,0]

for i in range(1,N+1):
    Combi[i].append(1)
    for j in range(i):
        Combi[i].append(Combi[i-1][j]+Combi[i-1][j+1])
    Combi[i].append(0)


from math import gcd,lcm

N,M,Y=map(int,input().split())
A=list(map(int,input().split()))

ANS=0
for i in range(1<<N):
    LCM=1
    count=0

    for j in range(N):
        if i & (1<<j) != 0:
            LCM=lcm(LCM,A[j])
            count+=1

        if LCM>Y:
            break

    #print(LCM,count,Y//LCM)

    if LCM<=Y and count>=M:
        if (count-M)%2==0:
            ANS+=Y//LCM*Combi[count][M]
        else:
            ANS-=Y//LCM*Combi[count][M]

print(ANS)

###############################################
[ai]

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, y_limit):
    if a == 0 or b == 0:
        return 0

    res_a = a // gcd(a, b)
    if b > y_limit // res_a:
        return y_limit + 1
    
    return res_a * b

def combinations(n, k):
    return math.comb(n, k)

def solve():
    N, M, Y = map(int, input().split())
    A = list(map(int, input().split()))

    if M == 0:

        print(0)
        return

    ans = 0
    
    for i in range(1, 1 << N):
        k = bin(i).count('1')

        if k < M:
            continue

        current_lcm = 1
        is_overflow = False

        for j in range(N):
            if (i >> j) & 1:
                current_lcm = lcm(current_lcm, A[j], Y)
                if current_lcm > Y:
                    is_overflow = True
                    break
        
        if is_overflow:
            continue

        S_k_contribution = Y // current_lcm
        
        term_sign = 1 if (k - M) % 2 == 0 else -1
        comb_val = combinations(k, M)
        
        ans += term_sign * comb_val * S_k_contribution

    print(ans)

if __name__ == "__main__":
    solve()

###############################################
