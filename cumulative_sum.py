    #cumulative sum
    for i in range(1, H+1):
        for j in range(1, W+1):
            Z[i][j] = Z[i][j-1] + X[i][j]
    for j in range(1, W+1):
        for i in range(1, H+1):
            Z[i][j] = Z[i-1][j] + Z[i][j]
