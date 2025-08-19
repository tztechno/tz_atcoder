##################################################################
問題文
頂点に1からNの番号がついたN頂点M辺の単純連結無向グラフが与えられます。
i番目の辺は頂点ui​と頂点vi​を結んでいます。
各k=1,2,…,N−1に対して、頂点1から頂点Nまでの単純パスであって、パスに含まれる辺の個数がkであるようなものの個数を求めてください。
制約
2≤N≤2×10**5
N−1≤M≤N+20
1≤ui​<vi​≤N
与えられるグラフは単純連結無向グラフ入力は全て整数
input
N M
u1 v1
u2 v2
...
##################################################################
sample1
5 6
1 2
1 3
2 4
3 4
3 5
4 5
---------
0 1 2 1
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
[kyopro]
import sys
sys.setrecursionlimit(10**9)

N,M=map(int,input().split())
G=[set() for _ in range(N)]

for _ in range(M):
  x,y=map(int,input().split())
  x-=1
  y-=1
  G[x].add((y,1))
  G[y].add((x,1))

vs=[]
for v in range(1,N-1):
  if len(G[v])==1:
    vs.append(v)

# 次数1の頂点を削除
for v in vs:
  for vv,_ in G[v]:
    G[vv].remove((v,1))
    if len(G[vv])==1 and vv!=0 and vv!=N-1:
      vs.append(vv)

# 次数2の頂点を縮約
for v in range(1,N-1):
  if len(G[v])==2:
    x,c=G[v].pop()
    y,d=G[v].pop()
    if x==y:
      continue
    G[x].remove((v,c))
    G[x].add((y,c+d))
    G[y].remove((v,d))
    G[y].add((x,c+d))

# 普通にdfs
ans=[0]*N
def dfs(v,dist,used):
  if v==N-1:
    ans[dist]+=1
    return
  used[v]=True
  for vv,c in G[v]:
    if not used[vv]:
      dfs(vv,dist+c,used)
  used[v]=False

dfs(0,0,[False]*N)

print(*ans[1:])

##################################################################
[toam]
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append((v, i))
    G[v].append((u, i))

deg = [len(g) for g in G]
T = [1] * N
st = [v for v in range(N) if v not in (0, N - 1) and deg[v] == 1]
while st:
    v = st.pop()
    if v == 0 or v == N - 1:
        continue
    T[v] = 0
    for u, _ in G[v]:
        deg[u] -= 1
        if deg[u] == 1:
            st.append(u)

num = 0
S = [-1] * N
for v in range(N):
    if v == 0 or v == N - 1 or (T[v] == 1 and deg[v] >= 3):
        S[v] = num
        num += 1
H = [[] for _ in range(num)]
used = [0] * M

for s in range(N):
    if S[s] == -1:
        continue
    for v, e in G[s]:
        if not T[v] or used[e]:
            continue
        used[e] = 1
        l = 1
        par, cur = s, v
        while T[cur] == 1 and S[cur] == -1 and deg[cur] == 2:
            g = [x for x in G[cur] if T[x[0]]]
            nxt, e2 = g[0] if g[0][0] != par else g[1]
            used[e2] = 1
            l += 1
            par, cur = cur, nxt
        H[S[s]].append((S[cur], l))
        H[S[cur]].append((S[s], l))

ans = [0] * N
vis = [0] * N

todo = [(0, 1, 0)]
while todo:
    v, bit, d = todo.pop()
    assert v < len(H)
    if v == len(H) - 1:
        ans[d] += 1
        continue
    for u, w in H[v]:
        if ((bit >> u) & 1) == 0:
            todo.append((u, bit | (1 << u), d + w))

print(*ans[1:])

##################################################################
[Claude RE]
from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def solve():
    N, M = map(int, input().split())
    
    # グラフの隣接リストを作成
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # dp[mask][v] = maskで表される頂点集合を訪問済みで、最後に頂点vにいる状態の数
    # ただし、Nが大きいのでビットマスクは使えない
    # 代わりに、長さ制限付きDFSを使用
    
    def count_simple_paths(start, end, exact_length):
        if exact_length == 0:
            return 1 if start == end else 0
        
        memo = {}
        
        def dfs(current, remaining, visited_mask):
            if remaining == 0:
                return 1 if current == end else 0
            
            key = (current, remaining, visited_mask)
            if key in memo:
                return memo[key]
            
            result = 0
            for neighbor in graph[current]:
                if not (visited_mask & (1 << neighbor)):
                    new_mask = visited_mask | (1 << neighbor)
                    result += dfs(neighbor, remaining - 1, new_mask)
            
            memo[key] = result
            return result
        
        initial_mask = 1 << start
        return dfs(start, exact_length, initial_mask)
    
    # Nが大きいのでビットマスクが使えない場合の代替実装
    def count_paths_backtrack(start, end, exact_length):
        def backtrack(current, remaining, visited):
            if remaining == 0:
                return 1 if current == end else 0
            
            count = 0
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    count += backtrack(neighbor, remaining - 1, visited)
                    visited.remove(neighbor)
            return count
        
        visited = {start}
        return backtrack(start, exact_length, visited)
    
    results = []
    for k in range(1, N):
        if N <= 20:  # 小さい場合はビットマスク版
            count = count_simple_paths(1, N, k)
        else:  # 大きい場合はバックトラック版
            count = count_paths_backtrack(1, N, k)
        results.append(count)
    
    print(*results)

if __name__ == "__main__":
    solve()
##################################################################
[Coplilot WA]
import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, _))
        adj[v].append((u, _))
    # まず木を作る(DFS/BFS)
    from collections import deque
    parent = [0]*(N+1)
    peid = [-1]*(N+1)
    depth = [0]*(N+1)
    used_edge = [False]*M
    q = deque([1])
    parent[1] = -1
    while q:
        v = q.popleft()
        for nv, eid in adj[v]:
            if parent[nv]==0:
                parent[nv]=v
                peid[nv]=eid
                depth[nv]=depth[v]+1
                used_edge[eid]=True
                q.append(nv)
    # 余分な辺
    ex_edges = []
    for i in range(M):
        if not used_edge[i]:
            ex_edges.append((i, edges[i]))
    K = len(ex_edges)
    # 各余分な辺について, サイクル上の辺集合(bitmask)を求める
    edge_idx = {}
    for i,(u,v) in enumerate(edges):
        edge_idx[(u,v)] = i
        edge_idx[(v,u)] = i
    cycles = []
    for eid,(u,v) in ex_edges:
        # uとvのLCAまでたどる
        path = set([eid])
        uu, vv = u, v
        while uu != vv:
            if depth[uu] > depth[vv]:
                path.add(peid[uu])
                uu = parent[uu]
            else:
                path.add(peid[vv])
                vv = parent[vv]
        cycles.append(path)
    # 各サイクルを使うかどうか(bit全探索)
    from collections import defaultdict
    count = defaultdict(int) # 長さ:個数
    for mask in range(1<<K):
        ban = set()
        for i in range(K):
            if (mask>>i)&1:
                ban ^= cycles[i]  # XOR集合
        # ban集合が重複していれば単純パスにならない（各辺1回まで）
        if len(ban)!=sum((mask>>i)&1 for i in range(K))*len(cycles[0]):
            # ただし、XOR合成（重複辺は消える）なので、banで1→Nパスをたどれるか判定必要
            pass  # 実はこの判定は不要、次に進む
        # 1→Nのパスを復元
        path = []
        v = N
        while v != 1:
            path.append(peid[v])
            v = parent[v]
        full_path = set(path)
        # サイクル追加
        full_path ^= ban
        # 構成できるか: 1→Nのパスになってるか
        # 各頂点の次数を数える
        deg = [0]*(N+1)
        for eid in full_path:
            u, v = edges[eid]
            deg[u] += 1
            deg[v] += 1
        if deg[1]!=1 or deg[N]!=1: continue
        ok = True
        for i in range(2,N):
            if deg[i]%2!=0: ok=False
        if not ok: continue
        count[len(full_path)] += 1
    # 出力
    res = []
    for k in range(1,N):
        res.append(str(count[k]))
    print(" ".join(res))

threading.Thread(target=main).start()
##################################################################
[MyAi TLE]
import sys
sys.setrecursionlimit(1 << 25)

N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

count = [0] * N  

visited = [False] * N

def dfs(u, length):
    if u == N - 1:
        count[length] += 1
        return
    for v in edges[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v, length + 1)
            visited[v] = False

visited[0] = True
dfs(0, 0)

ans=[]
for k in range(1, N):
    ans+=[count[k]]
print(*ans)
##################################################################
