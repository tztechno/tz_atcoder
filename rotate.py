#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################

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

def rotate_matrix(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]
    
test_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result0 = spiral_rotate(test_matrix)
for row in result0:
    print(row)

result1 = rotate_matrix(test_matrix)
for row in result1:
    print(row)

resut0
[13, 9, 5, 1]
[14, 11, 10, 2]
[15, 7, 6, 3]
[16, 12, 8, 4]

result1
[13, 9, 5, 1]
[14, 10, 6, 2]
[15, 11, 7, 3]
[16, 12, 8, 4]

#####################################################

2つの関数は確かに行列の回転を行っていますが、その方法と結果には重要な違いがあります。

1. 回転のパターン:

   `rotate_matrix`:
   - 行列全体を一様に90度時計回りに回転させます。
   - すべての要素が同じ方向に同じ量だけ移動します。

   `spiral_rotate`:
   - 行列を同心の四角形（層）に分け、各層ごとに異なる回転を適用します。
   - 外側の層から内側に向かって、90度時計回り、180度、90度反時計回り、回転なし、という順序で回転が適用されます。

2. アルゴリズムの複雑さ:

   `rotate_matrix`:
   - シンプルで直接的なアプローチを使用しています。
   - 転置と行の反転という2つの基本操作を組み合わせています。

   `spiral_rotate`:
   - より複雑なロジックを使用しています。
   - 各要素の位置に基づいて、どの層に属するかを計算し、適切な回転を適用します。

#####################################################

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
    
#####################################################

def rotate_matrix(matrix):
    # 転置して各行を反転させることで時計回りに90度回転させる
    return [list(reversed(row)) for row in zip(*matrix)]

rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)

#####################################################
