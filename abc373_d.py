abc373_d.py

######################################################
######################################################
DFS : set VISITED and STACK
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
[my TLE ans]

N,M=map(int,input().split())
from collections import defaultdict,deque
cnt = defaultdict(deque)
for i in range(M):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  cnt[u].append((v,w))
  cnt[v].append((u,-w))

VISIT=[False]*N
ANS=[0]*N
STACK=[]

for i in range(N):
  if VISIT[i]:
    continue
  VISIT[i]=True
  STACK+=[i]
  
  while STACK:
    u=STACK.pop()
    for v,w in cnt[u]:
      ANS[v]=ANS[u]+w
      VISIT[v]=True
      STACK+=[v]
      
print(*ANS)

######################################################

[my AC ans]

from collections import defaultdict,deque,Counter
N,M=map(int,input().split())
cnt = []
for i in range(N):
  cnt+=[[]]
for i in range(M):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  cnt[u].append((v,w))
  cnt[v].append((u,-w))
  
VISITED=[False]*N
ANS=[0]*N

for j in range(N):
  if VISITED[j]:
    continue
  VISITED[j]=True
  stack=[j]
  while stack:
    u=stack.pop()
    for v,w in cnt[u]:
      if VISITED[v]==False:
        ANS[v]=ANS[u]+w
        VISITED[v]=True
        stack+=[v]
      
print(*ANS)

######################################################
[my AC ans]

from collections import defaultdict,deque,Counter
cnt = defaultdict(deque)
N,M=map(int,input().split())
for i in range(M):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  cnt[u].append((v,w))
  cnt[v].append((u,-w))
  
VISITED=[False]*N
ANS=[0]*N

for j in range(N):
  if VISITED[j]:
    continue
  VISITED[j]=True
  stack=[j]
  while stack:
    u=stack.pop()
    for v,w in cnt[u]:
      if VISITED[v]==False:
        ANS[v]=ANS[u]+w
        VISITED[v]=True
        stack+=[v]
      
print(*ANS)

######################################################
[my WA ans]

from collections import defaultdict,deque,Counter

cnt = defaultdict(deque)
N,M=map(int,input().split())
for i in range(M):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  cnt[u].append((v,w))
  cnt[v].append((u,-w))
DONE=[False]*N
ANS=[0]*N
DONE[0]=True

for i in range(N):
  if cnt[i]:
    nexts=cnt[i]
    for nt in nexts:
      if DONE[nt[0]]==False:
        ANS[nt[0]]=ANS[i]+nt[1]
        DONE[nt[0]]=True
        
print(*ANS)

######################################################
[partially understand]

# 入力を読み込む
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, -w))

visited = [False] * N  # 値が確定しているかどうか
ans = [0] * N  # 書き込む値
for i in range(N):
    # すでに値が確定しているならばスキップ
    if visited[i]:
        continue
    # 頂点 i の値を 0 に確定し，探索を始める
    st = [i]
    visited[i] = True
    while st:
        # いま頂点 u にいる
        u = st.pop()
        # 頂点 u に隣接する頂点 v を調べる
        for v, w in G[u]:
            if not visited[v]:
                # まだ頂点 v の値が確定していないならば，頂点 u の値と整合的になるように，頂点 v の値を確定させる
                visited[v] = True
                ans[v] = ans[u] + w
                st.append(v)
print(*ans)

######################################################
[unique approach, not understand]

from heapq import heapify, heappop, heappush

n,m = map(int, input().split())
adjacents = {i: [[], []] for i in range(1, n+1)}


for _ in range(m):
    u,v, w = map(int, input().split())
    adjacents[u][0].append((v, w))
    adjacents[v][1].append((u, w))

values = {}

for i in range(1, n+1):
    if len(values.keys()) >=n: break
    if i in values: continue
    heap = [i]
    values[i] = 0
    while len(heap) >0:
        last = heappop(heap)
        for e, w in adjacents[last][1]:
            if e in values: continue
            values[e] = values[last] - w
            heappush(heap, e)

        for e, w in adjacents[last][0]:
            if e in values: continue
            values[e] = values[last] + w
            heappush(heap, e)

for i in range(1, n+1):
    print(values[i], end=" ")
  
######################################################
[PARTIALY UNDERSTAND]

import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
h = [[] for i in range(n)]
lim = 10**18
ans = [lim]*n

for i in range(m):
  u,v,w = map(int,input().split())
  h[u-1].append((v-1,w))
  h[v-1].append((u-1,-w))
  
def write(x):
  i = ans[x]
  for j in h[x]:
    r = j[0]
    w = j[1]
    if ans[r] == lim:
      ans[r] = i+w
      write(r)

for i in range(n):
  if ans[i] == lim:
    ans[i] = 0
    write(i)

print(*ans)
######################################################
[NOT UNDERSTAND]

from collections import defaultdict,deque

n,m=map(int,input().split())
edge=[list(map(int,input().split())) for _ in range(m)]
E=[[] for _ in range(n+1)]
for a,b,c in edge:
  E[a].append([b,c])
  E[b].append([a,-c])

ans=[-1]*(n+1)
S=set()
for i in range(1,n+1):
  if i in S:
    continue
  S.add(i)
  q=deque([i])
  ans[i]=0
  while q:
    x=q.popleft()
    for nx,c in E[x]:
      if nx in S:
        continue
      else:
        ans[nx]=ans[x]+c
        q.append(nx)
        S.add(nx)
print(*ans[1:])
######################################################
[NOT UNDERSTAND]

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
E=[[] for i in range(N)]

for i in range(M):
    a,b,w=map(int,input().split())
    a-=1
    b-=1

    E[a].append((b,w))
    E[b].append((a,-w))

ANS=[0]*N

Q=list(range(N))
while Q:
    x=Q.pop()
    for to,w in E[x]:
        if ANS[to]==ANS[x]+w:
            continue
        else:
            ANS[to]=ANS[x]+w
            Q.append(to)

print(*ANS)
######################################################
