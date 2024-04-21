####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
N,M=map(int,input().split())
A=[0 for i in range(M)]
B=[0 for i in range(M)]
points=set()
X=set()
Y=set()
for i in range(M):
    A[i],B[i]=map(int,input().split())
    A[i]-=1
    B[i]-=1
    points.add((A[i],B[i]))
    X.add((A[i]-B[i])%N)
j=0
while(j<N and len(X)<M):
    X.add(j)
    j+=1

ans=[]
ALL=M
for x in X:
    for i in range(N):
        a,b=((x+i)%N),i
        ans.append((a,b))

print(len(ans))
for i,j in ans:
    print(i+1,j+1)
exit()
P=[0 for i in range(N)]
Q=[0 for i in range(N)]
board=[[0 for j in range(N)]for i in range(N)]

for a,b in points:
    P[a]+=1
    Q[b]+=1
    board[a][b]+=1
for i,j in ans:
    P[i]+=1
    Q[j]+=1
    board[i][j]+=1
print(P,Q,M)
print(*board,sep="\n")

####################################################################
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

A=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append((b-a)%N)

A=set(A)

now=1
while len(A)<M:
    A.add(now)
    now+=1

ANS=[]
for a in A:
    for i in range(1,N+1):
        j=(i+a)%N
        if j==0:
            j=N
        ANS.append((i,j))

print(len(ANS))
for a,b in ANS:
    print(a,b)


####################################################################
[my ans with RE]

from itertools import permutations


def generate_matrix(n, M):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(M):
            matrix[i][(i+j) % n] = 1
    return matrix


def modify_matrix(matrix, coordinates):
    modified_matrix = [list(row) for row in matrix]
    for coord in coordinates:
        x, y = coord
        modified_matrix[x][y] = 1
    return modified_matrix


def find_ones_coordinates(matrix):
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                coordinates.append((i, j))
    return coordinates


def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def find_solution(matrix, coordinates):
    for perm in permutations(range(len(matrix))):
        perm_matrix = [matrix[i] for i in perm]
        modified_matrix = modify_matrix(perm_matrix, coordinates)
        ones_coordinates = find_ones_coordinates(modified_matrix)
        if set(ones_coordinates) == set(coordinates):
            return perm_matrix, ones_coordinates
    return None, None


def find_ones_coordinates(matrix):
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                coordinates.append((i + 1, j + 1))
    return coordinates
    
    
n, M = map(int, input().split())
print(n*M)

coordinates = []
for i in range(M):
    a, b = map(int, input().split())
    coordinates.append((a - 1, b - 1))

result = generate_matrix(n, M)

ones_coordinates = find_ones_coordinates(result)
for coord in ones_coordinates:
    print(*coord)    
####################################################################
