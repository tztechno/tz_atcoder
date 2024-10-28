#####################################################
#####################################################
#####################################################
[my TLE21 2024-10-28]

import sys
input = sys.stdin.readline
N,m=map(int,input().split())
M=list(range(1,m+1))
R=[]
for i in range(N):
  l,r=map(int,input().split())
  R+=[(l,r)]
T=[]
for i in range(1,m+1):
  for j in range(i,m+1):
    t=0
    for ri in R:
      if ri[0]>=i and ri[1]<=j: #ijが安全包含される
        t=1
        break
    if t==0: #どれにも完全包含されない
      T+=[(i,j)]
print(len(set(T)))
#print(set(T))
        

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
