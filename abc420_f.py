
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[myai TLE]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

sparse_table = []
heights = []
prefix_sum_k_div = []

def build_sparse_table(arr):
    global sparse_table
    n = len(arr)
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1
    
    sparse_table = [[0] * n for _ in range(log_table[n] + 1)]
    sparse_table[0] = list(range(n))
    
    for k in range(1, log_table[n] + 1):
        for i in range(n - (1 << k) + 1):
            idx1 = sparse_table[k-1][i]
            idx2 = sparse_table[k-1][i + (1 << (k-1))]
            sparse_table[k][i] = idx1 if heights[idx1] < heights[idx2] else idx2
    
    return log_table

def query_min_idx(l, r, log_table):
    global sparse_table, heights
    k = log_table[r - l + 1]
    idx1 = sparse_table[k][l]
    idx2 = sparse_table[k][r - (1 << k) + 1]
    return idx1 if heights[idx1] < heights[idx2] else idx2

def S(W, H, K):
    global prefix_sum_k_div
    if W <= 0 or H <= 0:
        return 0
    
    w_border = K // H if H > 0 else 0
    res = 0
    
    end1 = min(W, w_border)
    res += end1 * H
    
    start2 = w_border + 1
    if W >= start2:
        res += prefix_sum_k_div[W] - prefix_sum_k_div[start2 - 1]
    
    return res

def solve(l, r, log_table, K):
    if l > r:
        return 0
    
    m = query_min_idx(l, r, log_table)
    h_m = heights[m]
    count = 0
    
    if m - l <= r - m:
        for i in range(l, m + 1):
            w_l = m - i
            w_r_max = r - m
            w_start = w_l + 1
            w_end = w_l + w_r_max + 1
            count += S(w_end, h_m, K) - S(w_start - 1, h_m, K)
    else:
        for j in range(m, r + 1):
            w_r = j - m
            w_l_max = m - l
            w_start = w_r + 1
            w_end = w_r + w_l_max + 1
            count += S(w_end, h_m, K) - S(w_start - 1, h_m, K)
    
    count += solve(l, m - 1, log_table, K)
    count += solve(m + 1, r, log_table, K)
    return count

def main():
    N, M, K = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    
    up = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            up[i][j] = up[i-1][j] + 1 if i > 0 and grid[i][j] == '.' else int(grid[i][j] == '.')
    
    ans = 0
    global heights, prefix_sum_k_div
    
    for i in range(N):
        heights = up[i]
        prefix_sum_k_div = [0] * (M + 1)
        for w in range(1, M + 1):
            prefix_sum_k_div[w] = prefix_sum_k_div[w-1] + K // w
        
        log_table = build_sparse_table(heights)
        ans += solve(0, M - 1, log_table, K)
    
    print(ans)

if __name__ == "__main__":
    main()
##################################################################
