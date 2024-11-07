
#############################################################

#############################################################

#############################################################
[my ans TLE]

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=[0]
for ai in A:
  B+=[(B[-1]+ai%M)%M]
from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
for i in range(1,N+1):
  for j in range(i,N+1):
    cnt[(B[j]-B[i-1])%M]+=1
ANS=0
for c in list(cnt):
  ANS+=c*cnt[c]
print(ANS)


#############################################################
[cannot understand]

#!/usr/bin/env python3
from itertools import accumulate
from atcoder.fenwicktree import FenwickTree


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0] + [x % M for x in accumulate(A)]
    ft = FenwickTree(M)

    s = 0
    ans = 0

    for r in range(N+1):
        ans += S[r] * r - s + ft.sum(S[r] + 1, M) * M
        s += S[r]
        ft.add(S[r], 1)
    print(ans)


if __name__ == '__main__':
    main()

#############################################################

from itertools import accumulate
from atcoder.fenwicktree import FenwickTree
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] + [x % M for x in accumulate(A)]
ft = FenwickTree(M)
s = 0
ans = 0
for r in range(N + 1):
    ans += S[r] * r - s + ft.sum(S[r] + 1, M) * M
    s += S[r]
    ft.add(S[r], 1)
print(ans)

#############################################################

import sys
input = sys.stdin.readline

N,mod=map(int,input().split())
A=list(map(int,input().split()))

for i in range(N):
    A[i]%=mod

S=[0]
for a in A:
    S.append(S[-1]+a)

ANS1=sum(S)
SUM=ANS1
for i in range(N):
    SUM-=A[i]*(N-i)
    ANS1+=SUM

LEN=mod+5

BIT=[0]*(LEN+1) # 1-indexedなtree. 配列BITの長さはLEN+1にしていることに注意。

def update(v,w): # index vにwを加える
    while v<=LEN:
        BIT[v]+=w
        v+=(v&(-v)) # v&(-v)で、最も下の立っているビット. 自分を含む大きなノードへ. たとえばv=3→v=4

def getvalue(v): # [1,v]の区間の和を求める
    ANS=0
    while v!=0:
        ANS+=BIT[v]
        v-=(v&(-v)) # 自分より小さい自分の和を構成するノードへ. たとえばv=14→v=12へ
    return ANS

now=0
ANS=0
update(A[0]+2,1)
for i in range(1,N):
    a=A[i]
    nec=(now-a)%mod

    # nec から nowまでのものを足し合わせる

    if nec<=now:
        ANS+=(getvalue(now-1+2)-getvalue(nec-1+2))*(N-i)
    else:
        ANS+=(getvalue(now-1+2) + getvalue(LEN) - getvalue(nec-1 + 2))*(N-i)

    update((nec+a)%mod + 2,1)

    now=nec

print(ANS1-ANS*mod)

#############################################################
