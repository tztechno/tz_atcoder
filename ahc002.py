
###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################
[焼きなまし with error]

import sys
import random
import math

# 標準入力からのデータ読み込み
input = sys.stdin.read
data = input().splitlines()

# 初期位置
si, sj = map(int, data[0].split())

# タイル情報 T の読み込み
T = []
for i in range(50):
    T.append(list(map(int, data[1 + i].split())))

# 得点情報 P の読み込み
P = []
for i in range(50):
    P.append(list(map(int, data[51 + i].split())))

h, w = 50, 50
A = [[0 for _ in range(50)] for _ in range(50)]
A[si][sj] = 1  # スタート位置は訪問済みに設定

# 焼きなまし法のパラメータ
initial_temperature = 100.0
cooling_rate = 0.99
num_iterations = 1000

# 目的関数: 経路全体の得点を合計
def calculate_score(route):
    return sum(P[i][j] for i, j in route)

# 隣接セルへのルート生成（訪問済みチェック込み）
def generate_neighbor(route):
    temp_A = [row[:] for row in A]
    i, j = route[-1]
    neighbors = []
    
    # 未訪問の隣接セルへの移動
    if 0 <= i+1 < h and A[i+1][j] == 0:
        neighbors.append([i+1, j])
    if 0 <= i-1 < h and A[i-1][j] == 0:
        neighbors.append([i-1, j])
    if 0 <= j+1 < w and A[i][j+1] == 0:
        neighbors.append([i, j+1])
    if 0 <= j-1 < w and A[i][j-1] == 0:
        neighbors.append([i, j-1])
    
    # ランダムに未訪問の隣接セルを選択
    if neighbors:
        next_position = random.choice(neighbors)
        route.append(next_position)
        A[next_position[0]][next_position[1]] = 1
        return route
    return route

# 焼きなまし法のメインループ
current_route = [[si, sj]]
current_score = calculate_score(current_route)
temperature = initial_temperature

for _ in range(num_iterations):
    new_route = generate_neighbor(current_route[:])  # 現在のルートのコピーを作成
    new_score = calculate_score(new_route)
    
    # ルート変更の確率的受け入れ
    if new_score > current_score or random.random() < math.exp((current_score - new_score) / temperature):
        current_route = new_route
        current_score = new_score
    else:
        # 更新されなかった場合、Aの状態をリセット
        for cell in new_route[len(current_route):]:
            A[cell[0]][cell[1]] = 0
    
    # 温度を下げる
    temperature *= cooling_rate

# 移動履歴を生成
def udgen(route):
    trace = ''
    for i in range(1, len(route)):
        d1i, d1j = route[i]
        d0i, d0j = route[i - 1]
        if d1j - d0j == 1:
            trace += 'R'
        elif d1j - d0j == -1:
            trace += 'L'
        elif d1i - d0i == 1:
            trace += 'D'
        elif d1i - d0i == -1:
            trace += 'U'
    return trace

# 結果の表示
print(udgen(current_route))
print("Score:", current_score)

###################################################################

import sys
import time
from heapq import heappop, heappush, nsmallest
ints = lambda: map(int, sys.stdin.readline().split())

dist = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

si, sj = ints()
t = [[*ints()] for _ in range(50)]
p = [[*ints()] for _ in range(50)]

best = 0
res = []
start = time.time()
queue = []
v0 = [0] * (max(map(max, t)) + 1)
v0[t[si][sj]] = 1
heappush(queue, (0, [], v0, si, sj))

def traverse():
    global best, res
    d, path, visited, i, j = heappop(queue)
    if d < best:
        best = d
        res = path
    for c, (di, dj) in dist.items():
        ni, nj = i + di, j + dj
        if not (0 <= ni < 50 and 0 <= nj < 50):
            continue
        ti = t[ni][nj]
        if visited[ti]:
            continue
        heappush(
            queue,
            (
                d - p[ni][nj],
                [*path, c],
                [*visited[:ti], 1, *visited[ti + 1:]],
                ni, nj
            )
        )

while True:
    for _ in range(200):
        traverse()
    queue = nsmallest(200, queue)
    if time.time() - start > 1.88:
        break
print(*res, sep='')

###################################################################
[standard method]

x,y= map(int, input().split())
T=[]
for i in range(50):
    T+=[list(map(int, input().split()))]
P=[]
for i in range(50):
    P+=[list(map(int, input().split()))]

A=[]
for i in range(50):
    a=[]
    for j in range(50):
        a+=[0]
    A+=[a]  

h,w=50,50
A[x][y]=1



def nextgo6(R):
    R1=[]
    for itemR in R:
        i=itemR[-1][0]
        j=itemR[-1][1]
        p=T[i][j]
        
        if (0<j-1<w) and T[i][j-1]==p:
                A[i][j-1]=1
        if (0<j+1<w) and T[i][j+1]==p:
                A[i][j+1]=1 
        if (0<i-1<h) and T[i-1][j]==p:
                A[i-1][j]=1        
        if (0<i+1<h) and T[i+1][j]==p:
                A[i+1][j]=1        
        
        if (0<i+1<h) and (A[i+1][j]==0) and (T[i+1][j]!=p):
            R1+=[itemR+[[i+1,j]]]
            A[i+1][j]=1

        elif (0<j+1<w) and (A[i][j+1]==0) and (T[i][j+1]!=p):
            R1+=[itemR+[[i,j+1]]]
            A[i][j+1]=1
            
        elif (0<i-1<h) and (A[i-1][j]==0) and (T[i-1][j]!=p):
            R1+=[itemR+[[i-1,j]]]
            A[i-1][j]=1
            
        elif (0<j-1<w) and (A[i][j-1]==0) and (T[i][j-1]!=p):
            R1+=[itemR+[[i,j-1]]]   
            A[i][j-1]=1
                
        else:
            return R
        
    return R1


R=[[[x,y]]]
for i in range(2500):
    R=nextgo6(R)

def udgen(R):
    D=R[0]
    trace=''
    for i in range(1,len(D)):
        d1i=D[i][0]
        d1j=D[i][1]
        d0i=D[i-1][0]
        d0j=D[i-1][1]
        if d1j-d0j==1:
            trace+='R'
        if d1j-d0j==-1:
            trace+='L'
        if d1i-d0i==1:
            trace+='D'
        if d1i-d0i==-1:
            trace+='U'
    return trace    
    
print(udgen(R))

###################################################################
