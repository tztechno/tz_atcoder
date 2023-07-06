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

import itertools
from itertools import permutations

N2=list(range(1,n+1))
C0=list(permutations(N2))
POINTS=[]
for ci in C0:
  points=Point(list(ci))
  #print(ci,points)
  POINTS+=[points]
  
print(max(POINTS))
##########################################################
