
##################################################################
整数列 A=(A1,…,AN), B=(B1,…,BN) がある。
Q 個のクエリが与えられ、各クエリは文字 ci と整数 Xi, Vi で構成される。
もし ci=A なら A[Xi]=Vi、もし ci=B なら B[Xi]=Vi。
その後、sum_{k=1}^N min(Ak,Bk) を出力せよ。
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[mybrain AC]
import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
t=0
for a,b in zip(A,B):
  t+=min(a,b)
for _ in range(Q):
  c,x,v=map(str,input().split())
  y=int(x)-1
  if c=='A':
    t=t-min(A[y],B[y])+min(int(v),B[y])
    print(t)
    A[y]=int(v)
  else:
    t=t-min(A[y],B[y])+min(int(v),A[y])
    print(t)    
    B[y]=int(v)

##################################################################
[mybrain AC]
import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
t=0
for a,b in zip(A,B):
  t+=min(a,b)
for _ in range(Q):
  c,x,v=map(str,input().split())
  if c=='A':
    t=t-min(A[int(x)-1],B[int(x)-1])+min(int(v),B[int(x)-1])
    print(t)
    A[int(x)-1]=int(v)
  else:
    t=t-min(A[int(x)-1],B[int(x)-1])+min(int(v),A[int(x)-1])
    print(t)    
    B[int(x)-1]=int(v)
##################################################################
[mybrain TLE]
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
T=[]
for a,b in zip(A,B):
  T+=[min(a,b)]
for _ in range(Q):
  c,x,v=map(str,input().split())
  if c=='A':
    A[int(x)-1]=int(v)
    T[int(x)-1]=min(int(v),B[int(x)-1])    
  else:
    B[int(x)-1]=int(v)
    T[int(x)-1]=min(int(v),A[int(x)-1])
  print(sum(T))  

##################################################################
[mybrain TLE]
import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for _ in range(Q):
  c,x,v=map(str,input().split())
  if c=='A':
    A[int(x)-1]=int(v)
  else:
    B[int(x)-1]=int(v)
  t=0
  for a,b in zip(A,B):
    t+=min(a,b)
  print(t)
    
##################################################################
[obt]
import sys

it = iter(sys.stdin.buffer.read().split())
N = int(next(it))
Q = int(next(it))

A = [int(next(it)) for _ in range(N)]
B = [int(next(it)) for _ in range(N)]

# 現在の合計 sum(min(Ak, Bk))
S = sum(min(a, b) for a, b in zip(A, B))

out_lines = []
for _ in range(Q):
    c = next(it).decode()
    x = int(next(it)) - 1  # 0-index
    v = int(next(it))

    if c == 'A':
        # 変更前の寄与を引き、変更後の寄与を足す
        S += min(v, B[x]) - min(A[x], B[x])
        A[x] = v
    else:  # c == 'B'
        S += min(A[x], v) - min(A[x], B[x])
        B[x] = v

    out_lines.append(str(S))

print("\n".join(out_lines))

##################################################################
[lazy]
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]

base = sum(min(a, b) for a, b in zip(A[0], A[1]))

for _ in range(Q):
  c, x, v = input().split()
  x = int(x) - 1
  v = int(v)
  
  a = ord(c) - 65
  base -= min(A[0][x], A[1][x])
  A[a][x] = v
  base += min(A[0][x], A[1][x])
  print(base)

##################################################################
[titia]
import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

MIN=[]
for i in range(N):
    MIN.append(min(A[i],B[i]))
SUM=sum(MIN)
for i in range(Q):
    x,y,z=input().split()
    y=int(y)-1
    z=int(z)
    if x=="A":
        now=MIN[y]
        SUM-=now
        A[y]=z
        to=min(A[y],B[y])
        MIN[y]=to
        SUM+=to
        print(SUM)
    else:
        now=MIN[y]
        SUM-=now
        B[y]=z
        to=min(A[y],B[y])
        MIN[y]=to
        SUM+=to
        print(SUM)
##################################################################
[myai AC]
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = sum(min(A[i], B[i]) for i in range(N))

for _ in range(Q):
    c, X, V = input().split()
    X = int(X) - 1
    V = int(V)
    
    S -= min(A[X], B[X])
    if c == 'A':
        A[X] = V
    else:
        B[X] = V
    S += min(A[X], B[X])
    
    print(S)
##################################################################
