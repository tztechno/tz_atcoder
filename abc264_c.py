##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
[my ans TLE]

H1,W1=map(int,input().split())
A0=[]
for i in range(H1):
  A0+=[list(map(int,input().split()))]
H2,W2=map(int,input().split())
B0=[]
for i in range(H2):
  B0+=[list(map(int,input().split()))]
import numpy as np
H=list(range(H1))
W=list(range(W1))
from itertools import product,permutations,combinations,accumulate
CH=list(combinations(H,H2))
CW=list(combinations(W,W2))
CP=list(product(CH,CW))
A=np.array(A0)
B=np.array(B0)
for c in CP:
  Ai=A[list(c[0])]
  Ai2=Ai[:,list(c[1])]
  if np.array_equal(Ai2,B):
    print('Yes')
    exit()
else:
  print('No')
  
##########################################################
##########################################################
##########################################################
