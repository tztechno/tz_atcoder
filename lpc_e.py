###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[fac explanation]

提供されたPythonコードは、この**二部マッチング問題**を**最小費用流**で解くためのものです。与えられた制約下で、各行と各列から最大K個のマスを選ぶという条件を満たしつつ、選ばれたマスの合計値を最大化します。

---

### 問題の解説

この問題は、**アサインメント問題**の拡張版と見なすことができます。
- **行**を**人**、**列**を**仕事**に対応させます。
- マス $(i, j)$ に書かれた数 $A_{i,j}$ を、人 $i$ が仕事 $j$ をしたときの**報酬**と見なします。
- 「どの行についても、選ばれたマスの個数は K 個以下」という制約は、「各人が担当できる仕事の数は最大 K 個」という条件に対応します。
- 「どの列についても、選ばれたマスの個数は K 個以下」という制約は、「各仕事に割り当てられる人の数は最大 K 個」という条件に対応します。

この問題の目的は、総報酬を最大化することです。これは、二部グラフにおける**最大重みマッチング**の一般化された問題です。

---

### 最小費用流への変換

最大化問題を最小化問題に変換し、最小費用流で解きます。

1.  **グラフの構築**:
    - **ソース** `start` と **シンク** `goal` を設けます。
    - **行**を表す $N$ 個の頂点（`0`から`N-1`）と、**列**を表す $N$ 個の頂点（`N`から`2N-1`）を作成します。
    - **ソースから行への辺**: `start`から各行の頂点 `i` へ、容量が `K`、費用が `0` の辺を張ります。これは、各行から最大 K 個のマスを選べるという制約を表現しています。
    - **列からシンクへの辺**: 各列の頂点 `j+N` から `goal` へ、容量が `K`、費用が `0` の辺を張ります。これは、各列から最大 K 個のマスを選べるという制約を表現しています。
    - **行から列への辺**: 各行の頂点 `i` から各列の頂点 `j+N` へ、容量が `1`、費用が $B - A_{i,j}$ の辺を張ります。ここで $B$ は $A_{i,j}$ の最大値よりも十分に大きな定数です（コードでは $10^9$ よりもはるかに大きな $1 << 50$ を使用）。この費用の設定により、マス $(i, j)$ を選ぶこと（対応する辺に流量が流れること）は、合計コストを $B - A_{i,j}$ だけ増加させます。$B - A_{i,j}$ が最小になるのは $A_{i,j}$ が最大になるときなので、この変換により**最大化が最小化に帰着**します。

2.  **流量の決定**:
    - 全ての行と列の制約を考慮すると、最大で $N \times K$ 個のマスを選ぶ可能性があります。
    - したがって、`start`から`goal`へ**合計 $N \times K$ の流量**を流し、その際の**最小費用**を求めます。

---

### 結果の出力

-   **最大合計値**: 最小費用流アルゴリズムで得られた**総費用**`cost`は、$\sum (B - A_{i,j})$ の最小値です。
    - 求める最大値は $B \times (\text{流した流量}) - \text{cost}$ で計算できます。
    - この問題では、流した流量が $N \times K$ なので、最大値は $B \times N \times K - \text{cost}$ となります。
-   **選んだマスの表示**: 最小費用流の解では、容量1の辺に流れた流量が**1**であれば、そのマスが選ばれたことを意味します。この情報を使って、マス $(i,j)$ に`X`、それ以外に`.`を配置してグリッドとして出力します。

###############################################
[fac]
n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
from atcoder.mincostflow import MCFGraph

B=1<<50
start,goal=n*2,n*2+1
graph=MCFGraph(goal+1)
edges=[[] for _ in range(n)]
for i in range(n):
    graph.add_edge(start,i,k,0)
for j in range(n):
    graph.add_edge(j+n,goal,k,0)
for i in range(n):
    for j in range(n):
        ei=graph.add_edge(i,j+n,1,B-a[i][j])
        edges[i].append(ei)
graph.add_edge(start,goal,n*k,B)
cost=graph.flow(start,goal,n*k)[1]
print(B*n*k-cost)
ans_grid=list(["."]*n for _ in range(n))
for i in range(n):
    for j in range(n):
        if graph.get_edge(edges[i][j]).flow>0:
            ans_grid[i][j]="X"

for row in ans_grid:
    print("".join(row))
  
###############################################
[blue]
from atcoder.mincostflow import MCFGraph

B = 1 << 50

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

graph = MCFGraph(N * 2 + 2)
start, goal = N * 2, N * 2 + 1

edges = [[-1] * N for _ in range(N)]
for i in range(N):
    graph.add_edge(start, i, K, 0)
    graph.add_edge(i + N, goal, K, 0)

    for j in range(N):
        edges[i][j] = graph.add_edge(i, j + N, 1, B - A[i][j])

graph.add_edge(start, goal, N * K, B)

_, cost = graph.flow(start, goal, N * K)
print(B * N * K - cost)

ans_grid = [['.'] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph.get_edge(edges[i][j]).flow > 0:
            ans_grid[i][j] = 'X'

for row in ans_grid:
    print(*row, sep='')


###############################################
[yuki]
import sys, re
from time import time
from itertools import permutations
from random import randint, shuffle
from functools import reduce, cmp_to_key
from math import gcd, inf, atan2, pi, lcm
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify
from operator import xor, add, itemgetter, or_
from atcoder.mincostflow import MCFGraph

input = sys.stdin.readline

rn = lambda: int(input())
rs = lambda: input().strip()
rl = lambda: list(map(int, input().split()))


def solve():
    (n, k) = rl()
    a = [rl() for _ in range(n)]
    src, dest = n * 2, n * 2 + 1

    b = 1 << 40

    def build_graph():
        graph = MCFGraph(n * 2 + 2)

        for i in range(n):
            for j in range(n):
                graph.add_edge(i, n + j, 1, b - a[i][j])

        for i in range(n):
            graph.add_edge(src, i, k, 0)
            graph.add_edge(n + i, dest, k, 0)
        graph.add_edge(src, dest, n * k, b)
        return graph

    graph = build_graph()
    flow, cost = graph.flow(src, dest, n * k)

    res = [['.'] * n for _ in range(n)]
    for edge in graph.edges():
        u, v, flow = edge.src, edge.dst, edge.flow
        if max(u, v) < n + n and flow == 1:
            res[u][v - n] = 'X'

    print(b * n * k - cost)
    [print(''.join(row)) for row in res]


solve()

###############################################
[fer]
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k_val = int(next(it))
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(next(it)))
        matriz.append(fila)
    
    total_nodos = 2 + 2 * n
    s = 0
    t = 1
    grafo = [[] for _ in range(total_nodos)]
    
    def agregar_arista(u, v, capacidad, costo):
        idx1 = len(grafo[u])
        idx2 = len(grafo[v])
        grafo[u].append([v, capacidad, costo, idx2])
        grafo[v].append([u, 0, -costo, idx1])
    
    for i in range(n):
        agregar_arista(s, 2 + i, k_val, 0)
    
    for j in range(n):
        agregar_arista(2 + n + j, t, k_val, 0)
    
    for i in range(n):
        for j in range(n):
            agregar_arista(2 + i, 2 + n + j, 1, -matriz[i][j])
    
    INF = 10**18
    costo_total = 0
    while True:
        dist = [INF] * total_nodos
        padre = [-1] * total_nodos
        idx_padre = [-1] * total_nodos
        en_cola = [False] * total_nodos
        cola = deque()
        dist[s] = 0
        cola.append(s)
        en_cola[s] = True
        
        while cola:
            u = cola.popleft()
            en_cola[u] = False
            for idx, arista in enumerate(grafo[u]):
                v, cap, costo, rev_idx = arista
                if cap > 0:
                    nueva_dist = dist[u] + costo
                    if nueva_dist < dist[v]:
                        dist[v] = nueva_dist
                        padre[v] = u
                        idx_padre[v] = idx
                        if not en_cola[v]:
                            en_cola[v] = True
                            cola.append(v)
        
        if dist[t] == INF or dist[t] > 0:
            break
        
        flujo = 1
        costo_total += flujo * dist[t]
        v = t
        while v != s:
            u = padre[v]
            idx_arista = idx_padre[v]
            arista = grafo[u][idx_arista]
            arista[1] -= flujo
            rev_arista = grafo[v][arista[3]]
            rev_arista[1] += flujo
            v = u
    
    resultado = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        nodo_u = 2 + i
        for arista in grafo[nodo_u]:
            v, capacidad, costo, rev_idx = arista
            if 2 + n <= v < 2 + 2 * n:
                j = v - (2 + n)
                if 0 <= j < n and capacidad == 0:
                    resultado[i][j] = 'X'
    
    print(-costo_total)
    for fila in resultado:
        print(''.join(fila))

if __name__ == '__main__':
    main()

###############################################
