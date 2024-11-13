##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

[not understand]

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for bit_h in range(1 << H1):
  tmp = []
  for i in range(H1):
    if bit_h & (1 << i):
      tmp.append(A[i][:])
  
  for bit_w in range(1 << W1):
    Flag = [False] * W1
    for j in range(W1):
      if bit_w & (1 << j):
        Flag[j] = True
    
    C = [[] for _ in range(len(tmp))]
    for i in range(len(tmp)):
      for j in range(W1):
        if Flag[j]:
          C[i].append(tmp[i][j])
    
    if B == C:
      exit(print("Yes"))

print("No")

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

[MY ANS TLE9]

from itertools import combinations
import numpy as np

H1, W1 = map(int, input().split()) 
A0 = [list(map(int, input().split())) for _ in range(H1)] 
H2, W2 = map(int, input().split()) 
B0 = [list(map(int, input().split())) for _ in range(H2)]  
B=np.array(B0)
for a_ind in combinations(range(H1), H2): 
  for b_ind in combinations(range(W1), W2): 
    A1=np.array(A0)
    A2=A1[list(a_ind)]
    A3=A2[:,list(b_ind)]
    if np.all(np.equal(A3,B)):
      print('Yes')
      exit()
else:
  print('No')


##########################################################
##########################################################
##########################################################
