import sys
input = sys.stdin.readline

from heapq import heappop,heappush

N=int(input())
LIST=[list(map(int,input().split())) for i in range(N-1)]

DP=[1<<60]*(N)
DP[0]=0

Q=[(0,0)]

while Q:
    time,now=heappop(Q)

    if DP[now]!=time:
        continue
    if now==N-1:
        continue

    a,b,x=LIST[now]
    if DP[now+1]>DP[now]+a:
        DP[now+1]=DP[now]+a
        heappush(Q,(DP[now+1],now+1))

    if DP[x-1]>DP[now]+b:
        DP[x-1]=DP[now]+b
        heappush(Q,(DP[x-1],x-1))

print(DP[-1])
