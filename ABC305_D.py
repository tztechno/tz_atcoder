#################################

#RE
import sys
input = sys.stdin.readline
import numpy as np
 
n=int(input())
A=list(map(int,input().split()))
T=np.zeros((A[-1]+10))
 
for i in range(n//2):
  T[A[2*i+1]:A[2*i+2]]=1
 
q=int(input())
Q=[]
for i in range(q):
  l,r=map(int,input().split())
  print(int(T[l:r].sum()))
  
#################################
#titia 

import sys
input = sys.stdin.readline
from bisect import bisect

N=int(input())
A=list(map(int,input().split()))

SUM=[0]*(N+1)
for i in range(N):
    if i>0 and i%2==0:
        SUM[i+1]=SUM[i]+(A[i]-A[i-1])
    else:
        SUM[i+1]=SUM[i]
SUM.append(SUM[-1])

Q=int(input())
for tests in range(Q):
    x,y=map(int,input().split())
    k=bisect(A,x)
    if k>0 and k%2==0:
        s1=SUM[k+1]-(A[k]-x)
    else:
        s1=SUM[k+1]
    k=bisect(A,y)
    if k>0 and k%2==0:
        s2=SUM[k+1]-(A[k]-y)
    else:
        s2=SUM[k+1]
    print(s2-s1)
            
#################################
