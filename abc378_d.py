###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################

h, w, k_s = map(int, input().split())
m = [list(input()) for _ in range(h)]

ans = 0
vis = [[False for _ in range(w)] for _ in range(h)]
def dfs(i, j, k):
	global ans
	if k == k_s:
		ans += 1
		return
	dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	
	
	for dx, dy in dir:
		ni, nj = dx+i, dy+j
		if ni >= 0 and ni < h and nj >= 0 and nj < w \
			and not vis[ni][nj] and m[ni][nj] == ".":
			vis[i][j] = True
			dfs(ni, nj, k+1)
			vis[i][j] = False
	
	
for i in range(h):
	for j in range(w):
		if m[i][j] == ".":
			dfs(i, j, 0)

print(ans)
###########################################################

import sys
input = sys.stdin.readline

H,W,K=map(int,input().split())

MAP=[input().strip() for i in range(H)]

ANS=[0]

def calc(x,y,History,K):
    if K==0:
        ANS[0]+=1
        return

    if x+1<H and MAP[x+1][y]=="." and not ((x+1)*W+y in History):
        calc(x+1,y,History|{(x+1)*W+y},K-1)

    if x-1>=0 and MAP[x-1][y]=="." and not ((x-1)*W+y in History):
        calc(x-1,y,History|{(x-1)*W+y},K-1)

    if y+1<W and MAP[x][y+1]=="."  and not (x*W+y+1 in History):
        calc(x,y+1,History|{x*W+y+1},K-1)

    if y-1>=0 and MAP[x][y-1]=="."  and not (x*W+y-1 in History):
        calc(x,y-1,History|{x*W+y-1},K-1)
        
    
for i in range(H):
    for j in range(W):
        if MAP[i][j]==".":
            calc(i,j,{i*W+j},K)

print(ANS[0])
###########################################################
