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
[ere understand]

N, M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

B = [0]*(M+1) #係数はM+1ある
#桁の大きい方から決めていく、後ろから
for j in range(M,-1,-1): #Bの係数、M種類
  B[j] = C[N+j]//A[N] #B の係数が一つ決まる
  for i in range(N,-1,-1): #Aの係数、N種類
    C[i+j] -= A[i]*B[j] #一つ決まったB係数に関わるCをN種類修正して行く
    
  print("----------")
  print(j)
  print('A',A)
  print('B',B)
  print('C',C)

#print(*B)

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
