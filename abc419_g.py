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

##################################################################

##################################################################

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
