###############################################
###############################################
###############################################

AtCoder の `atcoder` パッケージに含まれている **`DSU` (Disjoint Set Union)** について。

---

## 1. DSUとは

`DSU` は **Union-Find**（素集合データ構造）を実装したクラスです。

* 複数の要素をグループ分けして管理する
* 「2つの要素が同じグループか？」を効率よく判定できる
* 「2つのグループを結合する」操作を効率よく行える

グラフ問題や連結判定、クラスター分けなどでよく使われます。

---

## 2. 使い方

```python
from atcoder.dsu import DSU

# 要素数 n を持つDSUを作成
uf = DSU(n)
```

### メソッド一覧

1. **`uf.merge(a, b)`**

   * 要素 `a` と `b` を同じグループにまとめる。
   * すでに同じグループなら何も起きない。
   * 結果としてグループの代表（根）を返す。

2. **`uf.same(a, b)`**

   * 要素 `a` と `b` が同じグループかどうかを返す（`True`/`False`）。

3. **`uf.leader(a)`**

   * 要素 `a` が属するグループの代表（根）を返す。

4. **`uf.size(a)`**

   * 要素 `a` が属するグループの要素数を返す。

5. **`uf.groups()`**

   * すべてのグループをリストで返す。
   * `[[要素1, 要素2, ...], [要素3, ...], ...]` という形。

---

## 3. 簡単な例

```python
from atcoder.dsu import DSU

# 要素 0,1,2,3,4 を持つ
uf = DSU(5)

uf.merge(0, 1)
uf.merge(1, 2)

print(uf.same(0, 2))  # True（0,1,2は同じグループ）
print(uf.same(0, 3))  # False（3は別グループ）

print(uf.size(1))     # 3（グループ{0,1,2}の大きさ）
print(uf.groups())    # [[0,1,2], [3], [4]]
```

---

## 4. 計算量

* `merge`, `same`, `leader`, `size` は **ほぼ O(1)**（逆アッカーマン関数）。
* `groups` は全要素をなめるので O(n)。

効率的に連結成分を管理できるため、グラフや集合操作で多用されます。

---
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[hide]
import sys

sys.setrecursionlimit(20000000)

from collections import defaultdict
from typing import List

# UnionFind木
class UnionFind:
    """
    rollbackをデフォルトで装備済み
    計算量は、経路圧縮を行わないため、基本的なUnionFindの動作は、一回あたり、O(log N)
    rollbackは、一回あたり、O(1)で行える。
    """

    def __init__(self, n: int) -> None:
        self.size = n
        self.data = [-1] * n
        self.hist = []

    def leader(self, vtx: int) -> int:
        """
        頂点vtxの親を出力します
        """
        if self.data[vtx] < 0:
            return vtx

        return self.leader(self.data[vtx])

    def same(self, a: int, b: int):
        """
        aとbが連結しているかどうか判定します
        """
        return self.leader(a) == self.leader(b)

    def merge(self, a: int, b: int) -> bool:
        """
        aとbを結合します
        leaderが同じでも、履歴には追加します
        """
        ra, rb = self.leader(a), self.leader(b)

        # 履歴を作成する
        new_hist = [ra, rb, self.data[ra], self.data[rb]]
        self.hist.append(new_hist)

        if ra == rb:
            return False

        if self.data[ra] > self.data[rb]:
            ra, rb = rb, ra

        self.data[ra] += self.data[rb]
        self.data[rb] = ra

        return True

    def rollback(self):
        """
        undoします
        redoはありません
        """
        if not self.hist:
            return False

        ra, rb, da, db = self.hist.pop()
        self.data[ra] = da
        self.data[rb] = db
        return True

    def all(self) -> List[List[int]]:
        D = defaultdict(list)

        for i in range(self.size):
            D[self.leader(i)].append(i)

        res = []

        for l in D.values():
            res.append(l)

        return res


N, Q = map(int, input().split())
UF = UnionFind(N)

for _ in [0] * Q:
    t, u, v = map(int, input().split())

    if t == 0:
        UF.merge(u, v)
    else:
        print(int(UF.same(u, v)))

###############################################
[hana]
from atcoder.dsu import DSU

n,q = map(int, input().split())
uf = DSU(n)
for i in range(q):
    t,u,v = map(int, input().split())
    if t == 0:
        uf.merge(u,v)
    else:
     if uf.same(u,v):
           print(1)
     else:
         print(0)
###############################################
[titia]
N,Q=map(int,input().split())

Group = [i for i in range(N+1)] # グループ分け
Nodes = [1]*(N+1) # 各グループのノードの数

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:
            
            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)
            
        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)

for i in range(Q):
    t,u,v=map(int,input().split())
    if t==0:
        Union(u,v)
    else:
        if find(u)==find(v):
            print(1)
        else:
            print(0)
###############################################
[cgpt TLE9] #DFS/BFS
from collections import defaultdict, deque

def is_connected(edges, start, goal):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 無向グラフ想定
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        if node == goal:
            return 1
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return 0

N,Q=map(int,input().split())
T=[]
for i in range(Q):
  q=list(map(int,input().split()))
  if q[0]==0:
    u,v=q[1],q[2]
    T+=[(u,v)]
  elif q[0]==1:
    u,v=q[1],q[2]   
    print(is_connected(T,u,v))
    
###############################################
[cgpt AC] #unionFind
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
N,Q=map(int,input().split())

uf = UnionFind(N)
edges=[]
for i in range(Q):
  q=list(map(int,input().split()))
  if q[0]==0:
    u,v=q[1],q[2]
    uf.union(u, v)
  elif q[0]==1:
    u,v=q[1],q[2]  
    ans=uf.connected(u,v)
    if ans==True:
      print(1)
    else:
      print(0)
      
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
