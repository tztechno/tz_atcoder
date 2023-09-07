##############################################
#stpete
#AC
import sys
input = sys.stdin.readline
INF = float("INF")
N,M=map(int,input().split())
C=[]
for i in range(M):
  C+=[int(input().replace(' ',''),2)]
#print(C)#クーポンを2進法で示す
DP=[INF]*(1<<N)#使ったクーポンの枚数を格納
DP[0]=0
#print('a,c,a|c')
for a in range(1<<N):# 既に確保した商品のリスト、何のクーポンを使ったか知らんけど
  for c in C:#クーポンを追加で1枚使うことを想定
    try:
      #print(a,c,a|c)
      DP[a|c]=min(DP[a|c],DP[a]+1)
    except:
      pass
#print(DP)
if DP[-1]==INF:
  print(-1)
else:
  print(DP[-1])
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
