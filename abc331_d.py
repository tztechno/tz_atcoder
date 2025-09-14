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
###############################################
###############################################
[tetsu]
n, q = map(int, input().split())
p = [list(map(str, input())) for _ in range(n)]

accum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        s = 1 if p[i-1][j-1] == 'B' else 0
        accum[i][j] = accum[i-1][j] + accum[i][j-1] - accum[i-1][j-1] + s


def f(r, c):
    top_left = (r//n) * (c//n) * accum[n][n]
    top_right = (r//n) * accum[n][c%n]
    bottom_left = (c//n) * accum[r%n][n]
    bottom_right = accum[r%n][c%n]
    return top_left + top_right + bottom_left + bottom_right


for _ in range(q):
    query = list(map(int, input().split()))
    a, b, c, d = query
    print(f(c+1, d+1) - f(c+1, b) - f(a, d+1) + f(a, b))

###############################################
[tip]
n,q=map(int,input().split())
s=[list(input()) for _ in range(n)]
accum=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        accum[i+1][j+1]=accum[i][j+1]+accum[i+1][j]-accum[i][j]
        if s[i][j]=='B':
            accum[i+1][j+1]+=1
            
def f(x,y):
    ret=0
    ret+=accum[n][n]*(x//n)*(y//n)
    ret+=accum[x%n][n]*(y//n)
    ret+=accum[n][y%n]*(x//n)
    ret+=accum[x%n][y%n]
    return ret

for _ in range(q):
    a,b,c,d=map(int,input().split())
    print(f(c+1,d+1)-f(a,d+1)-f(c+1,b)+f(a,b))
    
###############################################
[zero]
def calc(r, c):
  qi, mi = divmod(r, N)
  qj, mj = divmod(c, N)
  
  ret = acc[N][N] * (qi * qj)
  ret += acc[mi][N] * qj
  ret += acc[N][mj] * qi
  ret += acc[mi][mj]
  
  return ret

N, Q = map(int, input().split())
P = [input() for _ in range(N)]

acc = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
  for j in range(N):
    if P[i][j] == "B":
      acc[i + 1][j + 1] = 1

for i in range(1, N + 1):
  for j in range(1, N + 1):
    acc[i][j] += acc[i][j - 1]

for j in range(1, N + 1):
  for i in range(1, N + 1):
    acc[i][j] += acc[i - 1][j]

for _ in range(Q):
  A, B, C, D = map(int, input().split())
  C += 1; D += 1
  print(calc(C, D) - calc(C, B) - calc(A, D) + calc(A, B))
###############################################
[titia]
import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

MAP=[input().strip() for i in range(N)]

S=[[0]*(2*N+1) for i in range(2*N+1)]

for i in range(2*N):
    for j in range(2*N):
        if MAP[i%N][j%N]=="B":
            S[i+1][j+1]+=1

for i in range(2*N+1):
    for j in range(2*N+1):
        if i-1>=0:
            S[i][j]+=S[i-1][j]

for i in range(2*N+1):
    for j in range(2*N+1):
        if j-1>=0:
            S[i][j]+=S[i][j-1]

def calc(a,b,c,d):
    return S[c][d]-S[a][d]-S[c][b]+S[a][b]

for tests in range(Q):
    a,b,c,d=map(int,input().split())
    c+=1
    d+=1

    r=a//N
    a-=r*N
    c-=r*N

    r=b//N
    b-=r*N
    d-=r*N

    #print(a,b,c,d)

    x=(c-a)//N
    y=(d-b)//N

    c-=x*N
    d-=y*N


    ANS=calc(0,0,N,N)*x*y+y*calc(a,0,c,N)+x*calc(0,b,N,d)+calc(a,b,c,d)

    #print(x,y,a,b,c,d,calc(0,0,N,N),calc(a,0,c,N),calc(0,b,N,d),calc(a,b,c,d))

    print(ANS)

    
    

###############################################
