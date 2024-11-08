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
[MY ANS TLE4]

import numpy as np
from itertools import product,permutations,combinations,accumulate

H1,W1=map(int,input().split())
A0=[]
for i in range(H1):
  A0+=[list(map(int,input().split()))]
H2,W2=map(int,input().split())
B0=[]
for i in range(H2):
  B0+=[list(map(int,input().split()))]

A=np.array(A0)
B=np.array(B0)

H=set()
for i in range(H1):
  Ai=A[i]
  for j in range(H2):
    Bj=B[j]
    if all(element in Ai for element in Bj):
      H.add(i)
if H==set():
  print('No')
  exit()

A2=A[list(H)]

W=set()
for i in range(W1):
  Ai=A2[:,i]
  for j in range(W2):
    Bj=B[:,j]
    if all(element in Ai for element in Bj):
      W.add(i)
if W==set():
  print('No')
  exit()
  
A3=A2[:,list(W)]
#print(A3.shape)

CH=list(combinations(list(range(A3.shape[0])),H2))
CW=list(combinations(list(range(A3.shape[1])),W2))
CP=list(product(CH,CW))
#print(A2)
for c in CP:
  #print(c)
  Ai=A3[list(c[0])]
  Ai2=Ai[:,list(c[1])]

  if np.array_equal(Ai2,B):
    print('Yes')
    exit()
else:
  print('No')
  
  
##########################################################
##########################################################
##########################################################
