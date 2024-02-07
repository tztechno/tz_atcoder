// Max MEX ABC290_C


#########################
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a=set(a)
for i in range(k):
    if i not in a:
        print(i)
        exit()
print(k)

#########################

n, k = map(int, input().split())
a = list(map(int, input().split()))
se = set(a)
ans = set()

for i in sorted(list(se)):
    if len(ans) < k:
        ans.add(i)
    else:
        break
cnt = 0
for i, j in enumerate(sorted(list(ans))):
    if i == j:
        cnt += 1
    else:
        break 
   
print(cnt)
#########################

#!/usr/bin/env python3

import sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict

sys.setrecursionlimit(10**7)
input = lambda :sys.stdin.readline().rstrip()
MOD = 998244353


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = set(A)
    i = 0
    while i in B and i < K:
        i += 1
    print(i)



if __name__ == '__main__':
    main()
    
 #########################

def readints():
  return list(map(int, input().split()))

def deep_recursion():
  import sys
  import pypyjit
  sys.setrecursionlimit(550000)
  pypyjit.set_param('max_unroll_recursion=-1')

def main():
  N, K = readints()
  A = readints()
  A = sorted(set(A))

  for i in range(K):
    if i == len(A) or A[i] != i:
      print(i)
      return
  print(K)


if __name__ == '__main__':
  # import sys
  # flush = lambda: sys.stdout.flush()
  # deep_recursion()
  main()
#########################
