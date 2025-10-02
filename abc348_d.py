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
[ds1]
from collections import deque
import sys

def main():
    H, W = map(int, input().split())
    grid = []
    start = None
    goal = None
    
    for i in range(H):
        row = input().strip()
        grid.append(row)
        for j in range(W):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'T':
                goal = (i, j)
    
    N = int(input())
    medicine = [[-1] * W for _ in range(H)]
    
    for _ in range(N):
        r, c, e = map(int, input().split())
        r -= 1
        c -= 1
        medicine[r][c] = e
    
    # 各マスで達成可能な最大エネルギー
    max_energy = [[-1] * W for _ in range(H)]
    
    # BFS: (row, col, energy)
    queue = deque()
    sr, sc = start
    queue.append((sr, sc, 0))
    max_energy[sr][sc] = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, energy = queue.popleft()
        
        # 薬を使う場合
        if medicine[r][c] != -1:
            new_energy = medicine[r][c]
            if new_energy > max_energy[r][c]:
                max_energy[r][c] = new_energy
                queue.append((r, c, new_energy))
        
        # エネルギーが0なら移動できない
        if energy == 0:
            continue
        
        # 移動する場合
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#':
                new_energy = energy - 1
                if new_energy > max_energy[nr][nc]:
                    max_energy[nr][nc] = new_energy
                    queue.append((nr, nc, new_energy))
    
    gr, gc = goal
    if max_energy[gr][gc] >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
###############################################
[ds2]
from collections import deque
import sys

H, W = map(int, input().split())
grid = []
start = None
goal = None

for i in range(H):#0start
    row = input().strip()
    grid.append(row)
    for j in range(W):
        if row[j] == 'S':
            start = (i, j)
        elif row[j] == 'T':
            goal = (i, j)

N = int(input())
medicine = [[-1] * W for _ in range(H)]

for _ in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    medicine[r][c] = e

#medicine filedにenergyのvalueが入る



# 各マスで達成可能な最大エネルギー
max_energy = [[-1] * W for _ in range(H)]

# BFS: (row, col, energy)
queue = deque()
sr, sc = start
queue.append((sr, sc, 0))
max_energy[sr][sc] = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while queue:
    r, c, energy = queue.popleft()
    
    # 薬を使う場合
    if medicine[r][c] != -1:
        new_energy = medicine[r][c]
        if new_energy > max_energy[r][c]:
            max_energy[r][c] = new_energy
            queue.append((r, c, new_energy))
    
    # エネルギーが0なら移動できない
    if energy == 0:
        continue
    
    # 移動する場合
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#':
            new_energy = energy - 1
            if new_energy > max_energy[nr][nc]:
                max_energy[nr][nc] = new_energy
                queue.append((nr, nc, new_energy))

gr, gc = goal
if max_energy[gr][gc] >= 0:
    print("Yes")
else:
    print("No")

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
