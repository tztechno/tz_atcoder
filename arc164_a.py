
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
import numpy as np
T = int(input())

for t in range(T):
    n,k = map(int,input().split())
    t = sum(list(map(int,np.base_repr(n,3))))
    if n%2 == k%2 and k >= t:
        print("Yes")
    else:
        print("No")
#######################################
for _ in range(T := int(input())):
  N, K = map(int, input().split())
  dgt_sum = 0
  while N:
    dgt_sum += N%3
    N //= 3
  if dgt_sum <= K and dgt_sum%2 == K%2:
    print("Yes")
  else:
    print("No")
#######################################
[MY AC]

import math
T=int(input())
for i in range(T):
  n,k=map(int,input().split())
  m=int(math.log(n)/math.log(3))+1
  t=0
  for j in range(m,-1,-1):
    t+=n//(3**j)
    n=n%(3**j)
  if k<t:
    print('No')
  elif k==t:
    print('Yes')
  elif k>t:
    if (k-t)%2==0:
      print('Yes')
    else:
      print('No')

#######################################
