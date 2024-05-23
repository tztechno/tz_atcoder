abc319_c.py
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
[wase]
from itertools import permutations as p
t = [list(map(int, input().split())) for _ in range(3)]
f = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
n = 0
for l in p(range(9)):
  g = [[] for _ in range(8)]
  for p in l:
    for q in range(8):
      if p in f[q]:
        g[q].append(t[p // 3][p % 3])
  n += any([a == b and b != c for a, b, c in g])
print(1 - n / 362880)
#############################################
#############################################
[shaka,BEST]
import itertools
C=[int(i) for i in input().split()]+[int(i) for i in input().split()]+[int(i) for i in input().split()]
ALL=0
cnt=0
COMBO=[(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
board=[set() for i in range(9)]
for i,st in enumerate(COMBO):
    for x in st:
        board[x].add(i)
for seq in itertools.permutations(range(9),9):
    ALL+=1
    abc=[[] for i in range(8)]
    flag=False
    for x in seq:
        for i in board[x]:
            abc[i].append(C[x])
            if len(abc[i])==2 and abc[i][0]==abc[i][1]:
                flag=True
                break
        if flag:
            break
    if flag:
        cnt+=1
print(1-cnt/ALL)
#############################################
#############################################
[titia]
import sys
input = sys.stdin.readline

MAP=[]
for i in range(3):
    X=list(map(int,input().split()))
    MAP+=X

ALL=362880

from itertools import permutations

ANS=0
L=list(permutations(range(9)))
for x in L:
    LIST=list(x)

    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    H=[]

    for k in range(9):
        i=LIST[k]
    
        if i%3==0:
            A.append(MAP[i])
        elif i%3==1:
            B.append(MAP[i])
        elif i%3==2:
            C.append(MAP[i])

        if i//3==0:
            D.append(MAP[i])
        elif i//3==1:
            E.append(MAP[i])
        elif i//3==2:
            F.append(MAP[i])

        if i in [0,4,8]:
            G.append(MAP[i])

        if i in [2,4,6]:
            H.append(MAP[i])

    flag=1

    if A[0]==A[1] and A[1]!=A[2]:
        flag=0
    if B[0]==B[1] and B[1]!=B[2]:
        flag=0
    if C[0]==C[1] and C[1]!=C[2]:
        flag=0
    if D[0]==D[1] and D[1]!=D[2]:
        flag=0
    if E[0]==E[1] and E[1]!=E[2]:
        flag=0
    if F[0]==F[1] and F[1]!=F[2]:
        flag=0
    if G[0]==G[1] and G[1]!=G[2]:
        flag=0
    if H[0]==H[1] and H[1]!=H[2]:
        flag=0

    ANS+=flag

print(ANS/ALL)

#############################################
[my WA]
A=[]
t=0
for i in range(3):
    a=list(map(int,input().split()))
    A+=a
    if len(set(a))==2:
        t+=1
B=[[A[0],A[3],A[6]],[A[1],A[4],A[7]],[A[2],A[5],A[8]],[A[0],A[4],A[8]],[A[2],A[4],A[6]]]
for b in B:
    if len(set(b))==2:
        t+=1
print((2/3)**t)
#############################################
