###############################################
[claude,deepseek WA]
###############################################
###############################################
###############################################
[gemini AC]
# 改善版: より読みやすく、効率的な最小費用流による解法

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

from atcoder.mincostflow import MCFGraph

# 定数の改善: より小さな値で十分（オーバーフローリスクを減らす）
MAX_VALUE = max(max(row) for row in a)
B = MAX_VALUE + 1  # 元の値より少し大きい値で十分

# より明確な変数名
SOURCE = n * 2
SINK = n * 2 + 1
graph = MCFGraph(SINK + 1)

# エッジIDの管理を改善
grid_edges = [[0] * n for _ in range(n)]

# グラフ構築
# 1. SOURCE -> 各行（容量k: 各行で最大k個選択可能）
for i in range(n):
    graph.add_edge(SOURCE, i, k, 0)

# 2. 各列 -> SINK（容量k: 各列で最大k個選択可能）
for j in range(n):
    graph.add_edge(j + n, SINK, k, 0)

# 3. 行i -> 列(j+n)（容量1, コストB-a[i][j]で最大化を最小化に変換）
for i in range(n):
    for j in range(n):
        edge_id = graph.add_edge(i, j + n, 1, B - a[i][j])
        grid_edges[i][j] = edge_id

# 4. SOURCE -> SINK（必要な流量確保のため）
# 改善: 実際に必要な流量のみ（n*kは過大）
max_possible_flow = min(n * k, n * n)  # 実際に選択可能な最大数
graph.add_edge(SOURCE, SINK, max_possible_flow, B)

# 最小費用流実行
flow_result = graph.flow(SOURCE, SINK, max_possible_flow)
total_flow = flow_result[0]
total_cost = flow_result[1]

# 実際の最大値計算（改善: より明確な計算）
max_sum = B * total_flow - total_cost

print(max_sum)

# 解の復元
result_grid = [['.' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        edge = graph.get_edge(grid_edges[i][j])
        if edge.flow > 0:
            result_grid[i][j] = 'X'

# 出力
for row in result_grid:
    print(''.join(row))
###############################################
###############################################
###############################################
###############################################
[fac explanation]

提示されたコードは「行と列の選択制限付きでマスの和を最大化する問題」を **最小費用流 (Min Cost Flow)** を使って解く方法です。

---

## 1. 問題の理解

* $N \times N$ のマス目があり、各マス $(i,j)$ に値 $A_{i,j}$ がある。
* 選ぶマスを決める。
* 条件：

  * 各行から選ぶマスは **最大 K 個**。
  * 各列から選ぶマスは **最大 K 個**。
* 目的：選んだマスの総和を最大化。

ポイント：行・列制限付きで「和を最大化する」問題は **二部マッチング＋流量制限** として扱うと便利。

---

## 2. 最小費用流への変換

1. **二部グラフの構築**：

   * 左側の頂点：行 $i=0\ldots N-1$
   * 右側の頂点：列 $j=0\ldots N-1$
   * 辺：各マス $(i,j)$ から行頂点→列頂点へ容量 1、コスト $B - A_{i,j}$ の辺を張る

     * $B$ は大きな定数（例えば $1 \ll 50$）
     * ここで $B - A_{i,j}$ とする理由は「最小費用流で最大和を求める」ため

       * コストが小さいほど選ばれるので、`B - A[i][j]` をコストにすると大きい値のマスが優先される

2. **行・列の選択制限**：

   * 行頂点 $i$ から **開始ノード (start)** へ容量 $K$ の辺
   * 列頂点 $j$ から **終了ノード (goal)** へ容量 $K$ の辺
   * これにより各行・列の最大選択数が **K** に制限される

3. **フローの強制**：

   * `start` → `goal` に容量 $n*k$ の直接辺を作って、フローが必ず最大 $n*k$ 流れるようにしている
   * こうすることで最大和が保証される

---

## 3. フロー計算

```python
cost=graph.flow(start,goal,n*k)[1]
```

* 最小費用流を計算
* `graph.flow()` は `(フロー量, コスト)` を返す
* 最終的な **最大和** は以下で求められる：

$$
\text{最大和} = B \cdot n \cdot k - \text{最小コスト}
$$

---

## 4. 選んだマスの復元

```python
ans_grid=list(["."]*n for _ in range(n))
for i in range(n):
    for j in range(n):
        if graph.get_edge(edges[i][j]).flow>0:
            ans_grid[i][j]="X"
```

* 各行の各マスについて、フローが1なら選ばれたマス
* 選ばれたマスを `"X"`、選ばれなかったマスを `"."` として表示

---

## 6. まとめ

* **最大和問題** → **最小費用流問題** に変換
* 行・列の選択制限は容量制約として表現
* 「B - A\[i]\[j]」のコスト設定で、最小費用流が最大和を導く
* フローを確認して選んだマスを復元

---

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
