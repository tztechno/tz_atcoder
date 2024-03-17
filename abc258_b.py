dif 511
#########################################
#########################################
n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]

dxdy = []
for dx in -1, 0, 1:
    for dy in -1, 0, 1:
        if dx == dy == 0:
            continue
        dxdy.append((dx, dy))

ans = 0
for x in range(n):
    for y in range(n):
        for dx, dy in dxdy:
            s = str(a[x][y])
            for _ in range(n-1):
                x += dx
                x %= n
                y += dy
                y %= n
                s = str(a[x][y]) + s
            ans = max(ans, int(s))

print(ans)
#########################################
import sys
input = sys.stdin.readline

N=int(input())

A=[input().strip() for i in range(N)]

MAX=-1

for i in range(N):
    for j in range(N):
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:
                    continue

                score=[]

                nx=i
                ny=j

                for p in range(N):
                    score.append(A[nx][ny])
                    nx+=x
                    ny+=y
                    nx%=N
                    ny%=N

                MAX=max(MAX,int("".join(map(str,score))))

print(MAX)
                    

#########################################
dx=[0,0,-1,-1,-1,1,1,1]
dy=[1,-1,1,0,-1,1,0,-1]
n=int(input())
ans=0
mp=[input()for i in range(n)]
for i in range(n):
  for j in range(n):
    for f in range(8):
      x=i;y=j
      res=0
      for k in range(n):
        res=res*10+int(mp[x][y])
        x=(x+dx[f])%n;y=(y+dy[f])%n
      ans=max(ans,res)
print(ans)
#########################################
n = int(input())
a = [input() for _ in range(n)]
dir8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
ans = 0
for si in range(n):
    for sj in range(n):
        for d in dir8:
            i, j = si, sj
            x = 0
            for k in range(n):
                x = x * 10 + int(a[i][j])
                i += d[0]
                j += d[1]
                i = (i + n) % n
                j = (j + n) % n
            ans = max(ans, x)
print(ans)
#########################################
n = int(input())
grid = []
max_ = '1'
for i in range(n):
  s = input()
  for j in range(n):
    max_ = max(max_,s[j])
  grid.append(s)
def move(x,y):
  ans = '1'
  for x0,y0 in [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]:
    tmp = ''
    x1,y1 = x,y
    for i in range(n):
      tmp += grid[x1][y1]
      x1 = (x1+x0)%n
      y1 = (y1+y0)%n
    ans = max(ans,tmp)
  return ans
res = '1'
for i in range(n):
  for j in range(n):
    if grid[i][j] == max_:
      res = max(res,move(i,j))
print(res)
#########################################
