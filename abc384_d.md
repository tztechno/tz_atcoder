
```
############################################

############################################

############################################

############################################

[myans TLE]

import sys
input = sys.stdin.readline
N,S=map(int,input().split())
A=list(map(int,input().split()))
suma=sum(A)
R=S%suma
V=set()
AR=A[::-1]
AF=[0]
AB=[0]
for a in A:
  AF+=[AF[-1]+a]
for ar in AR:
  AB+=[AB[-1]+ar]
for af in set(AF):
  for ab in set(AB):
    if R==(ab+af)%suma:
        print('Yes')
        exit()
else:
  print('No')
############################################
[titia]

import sys
input = sys.stdin.readline

N,S=map(int,input().split())
A=list(map(int,input().split()))

SUM=[0]
for a in A:
    SUM.append(SUM[-1]+a)

SUM0=SUM[-1]
S%=SUM0

for a in A:
    SUM.append(SUM[-1]+a)
for a in A:
    SUM.append(SUM[-1]+a)

SET=set(SUM)
for a in SUM:
    if S+a in SET:
        print("Yes")
        exit()

print("No")

############################################

```



---
---
```
[cgpt]

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の計算
SUM = [0]
for a in A:
    SUM.append(SUM[-1] + a)

SUM0 = SUM[-1]
S %= SUM0

# 部分列の検出
SET = set(SUM)
for a in SUM:
    if S + a in SET:
        print("Yes")
        exit()

print("No")
```
---

このコードは、与えられた整数列 \( A \) と目標値 \( S \) をもとに、配列の連続する部分列の和が \( S \) に一致するかを判定します。

---

### コードの詳細な説明

#### 1. **入力の受け取り**
```python
N, S = map(int, input().split())
A = list(map(int, input().split()))
```
- \( N \): 配列 \( A \) の要素数。
- \( S \): 目標となる部分列の和。
- \( A \): 長さ \( N \) の整数列。

#### 2. **累積和の計算**
```python
SUM = [0]
for a in A:
    SUM.append(SUM[-1] + a)
```
- 配列 \( A \) の累積和を計算します。
- \( \text{SUM}[i] \) には、\( A \) の最初から \( i-1 \) 番目までの要素の合計が格納されます。
  - 例: \( A = [2, 3, 5] \) の場合、累積和 \( \text{SUM} = [0, 2, 5, 10] \)。

#### 3. **目標値 \( S \) の正規化**
```python
SUM0 = SUM[-1]
S %= SUM0
```
- \( \text{SUM0} \): 配列 \( A \) の総和。
- \( S \) を \( \text{SUM0} \) で割った余りに変換することで、配列を繰り返しても同じ結果になることを利用します。
  - 例: 配列 \( A = [2, 3, 5] \) の総和 \( \text{SUM0} = 10 \) で、目標値 \( S = 23 \) の場合、\( S \%= 10 \) により \( S = 3 \) となります。

#### 4. **部分列の検出**
```python
SET = set(SUM)
for a in SUM:
    if S + a in SET:
        print("Yes")
        exit()
```
- 累積和 \( \text{SUM} \) を集合（`SET`）として管理します。この集合により、指定された値が含まれているかどうかを高速に判定できます。
- 部分列の和を検出するロジック：
  - 累積和のリスト \( \text{SUM} \) の要素 \( a \) について、\( S + a \) が \( \text{SET} \) に含まれるかを確認します。
  - 部分列の和が \( S \) に一致する場合、累積和の関係から次が成り立つ：
    \[
    \text{SUM}[j] - \text{SUM}[i] = S
    \]
    これを変形すると \( \text{SUM}[j] = S + \text{SUM}[i] \) となり、検出条件 \( S + a \in \text{SET} \) に対応します。
- 条件を満たした場合は `"Yes"` を出力し、プログラムを終了します。

#### 5. **結果の出力**
```python
print("No")
```
- 条件を満たす部分列が存在しない場合は `"No"` を出力します。

---

### 計算量
- **累積和の計算**：\( O(N) \)
- **部分列の検出**：\( O(N) \)（集合への挿入・検索は平均 \( O(1) \)）
- **合計**：\( O(N) \)

---

### サンプル実行例

#### 入力例 1
```plaintext
4 6
1 2 3 4
```

#### 処理の流れ
1. 累積和を計算：
   \[
   \text{SUM} = [0, 1, 3, 6, 10]
   \]
2. 総和 \( \text{SUM0} = 10 \)。目標値 \( S = 6 \) を変換：
   \[
   S = 6 \% 10 = 6
   \]
3. 集合 \( \text{SET} = \{0, 1, 3, 6, 10\} \) に対して検出：
   - \( S + a = 6 + 0 = 6 \in \text{SET} \)。
   - 条件を満たすため `"Yes"` を出力。

#### 出力例 1
```plaintext
Yes
```

---

#### 入力例 2
```plaintext
3 15
4 5 6
```

#### 処理の流れ
1. 累積和を計算：
   \[
   \text{SUM} = [0, 4, 9, 15]
   \]
2. 総和 \( \text{SUM0} = 15 \)。目標値 \( S = 15 \% 15 = 0 \)。
3. 集合 \( \text{SET} = \{0, 4, 9, 15\} \) に対して検出：
   - \( S + a = 0 + 0 = 0 \in \text{SET} \)。
   - 条件を満たすため `"Yes"` を出力。

#### 出力例 2
```plaintext
Yes
```

#### 入力例 3
```plaintext
3 20
4 5 6
```

#### 処理の流れ
1. 累積和を計算：
   \[
   \text{SUM} = [0, 4, 9, 15]
   \]
2. 総和 \( \text{SUM0} = 15 \)。目標値 \( S = 20 \% 15 = 5 \)。
3. 集合 \( \text{SET} = \{0, 4, 9, 15\} \) に対して検出：
   - \( S + a = 5 + 0 = 5 \notin \text{SET} \)。
   - 条件を満たさないため `"No"` を出力。

#### 出力例 3
```plaintext
No
```

