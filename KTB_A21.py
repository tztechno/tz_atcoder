##########################################################
#stpete AC, use DP
N=int(input())
P=[None]*(N)
A=[None]*(N)
for i in range(N):
  P[i],A[i]=map(int,input().split())
DP=[]
for i in range(N+1):
  DP+=[[0]*(N+1)]
#LEN is lenghth before removing
for LEN in range(N,1,-1): #LEN:N..2
  for L in range(0,N-1):
    R=L+LEN-1
    if R<=N-1:
      #print(L,R,LEN) #LR:0...N-1
      score0=score1=0
      if L+1<=P[L]-1<=R:
        score0=A[L]
      if L<=P[R]-1<=R-1:
        score1=A[R]
      DP[L+1][R]=max(DP[L+1][R],DP[L][R]+score0)
      DP[L][R-1]=max(DP[L][R-1],DP[L][R]+score1)
ANS=[]
for i in range(len(DP)):
  ANS+=[max(DP[i])]
print(max(ANS))

##########################################################
#stpete WA, use itertools
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
      Nij=N[i:n-j]   ####
      #print(i,j,Nij)
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
#stpete WA, use pop
import sys
input = sys.stdin.readline
n=int(input())
P=[None]*(n)
A=[None]*(n)
for i in range(n):
  P[i],A[i]=map(int,input().split())
N=list(range(1,n+1))
#print('N',N)
DP=[]
for i in range(n):
  DP+=[[0]*(n)]
AC=DP.copy()
def pop_left(lst, i):
    return [lst.pop(0) for _ in range(i)]
def pop_right(lst, j):
    return [lst.pop() for _ in range(j)]
for i in range(n):
  for j in range(n):
    if 0<i+j<n:
      Nij=N.copy()
      pop_left(Nij,i)      ####
      pop_right(Nij,j)     ####
      #print('Nij',i,j,Nij)
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
ANS=[]
for i in range(n):
  ANS+=[AC[n-1-i][i]]
print(max(ANS))
##########################################################
