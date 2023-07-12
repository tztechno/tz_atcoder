###################################################

#cumulative sum

    for i in range(1, H+1):
        for j in range(1, W+1):
            Z[i][j] = Z[i][j-1] + X[i][j]
    for j in range(1, W+1):
        for i in range(1, H+1):
            Z[i][j] = Z[i-1][j] + Z[i][j]

###################################################

def cumulative_sum_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 二次元累積和用の配列を作成
    cumulative_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

    # 二次元累積和を計算
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cumulative_sum[i][j] = cumulative_sum[i - 1][j] + cumulative_sum[i][j - 1] - cumulative_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

    return cumulative_sum

# 使用例
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

cumulative_sum = cumulative_sum_2d(matrix)
for row in cumulative_sum:
    print(row)
    
###################################################
