###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[kom]
import sys
sys.setrecursionlimit(pow(10,9))

n=int(input())


list_graph=[[] for i in range(n+1)]

for i in range(1,n+1):
    a,b=map(int,input().split())
    list_graph[a].append(i)
    list_graph[b].append(i)

skills = [0]*(n+1)
skills[0] = 1

def dfs(i):
    skills[i]=1
    for ref_i in list_graph[i]:
        if not skills[ref_i]:
            dfs(ref_i)

dfs(0)

print(sum(skills)-1)
###############################################
[hob]
from collections import deque

N = int(input())
G = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    a, b = map(int, input().split())
    G[a].append(i)  # a->i, (a,b)=(0,0) の場合も含む
    if b:  # (a,b)=(0,0) の場合を含まない
        G[b].append(i)  # b->i

S = set()
vis = [False] * (N + 1)
vis[0] = True
que = deque([0])  # BFS
while que:
    u = que.popleft()
    for v in G[u]:
        if not vis[v]:
            vis[v] = True
            que.append(v)
            S.add(v)
print(len(S))

###############################################
[titia]
import sys
input = sys.stdin.readline

N=int(input())

OK=[0]*(N+1)
E=[[] for i in range(N+1)]

Q=[]

for i in range(N):
    a,b=map(int,input().split())

    if a==0 and b==0:
        OK[i+1]=1
        Q.append(i+1)
    else:
        E[a].append(i+1)
        E[b].append(i+1)

while Q:
    x=Q.pop()
    OK[x]=1

    for to in E[x]:
        if OK[to]==0:
            OK[to]=1
            Q.append(to)

print(sum(OK))

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
