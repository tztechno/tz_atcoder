#########################################################
'''
N 個のブロックが並べられており、左から順に1,2,⋯,N と番号が付けられています。
以下の 2 種類の操作を何回か行うことで、すべてのブロックを取り除きたいです。
今ある中で 一番左のブロックを取り除く。今ある中で 一番右のブロックを取り除く。
ブロックi(i=1,2,⋯,N) をブロックPiより先に取り除いた場合、Ai点が得られます。
合計得点としてあり得る最大値を出力する
'''
##########################################################
#stpete WA
import itertools
from itertools import permutations
n=int(input())
P=[]
A=[]
for i in range(n):
  pi,ai=map(int,input().split())
  P+=[pi]
  A+=[ai]
def Point(orders):
  N=list(range(1,n+1))
  points=0
  for i in orders:
    q=P[i-1]
    if i in N:
      N.remove(i)
      if q in N:
        points+=A[i-1]
  return points
N2=list(range(1,n+1))
C0=list(permutations(N2))
POINTS=[]
for ci in C0:
  points=Point(list(ci))
  #print(ci,points)
  POINTS+=[points]
print(max(POINTS))
##########################################################
#stpete WA
import sys
input = sys.stdin.readline
n=int(input())
P=[None]*n
A=[None]*n
for i in range(n):
  P[i],A[i]=map(int,input().split())
N=list(range(1,n+1))
DP=[]
for i in range(n):
  DP+=[[0]*n]
AC=DP.copy()
for i in range(n):
  for j in range(n):
    if 0<i+j<n:
      Nij=N[i:n-j]
      print(i,j,Nij)
      if (i+j) not in Nij and P[i+j-1] in Nij:
        DP[i][j]+=A[i+j-1]
#print(DP)
for i in range(n):
  for j in range(n):
    if i==0 and 0<i+j<n:
      AC[i][j]=AC[i][j-1]+DP[i][j]
    elif j==0 and 0<i+j<n:
      AC[i][j]=AC[i-1][j]+DP[i][j]
    elif 0<i+j<n:
      AC[i][j]=max(AC[i-1][j]+DP[i][j],AC[i][j-1]+DP[i][j])
#print(AC)
MAX=0
for i in range(n):
  if MAX<max(AC[i]):
    MAX=max(AC[i])
print(MAX)
##########################################################
