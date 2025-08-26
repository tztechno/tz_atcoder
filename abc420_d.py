
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
高橋君がはじめスタートマスにいる状態からゴールマスにいる状態にするよう操作できるか判定し、可能な場合は必要な操作回数の最小値を求めてください。
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

##################################################################

##################################################################

##################################################################

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
