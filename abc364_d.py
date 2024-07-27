abc364_d.py
##################################################
##################################################
##################################################
##################################################
from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = []
K = []
for i in range(Q):
    b, k = map(int, input().split())
    B.append(b)
    K.append(k)

A.sort()
result = []

for i in range(Q):
    b = B[i]
    k = K[i]
    left = -1
    right = 10**9

    while left + 1 < right:
        mid = (left + right) // 2
        count = bisect_right(A, b + mid) - bisect_left(A, b - mid)
        if count >= k:
            right = mid
        else:
            left = mid
    
    print(right)


##################################################
[titia]
import sys
input = sys.stdin.readline

from bisect import bisect,bisect_left

N,Q=map(int,input().split())
A=list(map(int,input().split()))

A.sort()

for tests in range(Q):
    b,k=map(int,input().split())

    OK=10**9
    NG=-1

    while OK>NG+1:
        mid=(OK+NG)//2

        x=bisect(A,b+mid)
        y=bisect_left(A,b-mid)

        if x-y>=k:
            OK=mid
        else:
            NG=mid

    print(OK)
##################################################
[my TLE]
import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))

for i in range(Q):
  b,k=map(int,input().split())
  my_dict={}
  my_set=set()
  for a in A:
    if abs(a-b) in my_dict:
      my_dict[abs(a-b)] += 1
    else:
      my_set.add(abs(a-b))
      my_dict[abs(a-b)] = 1
  total=0
  for d in sorted(my_set):
    total+=my_dict[d]
    if total>=k:
      print(d)
      break
##################################################
