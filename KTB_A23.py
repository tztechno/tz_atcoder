##############################################
#stpete
#TLE1
import sys
input = sys.stdin.readline
from itertools import combinations
N,M=map(int,input().split())
M2=list(range(1,M+1))
S=[]
for i in range(M):
  S+=[list(map(int,input().split()))]
for t in range(1,M+1):
  C0=list(combinations(M2,t))
  for ci in C0:    
    T=[False]*N
    for cii in list(ci): 
      for i in range(N):
        T[i]|=bool(S[cii-1][i])
    if all(T):
      print(t)
      exit()
print(-1)
##############################################
#stpete
#TLE1
import sys
input = sys.stdin.readline
from itertools import combinations
N,M=map(int,input().split())
M2=list(range(1,M+1))
S=[]
for i in range(M):
  S+=[list(map(int,input().split()))]
for t in range(1,M+1):
  C0=list(combinations(M2,t))
  for ci in C0:
        
    T=[0]*N
    for cii in list(ci): 
      for i in range(N):
        T[i] or=S[cii-1][i]
        
    if 0 not in T:
      print(t)
      exit()
print(-1)
##############################################
