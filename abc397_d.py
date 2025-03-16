###################################################
###################################################
###################################################
###################################################
[my TLE] y:forloop,w:binary tree

def f(a, b):
    return a*a*a-b*b*b
N=int(input())
for y in range(1,10000000):
    ok=1
    ng=int(1e7)
    while (ng-ok)>1:
        m=(ok+ng)//2
        if(f(y+m,y)<=N): 
          ok=m
        else: 
          ng=m
    if(f(y+ok,y)==N):
        print(y+ok,y)
        exit()
print(-1)
###################################################
[ard]

n = int(input())

for i in range(1, 1_000_000 + 5):
    if n % i != 0:
        continue
    target = n // i

    ok = 1
    ng = 1_000_000_000 + 20

    while ng-ok>1:
        mid = (ok+ng)>>1
        val = 3*mid*mid + 3*i*mid + i*i
  
        if val <= target:
            ok = mid
        else:
            ng = mid

    val = 3*ok*ok + 3*i*ok + i*i
    if val == target:
        x = i + ok
        print(x, ok)
        exit(0)  
print(-1)


###################################################
[tetsu] w:forloop,y:binary tree

def f(a, b):
    return a*a*a-b*b*b

N=int(input())

for w in range(1,1000000):
    ok=1
    ng=int(1e9)
    while (ng-ok)>1:
        m=(ok+ng)//2
        if(f(w+m,m)<=N): ok=m
        else: ng=m

    if(f(ok+w,ok)==N):
        print(ok+w,ok)
        exit()
print(-1)

###################################################
[titia]

import sys
input = sys.stdin.readline
from math import sqrt

N=int(input())

for k in range(1,10**6+10):
    a=3*k
    b=3*k*k
    c=k*k*k-N
    if b*b-4*a*c>=0:
        y=(-b+sqrt(b*b-4*a*c))/(2*a)
        y=round(y)
        x=y+k
        if x>0 and y>0 and x*x*x-y*y*y==N:
            print(x,y)
            exit()
print(-1)

###################################################
[my TLE,RE31]
N=int(input())
D=[]
for i in range(1,N):
  D+=[(i**3,i)]
for x in range(N):
  for y in range(x):
    if D[x][0]-D[y][0]==N:
      print(D[x][1],D[y][1])
      exit()
else:
  print(-1)
###################################################
[my TLE26]
N=int(input())
for x in range(1,N):
  for y in range(1,x):
    if x**3-y**3==N:
      print(x,y)
      exit()
else:
  print(-1)
###################################################
