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
[gemini AC]
from collections import deque

# 入力
N, K = map(int, input().split())
P = list(map(int, input().split()))

# 各値の位置を記録
pos = [0] * (N + 1)
for idx, val in enumerate(P):
    pos[val] = idx

ans = N

# 1. dequeでスライドウィンドウのインデックスを管理する
# (ここでは、値ではなくインデックスを格納する)
dq_min = deque()
dq_max = deque()

# 最初のウィンドウ [1, K] の処理
for i in range(1, K + 1):
    idx = pos[i]
    while dq_min and pos[dq_min[-1]] >= idx:
        dq_min.pop()
    dq_min.append(i)
    
    while dq_max and pos[dq_max[-1]] <= idx:
        dq_max.pop()
    dq_max.append(i)

# 最小区間長を初期化
ans = pos[dq_max[0]] - pos[dq_min[0]]

# 2. スライドウィンドウを移動
# a: ウィンドウの左端の要素 (1-indexed)
for a in range(2, N - K + 2):
    # 古い値を削除 (ウィンドウから外れた要素をdequeから取り除く)
    # dequeの先頭のインデックスが現在のウィンドウの左端より小さければ削除
    if dq_min and dq_min[0] < a:
        dq_min.popleft()
    if dq_max and dq_max[0] < a:
        dq_max.popleft()

    # 新しい値を追加 (ウィンドウの右端に加わった要素)
    new_val = a + K - 1
    new_idx = pos[new_val]
    
    # deque_min を更新
    while dq_min and pos[dq_min[-1]] >= new_idx:
        dq_min.pop()
    dq_min.append(new_val)

    # deque_max を更新
    while dq_max and pos[dq_max[-1]] <= new_idx:
        dq_max.pop()
    dq_max.append(new_val)

    # 現在の区間長を計算して最小値を更新
    current_span = pos[dq_max[0]] - pos[dq_min[0]]
    ans = min(ans, current_span)

print(ans)
###############################################
[gemini 解説]
from collections import deque # dequeを使用するためにdequeモジュールをインポート

# 入力
N, K = map(int, input().split()) # NとKを標準入力から取得
P = list(map(int, input().split())) # Pのリストを標準入力から取得

# 各値の位置を記録
pos = [0] * (N + 1) # pos[i] に、値 i が配列 P のどこにあるかのインデックスを格納するリスト
for idx, val in enumerate(P):
    pos[val] = idx # P[idx] = val なので、pos[val] = idx となる

ans = N # 答えの初期値をNに設定。これは最小区間長を求める問題なので、考えられる最大値で初期化する

# 1. dequeでスライドウィンドウのインデックスを管理する
# (ここでは、値ではなくインデックスを格納する)
dq_min = deque() # 最小値を管理するためのdeque
dq_max = deque() # 最大値を管理するためのdeque

# 最初のウィンドウ [1, K] の処理
for i in range(1, K + 1): # iは1からKまでの値
    idx = pos[i] # iがPのどこにあるか（pos[i]）を取得
    while dq_min and pos[dq_min[-1]] >= idx: # dq_minの末尾の要素が新しい要素より大きい場合
        dq_min.pop() # 末尾の要素を削除（新しい要素がより良い候補になるため）
    dq_min.append(i) # 現在の要素をdq_minの末尾に追加
    
    while dq_max and pos[dq_max[-1]] <= idx: # dq_maxの末尾の要素が新しい要素より小さい場合
        dq_max.pop() # 末尾の要素を削除
    dq_max.append(i) # 現在の要素をdq_maxの末尾に追加

# 最小区間長を初期化
ans = pos[dq_max[0]] - pos[dq_min[0]] # 最初のウィンドウの最大値と最小値の位置の差を計算し、ansを更新

# 2. スライドウィンドウを移動
# a: ウィンドウの左端の要素 (1-indexed)
for a in range(2, N - K + 2): # ウィンドウを右に一つずつスライド (aはウィンドウの左端の要素)
    # 古い値を削除 (ウィンドウから外れた要素をdequeから取り除く)
    # dequeの先頭のインデックスが現在のウィンドウの左端より小さければ削除
    if dq_min and dq_min[0] < a: # dq_minの先頭の要素（値）が現在のウィンドウから外れた場合
        dq_min.popleft() # 先頭の要素を削除
    if dq_max and dq_max[0] < a: # dq_maxの先頭の要素（値）が現在のウィンドウから外れた場合
        dq_max.popleft() # 先頭の要素を削除

    # 新しい値を追加 (ウィンドウの右端に加わった要素)
    new_val = a + K - 1 # ウィンドウの右端に新しく入る要素
    new_idx = pos[new_val] # 新しい要素のP内での位置を取得
    
    # deque_min を更新
    while dq_min and pos[dq_min[-1]] >= new_idx: # dq_minの末尾を更新
        dq_min.pop()
    dq_min.append(new_val)

    # deque_max を更新
    while dq_max and pos[dq_max[-1]] <= new_idx: # dq_maxの末尾を更新
        dq_max.pop()
    dq_max.append(new_val)

    # 現在の区間長を計算して最小値を更新
    current_span = pos[dq_max[0]] - pos[dq_min[0]] # 現在のウィンドウでの最大値と最小値の位置の差を計算
    ans = min(ans, current_span) # 最小値を更新

print(ans) # 最終的な答えを出力
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
