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
[cgpt]
import sys
input = sys.stdin.readline

INF = 1 << 60

N, M = map(int, input().split())
D = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    D[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c *= 2
    D[a][b] = D[b][a] = min(D[a][b], c)

K, T = map(int, input().split())
Air = list(map(lambda x: int(x) - 1, input().split()))

for a in Air:
    D[a][N] = D[N][a] = T

# ワーシャル・フロイド
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

# 距離合計（i<jのみ）
ANS = sum(D[i][j] for i in range(N) for j in range(i + 1, N) if D[i][j] < INF)

def update_dist(x, y, new_dist):
    global ANS
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            d1 = D[i][x] + new_dist + D[y][j]
            d2 = D[i][y] + new_dist + D[x][j]
            d = min(d1, d2)
            if d < D[i][j]:
                if i < N and j < N:
                    if D[i][j] >= INF:
                        ANS += d
                    else:
                        ANS -= D[i][j] - d
                D[i][j] = D[j][i] = d

Q = int(input())
LANS = []

for _ in range(Q):
    L = list(map(int, input().split()))
    t = L[0]
    if t == 3:
        LANS.append(ANS)
    elif t == 2:
        x = L[1] - 1
        D[x][N] = D[N][x] = T
        update_dist(x, N, T)
    elif t == 1:
        x, y, z = L[1] - 1, L[2] - 1, L[3] * 2
        if D[x][y] > z:
            update_dist(x, y, z)

# 出力（合計距離は内部で1回のみ数えたので /2 不要）
print(*LANS)

##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

D=[[1<<60]*(N+1) for i in range(N+1)]

for i in range(N+1):
    D[i][i]=0

for i in range(M):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    c*=2
    D[a][b]=min(D[a][b],c)
    D[b][a]=min(D[b][a],c)

K,T=map(int,input().split())
Air=list(map(int,input().split()))

for air in Air:
    D[air-1][N]=T
    D[N][air-1]=T

for k in range(N+1): # k個までの町を使ってのDisが知れているときに
    for i in range(N+1): # 町iと
        for j in range(N+1): # 町jとの最短距離は、
            length=D[i][k]+D[j][k]
            if D[i][j]>length:
                D[i][j]=D[j][i]=length

ANS=0
for i in range(N):
    for j in range(N):
        if D[i][j]<(1<<60):
            ANS+=D[i][j]

Q=int(input())
LANS=[]

for tests in range(Q):
    L=list(map(int,input().split()))
    #print(L,D)

    if L[0]==3:
        LANS.append(ANS//2)
    elif L[0]==2:
        x=L[1]-1
        D[x][N]=T
        D[N][x]=T

        for i in range(N+1):
            for j in range(i+1,N+1):
                length=min(D[i][x]+T+D[j][N],D[i][N]+T+D[j][x])

                if length<D[i][j]:
                    if i<N and j<N:
                        if D[i][j]>=(1<<60):
                            ANS+=length*2
                        else:
                            ANS-=(D[i][j]-length)*2
                    D[i][j]=length
                    D[j][i]=length
    elif L[0]==1:
        #print("!!",ANS)
        x,y,z=L[1],L[2],L[3]
        x-=1
        y-=1
        z*=2

        if D[x][y]>z:
            for i in range(N+1):
                for j in range(i+1,N+1):
                    length=min(D[i][x]+z+D[j][y],D[i][y]+z+D[j][x])

                    if length<D[i][j]:
                    
                        if i<N and j<N:
                            if D[i][j]>=(1<<60):
                                ANS+=length*2
                            else:
                                ANS-=(D[i][j]-length)*2

                        #print(D[i][j],length,ANS)
                        D[i][j]=length
                        D[j][i]=length

print(*LANS)

##################################################################
