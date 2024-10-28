###########################################################
###########################################################
###########################################################
[my WA 1028]

N,M=map(int,input().split())

from collections import defaultdict,deque,Counter

cnt = defaultdict(deque)

for i in range(M):
  a,b=map(int,input().split())
  cnt[a-1].append(b-1)
  
VISITED=[False]*N
VISITED[0]=True
STACK=[0]
ANS=0
ANS2=[]

while STACK:
  now=STACK.pop()
  nxs=cnt[now]
  for ni in nxs:
    if 0 in nxs:
      ANS+=1
      ANS2+=[ANS]
    elif VISITED[ni]==False:
      VISITED[ni]=True
      ANS+=1
      STACK+=[ni]

if len(ANS2)==0:
  print(-1)
else:
  print(min(ANS2))
  
###########################################################
[good solution, perfectly undesrstand]

N,M=map(int,input().split())
G=[set() for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1;b-=1
    G[a].add(b)
dist=[1<<30 for _ in range(N)]
dist[0]=0
from collections import deque
Q=deque()
Q.append(0)
while Q:
    now=Q.popleft()
    for nxt in G[now]:
        if nxt==0:
            exit(print(dist[now]+1))
        if dist[nxt]==1<<30:
            dist[nxt]=dist[now]+1
            Q.append(nxt)
print(-1)

###########################################################
[giveup]

N=8**6
g=[[]for _ in range(N)]
for z in[*open(0)]:a,b=map(int,z.split());g[a]+=b,
Q=[1]
d=Q*N
for c in Q:
 for e in g[c]:
  if e<2:exit(print(d[c]))
  if d[e]<2:d[e]=d[c]+1;Q+=e,
print(-1)

###########################################################

import sys
input = sys.stdin.readline

from collections import deque

N,M=map(int,input().split())
E=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    E[a].append(b)

Q=deque()

DEPTH=[1<<60]*(N+1)
DEPTH[1]=0
Q=deque()
Q.append(1)

ANS=1<<60

while Q:
    x=Q.popleft()
    for to in E[x]:
        if to==1:
            ANS=min(ANS,DEPTH[x]+1)
        elif DEPTH[to]>DEPTH[x]+1:
            DEPTH[to]=DEPTH[x]+1
            Q.append(to)
if ANS>1<<40:
    print(-1)
else:
    print(ANS)

###########################################################
