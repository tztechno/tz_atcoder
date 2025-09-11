##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################

1. **距離計算**

   * 各非常口 `E` を始点とする **多点同時 BFS** を行い、全ての通路マス `.` に対して最近接非常口までの最短距離 `d(i,j)` を求める。
   * 壁 `#` は通れない。

2. **矢印の決定**

   * BFS をするときに「どこから来たか」を記録する。
   * 例えば `(nx,ny)` が `(x,y)` から到達したなら、`(nx,ny)` に矢印を書き込むときは「`(x,y)` 方向を向かせる」。
   * これを逆向きに考えると：

     * 非常口から1手で行けるマスは、非常口に向かう矢印を持つべき。
     * つまり BFS 拡張時に「次のマスに非常口方向を示す矢印」を置く。

3. **出力**

   * 壁と非常口はそのまま出力。
   * 通路マスには BFS で決めた矢印を出力。

##############################
[titia]
import sys
input = sys.stdin.readline

from collections import deque

H,W=map(int,input().split())
MAP=[input().strip() for i in range(H)]
DIS=[[1<<30]*W for i in range(H)]
Q=deque()

for i in range(H):
    for j in range(W):
        if MAP[i][j]=="E":
            Q.append((i,j))
            DIS[i][j]=0

while Q:
    x,y=Q.popleft()

    for z,w in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=z<H and 0<=w<W:
            if MAP[z][w]==".":
                if DIS[z][w]>DIS[x][y]+1:
                    DIS[z][w]=DIS[x][y]+1
                    Q.append((z,w))

ANS=[["#"]*W for i in range(H)]

for i in range(H):
    for j in range(W):
        if MAP[i][j]!=".":
            ANS[i][j]=MAP[i][j]
        else:
            x=DIS[i][j]

            for z,w in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=z<H and 0<=w<W:
                    if DIS[z][w]<DIS[i][j]:
                        if z==i-1:
                            ANS[i][j]="^"
                        elif z==i+1:
                            ANS[i][j]="v"
                        elif w==j-1:
                            ANS[i][j]="<"
                        else:
                            ANS[i][j]=">"

for ans in ANS:
    print("".join(ans))

##############################
[hung]
from collections import deque
grid = []
h, w = map(int, input().split())
for i in range(h):
    grid.append(list(input()))

directions = [(0, 1, '<'), (0, -1, '>'), (-1, 0, 'v'), (1, 0, '^')]
q = deque()

for i in range(h):
    for j in range(w):
        if grid[i][j] == 'E':
            q.append(('E', i, j))
        
while q:
    val, i, j = q.popleft()
    for dx, dy, char in directions:
        di = i + dx
        dj = j + dy
        
        if 0 <= di < h and 0 <= dj < w and grid[di][dj] == '.':
            grid[di][dj] = char
            q.append((grid[di][dj], di, dj))

for row in grid:
    print(''.join(row))
##############################
[rin]
from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

Q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            Q.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
A = ['^', '<', 'v', '>']

def ok(i, j):
    return 0 <= i < H and 0 <= j < W

while Q:
    i, j = Q.popleft()
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if not ok(ni, nj):
            continue
        if S[ni][nj] != '.':
            continue
        S[ni][nj] = A[k]
        Q.append((ni, nj))

for row in S:
    print(''.join(row))

##############################
[myai AC]

from collections import deque

H,W = map(int,input().split())
S = [list(input().strip()) for _ in range(H)]

# 矢印を格納する配列（最終的に答えになる）
T = [row[:] for row in S]

q = deque()
dist = [[-1]*W for _ in range(H)]

# 初期化：非常口からスタート
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            q.append((i,j))
            dist[i][j] = 0

dirs = [(-1,0,'v'),(1,0,'^'),(0,-1,'>'),(0,1,'<')]  

while q:
    x,y = q.popleft()
    for dx,dy,arrow in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<H and 0<=ny<W:
            if S[nx][ny]=='.' and dist[nx][ny]==-1:
                dist[nx][ny] = dist[x][y]+1
                T[nx][ny] = arrow  # このマスには親方向の矢印
                q.append((nx,ny))

# 出力
for row in T:
    print("".join(row))
##############################
