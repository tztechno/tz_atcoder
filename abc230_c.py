###############################################
###############################################
###############################################
###############################################
[tr3]
N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

for i in range(P,Q+1):
  C = []
  for j in range(R,S+1):
   if  abs(i-A)==abs(j-B):
    C.append("#")
   else:
    C.append(".")
  print("".join(C))
###############################################
[oto]
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

P -= 1
Q -= 1
R -= 1
S -= 1

grids: list[list[str]] = []
for i in range(Q - P + 1):
    row: list[str] = []
    for j in range(S - R + 1):
        # 絶対座標
        ii = P + i
        jj = R + j

        # A, Bから見た相対位置
        di = ii - (A - 1)
        dj = jj - (B - 1)

        # print(i, j)
        # print(di, dj)
        if di == dj:
            if max(1 - A, 1 - B) <= di and di <= min(N - A, N - B):
                row.append("#")
                continue

        if di == -dj:
            if max(1 - A, B - N) <= di and di <= min(N - A, B - 1):
                row.append("#")
                continue

        row.append(".")
    grids.append(row)

for row in grids:
    print("".join(row))
    print("".join(row))

###############################################
###############################################
###############################################
[gemini,AC]
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = int(data[1])
B = int(data[2])
P = int(data[3])
Q = int(data[4])
R = int(data[5])
S = int(data[6])

row_len = Q - P + 1
col_len = S - R + 1

output_lines = []

for i in range(row_len):
  
    current_row = P + i
    c = ['.'] * col_len
    col1 = current_row - (A - B) 

    if 1 <= col1 <= N:
        if R <= col1 <= S:
            j = col1 - R
            c[j] = '#'

    col2 = (A + B) - current_row

    if 1 <= col2 <= N:
        if R <= col2 <= S:
            j = col2 - R
            c[j] = '#'

    output_lines.append("".join(c))

print('\n'.join(output_lines))

###############################################
[gemini,AC]
import sys
# 標準入力の読み込みを高速化 (微調整)
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = int(data[1])
B = int(data[2])
P = int(data[3])
Q = int(data[4])
R = int(data[5])
S = int(data[6])

# 矩形領域のサイズを計算
row_len = Q - P + 1
col_len = S - R + 1

output_lines = []

# 各行 i (0 <= i < row_len) について処理する
# i は矩形内の行インデックス
for i in range(row_len):
    
    # 矩形内の i 行目は、元のグリッドの P+i 行目にあたる
    current_row = P + i
    
    # 行を初期化
    c = ['.'] * col_len

    # --- 対角線 1 (傾き +1) の交差判定 ---
    
    # 対角線1の式: current_row = col + (A - B)
    # これを満たす col は: col = current_row - (A - B)
    
    col1 = current_row - (A - B) 
    
    # N x N グリッド内の制約: 1 <= col1 <= N
    if 1 <= col1 <= N:
        # 矩形領域内の列 R <= col1 <= S に入っているか？
        if R <= col1 <= S:
            # 矩形内の列インデックス j を計算: j = col1 - R
            j = col1 - R
            c[j] = '#'

    # --- 対角線 2 (傾き -1) の交差判定 ---
    
    # 対角線2の式: current_row = (A + B) - col
    # これを満たす col は: col = (A + B) - current_row
    
    col2 = (A + B) - current_row
    
    # N x N グリッド内の制約: 1 <= col2 <= N
    if 1 <= col2 <= N:
        # 矩形領域内の列 R <= col2 <= S に入っているか？
        if R <= col2 <= S:
            # 矩形内の列インデックス j を計算: j = col2 - R
            j = col2 - R
            c[j] = '#'

    # 行の結果を出力リストに追加
    output_lines.append("".join(c))

# 全ての行をまとめて出力
print('\n'.join(output_lines))
###############################################
###############################################
###############################################
###############################################
[TLE31]
N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
from collections import defaultdict,deque,Counter
cnt = defaultdict(list)

for k in range(max(1-A,1-B),min(N-A,N-B)+1):
  if P-1<=A+k-1<Q and R-1<=B+k-1<S:
    cnt[A+k-1-(P-1)].append(B+k-1-(R-1))
    
for k in range(max(1-A,B-N),min(N-A,B-1)+1):
  if P-1<=A+k-1<Q and R-1<=B-k-1<S: 
    cnt[A+k-1-(P-1)].append(B-k-1-(R-1))

#print(cnt)
c0=["."]*(S-(R-1))
for i in range(Q-(P-1)):
  c=c0.copy()
  lst=cnt[i]
  for j in lst:
    c[j]='#'
  print(''.join(c))
###############################################
[TLE32]
N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
from collections import defaultdict,deque,Counter
cnt = defaultdict(list)

for k in range(max(1-A,1-B),min(N-A,N-B)+1):
  if P-1<=A+k-1<Q and R-1<=B+k-1<S:
    cnt[A+k-1-(P-1)].append(B+k-1-(R-1))
    
for k in range(max(1-A,B-N),min(N-A,B-1)+1):
  if P-1<=A+k-1<Q and R-1<=B-k-1<S: 
    cnt[A+k-1-(P-1)].append(B-k-1-(R-1))

#print(cnt)
for i in range(Q-(P-1)):
  c=""
  lst=cnt[i]
  lst.sort()
  for j in range(S-(R-1)):
    if j in lst:
      c+='#'
    else:
      c+='.'
  print(c)


###############################################
[TLE31]
N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())

C=[]
for k in range(max(1-A,1-B),min(N-A,N-B)+1):
  if P-1<=A+k-1<Q and R-1<=B+k-1<S:
    C+=[(A+k-1,B+k-1)]
for k in range(max(1-A,B-N),min(N-A,B-1)+1):
  if P-1<=A+k-1<Q and R-1<=B-k-1<S: 
    C+=[(A+k-1,B-k-1)]
#print(len(C))
C2=[]
for i in range(Q-(P-1)):
  C2+=[['.']*(S-(R-1))]
  
for ci in C:
  i0,j0=ci[0],ci[1]
  i=i0-(P-1)
  j=j0-(R-1)
  C2[i][j]='#'

for i in range(len(C2)):
  print(''.join(list(C2[i])))

###############################################
###############################################
[claude,TLE31]
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

# 2次元グリッドを直接初期化
height = Q - P + 1
width = S - R + 1
grid = [['.' for _ in range(width)] for _ in range(height)]

# 対角線1: 右下方向 (A+k, B+k)
for k in range(max(1-A, 1-B), min(N-A, N-B) + 1):
    i, j = A + k - 1, B + k - 1
    if P - 1 <= i < Q and R - 1 <= j < S:
        grid[i - (P - 1)][j - (R - 1)] = '#'

# 対角線2: 右上方向 (A+k, B-k)
for k in range(max(1-A, B-N), min(N-A, B-1) + 1):
    i, j = A + k - 1, B - k - 1
    if P - 1 <= i < Q and R - 1 <= j < S:
        grid[i - (P - 1)][j - (R - 1)] = '#'

# 出力
for row in grid:
    print(''.join(row))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
