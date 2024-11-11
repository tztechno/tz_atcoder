
###################################################################


###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################

###################################################################
[焼きなまし]

import random
import math

# 初期位置の設定
x, y = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(50)]
P = [list(map(int, input().split())) for _ in range(50)]

h, w = 50, 50
goal_x, goal_y = 49, 49  # 目的地（例として設定）
A = [[0 for _ in range(50)] for _ in range(50)]
A[x][y] = 1

# 焼きなまし法のパラメータ
initial_temperature = 100.0
cooling_rate = 0.99
num_iterations = 1000

# 目的関数
def calculate_cost(route):
    last_x, last_y = route[-1]
    return abs(last_x - goal_x) + abs(last_y - goal_y)  # マンハッタン距離を使った目的関数

# ルート生成
def generate_neighbor(route):
    i, j = route[-1]
    neighbors = []
    
    # 隣接するセルへの移動
    if 0 <= i+1 < h:
        neighbors.append([i+1, j])
    if 0 <= i-1 < h:
        neighbors.append([i-1, j])
    if 0 <= j+1 < w:
        neighbors.append([i, j+1])
    if 0 <= j-1 < w:
        neighbors.append([i, j-1])
    
    # ランダムに隣接セルを選択
    if neighbors:
        next_position = random.choice(neighbors)
        return route + [next_position]
    return route

# 焼きなまし法のメインループ
current_route = [[x, y]]
current_cost = calculate_cost(current_route)
temperature = initial_temperature

for _ in range(num_iterations):
    new_route = generate_neighbor(current_route)
    new_cost = calculate_cost(new_route)
    
    # ルート変更の確率的受け入れ
    if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
        current_route = new_route
        current_cost = new_cost
    
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
