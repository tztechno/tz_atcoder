###########################################
###########################################
###########################################
###########################################
###########################################
#TLE19
from collections import defaultdict,deque,Counter
N,T=map(int,input().split())
A=[0]*N
for i in range(T):
  a,b=map(int,input().split())
  A[a-1]+=b
  C=Counter(A)
  print(len(list(C)))
###########################################
#TLE19
from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
N,T=map(int,input().split())
for j in range(N):
  cnt[j+1]+=0
for i in range(T):
  a,b=map(int,input().split())
  cnt[a]+=b
  print(len(set(cnt.values())))
###########################################
#TLE19
N,T=map(int,input().split())
S=[0]*N
for i in range(T):
  a,b=map(int,input().split())
  S[a-1]+=b
  print(len(set(S)))
###########################################
