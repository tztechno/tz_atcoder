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
[ngid]
T = int(input())
cases = []
for i in range(T):
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A = sorted(A, reverse=True)
    B = sorted(B)
    n = len(A)
    pairs = 0
    i = 0
    j = 0
    for i in range(n):
        while j < n and A[i] + B[j] < M:
            j += 1
        if j >= n:
            break
        pairs += 1
        j += 1
    
    res = sum(A) + sum(B) - pairs * M
    print(res)

##################################################################
[hey]
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))
    c, idx = 0, 0
    for v in a:
        while idx < n and b[idx] + v < m:
            idx += 1
        if idx >= n:
            break
        c += 1
        idx += 1
    print(sum(a) + sum(b) - m * c)

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
[my TLE]
import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        N, M = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        B = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        A.sort()
        B.sort()
        
        min_sum = float('inf')
        
        for i in range(N):
            current_sum = 0
            for j in range(N):
                current_sum += (A[j] + B[(j + i) % N]) % M
            min_sum = min(min_sum, current_sum)
            
            if i == 0:
                B.reverse()
                current_sum = 0
                for j in range(N):
                    current_sum += (A[j] + B[j]) % M
                min_sum = min(min_sum, current_sum)
        
        print(min_sum)

solve()
##################################################################
[my TLE]
import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        N, M = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        B = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        A.sort()
        B.sort()
        
        min_sum = float('inf')
        
        for shift in range(N):
            current_sum = 0
            for i in range(N):
                current_sum += (A[i] + B[(i + shift) % N]) % M
            min_sum = min(min_sum, current_sum)
        
        B.sort(reverse=True)
        
        for shift in range(N):
            current_sum = 0
            for i in range(N):
                current_sum += (A[i] + B[(i + shift) % N]) % M
            min_sum = min(min_sum, current_sum)
        
        print(min_sum)

solve()
##################################################################
