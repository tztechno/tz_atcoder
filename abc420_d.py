
##################################################################
問題文
H行W列のグリッドがあります。上からi行目、左からj列目のマス目を(i,j)と表します。
各マスの状態は文字Ai,j​で表され、意味は以下の通りです。

.：空きマス。
#：障害物マス。
S：スタートマス。
G：ゴールマス。
o：開いたドアのマス。
x：閉じたドアのマス。
?：スイッチマス。

高橋君は、1回の操作で今いるマスから上下左右に隣り合う、障害物マスでも閉じたドアでもないマスへ移動することができます。
また、スイッチマスに移動する度に全ての開いたドアのマスは閉じたドアのマスに、閉じたドアのマスは開いたドアのマスに変わります。
高橋君がはじめスタートマスにいる状態からゴールマスにいる状態にするよう操作できるか判定し、
可能な場合は必要な操作回数の最小値を求めてください。
##################################################################
2 4
S.xG
#?o.
------
5
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[gemini AC]
import collections

def solve():
    """
    状態拡張BFSを用いて迷路の最短経路を解く関数
    """
    try:
        H, W = map(int, input().split())
        A = [input() for _ in range(H)]
    except (IOError, ValueError):
        print("入力形式が正しくありません。")
        return

    # スタート(S)とゴール(G)の座標を探す
    sy, sx, gy, gx = -1, -1, -1, -1
    for r in range(H):
        for c in range(W):
            if A[r][c] == 'S':
                sy, sx = r, c
            elif A[r][c] == 'G':
                gy, gx = r, c

    # 3次元の距離配列: dist[y][x][s]
    # s=0: スイッチを偶数回押した状態
    # s=1: スイッチを奇数回押した状態
    # 値は-1で未訪問を表す
    dist = [[[-1] * 2 for _ in range(W)] for _ in range(H)]

    # BFSで使うキュー: (y座標, x座標, スイッチ状態)
    q = collections.deque()

    # --- 初期設定 ---
    # スタート地点をキューに追加
    dist[sy][sx][0] = 0
    q.append((sy, sx, 0))

    # 上下左右への移動方向ベクトル
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    # --- BFS開始 ---
    while q:
        y, x, s = q.popleft()
        cost = dist[y][x][s]

        # 4方向への移動を試す
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 1. グリッドの範囲内かチェック
            if not (0 <= ny < H and 0 <= nx < W):
                continue

            cell = A[ny][nx]
            next_s = s  # 次のスイッチ状態

            # 2. 移動可能かチェック
            if cell == '#':  # 障害物
                continue
            if cell == 'x' and s == 0:  # 閉じたドア (スイッチOFF)
                continue
            if cell == 'o' and s == 1:  # 開いたドア (スイッチON -> 閉じる)
                continue

            # 3. スイッチマスの場合、状態を反転
            if cell == '?':
                next_s = 1 - s

            # 4. 既に訪問済みかチェック
            if dist[ny][nx][next_s] != -1:
                continue

            # 5. 訪問処理: 距離を更新してキューに追加
            dist[ny][nx][next_s] = cost + 1
            q.append((ny, nx, next_s))

    # --- 結果の計算 ---
    # ゴール地点での2つの状態コストを取得
    cost_s0 = dist[gy][gx][0]
    cost_s1 = dist[gy][gx][1]

    # 両方とも到達不可能な場合
    if cost_s0 == -1 and cost_s1 == -1:
        print(-1)
    # 片方だけ到達可能な場合
    elif cost_s0 == -1:
        print(cost_s1)
    elif cost_s1 == -1:
        print(cost_s0)
    # 両方とも到達可能な場合は、最小値を出力
    else:
        print(min(cost_s0, cost_s1))

# --- 実行 ---
if __name__ == '__main__':
    solve()
##################################################################
[gptoss AC]
import sys
from collections import deque

def solve() -> None:
    it = iter(sys.stdin.read().strip().splitlines())
    try:
        h, w = map(int, next(it).split())
    except StopIteration:
        return

    grid = []
    start = goal = None
    for i in range(h):
        line = next(it)
        grid.append(line)
        for j, ch in enumerate(line):
            if ch == 'S':
                start = (i, j)
            elif ch == 'G':
                goal = (i, j)

    # visited[h][w][2]
    visited = [[[False] * 2 for _ in range(w)] for _ in range(h)]
    q = deque()

    sr, sc = start
    q.append((sr, sc, 0, 0))          # i, j, door_state, distance
    visited[sr][sc][0] = True

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r, c, d, dist = q.popleft()

        if (r, c) == goal:
            print(dist)
            return

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            ch = grid[nr][nc]
            if ch == '#':
                continue

            # walkability test for current door state d
            walkable = False
            if ch in '.S?G':
                walkable = True
            elif ch == 'o':            # originally open
                walkable = (d == 0)
            elif ch == 'x':            # originally closed
                walkable = (d == 1)

            if not walkable:
                continue

            nd = d
            if ch == '?':
                nd ^= 1                 # toggle door state

            if not visited[nr][nc][nd]:
                visited[nr][nc][nd] = True
                q.append((nr, nc, nd, dist + 1))

    # unreachable
    print(-1)

if __name__ == "__main__":
    solve()
##################################################################
[kimi RE]
#!/usr/bin/env python3
import sys
from collections import deque

def main() -> None:
    H, W = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().rstrip() for _ in range(H)]

    # ----- 1. index, start, goal の収集 -----
    sx = sy = gx = gy = -1              # start / goal
    doors = []                          # (i, j) の順に収集
    door_id = {}                        # (i, j) → bit index
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c == 'S':
                sx, sy = i, j
            elif c == 'G':
                gx, gy = i, j
            elif c == 'o' or c == 'x':
                door_id[(i, j)] = len(doors)
                doors.append((i, j))
    K = len(doors)                      # ドアマスの数
    MASK = (1 << K) - 1                # 全ビット 1

    # 初期ビットマスク作成 : o が立っている, x は落ちている
    mask0 = 0
    for k, (i, j) in enumerate(doors):
        if grid[i][j] == 'o':
            mask0 |= 1 << k

    # ----- 2. BFS 準備 -----
    INF = 1 << 60
    dist = [None] * H
    for i in range(H):
        dist[i] = [None] * W
        for j in range(W):
            dist[i][j] = [INF] * (1 << K)

    Q = deque()
    Q.append((sx, sy, mask0))
    dist[sx][sy][mask0] = 0

    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = INF

    while Q:
        x, y, m = Q.popleft()
        d = dist[x][y][m]
        if x == gx and y == gy:
            ans = d
            break
        
        for dx, dy in DIR:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            nc = grid[nx][ny]
            if nc == '#':
                continue

            # ドアマスかチェック
            if nc == 'x' or nc == 'o':
                k = door_id[(nx, ny)]
                if not (m >> k & 1):     # 0 -> closed
                    continue

            new_m = m
            if nc == '?':
                new_m ^= MASK           # スイッチなら全ビット反転

            if dist[nx][ny][new_m] == INF:
                dist[nx][ny][new_m] = d + 1
                Q.append((nx, ny, new_m))

    print(ans if ans != INF else -1)

if __name__ == '__main__':
    main()
##################################################################
[deepseek AC]
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    H, W = map(int, data[0].split())
    grid = []
    for i in range(1, 1+H):
        grid.append(data[i].strip())
    
    # スタートとゴールの位置を探す
    start = None
    goal = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'G':
                goal = (i, j)
    
    # 距離を記録する3次元配列: dist[i][j][state] (state0=偶数回, state1=奇数回)
    INF = 10**9
    dist = [[[INF] * 2 for _ in range(W)] for __ in range(H)]
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    q = deque()
    i0, j0 = start
    dist[i0][j0][0] = 0
    q.append((i0, j0, 0))
    
    while q:
        i, j, state = q.popleft()
        d = dist[i][j][state]
        if (i, j) == goal:
            print(d)
            return
            
        for dx, dy in directions:
            ni = i + dx
            nj = j + dy
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            cell = grid[ni][nj]
            # 障害物は常にダメ
            if cell == '#':
                continue
                
            # 現在の状態で通行可能かチェック
            if cell == 'o':
                # 状態0なら通行可能、状態1なら通行不可
                if state == 1:
                    continue
            elif cell == 'x':
                # 状態0なら通行不可、状態1なら通行可能
                if state == 0:
                    continue
                    
            # それ以外（'.','S','G','?'）は通行可能（ただし'S','G'は状態によらず）
            # 次のマスがスイッチなら状態が反転、そうでなければ同じ状態
            next_state = state
            if cell == '?':
                next_state = 1 - state
                
            if dist[ni][nj][next_state] > d + 1:
                dist[ni][nj][next_state] = d + 1
                q.append((ni, nj, next_state))
                
    print(-1)

if __name__ == "__main__":
    main()
##################################################################
[moon]
n,q=map(int,input().split())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
s=sum(min(i,j)for i,j in zip(a,b))
for _ in range(q):
  c,x,v=input().split()
  x=int(x)-1
  v=int(v)
  s-=min(a[x],b[x])
  if c=='A':
    a[x]=v
  else:
    b[x]=v
  s+=min(a[x],b[x])
  print(s)
##################################################################
[ryo]
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum_mins = 0

for a, b in zip(A, B):
    sum_mins += min(a, b)

for _ in range(Q):
    c, x, v = input().split()
    x, v = int(x), int(v)

    num = min(A[x - 1], B[x - 1])
    sum_mins -= num
    if c == 'A':
        A[x - 1] = v
    else:
        B[x - 1] = v
    sum_mins += min(A[x - 1], B[x - 1])
    print(sum_mins)
    
##################################################################
[toka]
N,Q = map(int,input().split())
A = list(map(int,input().split())) 
B = list(map(int,input().split())) 
ans = 0
for i in range(N):
  ans += min(A[i],B[i])
for i in range(Q):
  c,X,V = input().split()
  X = int(X)
  V = int(V)
  X -= 1
  temp = min(A[X],B[X])
  if c == "A":
    A[X] = V
  else:
    B[X] = V
  new = min(A[X],B[X])
  ans += (new - temp)
  print(ans)
##################################################################
[titia]
import sys
input = sys.stdin.readline

X=int(input())

ANS=[]
for i in range(10**8+1):
    if (X-i*i)%(2*i-1)==0:
        beta=(X-i*i)//(2*i-1)
        #print(beta)
        ANS.append(beta)
        ANS.append(-beta-1)
        
ANS=sorted(set(ANS))

print(len(ANS))
print(*ANS)

##################################################################
[myai AC]
from collections import deque

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            sx, sy = i, j
        if grid[i][j] == 'G':
            gx, gy = i, j

INF = 10**9
dist = [[[INF]*2 for _ in range(W)] for _ in range(H)]
dq = deque()
dist[sx][sy][0] = 0
dq.append((sx, sy, 0))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def can_move(cell, t):
    if cell == '#':
        return False
    if cell == 'o':
        return t == 0
    if cell == 'x':
        return t == 1
    return True

while dq:
    x, y, t = dq.popleft()
    d = dist[x][y][t]
    if (x, y) == (gx, gy):
        print(d)
        exit()
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        cell = grid[nx][ny]
        if not can_move(cell, t):
            continue
        nt = t
        if cell == '?':
            nt = 1 - t
        if dist[nx][ny][nt] > d+1:
            dist[nx][ny][nt] = d+1
            dq.append((nx, ny, nt))

print(-1)
##################################################################
