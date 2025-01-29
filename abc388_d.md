

---
```


```
---
---
```


```
---
---
```

N = int(input())
A = list(map(int, input().split()))

memo = [0 for _ in range(len(A))]
ans = []
accumulator = 0
for i, v in enumerate(A):
    accumulator += memo[i]
    v += accumulator
    if v <= 0:
        ans.append(str(0))
        continue
    if i+1 < len(A):
        memo[i+1] += 1
    if i+v+1 < len(A):
        memo[i+v+1] -= 1
    v = max(0, v - ((len(A) - 1) - i))
    ans.append(str(v))

print(' '.join(ans))

```
---
---
```

n=int(input())
a=list(map(int,input().split()))
diff=[0]*(n+1)
for i in range(n):
    score=a[i]+diff[i]-(n-1-i)
    if score<0:
        diff[n+score]-=1
        score=0
    diff[i+1]+=diff[i]+1
    a[i]=score
print(*a)

```
---
---
```
N = int(input())
A = list(map(int, input().split()))
S = [0] * N
for i, a in enumerate(A):
    S[i] += S[i-1]
    a += S[i]
    
    remain = N - i - 1
    if remain == 0:
        A[i] = a
        continue
    
    if a >= remain:
        S[i+1] += 1
        A[i] = a - remain
    else:
        S[i+1] += 1
        S[i+a+1] -= 1
        A[i] = 0

print(*A)

```
---

---
```

N=int(input())
A=[-1]+list(map(int,input().split()))
given = [0]*(N+2)

for i in range(1,N+1):
  given[i] += given[i-1]
  A[i] += given[i]
  if A[i] > 0:
    given[i+1]+=1
    given[i+min(A[i] , N-i)+1]-=1
    A[i] -= min(A[i] , N-i)

print(*A[1:])

```
---
---

```
[titia]

import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

PLUS=[0]*(N+10)

for i in range(N):
    PLUS[i]+=PLUS[i-1]
    A[i]+=PLUS[i]
    a=A[i]
    # 最大N-i-1個をあげる。

    w=min(a,N-i-1)

    A[i]-=w
    if w>0:
        PLUS[i+1]+=1
        PLUS[i+1+w]-=1

print(*A)

```
---


このコードは、リスト `A` の要素を特定のルールに従って変更し、最終的なリストの状態を出力するプログラムです。以下にコードの詳細な説明を示します。


### コードの目的
- リスト `A` の各要素に対して、与えられた条件に基づいて調整を行います。
- その調整は、他の要素にも影響を及ぼすため、効率的に処理するために差分配列 `PLUS` を活用しています。


### 各部分の説明

#### 1. **入力部分**
```python
import sys
input = sys.stdin.readline

N = int(input())  # リストの長さを入力
A = list(map(int, input().split()))  # リストAを入力
```
- 標準入力から、整数 `N`（リストの長さ）とリスト `A` の内容を読み取ります。

#### 2. **差分配列の初期化**
```python
PLUS = [0] * (N + 10)
```
- `PLUS` は差分を管理するための配列です。配列サイズを `N+10` にしているのは、後の処理で安全にインデックスを操作できるようにするためです。

#### 3. **リストの更新処理**
```python
for i in range(N):
    PLUS[i] += PLUS[i-1]  # 現在の差分を反映
    A[i] += PLUS[i]  # 差分を A[i] に適用

    a = A[i]  # 現在の値を取得
```
- 差分を反映して、`A[i]` を更新します。
- この時点で `A[i]` には、これまでのすべての調整が適用されています。

```python
    w = min(a, N-i-1)  # 現在の値 a から次に調整する数 w を計算
```
- `A[i]` の値 `a` から、次に調整する値 `w` を決定します。
  - `w` の最大値は、現在の位置 `i` からリストの最後までの要素数 `N-i-1` です。

```python
    A[i] -= w  # 調整後の値を更新
    if w > 0:
        PLUS[i+1] += 1  # 次の要素から影響を与える
        PLUS[i+1+w] -= 1  # 範囲を超える部分で影響を打ち消す
```
- `A[i]` から `w` を引き、値を調整します。
- 差分配列 `PLUS` を用いて、範囲内の次の要素に影響を与えます。

#### 4. **結果の出力**
```python
print(*A)
```
- 最終的に更新されたリスト `A` を出力します。

### 動作の流れ（例）
入力例:
```
5
3 1 4 1 5
```

1. 初期状態:  
   - `A = [3, 1, 4, 1, 5]`  
   - `PLUS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

2. 各要素に対してループ処理:
   - i=0: `A = [2, 1, 4, 1, 5]`, `PLUS = [0, 1, -1, 0, 0, 0, ...]`  
   - i=1: `A = [2, 1, 4, 1, 5]`, `PLUS = [0, 1, -1, 0, 0, 0, ...]`  
   - i=2: `A = [2, 1, 3, 1, 5]`, `PLUS = [0, 1, -1, 1, -1, 0, ...]`  
   - i=3: `A = [2, 1, 3, 1, 5]`, `PLUS = [0, 1, -1, 1, -1, 0, ...]`  
   - i=4: `A = [2, 1, 3, 1, 4]`, `PLUS = [0, 1, -1, 1, -1, 1, ...]`

3. 最終出力:  
   ```
   2 1 3 1 4
   ```

### ポイント
1. **差分配列の活用**
   - `PLUS` を用いて効率的に値を調整する。
   - 一括で範囲内に変更を加えることができる。

2. **更新処理の工夫**
   - `A[i]` の値を直接操作するのではなく、差分で管理することで計算量を抑えている。

3. **計算量**
   - このアプローチは、各要素を1度だけ処理するため、計算量は O(N) です。
  
---
---
```
[my TLE ans]

N=int(input())
A=list(map(int,input().split()))
for i in range(1,N):
  diff = [0]*(N+1) 
  give = min(A[i-1],N-i)
  diff[i]+=1
  diff[i+give]-=1
  A[i-1]-=give
  current = 0
  for i in range(1,N):
    current += diff[i]
    A[i]+=current    
print(*A)
```
---
```
[my TLE ans]

N=int(input())
A=list(map(int,input().split()))
for i in range(N):
  for j in range(A[i]):
    if i+j+1<N:
      A[i+j+1]+=1
      A[i]-=1
print(*A)

このアプローチの計算量は O(sum(A)) であり、A の総和が大きい場合に TLE になります。

```
---


