#####################################################
#####################################################
#####################################################
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
