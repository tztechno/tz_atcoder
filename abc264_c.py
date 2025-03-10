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
        for k in range(len(C)):
            D=[]
            for l in range(W1):
                if j & (1<<l) != 0:
                    D.append(C[k][l])
            C[k]=D
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

[MY ANS AC]
[list is faster than array]

from itertools import combinations

H1, W1 = map(int, input().split()) 
A0 = [list(map(int, input().split())) for _ in range(H1)] 
H2, W2 = map(int, input().split()) 
B0 = [list(map(int, input().split())) for _ in range(H2)]  
B=B0
for a_ind in combinations(range(H1), H2):
    for b_ind in combinations(range(W1), W2):
        A2 = [A0[i] for i in a_ind]                   
        A3 = [[row[j] for j in b_ind] for row in A2]  
        if A3 == B:  
            print('Yes')
            exit()
else:
  print('No')
  
##########################################################

[CGPT AC]

H1, W1 = map(int, input().split()) 
A0 = [list(map(int, input().split())) for _ in range(H1)] 
H2, W2 = map(int, input().split()) 
B0 = [list(map(int, input().split())) for _ in range(H2)]  
B=B0
# H1 ビットの中で 1 の数が H2 になるパターン
a_candidates = [i for i in range(1 << H1) if bin(i).count('1') == H2]
# W1 ビットの中で 1 の数が W2 になるパターン
b_candidates = [i for i in range(1 << W1) if bin(i).count('1') == W2]

for a_mask in a_candidates:
    for b_mask in b_candidates:
        # a_mask, b_mask のビット位置が 1 のインデックスを抽出
        a_ind = [i for i in range(H1) if (a_mask >> i) & 1]
        b_ind = [j for j in range(W1) if (b_mask >> j) & 1]
        A2 = [A0[i] for i in a_ind]                    
        A3 = [[row[j] for j in b_ind] for row in A2]   
        if A3 == B:  
            print('Yes')
            exit()
else:
  print('No')

##########################################################
