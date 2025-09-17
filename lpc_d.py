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
###############################################
###############################################
###############################################
###############################################
[gemini AC]
import sys
from atcoder.maxflow import MFGraph

def solve():
    N, M = map(int, sys.stdin.readline().split())
    S = [sys.stdin.readline().strip() for _ in range(N)]
    
    source = N * M
    sink = N * M + 1
    mg = MFGraph(N * M + 2)
    
    result_grid = [list(row) for row in S]
    
    for i in range(N):
        for j in range(M):
            if S[i][j] == '#':
                continue
            
            u = i * M + j
            
            if (i + j) % 2 == 0:  # 白いマス (white squares)
                mg.add_edge(source, u, 1)
                # Add edges to adjacent black squares only
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < N and 0 <= nj < M and S[ni][nj] == '.' and 
                        (ni + nj) % 2 == 1):  # Only connect to black squares
                        v = ni * M + nj
                        mg.add_edge(u, v, 1)
            else:  # 黒いマス (black squares)
                mg.add_edge(u, sink, 1)
    
    max_flow = mg.flow(source, sink)
    print(max_flow)
    
    edges = mg.edges()
    # Debug: print the first edge attributes to see what's available
    if edges:
        print(f"Edge attributes: {dir(edges[0])}", file=sys.stderr)
    
    for edge in edges:
        if edge.flow == 1:
            u_node = edge.src
            v_node = edge.dst
            
            if u_node == source or v_node == sink:
                continue
                
            ui, uj = u_node // M, u_node % M
            vi, vj = v_node // M, v_node % M
            
            if result_grid[ui][uj] == '.' and result_grid[vi][vj] == '.':
                # Flow always goes from white (source side) to black (sink side)
                # So u_node should be white, v_node should be black
                if uj < vj:  # horizontal: white to black (left to right)
                    result_grid[ui][uj] = '>'
                    result_grid[vi][vj] = '<'
                elif uj > vj:  # horizontal: white to black (right to left)
                    result_grid[ui][uj] = '<'
                    result_grid[vi][vj] = '>'
                elif ui < vi:  # vertical: white to black (top to bottom)
                    result_grid[ui][uj] = 'v'
                    result_grid[vi][vj] = '^'
                elif ui > vi:  # vertical: white to black (bottom to top)
                    result_grid[ui][uj] = '^'
                    result_grid[vi][vj] = 'v'
    
    for row in result_grid:
        print("".join(row))

if __name__ == "__main__":
    solve()
###############################################
[maki]
from atcoder.maxflow import MFGraph
N,M = list(map(int,input().split()))
S = [input() for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
G = MFGraph(N*M+2)
START,T = N*M,N*M+1
for i in range(N):
    for j in range(M):
        if(S[i][j] == "#"):continue
        if((i+j)%2 == 0):
            G.add_edge(START,i*M+j,1)
            for k in range(4):
                next_y = i + dy[k]
                next_x = j + dx[k]
                if(next_y < 0 or N <= next_y):continue
                if(next_x < 0 or M <= next_x):continue
                if(S[next_y][next_x] == "#"):continue
                G.add_edge(i*M+j,next_y*M+next_x,1)
        else:
            G.add_edge(i*M+j,T,1)

ans = G.flow(START,T,N*M)

ans_graph = [["." if S[i][j] == "." else "#" for j in range(M)] for i in range(N)]
for i in G.edges():
    if(i.src == N*M):continue
    if(i.dst == N*M+1):continue
    if(i.flow == 0):continue
    sy = i.src//M
    sx = i.src%M
    ty = i.dst//M
    tx = i.dst%M
    if(sy+1 == ty):
        ans_graph[sy][sx] = "v"
        ans_graph[ty][tx] = "^"
    elif(sy-1 == ty):
        ans_graph[sy][sx] = "^"
        ans_graph[ty][tx] = "v"
    elif(sx+1 == tx):
        ans_graph[sy][sx] = ">"
        ans_graph[ty][tx] = "<"
    else:
        ans_graph[sy][sx] = "<"
        ans_graph[ty][tx] = ">"

print(ans)
for i in ans_graph:
    print("".join(i))
###############################################
[kei]
from atcoder.maxflow import MFGraph
n,m=map(int,input().split())
G=MFGraph(n*m+2)
S=[list(input()) for _ in range(n)]
D=[[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    for j in range(m):
        if S[i][j]=="#":
            continue
        if (i+j)%2==0:
            G.add_edge(0,i*m+j+1,1)
            for dx,dy in D:
                if 0<=i+dx<n and 0<=j+dy<m and S[i+dx][j+dy]==".":
                    G.add_edge(i*m+j+1,(i+dx)*m+(j+dy)+1,1)
        else:
            G.add_edge(i*m+j+1,n*m+1,1)
        
print(G.flow(0,n*m+1))
for src,dst,cap,flow in G.edges():
    if flow==1 and src!=0 and dst!=n*m+1:
        if src>dst:
            src,dst=dst,src
        src-=1
        dst-=1
        si,sj,di,dj=src//m,src%m,dst//m,dst%m
        if dst-src==m:
            S[si][sj]="v"
            S[di][dj]="^"
        else:
            S[si][sj]=">"
            S[di][dj]="<"
for s in S:
    print(''.join(s))
###############################################
[gemini AC]
import sys

# 再帰回数の上限を設定
sys.setrecursionlimit(200000)

def main():
    N, M = map(int, sys.stdin.readline().split())
    S = [sys.stdin.readline().strip() for _ in range(N)]

    # マスをチェッカーボードのように塗り分ける
    # 0: 白, 1: 黒
    color = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 1:
                color[i][j] = 1

    # 隣接リスト
    graph = [[] for _ in range(N * M)]
    for i in range(N):
        for j in range(M):
            if S[i][j] == '.':
                # 白いマスから黒いマスへの辺を追加
                if color[i][j] == 0:
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and S[ni][nj] == '.':
                            u = i * M + j
                            v = ni * M + nj
                            graph[u].append(v)

    # 探索済みフラグ
    visited = [False] * (N * M)
    # マッチング
    match = [-1] * (N * M)

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            w = match[v]
            if w == -1 or (not visited[w] and dfs(w)):
                match[v] = u
                return True
        return False

    matching_count = 0
    for i in range(N * M):
        if color[i // M][i % M] == 0 and match[i] == -1: # 白いマスでまだマッチングされていない頂点
            visited = [False] * (N * M)
            if dfs(i):
                matching_count += 1

    print(matching_count)

    result_grid = [list(row) for row in S]

    # マッチング結果を基にタイルを配置
    for i in range(N * M):
        if match[i] != -1:
            u, v = i, match[i]
            ui, uj = u // M, u % M
            vi, vj = v // M, v % M
            
            if uj < vj: # 横方向
                result_grid[ui][uj] = '>'
                result_grid[vi][vj] = '<'
            elif uj > vj: # 横方向
                result_grid[ui][uj] = '<'
                result_grid[vi][vj] = '>'
            elif ui < vi: # 縦方向
                result_grid[ui][uj] = 'v'
                result_grid[vi][vj] = '^'
            else: # 縦方向
                result_grid[ui][uj] = '^'
                result_grid[vi][vj] = 'v'
    
    for row in result_grid:
        print("".join(row))

if __name__ == "__main__":
    main()
###############################################
[cgpt AC]
import sys
from collections import deque

# Hopcroft–Karp algorithm
def hopcroft_karp(graph, U_size, V_size):
    INF = 10**9
    pairU = [-1] * U_size
    pairV = [-1] * V_size
    dist = [0] * U_size

    def bfs():
        q = deque()
        for u in range(U_size):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in graph[u]:
                    if pairV[v] == -1:
                        d = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return d != INF

    def dfs(u):
        for v in graph[u]:
            if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(U_size):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return matching, pairU, pairV


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [list(input().strip()) for _ in range(N)]

    # 黒白に分割（チェッカーボード）
    id_black, id_white = {}, {}
    b_id = w_id = 0
    id_map = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if S[i][j] == '.':
                if (i + j) % 2 == 0:
                    id_black[(i, j)] = b_id
                    id_map[i][j] = b_id
                    b_id += 1
                else:
                    id_white[(i, j)] = w_id
                    id_map[i][j] = w_id
                    w_id += 1

    # 黒 → 白 の二部グラフ構築
    graph = [[] for _ in range(b_id)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (i, j), u in id_black.items():
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and S[ni][nj] == '.':
                v = id_white.get((ni, nj), -1)
                if v != -1:
                    graph[u].append(v)

    # 最大マッチング
    max_match, pairU, pairV = hopcroft_karp(graph, b_id, w_id)

    # 出力用に盤面コピー
    T = [row[:] for row in S]

    # マッチ結果に基づいてタイルを描画
    for (i, j), u in id_black.items():
        v = pairU[u]
        if v != -1:
            # v に対応する白マスを探す
            for (ii, jj), wid in id_white.items():
                if wid == v:
                    if i == ii:  # 横
                        if j < jj:
                            T[i][j], T[ii][jj] = '>', '<'
                        else:
                            T[i][j], T[ii][jj] = '<', '>'
                    else:  # 縦
                        if i < ii:
                            T[i][j], T[ii][jj] = 'v', '^'
                        else:
                            T[i][j], T[ii][jj] = '^', 'v'
                    break

    # 出力
    print(max_match)
    for row in T:
        print(''.join(row))


if __name__ == "__main__":
    solve()

###############################################
