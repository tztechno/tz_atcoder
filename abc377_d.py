#####################################################
#####################################################
#####################################################
[my WA 2024-10-28]

import sys
input = sys.stdin.readline
N,M=map(int,input().split())
A=set(range(1,M+1))
for i in range(N):
  l,r=map(int,input().split())
  if l==r:
    M-=1
  elif l<r:
    for j in range(l,r):
      A-=set([j])
if M==0:
  print(0)
else:
  print(len(A)+M)


#####################################################

import sys
input = sys.stdin.readline

N,M=map(int,input().split())

LR=[list(map(int,input().split())) for i in range(N)]

LIST=[[] for i in range(M+2)]

for l,r in LR:
    LIST[l].append(r)

ANS=0
MIN=M+1

for i in range(M,0,-1):
    for r in LIST[i]:
        MIN=min(MIN,r)

    ANS+=MIN-i

    #print(i,MIN,ANS)

print(ANS)

#####################################################
