##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

import sys
input = sys.stdin.readline

H1,W1=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H1)]

H2,W2=map(int,input().split())
A2=[list(map(int,input().split())) for i in range(H2)]


for i in range(1<<H1):
    for j in range(1<<W1):

        C=[]

        for k in range(H1):
            if i & (1<<k) != 0 :
                C.append(A[k])

        #print(C)

        for k in range(len(C)):
            D=[]
            for l in range(W1):
                if j & (1<<l) != 0:
                    D.append(C[k][l])

            C[k]=D

        #print(C)

        if C==A2:
            print("Yes")
            exit()

print("No")

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
