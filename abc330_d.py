###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[deepseek 理解]
def main():
    import sys
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    grid = []
    for i in range(1, N+1):
        grid.append(data[i].strip())
    rows = [[] for _ in range(N)]
    cols = [[] for _ in range(N)]
    print(grid)

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                rows[i].append(j)#########
                cols[j].append(i)#########
    print(rows)
    print(cols)
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                row_count = len(rows[i]) - 1
                col_count = len(cols[j]) - 1
                ans += row_count * col_count
    print(ans)

if __name__ == "__main__":
    main()
###############################################
[deepseek]
各点をL字型の角（曲がり角）と仮定します。
その点と同じ行にある他の点の数と、同じ列にある他の点の数を掛け合わせると、その点を角とするL字型の数が得られます。
def main():
    import sys
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    grid = []
    for i in range(1, N+1):
        grid.append(data[i].strip())
    
    # 各行と各列に含まれる'o'の位置を記録
    rows = [[] for _ in range(N)]
    cols = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                rows[i].append(j)
                cols[j].append(i)
    
    ans = 0
    # 各点を中心点（L字の角）と仮定して計算
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                # 同じ行にある点の数（中心点除く）
                row_count = len(rows[i]) - 1
                # 同じ列にある点の数（中心点除く）
                col_count = len(cols[j]) - 1
                # これらの組み合わせでL字が作れる
                ans += row_count * col_count
                
    print(ans)

if __name__ == "__main__":
    main()
###############################################
[parra]
n=int(input())

rw,cl = [0] * n, [0] * n
g = []
for i in range(n):
  s_i = input()
  g.append(s_i)
  for j in range(n):
    if s_i[j] == 'o':
      rw[i] += 1
      cl[j] += 1

ans = 0
for i in range(n):
  for j in range(n):
    if g[i][j] == 'o':
      ans += (rw[i] -1)*(cl[j]-1)

print(ans)
###############################################
[sado]
N=int(input())
A=[input() for _ in range(N)]
B=list(zip(*A[::-1]))
W=[]
L=[]
ans=0
for i in range(N):
  W.append(A[i].count("o"))
  L.append(B[i].count("o"))
for i in range(N):
  for j in range(N):
    if A[i][j]=="o":
      ans+=(W[i]-1)*(L[j]-1)
print(ans)
###############################################
[nada]
from collections import deque
N=int(input())
grid = [input() for _ in range(N)]
xlist=[0]*N
ylist=[0]*N
for i in range(N):
    for j in range(N):
       if grid[i][j]=="o":
           xlist[j]+=1
           ylist[i]+=1
sum=0
for i in range(N):
    for j in range(N):
        if grid[i][j]=="o" and xlist[j]>= 2 and ylist[i]>= 2:
            sum+=(xlist[j]-1)*(ylist[i]-1)
print(sum)
###############################################
[titia]
import sys
input = sys.stdin.readline

N=int(input())
MAP=[input().strip() for i in range(N)]

H=[0]*N
W=[0]*N

for i in range(N):
    for j in range(N):
        if MAP[i][j]=="o":
            H[i]+=1
            W[j]+=1

ANS=0
for i in range(N):
    for j in range(N):
        if MAP[i][j]=="o":
            ANS+=(H[i]-1)*(W[j]-1)

print(ANS)
###############################################
[my TLE]
N=int(input())
S=[]
for i in range(N):
  s=list(input())
  for j,si in enumerate(s):
    if si=='o':
      S+=[(i,j)]
M=list(range(len(S)))
from itertools import product,permutations,combinations,accumulate
C=list(combinations(M,3))
t=0
for ci in C:
  c0=S[ci[0]]
  c1=S[ci[1]]
  c2=S[ci[2]]
  if len({c0[0], c1[0], c2[0]}) == 2 and len({c0[1], c1[1], c2[1]}) == 2:
    t+=1
print(t)
###############################################
