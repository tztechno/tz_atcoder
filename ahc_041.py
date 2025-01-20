
###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

###############################################################

#入力とかいろいろ
import sys
sys.setrecursionlimit(10**6)
def LI():
    return list(map(int,input().split()))
N,M,H=LI()
A=LI()
g=[[] for _ in range(N)]
ans=[-1]*N
visited=[0]*N
for _ in range(M):
    u,v=LI()
    g[u].append((A[v],v))
    g[v].append((A[u],u))

for i in range(N):
    g[i].sort()

def dfs(now,prev,h):
    ans[now]=prev
    visited[now]=1
    if h==H:
        return
    for ai,nxt in g[now]:
        if visited[nxt]:
            continue
        dfs(nxt,now,h+1)
for i in range(N):
    if visited[i]:
        continue
    dfs(i,-1,0)
print(*ans)

###############################################################

import sys
input=sys.stdin.readline
from array import array
from collections import deque

n,m,h=map(int,input().split())
a=array("i",map(int,input().split()))
G=list(list() for _ in range(n))
for _ in range(m):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)
xy=list(list(map(int,input().split())) for _ in range(n))
V=array("i",[0]*n)
P=array("i",[-1]*n)
for i in range(n):
    if V[i]:
        continue
    V[i]=1
    P[i]=-1
    q=deque([[i,0]])
    while q:
        cur,cnt=q.popleft()
        for nxt in G[cur]:
            if V[nxt]:
                continue
            V[nxt]=1
            P[nxt]=cur
            if cnt+1<h:
                q.append([nxt,cnt+1])
print(*P)

###############################################################

[titia]

import sys
input = sys.stdin.readline

from random import randint
from collections import deque

N,M,H=map(int,input().split())
A=list(map(int,input().split()))
E=[[] for i in range(M)]

for i in range(M):
    x,y=map(int,input().split())
    E[x].append(y)
    E[y].append(x)

P=[list(map(int,input().split())) for i in range(N)]

Lweight=10**9
LANS=[-1]*N
LHeight=[-1]*N
for tt in range(100):
    # まず、適当にrootおよび高さの小さい幹の部分を決める。

    USE=[0]*N
    weight=0
    ANS=[-1]*N
    Height=[-1]*N
    count=0

    while min(USE)==0:
        root=randint(0,N-1)
        if USE[root]==1:
            continue

        USE[root]=1
        Height[root]=5
        weight+=A[root]

        count+=1
        #print(root,count,weight,USE.count(0))

        now=root

        for i in range(5):
            LIST=[]
            for to in E[now]:
                if USE[to]==1:
                    continue
                LIST.append((A[to],to))

            if LIST==[]:
                break
            
            _,to=min(LIST)

            weight+=A[to]
            ANS[now]=to
            USE[to]=1
            Height[to]=5-1-i
            now=to
        
        Q=deque([root])
        while Q:
            x=Q.popleft()
            if Height[x]>=10:
                continue
            for to in E[x]:
                if Height[to]==-1 or Height[to]>Height[x]+1:
                    Height[to]=Height[x]+1
                    ANS[to]=x
                    USE[to]=1
                    Q.append(to)
    
    #print(weight)

    if weight<Lweight:
        Lweight=weight
        LANS=ANS
        LHeight=Height

print(" ".join(map(str,LANS)))
    
###############################################################





