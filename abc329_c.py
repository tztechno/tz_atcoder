##################################################################
英小文字からなる長さNの文字列Sが与えられます。
Sの空でない部分文字列であって、1種類の文字のみからなるものの数を求めてください。
ただし、文字列として等しい部分文字列同士は、取り出し方が異なっても区別しません。
なお、Sの空でない部分文字列とは、Sの先頭から0文字以上、末尾から0文字以上削除して得られる文字列のうち、長さが1以上であるもののことをいいます。
例えば、abやabcはabcの空でない部分文字列ですが、acや空文字列はabcの空でない部分文字列ではありません。
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[claude explanation]

目的は、文字列 `S` の「連続する同じ文字の最大長」を各文字ごとに求め、その合計を計算することです。

```python
char_max_length = {}
```

* 各文字ごとに「連続して出現する最大長」を格納する辞書。

---

```python
i = 0
while i < N:
    current_char = S[i]
    start = i
    while i < N and S[i] == current_char:
        i += 1
    length = i - start
    char_max_length[current_char] = max(char_max_length.get(current_char, 0), length)
```

1. `i` を使って文字列を走査。
2. `current_char` に現在の文字を代入。
3. 内側の `while` で同じ文字が続く限り `i` を進める。
4. `length = i - start` でその文字の連続部分の長さを計算。
5. `char_max_length[current_char]` に既存の最大値と比較して更新。

---

```python
total = sum(char_max_length.values())
print(total)
```

* 辞書に保存された各文字の「最大連続長」の合計を計算して出力。

---

💡 **ポイント**

* 内側の `while` で連続文字をまとめてスキップしているので効率的。
* 辞書を使うことで、文字ごとの最大長だけを保持できる。
* 計算量は O(N) です。

---

##################################################################
[claude AC]
N = int(input())
S = input()
char_max_length = {}
i = 0
while i < N:
    current_char = S[i]
    start = i
    while i < N and S[i] == current_char:
        i += 1
    length = i - start
    char_max_length[current_char] = max(char_max_length.get(current_char, 0), length)
total = sum(char_max_length.values())
print(total)
##################################################################
[deepseek WA]
[cgpt WA]
##################################################################
[gemini explanation]

```python
from itertools import groupby
```

* `itertools` モジュールから `groupby` をインポート
* `groupby` は **連続して同じ要素をまとめる**ために使います。

```python
max_lengths = {}
```

* 空の辞書を作ります。
* この辞書に **各文字の最長連続出現長** を保存していきます。

```python
if S:
    for key, group in groupby(S):
        length = len(list(group))
        if key not in max_lengths or length > max_lengths[key]:
            max_lengths[key] = length
```

* `if S:` は文字列が空でないか確認しています。
* `for key, group in groupby(S):` で文字列の連続する同じ文字の塊を順番に処理します：

  * `key` は文字
  * `group` はその連続する文字のイテレータ

* `length = len(list(group))` でその連続ブロックの長さを求めます。
* `if` 文は、辞書にまだ文字がない場合、または今回のブロックが既存の最大より長い場合に更新します。

```python
print(sum(max_lengths.values()))
```

* 辞書に保存された **各文字の最長連続長** の合計を出力します。

##################################################################
[gemini AC]
N=int(input())
S=str(input())
from itertools import groupby
max_lengths = {}
if S: 
    for key, group in groupby(S):
        length = len(list(group))
        if key not in max_lengths or length > max_lengths[key]:
            max_lengths[key] = length
print(sum(max_lengths.values()))
##################################################################
[mybrain TLE]
N = int(input())
S = list(input())
A = set()
for i in range(N):
  for j in range(i,N):
    if S[j]==S[i]:
      A.add(''.join(S[i:j+1]))
    else:
      break
print(len(A))
##################################################################
[mybrain TLE]
N = int(input())
S = list(input())
A = set()
for i in range(N+1):
  for j in range(i + 1, N+1):
    sp = S[i:j]
    if len(set(sp)) == 1:
      A.add(''.join(sp))
print(len(A))
##################################################################

