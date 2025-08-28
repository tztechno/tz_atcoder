##################################################################
問題文
N次多項式A(x)=AN​xN+AN−1​xN−1+⋯+A1​x+A0​とM次多項式B(x)=BM​xM+BM−1​xM−1+⋯+B1​x+B0​があります。
ここで、A(x),B(x)の各係数は絶対値が100以下の整数であり、最高次の係数は0ではありません。
また、それらの積をC(x)=A(x)B(x)=CN+M​xN+M+CN+M−1​xN+M−1+⋯+C1​x+C0​とします。
A0​,A1​,…,AN​およびC0​,C1​,…,CN+M​が与えられるので、B0​,B1​,…,BM​を求めてください。
ただし、与えられる入力に対して、条件をみたすB0​,B1​,…,BM​がただ一つ存在することが保証されます。
制約
1≤N<100
1≤M<100
∣Ai​∣≤100
∣Ci​∣≤106
AN​!=0
CN+M​!=0
条件をみたすB0​,B1​,…,BM​がただ一つ存在する。
#################################################################
NM
A0​A1​…AN−1​AN​
C0​C1​…CN+M−1​CN+M​
##################################################################
1 2
2 1
12 14 8 2
-------------
6 4 2
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[ere explanation]

---

### このコードのアルゴリズム

$A(x) \cdot B(x) = C(x)$ という関係において、
-   $A(x)$ の次数は $N$ (係数は $A_0, \dots, A_N$)
-   $B(x)$ の次数は $M$ (係数は $B_0, \dots, B_M$)
-   $C(x)$ の次数は $N+M$ (係数は $C_0, \dots, C_{N+M}$)

となっています。このコードは、$B$ の係数を $B_M, B_{M-1}, \dots, B_0$ の順に求めていきます。

---

### コードの動作解説

#### 1. 係数$B_M$を求める (ループの最初 `j=M`)
-   $C(x)$ の中で最も次数が高い項は $C_{N+M}x^{N+M}$ です。
-   この項は、$A(x)$ の最高次数項 ($A_N x^N$) と $B(x)$ の最高次数項 ($B_M x^M$) を掛け合わせた時にしか生まれません。
-   つまり、 $A_N \cdot B_M = C_{N+M}$ という関係が成り立ちます。
-   これを変形すると、$B_M = C_{N+M} / A_N$ となります。
-   コードの `B[j] = C[N+j] // A[N]` は、`j=M` のとき `B[M] = C[N+M] // A[N]` となり、まさしくこの計算をしています。

#### 2. $A(x) \cdot B_M x^M$ の影響を取り除く
-   $B_M$ が求まったので、今度は $C(x)$ から $A(x) \cdot (B_M x^M)$ の影響をすべて引き算します。
-   $A(x) \cdot B_M x^M = (A_N x^N + \dots + A_0) \cdot B_M x^M = (A_N B_M) x^{N+M} + \dots + (A_0 B_M) x^M$
-   この引き算を係数レベルで行っているのが内側のループ `C[i+j] -= A[i]*B[j]` です。`j=M` のとき、`i` が `N` から `0` まで動くことで、$C$ の係数 $C_{N+M}$ から $C_M$ までが更新されます。

#### 3. 係数$B_{M-1}$を求める (ループの2回目 `j=M-1`)
-   ステップ2によって、$C(x)$ から最高次数の影響が取り除かれました。
-   この更新された $C(x)$ における最高次数項は $C_{N+M-1}x^{N+M-1}$ です。
-   この項は、$A(x)$ の最高次数項 ($A_N x^N$) と、$B(x)$ の次に次数が高い項 ($B_{M-1} x^{M-1}$) を掛け合わせた時に生まれます。
-   したがって、ステップ1と同様に $A_N \cdot B_{M-1} = C_{N+M-1}$ (更新後のC) という関係から、$B_{M-1}$ を求めることができます。
-   この処理を、$j=0$ になるまで繰り返すことで、$B$ のすべての係数が求まります。

---

##################################################################
[ere]
#!/usr/bin/env python3
# abc245_d
# -min

def main():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    B = [0]*(M+1)
    
    for j in range(M,-1,-1):
        B[j] = C[N+j]//A[N]
        for i in range(N,-1,-1):
            C[i+j] -= A[i]*B[j]   
    
    print(*B)
    
if __name__ == '__main__':
    main()
##################################################################
[niji]
import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict, deque, Counter
import copy
from itertools import combinations, groupby, product, accumulate, permutations, combinations_with_replacement, accumulate
from bisect import bisect_right, bisect_left
import math
import heapq 
from functools import cmp_to_key
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, getcontext
dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#
N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

B = [0]*(M+1)
for j in range(M+1):
    count = 0
    for i in range(1, min(j, N)+1):
        count += B[j-i]*A[i]
    B[j] = (C[j]-count)//A[0]
print(*B[::-1])
##################################################################
[tos]
n,m=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
B=[0]*(m+1)
for i in range(m,-1,-1):
  B[i]=C[i+n]//A[n]
  for j in range(n+1):C[i+j]-=B[i]*A[j]
print(*B)
    
##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))

k=A[-1]
ANS=[]

for i in range(M,-1,-1):
    c=C[-1]
    x=c//k
    ANS.append(x)

    for j in range(len(A)):
        C[j+i]-=A[j]*x

    C.pop()

print(*ANS[::-1])

##################################################################
[myai RE]
N, M = map(int, input().split())
A = list(map(int, input().split()))      # 長さ N+1
C = list(map(int, input().split()))      # 長さ N+M+1

B = [0]*(M+1)

for k in range(M+1):
    s = 0
    # i は A のインデックス、B[k-i] が負にならないように
    for i in range(1, min(k, N)+1):
        s += A[i] * B[k-i]
    # A[0] != 0 は保証されているので整数割り算
    B[k] = (C[k] - s) // A[0]

print(*B)
##################################################################
[myai RE]
N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
B = [0] * (M + 1)
for k in range(M + 1):
    s = C[k]
    for i in range(1, min(N, k) + 1):
        s -= A[i] * B[k - i]
    B[k] = s // A[0]   
print(*B)
##################################################################
