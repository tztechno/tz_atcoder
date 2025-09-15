
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[cgpt AC explanation]
このコードは**Treap**（Tree + Heap）と呼ばれる平衡二分探索木を使用して、木材の切断とクエリ処理を行うプログラムです。以下に詳細な説明をします。

## 全体の概要
- 長さLの木材があり、Q個のクエリを処理します
- クエリタイプ1: 位置xで木材を切断
- クエリタイプ2: 位置xを含む木材片の長さを出力

## データ構造: Treap
```python
class TreapNode:
    __slots__ = ("key", "priority", "left", "right")
    def __init__(self, key):
        self.key = key          # 切断位置の座標
        self.priority = random.random()  # 優先度（ランダム）
        self.left = None        # 左子ノード
        self.right = None       # 右子ノード
```
- **二分探索木の性質**: 左子孫 < 親 < 右子孫
- **ヒープの性質**: 親の優先度 > 子の優先度
- これにより平衡が保たれ、効率的な操作が可能

## 主要関数の説明

### 1. `split(root, key)`
```python
def split(root, key):
    if not root:
        return (None, None)
    if key < root.key:
        l, root.left = split(root.left, key)
        return (l, root)
    else:
        root.right, r = split(root.right, key)
        return (root, r)
```
- 木をkeyを境に2つに分割
- keyより小さい部分と大きい部分に分ける

### 2. `merge(a, b)`
```python
def merge(a, b):
    if not a or not b:
        return a or b
    if a.priority > b.priority:
        a.right = merge(a.right, b)
        return a
    else:
        b.left = merge(a, b.left)
        return b
```
- 2つの木をマージ
- 優先度に基づいて再帰的に結合

### 3. `insert(root, node)`
```python
def insert(root, node):
    if not root:
        return node
    if node.priority > root.priority:
        l, r = split(root, node.key)
        node.left, node.right = l, r
        return node
    elif node.key < root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root
```
- 新しい切断位置を挿入
- 優先度が高い場合は分割して挿入
- 優先度が低い場合は通常のBST挿入

### 4. `lower_bound(root, key)`
```python
def lower_bound(root, key):
    res = None
    while root:
        if root.key >= key:
            res = root
            root = root.left
        else:
            root = root.right
    return res
```
- key以上の最小の切断位置を検索
- xを含む木材片の右端を求める

### 5. `prev_bound(root, key)`
```python
def prev_bound(root, key):
    res = None
    while root:
        if root.key < key:
            res = root
            root = root.right
        else:
            root = root.left
    return res
```
- key未満の最大の切断位置を検索
- xを含む木材片の左端を求める

## メイン処理の流れ

### 初期化
```python
L, Q = map(int, input().split())
root = TreapNode(0)           # 開始点(0)を挿入
root = insert(root, TreapNode(L))  # 終了点(L)を挿入
```
- 木材は最初 [0, L] の1区間

### クエリ処理
```python
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        root = insert(root, TreapNode(x))  # 切断位置を追加
    else:
        r = lower_bound(root, x)  # x以上の最小切断点
        l = prev_bound(root, x)   # x未満の最大切断点
        print(r.key - l.key)      # 木材片の長さを出力
```

## 具体例で見る動作

**例**: L=10, クエリ: (1,3), (1,7), (2,5)

1. 初期状態: 切断点 [0, 10] → 長さ10の木材1本
2. (1,3)で切断: 切断点 [0, 3, 10] → 木材 [0-3], [3-10]
3. (1,7)で切断: 切断点 [0, 3, 7, 10] → 木材 [0-3], [3-7], [7-10]
4. (2,5)のクエリ: 
   - lower_bound(5) = 7 (5以上の最小切断点)
   - prev_bound(5) = 3 (5未満の最大切断点)
   - 結果: 7 - 3 = 4

## 特徴と利点

1. **効率性**: 各操作が平均O(log N)時間
2. **動的更新**: 切断点の追加を効率的に処理
3. **範囲検索**: 前後の切断点を高速に検索可能

このTreapデータ構造により、大量のクエリを高速に処理できます。
###############################################
[cgpt AC]
import sys, random
input = sys.stdin.readline

class TreapNode:
    __slots__ = ("key", "priority", "left", "right")
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

def split(root, key):
    if not root:
        return (None, None)
    if key < root.key:
        l, root.left = split(root.left, key)
        return (l, root)
    else:
        root.right, r = split(root.right, key)
        return (root, r)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.priority > b.priority:
        a.right = merge(a.right, b)
        return a
    else:
        b.left = merge(a, b.left)
        return b

def insert(root, node):
    if not root:
        return node
    if node.priority > root.priority:
        l, r = split(root, node.key)
        node.left, node.right = l, r
        return node
    elif node.key < root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

def lower_bound(root, key):
    res = None
    while root:
        if root.key >= key:
            res = root
            root = root.left
        else:
            root = root.right
    return res

def prev_bound(root, key):
    res = None
    while root:
        if root.key < key:
            res = root
            root = root.right
        else:
            root = root.left
    return res


L, Q = map(int, input().split())
root = TreapNode(0)
root = insert(root, TreapNode(L))

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        root = insert(root, TreapNode(x))
    else:
        r = lower_bound(root, x)
        l = prev_bound(root, x)
        print(r.key - l.key)

###############################################
[cgpt TLE]
import sys
import bisect
L, Q = map(int, sys.stdin.readline().split())
C = [0, L]
for _ in range(Q):
    c, x = map(int, sys.stdin.readline().split())
    if c == 1:
        i = bisect.bisect(C, x)
        C.insert(i, x)   # O(N) 挿入
    else:
        i = bisect.bisect(C, x)
        print(C[i] - C[i-1])
###############################################
[my TLE]
L,Q=map(int,input().split())
C=[0,L]
from bisect import bisect_left,bisect_right,bisect
for i in range(Q):
  c,x=map(int,input().split())
  if c==1:
    C+=[x]
    C.sort()
  elif c==2:
    j=bisect(C,x)
    print(C[j]-C[j-1])
###############################################
