##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

def get_pos(num, i, j):
    if num == 0:
        return i, i + j
    elif num == 1:
        return i + j, N - i - 1
    elif num == 2:
        return N - i - 1, N - i - j - 1
    elif num == 3:
        return N - i - j - 1, i
    raise Exception()

def calc(N, A):
    # 右90度
    result = [[" " for n in range(N)] for n in range(N)]
    for i in range(N//2 + 1):
        for j in range(N - i * 2):
            m = i % 4
            for k in range(4):
                n_y, n_x = get_pos(k, i, j)
                y, x = get_pos((k - i - 1) % 4, i, j)
                result[n_y][n_x] = A[y][x]
    return result


N = int(input())
result = calc(N, [list(input()) for n in range(N)])
for a in result:
    print("".join(a))

##########################################################

def main():
    N = int(input())
    A = [ list(str(input())) for _ in range(N)]
    B = [['.']*(N) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            # n_layer = min(i,j,N-1-i,N-1-j)
            # 最初の外枠を90度回転に対応させるために1-indexとして扱う
            n_layer = min(i+1,j+1,N-1-i+1,N-1-j+1)
            
            ni,nj = i,j
            # 何回90度回転させるか
            for _ in range(n_layer%4):
                ni,nj = nj,ni
                nj = N-1-nj
            
            B[ni][nj] = A[i][j]
            
    for i in range(N):
        print("".join(B[i]))
    
if __name__ == '__main__':
    main()
    
##########################################################

import sys
input = sys.stdin.readline

n = int(input())
a = [list(input()) for _ in range(n)]
s = [[""] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    ni, nj = i, j
    for _ in range(min(i + 1, j + 1, n - i, n - j) % 4):
      ni, nj = nj, n - 1 - ni
    s[ni][nj] = a[i][j]
for t in s:
  print("".join(t))
    
##########################################################
[titia]

import sys
input = sys.stdin.readline

N=int(input())
MAP=[input().strip() for i in range(N)]

ANS=[["."]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        X=min(i,j,N-1-i,N-1-j)

        if X%4==0:
            ANS[i][j]=MAP[N-1-j][i]
        elif X%4==1:
            ANS[i][j]=MAP[N-1-i][N-1-j]
        elif X%4==2:
            ANS[i][j]=MAP[j][N-1-i]
        else:
            ANS[i][j]=MAP[i][j]

for ans in ANS:
    print("".join(ans))

##########################################################

対象の正方形に対して
spiral_rotate は層ごとに異なる回転を適用する
X % 4 == 0: マップを90度右に回転させた位置の値を取得。
X % 4 == 1: マップを180度回転させた位置の値を取得。
X % 4 == 2: マップを270度右に回転させた位置の値を取得。
X % 4 == 3: 元のマップの同じ位置の値を保持。

def spiral_rotate(matrix):
    N = len(matrix)
    rotated = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            X = min(i, j, N-1-i, N-1-j)
            if X % 4 == 0:
                rotated[i][j] = matrix[N-1-j][i]
            elif X % 4 == 1:
                rotated[i][j] = matrix[N-1-i][N-1-j]
            elif X % 4 == 2:
                rotated[i][j] = matrix[j][N-1-i]
            else:
                rotated[i][j] = matrix[i][j]
    return rotated

##########################################################
[my TLE]
[単純回転はそもそも間違い]

import sys
import numpy as np
input = sys.stdin.readline
N = int(input().strip())
A0 = []
for i in range(N):
    A0.append(list(input().strip())) 
A = np.array(A0)
for j in range(N // 2):
    A[j:N-j, j:N-j] = np.rot90(A[j:N-j, j:N-j], k=3)
for i in range(N):
    print(''.join(A[i])) 
  
##########################################################
