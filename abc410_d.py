
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

E=[[] for i in range(N)]

for i in range(M):
    a,b,w=map(int,input().split())
    a-=1
    b-=1
    E[a].append((b,w))

DP=[[0]*(1<<10) for i in range(N)]
DP[0][0]=1

Q=[(0,0)]

while Q:
    now,b=Q.pop()

    for to,w in E[now]:
        tob=b^w

        if DP[to][tob]==0:
            DP[to][tob]=1
            Q.append((to,tob))

MIN=1<<60
for i in range(1<<10):
    if DP[-1][i]==1:
        if i<MIN:
            MIN=i

if MIN>=(1<<50):
    print(-1)
else:
    print(MIN)
            
##################################################################
[myai WA]
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[a].append((b, w))

    reachable = [False] * (N + 1)
    q = deque([1])
    reachable[1] = True
    while q:
        u = q.popleft()
        for (v, _) in adj[u]:
            if not reachable[v]:
                reachable[v] = True
                q.append(v)
    if not reachable[N]:
        print(-1)
        return

    xor = [0] * (N + 1)
    visited = [False] * (N + 1)
    basis = [0] * 60 

    stack = [(1, False)]
    while stack:
        u, processed = stack.pop()
        if processed:
            for (v, w) in adj[u]:
                if visited[v]:
                    cycle_xor = xor[u] ^ xor[v] ^ w
                    if cycle_xor != 0:

                        x = cycle_xor
                        for i in reversed(range(60)):
                            if (x >> i) & 1:
                                if basis[i] == 0:
                                    basis[i] = x
                                    break
                                else:
                                    x ^= basis[i]
            continue
        if visited[u]:
            continue
        visited[u] = True
        stack.append((u, True))  
        for (v, w) in reversed(adj[u]):  
            if not visited[v]:
                xor[v] = xor[u] ^ w
                stack.append((v, False))

    res = xor[N]
    for i in reversed(range(60)):
        if (res >> i) & 1:
            if basis[i] != 0:
                res ^= basis[i]
    print(res)

if __name__ == "__main__":
    main()
##################################################################
[myai WA]
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 1-based indexing

for _ in range(M):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))

from collections import deque
def find_min_xor(N, adj):
    INF = 1 << 60
    xor = [0] * (N + 1)
    visited = [False] * (N + 1)
    basis = []

    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        u = q.popleft()
        for (v, w) in adj[u]:
            if not visited[v]:
                visited[v] = True
                xor[v] = xor[u] ^ w
                q.append(v)
            else:
                cycle_xor = xor[u] ^ xor[v] ^ w
                if cycle_xor != 0:
                    basis.append(cycle_xor)

    if not visited[N]:
        return -1

    min_xor = xor[N]
    for b in basis:
        min_xor = min(min_xor, min_xor ^ b)

    return min_xor

min_xor = find_min_xor(N, graph)
print(min_xor)

##################################################################
