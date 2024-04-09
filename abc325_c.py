//abc325_c.py

###############################################
###############################################
[shoppy]
#グラフを使って解く問題BFSやDFS
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def dfs(y, x):
    t = [(y, x)]
    while t:
        # print(t)
        y, x = t.pop()
        S[y][x] = "."
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                y2, x2 = y + dy, x + dx
                if 0 <= y2 < H and 0 <= x2 < W and S[y2][x2] == "#":
                    t.append((y2, x2))


ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            dfs(y, x)
            ans += 1
print(ans)

###############################################
[reimo]
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
def Judge(i,j):
    t=[[i,j]]
    while len(t)>0:
        x,y=t.pop()
        s[x][y]="."
        for di in range(-1,2):
            for dj in range(-1,2):
                a_x=x+di
                a_y=y+dj
                if 0<=a_x<h and 0<=a_y<w and s[a_x][a_y]=="#":
                    t.append([a_x,a_y])
ans=0
for i in range(h):  
    for j in range(w):
        if s[i][j]=="#":
            Judge(i,j)
            ans+=1
print(ans)
###############################################
[chame]
from sys import setrecursionlimit
setrecursionlimit(10**7)
h,w=map(int,input().split())
grid=[['.' for _ in range(w+2)]]
for _ in range(h):
    grid.append(['.']+list(input())+['.'])
grid.append(['.' for _ in range(w+2)])

visited=set()
def dfs(i,j,grid,visited):
    visited.add((i,j))
    for x in range(-1,2):
        for y in range(-1,2):
            if (x,y)!=(0,0) and grid[i+x][j+y]=='#' and not((i+x,j+y) in visited):
                dfs(i+x,j+y,grid,visited)
    return 1

count=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j]=='#' and not((i,j) in visited):
            count+=dfs(i,j,grid,visited)

print(count)
###############################################
[titia]
import sys
input = sys.stdin.readline

H,W=map(int,input().split())
MAP=[input().strip() for i in range(H)]

USE=[[0]*W for i in range(H)]

ANS=0

for i in range(H):
    for j in range(W):
        if MAP[i][j]=="#" and USE[i][j]==0:
            ANS+=1
            Q=[(i,j)]

            while Q:
                x,y=Q.pop()
                for z in range(x-1,x+2):
                    for w in range(y-1,y+2):
                        if 0<=z<H and 0<=w<W and USE[z][w]==0 and MAP[z][w]=="#":
                            USE[z][w]=1
                            Q.append((z,w))

print(ANS)
###############################################

[input sample]
3 3
#.#
.#.
#.#
###############################################

[stpete WA & TLE ans]

h,w=map(int,input().split())
S=[]
P=[]
t=0
for i in range(h):
  s=list(input())
  S+=[s]
  for j,si in enumerate(s):
    if si=='#':
      t+=1
      P+=[(i,j)]

T=[]
for i in range(t):
  T+=[set([i])]
  
for i in range(t):
  for j in range(i+1,t):
    if abs(P[i][0]-P[j][0])<=2 and abs(P[i][1]-P[j][1])<=2:
      T[i].add(j)
  
for i in range(len(T)):
  for j in range(i,len(T)):
    if T[i] & T[j] !=set():
      T[i]=T[i]|T[j]
      T[j]=T[i]|T[j]

T2=[]
for t in T:
  T2+=[str(sorted(t))]

print(len(set(T2)))
###############################################
###############################################
