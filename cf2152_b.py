###############################################
###############################################
###############################################
[gemini説明]
---
## コードの概要

このPythonコードは、チェス盤上でキングがドローンのいるマスにたどり着くために必要な最小ターン数を計算するものです。
キングはチェビシェフ距離で移動し、ドローンは各ターンでキングからチェビシェフ距離が一定以内の範囲にいる必要があります。
この問題は、与えられたターン数 `k` で条件を満たすことができるかを二分探索で探し、最小の `k` を見つけ出すことで解決されます。

---
## 関数 `solve_one` の説明

この関数は、与えられたキングとドローンの初期位置 `(rK, cK)`, `(rD, cD)`、および盤のサイズ `n` に対して、問題を解くメインロジックを実装しています。

- `if rK == rD and cK == cD: return 0`
    - キングとドローンが同じマスにいる場合、移動は不要なので0を返します。
- `min_steps = max(abs(rK - rD), abs(cK - cD))`
    - キングがドローンのマスに到達するのに必要な最小のターン数（チェビシェフ距離）を計算します。
- `L = max(1, min_steps - 2), R = min(2 * n, min_steps + 2 * n)`
    - 答えの候補となるターン数 `k` の探索範囲を定義します。
        - `L` (下限): 最小ステップ数から少し引いた値。
        - `R` (上限): 盤のサイズと最小ステップ数から妥当な大きな値。
    - この範囲内で、二分探索を行います。
- `while L <= R:`
    - 二分探索のループです。`mid` を現在の探索ターン数とします。
    - `max_cheb = max_cheb_for_k(n, rK, cK, rD, cD, mid)`
        - `mid` ターンでキングが到達できるすべてのマスについて、ドローンとのチェビシェフ距離の最大値を計算します。
    - `if max_cheb <= mid:`
        - もし `max_cheb` が `mid` 以下なら、`mid` ターンでキングがどのマスにいてもドローンとの距離は `mid` 以下に保たれることを意味します。つまり、`mid` ターンでキングはドローンに追いつくことができます。
        - `ans = mid` として、より小さな答えを探すために `R = mid - 1` とします。
    - `else:`
        - `mid` ターンでは追いつけないことを意味するので、より大きなターン数を試すために `L = mid + 1` とします。
- `return ans`
    - 最小の答え `ans` を返します。

---
## 関数 `max_cheb_for_k` の説明

この関数は、キングが `k` ターン後にいる可能性のあるすべてのマスの中から、ドローンとのチェビシェフ距離の最大値を計算します。

- **探索範囲の定義**:
    - `r_lo`, `r_hi`: キングが `k` ターン後にいる可能性のある行の範囲を計算します。
- **候補となる行の生成**:
    - チェビシェフ距離の最大値は、境界付近で発生する可能性が高いです。そのため、以下の行を候補として `candidates` に追加します。
        - 探索範囲の境界 (`r_lo`, `r_hi`)
        - ドローンの行 `rD`
        - キングの移動範囲の水平方向の境界に対応する行
        - チェビシェフ距離の式を微分して得られる、最大値を取りうる行
- **候補の近傍も探索**:
    - `for r in temp_list: for dr in [-1, 0, 1]:`
    - 理論的な候補点の近傍も最大値を取りうるため、それらの行も `candidates` に追加します。
- **最大チェビシェフ距離の計算**:
    - `for r in candidates:`
    - 候補の行 `r` ごとに以下の計算を行います。
    - `horiz = k - (r - rK)`: `k` ターンでキングが行 `r` に到達した場合に残っている水平方向の移動可能量です。
    - `c_left = max(0, cK - horiz)`, `c_right = min(n, cK + horiz)`: 行 `r` にいるときのキングの列の範囲です。
    - `cheb = max(abs(r - rD), abs(c_left - cD), abs(c_right - cD))`:
        - 行 `r` にいる場合、ドローンとの距離の最大値は `r` 自体の距離か、または `c_left` や `c_right` からドローンの列 `cD` までの距離のどちらか大きい方です。
        - これをすべての候補の行について計算し、全体の最大値を `best` に更新します。
- `return best`
    - 最終的な最大チェビシェフ距離を返します。

---
## 全体の流れ

1. ユーザーからの入力を受け取ります。
2. `solve_one` 関数を呼び出し、キングがドローンに追いつくために必要な最小ターン数を計算します。
3. `solve_one` 関数は、ターン数 `k` を二分探索で効率的に見つけます。
4. 各 `k` について、`max_cheb_for_k` 関数を使って、そのターン数でキングが移動できる範囲内でドローンとの最大チェビシェフ距離を計算します。
5. この最大距離が `k` 以下であれば、追いつくことが可能と判断し、より小さな `k` を探します。そうでない場合は、より大きな `k` を探します。
6. 二分探索が終了した時点で、見つかった最小のターン数を結果として出力します。

このコードは、キングの移動範囲とドローンの位置の関係性を分析し、最適化された二分探索を用いることで、効率的に問題を解決しています。
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[ds TLE]
import math

def max_cheb_for_k(n, rK, cK, rD, cD, k):
    r_lo = rK
    r_hi = min(n, rK + k)
    if r_lo > r_hi:
        return -10**30
    
    best = -10**30
    candidates = set()
    
    candidates.add(r_lo)
    candidates.add(r_hi)
    
    if r_lo <= rD <= r_hi:
        candidates.add(rD)
    
    r_left_bound = rK + k - cK
    if r_lo <= r_left_bound <= r_hi:
        candidates.add(r_left_bound)
    
    r_right_bound = rK + k - (n - cK)
    if r_lo <= r_right_bound <= r_hi:
        candidates.add(r_right_bound)
    
    r_candidate1 = (rD - cK + k + rK + cD) // 2
    if r_lo <= r_candidate1 <= r_hi:
        candidates.add(r_candidate1)
    
    r_candidate2 = (rD + cK + k + rK - cD) // 2
    if r_lo <= r_candidate2 <= r_hi:
        candidates.add(r_candidate2)
    
    temp_list = list(candidates)
    for r in temp_list:
        for dr in [-1, 0, 1]:
            neighbor = r + dr
            if r_lo <= neighbor <= r_hi:
                candidates.add(neighbor)
    
    for r in candidates:
        horiz = k - (r - rK)
        if horiz < 0:
            continue
            
        c_left = max(0, cK - horiz)
        c_right = min(n, cK + horiz)
        
        cheb = max(abs(r - rD), abs(c_left - cD), abs(c_right - cD))
        if cheb > best:
            best = cheb
    
    return best

def solve_one(n, rK, cK, rD, cD):
    if rK == rD and cK == cD:
        return 0
    
    min_steps = max(abs(rK - rD), abs(cK - cD))
    L = max(1, min_steps - 2)
    R = min(2 * n, min_steps + 2 * n)
    
    ans = -1
    
    while L <= R:
        mid = (L + R) // 2
        max_cheb = max_cheb_for_k(n, rK, cK, rD, cD, mid)
        
        if max_cheb <= mid:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    
    return ans

t = int(input())
out = []
for _ in range(t):
    n, rK, cK, rD, cD = map(int, input().split())
    out.append(str(solve_one(n, rK, cK, rD, cD)))
print("\n".join(out))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
