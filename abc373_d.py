abc373_d.py

######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################

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
