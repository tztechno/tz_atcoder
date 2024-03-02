###########################################
#titia
import sys
input = sys.stdin.readline
from collections import Counter
N,T=map(int,input().split())
SCORE=[0]*N
C=Counter(SCORE)
NOW=1
for i in range(T):
    a,b=map(int,input().split())
    a-=1
    k=SCORE[a]
    C[k]-=1
    if C[k]==0:
        NOW-=1
    SCORE[a]+=b
    if C[SCORE[a]]==0:
        NOW+=1
    C[SCORE[a]]+=1
    print(NOW)
###########################################
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
