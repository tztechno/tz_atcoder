#################################################
```
[my AC]

import sys
input = sys.stdin.readline
n=int(input())
H=list(map(int,input().split()))

Mcount=1
for d in range(1,n):
  for i in range(n):
    now=i
    nxt=i+d
    count=1
    while nxt<n and H[now]==H[nxt]:
        now=nxt
        nxt+=d
        count+=1
    Mcount=max(Mcount,count)

print(Mcount)
```

#################################################


```
[titia]

import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

ANS=1
for i in range(n):
    for j in range(1,n):
        now=i
        score=0
        while True:
            if now<n and A[now]==A[i]:
                score+=1
            else:
                break
            now+=j

        ANS=max(ANS,score)

print(ANS)
```

---

### コードの目的

このコードは、与えられた配列 `A` の中で、任意のスタート地点とステップ幅（`j`）を用いて同じ値が連続する部分列の長さを計算し、その最大値を求めるものです。

---

### 各部分の説明

#### 1. **入力の取得**
```python
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
```

- `sys.stdin.readline` を使って高速に入力を取得します。
- `n` は配列 `A` の長さ。
- `A` はスペース区切りの整数をリストとして取得します。

例:
```
入力: 
5
1 2 2 2 3
```
結果:
```
n = 5
A = [1, 2, 2, 2, 3]
```

---

#### 2. **初期化**
```python
ANS = 1
```

- 最長の部分列の長さを記録する変数 `ANS` を 1 に初期化しています。
  - 最短でも 1 要素からなる部分列が存在するため、初期値を 1 に設定。

---

#### 3. **二重ループの処理**
```python
for i in range(n):
    for j in range(1, n):
        now = i
        score = 0
        while True:
            if now < n and A[now] == A[i]:
                score += 1
            else:
                break
            now += j

        ANS = max(ANS, score)
```

この部分がアルゴリズムの中心です。

- **外側のループ**:  
  - スタート地点 `i` を 0 から `n-1` まで順に設定。
  - 配列 `A` の各要素を起点として処理を開始。

- **内側のループ**:  
  - ステップ幅 `j` を 1 から `n-1` まで試す。
  - つまり、「ある要素から `j` 間隔で同じ値がどれだけ続くか」を計算。

- **`while` ループ**:  
  - 現在のインデックス `now` が配列の範囲内かつ、`A[now]` がスタート地点 `A[i]` と同じ場合に処理を継続。
  - 条件を満たすたびに `score` を 1 増加させ、`now` を `j` だけ進めます。
  - 条件を満たさなくなったらループを終了。

- **最大値の更新**:  
  - 現在の部分列の長さ `score` を `ANS` と比較し、`ANS` に最大値を保存。

---

#### 4. **結果の出力**
```python
print(ANS)
```

- 最長の部分列の長さ `ANS` を出力します。

---

### 動作例

#### 入力例
```
5
1 2 2 2 3
```

#### 処理の流れ
1. `i = 0`, `A[i] = 1`
   - `j = 1`: 部分列は `[1]` → 長さ = 1
   - `j = 2`: 部分列は `[1]` → 長さ = 1
   - ...（他の `j` でも同様）

2. `i = 1`, `A[i] = 2`
   - `j = 1`: 部分列は `[2, 2, 2]` → 長さ = 3
   - `j = 2`: 部分列は `[2, 2]` → 長さ = 2
   - ...（他の `j` でも最大は 3）

3. `i = 2`, `A[i] = 2`
   - ...（同様の処理）

4. 最終的に `ANS = 3`。

#### 出力
```
3
```

---

### 計算量

- **外側ループ**: \(O(n)\)  
  スタート地点 `i` を全て試す。

- **内側ループ**: \(O(n)\)  
  ステップ幅 `j` を全て試す。

- **`while` ループ**: \(O(n)\)  
  ステップ幅ごとに最大で配列全体を探索。

- **総計**: \(O(n^3)\)  
  大きな入力に対して非常に非効率。

---

### 改善案

ステップ幅 `j` を考慮する必要がない場合、連続する同じ値だけを探索すれば良いです。この場合、計算量を \(O(n)\) に削減できます。


#################################################

