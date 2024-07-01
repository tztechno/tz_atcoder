abc075_c.py
graph_circle_bridge
######################################################
from collections import deque

n,m=map(int, input().split())
c=[0]+[list(map(int, input().split())) for _ in range(m)]
d=[[] for _ in range(n+1)]
v=deque()
v.append(1)
s=[False]*(n+1)
s[0]=True
s[1]=True
counts=0

for i in range(1,m+1):
  for j in range(1,m+1):
    if i == j:
      continue
    else:
      d[c[j][1]].append(c[j][0])
      d[c[j][0]].append(c[j][1])
  while v:
    k=v.popleft()
    for l in d[k]:
      if not s[l]:
        s[l]=True
        v.append(l)
  for p in range(n+1):
    if s[p]==False:
      counts+=1
      break
  d=[[] for _ in range(n+1)]
  v.append(1)
  s=[False]*(n+1)
  s[0]=True
  s[1]=True

print(counts)
######################################################
import sys
sys.setrecursionlimit(10**7)

n,m=map(int,input().split())
par=[i for i in range(n)]
def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def same(x,y):
    return find(x)==find(y)
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    par[x]=y

edges=[]
for i in range(m):
    a,b=map(int,input().split())
    edges.append((a-1, b-1))
ans=0
for i in range(m):
    par=[i for i in range(n)]
    for j in range(m):
        if i==j:
            continue
        a,b=edges[j]
        unite(a,b)
    for j in range(n-1):
        if not same(j,j+1):
            ans+=1
            break
print(ans)
######################################################
import sys

sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graphs = [[[] for _ in range(N)] for i in range(M)]

sides = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    sides.append([a, b])

for m in range(M):
    for m_idx in range(M):
        if m_idx == m:
            continue
        a, b = sides[m_idx]

        graphs[m][a].append(b)
        graphs[m][b].append(a)


def dfs(graph, v):
    seen[v] = True

    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v)


cnt = 0
for m in range(M):
    is_ok = True
    for i in range(N):
        seen = [False] * N
        dfs(graphs[m], i)
        if not min(seen):
            is_ok = False
            break
    if is_ok:
        cnt += 1

print(M - cnt)

######################################################
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
    
N, M = map(int, input().split())


edges = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i != j:
            a, b = edges[j]
            uf.union(a, b)
    temp = 0
    for n in uf.parents:
        if n < 0:
            temp += 1
    if temp >= 2:
        ans += 1
        
print(ans)
######################################################
######################################################
######################################################
######################################################
