#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
[MY BEST ANS]
import random
import numpy as np

mod=998244353
N,M,K=map(int,input().split())
A0=[]
for i in range(N):
    a=list(map(int,input().split()))
    A0+=[a]
B0=[]
BT0=[]#LU
BT1=[]#LD
BT2=[]#RU
BT3=[]#RD
for i in range(M):
  b2=[]
  for j in range(3):
    b=list(map(int,input().split()))
    b2+=[b]
  B0+=[b2]
  BT0+=[b2[0][0]]
  BT1+=[b2[2][0]]
  BT2+=[b2[0][2]]
  BT3+=[b2[2][2]]
A=np.array(A0)
B=np.array(B0)

def nearest_index(lst, target):
    return min(range(len(lst)), key=lambda i: abs(lst[i] - target))
    
ANS=[]
for i in range(K*10):
  min_value = np.min(A)

  indices = np.where(A == min_value)
  p=indices[0][0]
  q=indices[1][0]

  if p<=N-3 and q<=N-3:
    m=nearest_index(BT0,mod-A[p][q])
    A[p:p+3,q:q+3]+=B[m]
    A[p:p+3,q:q+3]%=mod
    ANS+=[[m,p,q]]
  elif p>N-3 and q<=N-3:
    m=nearest_index(BT1,mod-A[p][q])
    A[p-2:p+1,q:q+3]+=B[m]
    A[p-2:p+1,q:q+3]%=mod
    ANS+=[[m,p-2,q]]
  elif p<=N-3 and q>N-3:
    m=nearest_index(BT2,mod-A[p][q])
    A[p:p+3,q-2:q+1]+=B[m]
    A[p:p+3,q-2:q+1]%=mod
    ANS+=[[m,p,q-2]]
  elif p>N-3 and q>N-3:
    m=nearest_index(BT3,mod-A[p][q])
    A[p-2:p+1,q-2:q+1]+=B[m]
    A[p-2:p+1,q-2:q+1]%=mod
    ANS+=[[m,p-2,q-2]]
  
  if len(ANS)==K:
    break
    
print(len(ANS))
for i in range(len(ANS)):
  print(*ANS[i])

#################################################################
