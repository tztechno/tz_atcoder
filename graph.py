from collections import defaultdict,deque,Counter
graph = defaultdict(deque)
N=int(input())
for i in range(N):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
print(N)
print(g)
