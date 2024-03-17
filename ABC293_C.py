
#ABC293_C Make Takahashi Happy

################################################

total=H+W-2
for i in range(1<<total):
  for j in range(total):
    if i&(1<<j)!=0:#縦に進む場合
    else:#横に進む場合

<< 演算子は、ビット演算の左シフト演算子です。この演算子は、ビットパターンを左にシフトさせる際に使用されます。
    
具体的には、a << n は a のビットパターンを n ビット左にシフトさせます。

1 << n は、2のn乗の値を表すビットパターンを生成します。たとえば、1 << 3 は 0b1000 (2進数表記)、つまり8を表します。

与えられたコードでは、1 << total は、全ての可能な経路の組み合わせを表すビットマスクを生成するために使用されています。

たとえば、total=3 の場合、1 << total は 0b1000 (2進数表記)、つまり8を生成します。

次に、for i in range(1 << total): は、0から(1 << total) - 1までの範囲でループを回し、各ビットマスク i について処理を行います。

if i & (1 << j) != 0: は、i のビットマスクにおいて、j ビット目が1かどうかをチェックしています。

ビット演算子 & (ビット単位の論理積)を使って、i と 1 << j のビットパターンを比較しています。

この構造を使うことで、各ビットマスクから縦と横の移動を決定し、すべての可能な経路を生成することができます。

      
################################################
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
dict = defaultdict(int)
stamp = [[True for _ in range(w)] for _ in range(h)]
dy = [1, 0]
dx = [0, 1]
cnt = 0
def dfs(y, x):
  global cnt
  stamp[y][x] = False
  dict[A[y][x]] += 1
  if (y, x) in ((h - 1, w - 2), (h - 2, w - 1)):
    if dict[A[h - 1][w - 1]] == 0:
      cnt += 1
  else:
    for i in range(2):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < h and 0 <= nx < w:
        if stamp[ny][nx] and not dict[A[ny][nx]]:
          dfs(ny, nx)
  stamp[y][x] = True
  dict[A[y][x]] -= 1
dfs(0, 0)

print(cnt)
################################################
h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(list(map(int,input().split())))
ans=0
for bit in range(1<<(h+w-2)):
    record=[a[0][0]]
    i,j=0,0
    for shift in range(h+w-2):
        if bit>>shift&1:
            if i<h-1:
                i+=1
            else:
                break
        else:
            if j<w-1:
                j+=1
            else:
                break
        record.append(a[i][j])
    if len(set(record))==h+w-1:
        ans+=1
print(ans)
################################################
import sys
import copy
sys.setrecursionlimit(10**7)

H,W=map(int,input().split())
A=[]
for i in range(H):
    A.append(list(map(int,input().split())))
import sys
sys.setrecursionlimit(10**7)
global ans
ans=0
def dfs(x,y,X):
    if x<H and y<W:
        X.append(A[x][y])
        if len(X)==H+W-1:
            if len(set(X))==H+W-1:
                global ans
                ans+=1
        Y=copy.copy(X)
        dfs(x+1,y,Y)
        Y=copy.copy(X)
        dfs(x,y+1,Y)
    else:
        return
dfs(0,0,[])
print(ans)
################################################
import sys
input = sys.stdin.readline

H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]

ANS=0
for i in range(1<<(H+W-2)):
    x=0
    y=0

    flag=1
    SET={A[0][0]}

    for j in range(H+W-2):
        if i & (1<<j) != 0:
            if x+1<H and not(A[x+1][y] in SET):
                x+=1
                SET.add(A[x][y])
            else:
                flag=0
                break
        else:
            if y+1<W and not(A[x][y+1] in SET):
                y+=1
                SET.add(A[x][y])
            else:
                flag=0
                break

    ANS+=flag

print(ANS)

################################################

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(1 << (H + W - 2)):
    seen = set()
    pi = pj = 0
    seen.add(A[0][0])
    for j in range(H + W - 2):
        if (i >> j) & 1:
            pi += 1
        else:
            pj += 1
        if pi >= H or pj >= W:
            break
        if A[pi][pj] in seen:
            break
        seen.add(A[pi][pj])
    else:
        # print(pi, pj)
        if pi != H - 1 or pj != W - 1:
            continue
        ans += 1

print(ans)

################################################

H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

from itertools import product
ans=0
for pro in product((1,0),repeat=H+W-2):
    if sum(pro)!=H-1:continue
    st=set()
    st.add(A[0][0])
    x,y=0,0
    for i in range(H+W-2):
        if pro[i]==1:
            y+=1
        else:
            x+=1

        st.add(A[y][x])

    if len(st)==H+W-1:
        ans+=1

print(ans)

###############################################
### my revision using product w/AC

from itertools import product,permutations,combinations,accumulate

H,W=map(int,input().split())
A0=[]
for i in range(H):
  A0+=[list(map(int,input().split()))]

def check(ci):
  P=[0,0]
  R=[A0[0][0]]
  for cii in ci:
    if cii==0:
      P[1]+=1
    elif cii==1:
      P[0]+=1
    R+=[A0[P[0]][P[1]]]
  return R

D=['R']*(W-1)+['D']*(H-1)
C0=list(product((1,0),repeat=H+W-2))
C1=[]
for ci in C0:
  if sum(ci)==H-1:
    C1+=[ci]
#print(C1)
T=0
for ci in C1:
  R=check(ci)
  if len(set(R))==H+W-1:
    T+=1

print(T)
    
###############################################
# MYBEST w/TLE21
# permutations is the cause of delay

from itertools import product,permutations,combinations,accumulate

H,W=map(int,input().split())
A0=[]
for i in range(H):
  A0+=[list(map(int,input().split()))]

def check(ci):
  P=[0,0]
  R=[A0[0][0]]
  for cii in ci:
    if cii=='R':
      P[1]+=1
    elif cii=='D':
      P[0]+=1
    R+=[A0[P[0]][P[1]]]
  return R

D=['R']*(W-1)+['D']*(H-1)
C0=list(permutations(D))
C1=sorted(set(C0))

T=0
for ci in C1:
  R=check(ci)
  if len(set(R))==H+W-1:
    T+=1

print(T)
