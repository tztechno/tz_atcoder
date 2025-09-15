###############################################
32bit 整数に収まらない場合でも大丈夫
N種類セミ、Y年間、M種類大量発生する年が何回あるか
###############################################
問題文
AtCoder島にはN種類のセミが生息しています。種類iのセミ(1≤i≤N)はAi​の倍数の年にのみ大量発生します。
1年からY年までのY年間のうち、ちょうどM種類のセミが大量発生する年が何回あるかを求めてください。
制約
1≤M≤N≤20
1≤Y≤10**18
1≤Ai​≤10**18(1≤i≤N)
入力される値はすべて整数入力入力は以下の形式で標準入力から与えられる。
N　M　Y
A1​⋯AN​
出力答えを出力せよ。
入力例
3　2　16　
4　2　3
1年から16年までのうち、各種類のセミが大量発生するのは以下の年です。
種類1のセミは4,8,12,16年に大量発生する。
種類2のセミは2,4,6,8,10,12,14,16年に大量発生する。
種類3のセミは3,6,9,12,15年に大量発生する。
1年から16年までのうち、ちょうど2種類のセミが大量発生するのは4,6,8,16年の4回です。
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
[cgpt RE]
N, M, Y = map(int, input().split())
A = list(map(int, input().split()))
count = [0] * (Y + 1)
for a in A:
    for j in range(a, Y + 1, a):
        count[j] += 1
t = sum(1 for j in range(1, Y + 1) if count[j] == M)
print(t)
###############################################
[mybrain RE]
N,M,Y=map(int,input().split())
A=list(map(int,input().split()))
import numpy as np
S=np.zeros((N,Y))
for i in range(N):
  for j in range(1,Y+1):
    if j%A[i]==0:
      S[i][j-1]=1
t=0
for i in range(Y):
  if S[:,i].sum()==M:
    t+=1
print(t)
###############################################
[nani AC]
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
[was AC]
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
[coin AC]
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
[titia AC] 
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
[ai AC]

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
[cgpt AC]
import math
from itertools import combinations

N, M, Y = map(int, input().split())
A = list(map(int, input().split()))

# lcmがYを超えたらカウントに寄与しないので、その時点で打ち切り
def safe_lcm(a, b, limit):
    g = math.gcd(a, b)
    a_div = a // g
    if a_div > limit // b:
        return limit + 1
    return a_div * b

ans = 0

# 部分集合を全探索
for mask in range(1, 1 << N):
    bits = bin(mask).count("1")
    l = 1
    ok = True
    for i in range(N):
        if mask >> i & 1:
            l = safe_lcm(l, A[i], Y)
            if l > Y:
                ok = False
                break
    if not ok:
        continue
    cnt = Y // l
    if bits == M:
        ans += cnt
    if bits > M:
        # 包除原理で調整
        if (bits - M) % 2 == 1:
            ans -= math.comb(bits, M) * cnt
        else:
            ans += math.comb(bits, M) * cnt

print(ans)
###############################################

