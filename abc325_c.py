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

Judge 関数は、指定された位置から始まる領域の探索を行います。
この関数は、深さ優先探索（DFS）を使用して、連結した '#' の領域を探索し、見つけた領域内の '#' を '.' に変更します。
これにより、同じ領域が二度数えられることを防ぎます。

領域の外側を#が見つからなくなるまで、果てしなく探索するので、while+popを使うと都合がよい。

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

[stpete WA ans3]

h,w=map(int,input().split())

S=[]
for i in range(h):
  s=list(input())
  S+=[s]

t=0
for i in range(h):
  for j in range(w):
    if S[i][j]=='#':
      t+=1
      L=[]
      for p in range(-2,3):
        for q in range(-2,3):
          L+=[(i+p,j+q)]
      for li in L:
        x,y=li[0],li[1]
        if 0<=x<h and 0<=y<w:
          S[x][y]='.'
 
print(t)

連結した領域を探索するための範囲を広げることで、より広範囲を探索することができるようになりました。
しかし、それでもまだ十分ではありません。なぜならば、連結した領域がそれ以上の距離にある場合には、探索ができないからです。
また、同じ問題が残っています。つまり、連結した領域の探索を行っていない点です。

単に '#' を見つけてそれをカウントするだけで、実際には連結した領域を特定する作業が行われていません。
この修正では、探索範囲が広げられましたが、まだ連結した領域の探索を行っていないため、正しい結果を得ることはできません。
連結した領域を特定するためには、適切な探索アルゴリズム（例えば、深さ優先探索や幅優先探索）を使用する必要があります。

###############################################

[stpete WA ans2]

h,w=map(int,input().split())

S=[]
for i in range(h):
  s=list(input())
  S+=[s]

t=0
for i in range(h):
  for j in range(w):
    if S[i][j]=='#':
      t+=1
      L=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
      for li in L:
        x,y=li[0],li[1]
        if 0<=x<h and 0<=y<w:
          S[x][y]='.'
 
print(t)

このコードは、与えられたグリッド内の連結した領域の数を正しく数えることはできません。
なぜならば、コードが単純に '#' を見つけるたびに連結した領域として数えているだけで、
実際には連結した領域の探索を行っていないからです。

'#' のマスを見つけると、ただそれをカウントするだけで、そのマスを始点として連結した領域の探索を行っていません。
また、連結した領域を探索するための深さ優先探索（DFS）や幅優先探索（BFS）のような手法も使用されていません。

グリッド上の特定のマスの周囲をチェックするためにリスト L を使用していますが、この方法では正確な連結領域の探索ができません。
なぜならば、連結した領域が他の '#' の領域と繋がっている場合、その連結が見落とされるからです。

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
