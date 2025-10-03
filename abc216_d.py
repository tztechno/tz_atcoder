###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################

[ds]
from collections import deque, defaultdict

def main():

    N, M = map(int, input().split())
    
    tubes = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        tubes.append(a)
    
    # 各色がどの筒の一番上にあるかを記録
    color_to_tubes = defaultdict(list)
    
    # 各筒の現在の先頭インデックス
    top_index = [0] * M
    
    # キューの準備：取り除けるペアを管理
    queue = deque()
    
    # 初期状態：各筒の一番上のボールをチェック
    for i in range(M):

        if top_index[i] < len(tubes[i]):

            color = tubes[i][top_index[i]]
            color_to_tubes[color].append(i)
            
            # 同じ色が2つ揃ったらキューに追加
            if len(color_to_tubes[color]) == 2:
                queue.append(color)
    
    removed_count = 0
    
    while queue: 要素がある間
        color = queue.popleft()
        tube1, tube2 = color_to_tubes[color]
        
        # ボールを取り除く
        top_index[tube1] += 1
        top_index[tube2] += 1
        
        removed_count += 2
        
        # 筒1の新しい一番上のボールをチェック
        if top_index[tube1] < len(tubes[tube1]):
            new_color1 = tubes[tube1][top_index[tube1]]
            color_to_tubes[new_color1].append(tube1)
            if len(color_to_tubes[new_color1]) == 2:
                queue.append(new_color1)
        
        # 筒2の新しい一番上のボールをチェック
        if top_index[tube2] < len(tubes[tube2]):
            new_color2 = tubes[tube2][top_index[tube2]]
            color_to_tubes[new_color2].append(tube2)
            if len(color_to_tubes[new_color2]) == 2:
                queue.append(new_color2)
    
    # すべてのボールが取り除けたかチェック
    if removed_count == 2 * N:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################

この問題は、筒の一番上にあるボールのペアを同じ色で取り除いていく操作を繰り返して、すべての筒を空にできるか判定する問題です。

## 問題の理解

- 各色のボールはちょうど2個ずつ存在
- 筒はM本あり、各筒にはボールが積まれている
- 操作：異なる2本の空でない筒から一番上のボールを取り出し、それらが同じ色なら捨てる
- すべての筒を空にできるか判定

## 解法の方針

この問題は**グラフ理論**を用いて解くことができます。以下のように考えます：

1. **筒の一番上のボール**に注目する
2. 同じ色のボールが2つの筒の一番上にあるとき、それらをペアにできる
3. このペア関係をグラフで表現する

具体的なアルゴリズム：

1. 各色について、その色がどの筒の一番上にあるかを記録する
2. 同じ色が2つの筒の一番上にある場合、それらの筒の間に「依存関係」があると考える
3. キューを使って、取り除けるボールから順次処理する

## アルゴリズムの説明

1. **データ構造**：
   - `color_to_tubes`: 各色が現在どの筒の一番上にあるかを記録
   - `top_index`: 各筒で次に取り出すべきボールのインデックス
   - `queue`: 取り除ける色のキュー

2. **処理の流れ**：
   - 初期状態で、同じ色が2つの筒の一番上にある色をキューに追加
   - キューから色を取り出し、対応する筒のボールを取り除く
   - 取り除いた後、筒の新しい一番上のボールをチェック
   - 新しいボールの色が他の筒の一番上の色と一致したらキューに追加

3. **終了条件**：
   - すべてのボール(2N個)が取り除けたら「Yes」
   - そうでなければ「No」

この解法の時間計算量はO(N+M)で、制約内で効率的に動作します。
###############################################
###############################################
OK、このコードは「**同じ色のボールが2つ揃ったら取り除けるパズル**」を解くものです。
AtCoderの「ABC216 E – Pair of Balls」などの系統の問題ですね。
順を追って説明します。

---

## 📝 問題のイメージ

* N 色、M 本の筒（tube）がある。
* 各筒にはボールがいくつか入っている。
* **ルール**：同じ色のボールが同時に「それぞれの筒の一番上」にあるとき、その2つを同時に取り除ける。
* 最後まで全部のボールを取り除けるかどうか判定する。

---

## 📝 コードの構造

### 1. 入力の読み込み

```python
N, M = map(int, input().split())
```

* N: ボールの色の数（色は 1…N）。
* M: 筒の本数。

```python
tubes = []
for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    tubes.append(a)
```

* tubes[i]: i番目の筒に入っているボールの色（先頭が上にあるボール）。

---

### 2. 状態の管理用変数

```python
color_to_tubes = defaultdict(list)
top_index = [0] * M
queue = deque()
```

* `color_to_tubes[color]`:
  その色が**現在どの筒の一番上にあるか**を記録するリスト。
  → 同じ色が2つになったら「取り除ける」のでチェックする。

* `top_index[i]`:
  i番目の筒の「今の先頭インデックス」。
  （取り除いたボールの数ぶん進む）

* `queue`:
  同じ色が二つ揃って「今取り除ける色」のキュー。

---

### 3. 初期状態の構築

```python
for i in range(M):
    if top_index[i] < len(tubes[i]):
        color = tubes[i][top_index[i]]
        color_to_tubes[color].append(i)
        
        if len(color_to_tubes[color]) == 2:
            queue.append(color)
```

* 各筒の最初のボール（index=0）を見て、
  色ごとの場所を `color_to_tubes` に追加。
* 同じ色が2つ揃ったら `queue` に入れる。

---

### 4. メインループ（ボール除去処理）

```python
removed_count = 0

while queue:
    color = queue.popleft()
    tube1, tube2 = color_to_tubes[color]
    
    top_index[tube1] += 1
    top_index[tube2] += 1
    removed_count += 2
```

* キューから「今除去できる色」を取り出す。
* その色がある2本の筒のインデックスを取得。
* 先頭を1つずつ進めて（ボール除去）、除去数をカウント。

#### 新しい一番上を確認して登録

```python
if top_index[tube1] < len(tubes[tube1]):
    new_color1 = tubes[tube1][top_index[tube1]]
    color_to_tubes[new_color1].append(tube1)
    if len(color_to_tubes[new_color1]) == 2:
        queue.append(new_color1)

if top_index[tube2] < len(tubes[tube2]):
    new_color2 = tubes[tube2][top_index[tube2]]
    color_to_tubes[new_color2].append(tube2)
    if len(color_to_tubes[new_color2]) == 2:
        queue.append(new_color2)
```

* 除去後に新しく現れた一番上の色も記録する。
* もし同じ色が2本揃ったら再びキューに追加。

※ `color_to_tubes[color]` をクリアしていないけど、
問題ないのは「同じ色は最大2つ」かつ「取り除いた後はもう使わない」ため。

---

### 5. 最終判定

```python
if removed_count == 2 * N:
    print("Yes")
else:
    print("No")
```

* ボールは全部で N色×2個＝2N個あるので、
  全部取り除けたら「Yes」。

---

## 🔑 アルゴリズムの要点

* **同じ色が同時に「上」に来るのを待つ**。
* **取り除けるものから順に除去していく BFS 型の処理**。
* `color_to_tubes` と `queue` を使うことで、効率的に管理している。

計算量は O(ボール総数) で、ボールが最大でも 2N 個なので十分速い。

---

## 📝 まとめ

このコードは、
「同じ色のボールが2つ揃ったら取り除き、次のボールをチェックする」
というパズルのシミュレーションをしています。

* `color_to_tubes`: 色ごとの「現在上にある筒のリスト」。
* `queue`: 今まさに取り除ける色。
* `top_index`: 各筒の何個目まで取り除かれたか。

を管理することで、
最後までボールを取り除けるかどうかを効率的に判定しています。

###############################################
###############################################
###############################################
###############################################
###############################################
