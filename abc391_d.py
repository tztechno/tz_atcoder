####################################################


####################################################

####################################################


####################################################

####################################################


####################################################

####################################################


####################################################

####################################################


####################################################
[baro]

N, W = map(int, input().split())
pos = [[] for _ in range(W)]
vanished = [10**18] * N
for i in range(N):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    pos[X].append((Y, i))

min_cnt = 10**18
for p in pos:
    p.sort()
    min_cnt = min(min_cnt, len(p))

time = 0
for i in range(min_cnt):
    max_y = 0
    for x in range(W):
        max_y = max(max_y, pos[x][i][0] - time)
    for x in range(W):
        vanished[pos[x][i][1]] = time + max_y + 1
    time += max_y

ans = []
Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    A -= 1
    ans.append("Yes" if T < vanished[A] else "No")

for x in ans:
    print(x)

####################################################
[titia]

import sys
input = sys.stdin.readline
from heapq import heappop,heappush

N,W=map(int,input().split())

ANS=[1<<60]*N

H=[[] for i in range(W)]
for i in range(N):
    x,y=map(int,input().split())
    x-=1
    H[x].append((y,i))

for i in range(W):
    H[i].sort()

for ll in range(10**9):
    IND=[]
    MAX=0
    flag=1
    for i in range(W):
        if len(H[i])==ll:
            flag=0
            break
        else:
            height,ind=H[i][ll]
            MAX=max(MAX,height)
            IND.append(ind)

    if flag==0:
        break

    for ind in IND:
        ANS[ind]=MAX

#print(ANS)
        
Q=int(input())

for tests in range(Q):
    t,x=map(int,input().split())

    x-=1

    if ANS[x]<=t:
        print("No")
    else:
        print("Yes")

####################################################


