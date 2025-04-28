##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[my WA17,TLE16]

N,D=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(set(A))
from itertools import product,permutations,combinations,accumulate
C=list(combinations(B,2))
E=set()
for ci in C:
  if ci[1]-ci[0]==D:
    E.add(ci[1])
    E.add(ci[0])
print(len(E)//2)

##################################################################
[my TLE34]

N,D=map(int,input().split())
A=sorted(map(int,input().split()))
from itertools import product,permutations,combinations,accumulate
C=list(combinations(A,2))
E=set()
for ci in C:
  if ci[1]-ci[0]==D:
    E.add(ci[1])
    E.add(ci[0])
print(len(E)//2)

##################################################################
[titia]

import sys
input = sys.stdin.readline

N,D=map(int,input().split())
A=list(map(int,input().split()))

A.sort()

if D==0:
    ANS=0
    for i in range(1,N):
        if A[i]==A[i-1]:
            ANS+=1

    print(ANS)

    exit()

from collections import Counter

ANS=0
SA=sorted(set(A))
USE=[0]*1000010
C=Counter(A)
for a in SA:
    if USE[a]==0:
        LIST=[]

        x=a
        while C[x]>0:
            USE[x]=1
            LIST.append(C[x])
            x+=D

        #print(LIST)

        if len(LIST)==1:
            continue
        else:
            DP=[1<<63]*(len(LIST)+1)

            DP[0]=0

            for i in range(len(LIST)):
                DP[i+1]=min(DP[i+1],DP[i]+LIST[i],DP[i-1]+LIST[i])

            #print(LIST,DP)

            ANS+=min(DP[-1],DP[-2])

print(ANS)


##################################################################
