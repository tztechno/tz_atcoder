abc355_c.py
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
[shaka]
N,T=map(int,input().split())
A=[int(i)-1 for i in input().split()]
X=[N for i in range(N)]
Y=[N for i in range(N)]
Z=[N,N]
for i in range(T):
    b=A[i]//N
    c=A[i]%N
    X[b]-=1
    Y[c]-=1
    if X[b]==0 or Y[c]==0:
        print(i+1)
        exit()
    if b==c:
        Z[0]-=1
        if Z[0]==0:
            print(i+1)
            exit()
    if b+c==N-1:
        Z[1]-=1
        if Z[1]==0:
            print(i+1)
            exit()
print(-1)
#############################################
[titia]
import sys
input = sys.stdin.readline

N,T=map(int,input().split())
A=list(map(int,input().split()))

T=[0]*(N+1)
Y=[0]*(N+1)
N1=0
N2=0

for i in range(len(A)):
    a=A[i]-1
    x=a%N
    y=a//N

    T[x]+=1
    if T[x]==N:
        print(i+1)
        exit()

    Y[y]+=1
    if Y[y]==N:
        print(i+1)
        exit()

    if x==y:
        N1+=1
        if N1==N:
            print(i+1)
            exit()

    if x==N-1-y:
        N2+=1
        if N2==N:
            print(i+1)
            exit()

    #print(N1,N2)

print(-1)
#############################################
#############################################
[my TLE]
N,T=map(int,input().split())
A=list(map(int,input().split()))
S=list(range(1,N*N+1))
BINGO=[]
for i in range(N):
    BINGO+=[S[N*i:N*i+N]]#横
    bingo=[]
    for j in range(N):
        bingo+=[S[i+N*j]]#縦
    BINGO+=[bingo]
bingo2=[]
bingo3=[]    
for j in range(N):    
    bingo2+=[S[j+N*j]]
    bingo3+=[S[(N-1-j)+N*j]]    
BINGO+=[bingo2]
BINGO+=[bingo3]
#print(BINGO)
ANS=-1
for i in range(1,T+1):
  for b in BINGO:
    if set(b)-set(A[0:i])==set():
      ANS=i
      print(ANS)
      exit()
else:
  print(ANS)
#############################################
