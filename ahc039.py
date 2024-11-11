###########################################################

###########################################################

###########################################################

###########################################################

###########################################################

###########################################################

###########################################################

###########################################################
[pts 200000][my ans]

N=int(input())
X=[]
Y=[]
SABA=[]
IWASHI=[]
for i in range(N*2):
  x,y=map(int,input().split())
  if i<N:
    X+=[x]
    Y+=[y]
    SABA+=[(x,y)]
  else:
    IWASHI+=[(x,y)]

x0,x2=min(X),max(X)
y0,y2=min(Y),max(Y)

def count_diff(X0,Y0,X2,Y2):
  ct= 0
  for x, y in SABA:
    if X0 <= x <= X2 and Y0 <= y <= Y2:
      ct += 1
  mct = 0
  for x, y in IWASHI:
    if X0 <= x <= X2 and Y0 <= y <= Y2:
      mct += 1
  return ct-mct

diff=10**9
P=[]
for x1 in range(x0+1,x2,500):
  for y1 in range(y0+1,y2,500):
    diffi=count_diff(x0,y1,x1,y2)
    if diffi<diff:
      P=[x1,y1]
      diff=min(diff,diffi)
        
x1,y1=P[0],P[1]        

print(6)
print(x0,y1)
print(x0,y0)
print(x2,y0)
print(x2,y2)
print(x1,y2)
print(x1,y1)  

###########################################################
[pts 280000]

import sys
input = sys.stdin.readline

from time import time
from random import randint,choice

time0=time()

N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
B=[list(map(int,input().split())) for i in range(N)]

mapsize=100
comp=100000//mapsize

P=[[0]*mapsize for i in range(mapsize)]
Q=[[0]*mapsize for i in range(mapsize)]

for x,y in A:
    P[x//comp][y//comp]+=1
for x,y in B:
    Q[x//comp][y//comp]+=1

NOW=[[0]*(mapsize+5) for i in range(mapsize+5)]

for i in range(mapsize):
    for j in range(mapsize):
        NOW[i][j]=P[i][j]-Q[i][j]

for i in range(1,mapsize):
    for j in range(mapsize):
        NOW[i][j]+=NOW[i-1][j]

for i in range(mapsize):
    for j in range(1,mapsize):
        NOW[i][j]+=NOW[i][j-1]


MAX=0

MAX=0
ind=[-1,-1,-1,-1]

while time()-time0<1.8:
    x0=randint(0,mapsize-1)
    x1=randint(0,mapsize-1)

    if x0>x1:
        x0,x1=x1,x0
        
    y0=randint(0,mapsize-1)
    y1=randint(0,mapsize-1)

    if y0>y1:
        y0,y1=y1,y0

    score=NOW[x1][y1]-NOW[x1][y0-1]-NOW[x0-1][y1]+NOW[x0-1][y0-1]

    if score>MAX:
        MAX=score
        ind=[x0,x1,y0,y1]

print(4)
x0,x1,y0,y1=ind

print(x0*comp,y0*comp)
print(x0*comp,y1*comp)
print(x1*comp,y1*comp)
print(x1*comp,y0*comp)

###########################################################
[pts 380000]

import sys
input = sys.stdin.readline

from time import time
from random import randint,choice

time0=time()

N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
B=[list(map(int,input().split())) for i in range(N)]

mapsize=25
comp=100000//mapsize

P=[[0]*mapsize for i in range(mapsize)]
Q=[[0]*mapsize for i in range(mapsize)]

for x,y in A:
    P[x//comp][y//comp]+=1
for x,y in B:
    Q[x//comp][y//comp]-=1

NOW=[[0]*(mapsize+5) for i in range(mapsize+5)]

for i in range(mapsize):
    for j in range(mapsize):
        NOW[i][j]=P[i][j]+Q[i][j]*10

for i in range(1,mapsize):
    for j in range(mapsize):
        NOW[i][j]+=NOW[i-1][j]

for i in range(mapsize):
    for j in range(1,mapsize):
        NOW[i][j]+=NOW[i][j-1]

MAX=-1000
ind=[-1,-1,-1,-1]

while time()-time0<0.6:
    x0=randint(0,mapsize-2)
    x1=randint(0,mapsize-2)

    if x0>x1:
        x0,x1=x1,x0
        
    y0=randint(0,mapsize-2)
    y1=randint(0,mapsize-2)

    if y0>y1:
        y0,y1=y1,y0

    score=NOW[x1][y1]-NOW[x1][y0-1]-NOW[x0-1][y1]+NOW[x0-1][y0-1]

    if score>MAX:
        MAX=score
        ind=[x0,x1,y0,y1]

x0,x1,y0,y1=ind

Length=comp*((x1-x0+1)*2+(y1-y0+1)*2)

T=[[0]*(mapsize+1) for i in range(mapsize)]
Y=[[0]*mapsize for i in range(mapsize+1)]
USE=[[0]*mapsize for i in range(mapsize)]

for i in range(x0,x1+1):
    for j in range(y0,y1+1):
        USE[i][j]=1

for i in range(x0,x1+1):
    T[i][y0]=1
    T[i][y1+1]=1

for j in range(y0,y1+1):
    Y[x0][j]=1
    Y[x1+1][j]=1

def four_direction(x, y):
    RET = [T[x][y], Y[x][y]]

    if (x - 1 >= 0):
        RET.append(T[x-1][y])

    if (y - 1 >= 0):
        RET.append(Y[x][y-1])

    return sum(RET)

while time()-time0<1.8:
    x=randint(0,mapsize-2)
    y=randint(0,mapsize-2)

    if USE[x][y]==0:
        if P[x][y]+Q[x][y]<0:
            continue

        A = [T[x][y], Y[x][y], T[x][y + 1], Y[x + 1][y]]
        SUM=sum(A)

        if SUM==1:
            if Length+comp*2>400000:
                continue

        if (SUM == 1):
            if P[x][y]+Q[x][y]<0:
                continue

            if (T[x][y] == 1):
                if (four_direction(x, y + 1) == 0 and four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (Y[x][y] == 1) :
                if (four_direction(x + 1, y) == 0 and four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (T[x][y + 1] == 1):
                if (four_direction(x, y) == 0 and four_direction(x + 1, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (Y[x + 1][y] == 1):
                if (four_direction(x, y) == 0 and four_direction(x, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

        elif SUM==2:
            if P[x][y]+Q[x][y]<0:
                continue
            if (T[x][y] == 1 and Y[x][y] == 1):
                if (four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (Y[x][y] == 1 and T[x][y + 1] == 1):
                if (four_direction(x + 1, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (T[x][y + 1] == 1 and Y[x + 1][y] == 1):
                if (four_direction(x, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (Y[x + 1][y] == 1 and T[x][y] == 1):
                if (four_direction(x, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
        elif (SUM == 3):
            T[x][y] ^= 1;
            Y[x][y] ^= 1;
            T[x][y + 1] ^= 1;
            Y[x + 1][y] ^= 1;
            USE[x][y]^=1
            Length-=comp*2

    else:
        if P[x][y]+Q[x][y]>0:
            continue

        A = [T[x][y], Y[x][y], T[x][y + 1], Y[x + 1][y]]
        SUM=sum(A)

        if SUM==1:
            if Length+comp*2>400000:
                continue

        if (SUM == 1):
            if (T[x][y] == 1):
                if (four_direction(x, y + 1) == 0 and four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (Y[x][y] == 1) :
                if (four_direction(x + 1, y) == 0 and four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (T[x][y + 1] == 1):
                if (four_direction(x, y) == 0 and four_direction(x + 1, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

            if (Y[x + 1][y] == 1):
                if (four_direction(x, y) == 0 and four_direction(x, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
                    Length+=comp*2

        elif SUM==2:
            if (T[x][y] == 1 and Y[x][y] == 1):
                if (four_direction(x + 1, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (Y[x][y] == 1 and T[x][y + 1] == 1):
                if (four_direction(x + 1, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (T[x][y + 1] == 1 and Y[x + 1][y] == 1):
                if (four_direction(x, y) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1

            if (Y[x + 1][y] == 1 and T[x][y] == 1):
                if (four_direction(x, y + 1) == 0):
                    T[x][y] ^= 1
                    Y[x][y] ^= 1
                    T[x][y + 1] ^= 1
                    Y[x + 1][y] ^= 1
                    USE[x][y]^=1
        elif (SUM == 3):
            T[x][y] ^= 1;
            Y[x][y] ^= 1;
            T[x][y + 1] ^= 1;
            Y[x + 1][y] ^= 1;
            USE[x][y]^=1
            Length-=comp*2

#for u in USE:
#    print(*u)

sx=-1
sy=-1
for i in range(mapsize):
    if sx!=-1 and sy!=-1:
        break
    for j in range(mapsize):
        if USE[i][j]==1:
            sx=i
            sy=j
            break

def four_search(x, y):
    if T[x][y]==1 and USE2[x+1][y]==0:
        return (x+1,y)

    if Y[x][y]==1 and USE2[x][y+1]==0:
        return (x,y+1)

    if (x - 1 >= 0):
        if T[x-1][y]==1 and USE2[x-1][y]==0:
            return (x-1,y)

    if (y - 1 >= 0):
        if Y[x][y-1]==1 and USE2[x][y-1]==0:
            return (x,y-1)

    return (-1,-1)

USE2=[[0]*(mapsize+5) for i in range(mapsize+5)]

ANS=[(sx,sy)]
USE2[sx][sy]=1

x=sx
y=sy
while True:
    z,w=four_search(x,y)

    if z==-1 and w==-1:
        break
    else:
        x=z
        y=w
        ANS.append((x,y))
        USE2[x][y]=1

ANS2=[]
for x,y in ANS:
    if len(ANS2)<=2:
        ANS2.append((x,y))
    else:
        x2,y2=ANS2[-2]
        x1,y1=ANS2[-1]

        if y2==y1==y:
            ANS2.pop()
        elif x2==x1==x:
            ANS2.pop()

        ANS2.append((x,y))

print(len(ANS2))
for x,y in ANS2:
    print(x*comp,y*comp)
        





###########################################################

