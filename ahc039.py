###########################################################

###########################################################

###########################################################

###########################################################

###########################################################

###########################################################

###########################################################
[pts 490000]

import time
import random
import math
from collections import defaultdict

t0 = time.time()

#入力
N = int(input())  #N = 5000
pos = [list(map(int,input().split())) for _ in range(N*2)]

#前処理
W = 5000
K = 20
buckets = [[0]*(K+1) for _ in range(K+1)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#サバ
for i in range(N):
    x,y = pos[i]
    buckets[x//W][y//W] += 1
#イワシ
for i in range(N,N*2):
    x,y = pos[i]
    buckets[x//W][y//W] -= 1


class State:
    def __init__(self):
        self.data = [[0]*K for _ in range(K)]
        self.length = 0
        self.score = 0
        self.size = 0


def calc(state):
    vis = [[0]*K for _ in range(K)]
    length = 0
    score = 0
    cnt = 0
    
    for i in range(K):
        for j in range(K):
            if state.data[i][j]:
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if vis[x][y]:
                        continue
                    vis[x][y] = 1
                    score += buckets[x][y]
                    cnt += 1
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if nx < 0 or ny < 0 or nx >= K or ny >= K:
                            length += W
                            continue
                        if not state.data[nx][ny]:
                            length += W
                            continue
                        if vis[nx][ny]:
                            continue
                        stack.append((nx,ny))
                break
        else:
            continue
        break
    
    for i in range(K):
        for j in range(K):
            if not state.data[i][j]:
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if vis[x][y]:
                        continue
                    vis[x][y] = 1
                    cnt += 1
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if nx < 0 or ny < 0 or nx >= K or ny >= K:
                            continue
                        if state.data[nx][ny]:
                            continue
                        if vis[nx][ny]:
                            continue
                        stack.append((nx,ny))
                break
        else:
            continue
        break
    
    
    if cnt < K*K:
        return -1,-1
    else:
        return score,length

def output(state):
    vis = [[0]*K for _ in range(K)]
    to = defaultdict(lambda:[])
    sx,sy = -1,-1
    
    for i in range(K):
        for j in range(K):
            if state.data[i][j]:
                sx,sy = i,j
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if vis[x][y]:
                        continue
                    vis[x][y] = 1
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if nx < 0 or ny < 0 or nx >= K or ny >= K:
                            if k == 0:
                                to[(x,y+1)].append((x+1,y+1))
                                to[(x+1,y+1)].append((x,y+1))
                            if k == 1:
                                to[(x+1,y)].append((x+1,y+1))
                                to[(x+1,y+1)].append((x+1,y))
                            if k == 2:
                                to[(x,y)].append((x+1,y))
                                to[(x+1,y)].append((x,y))
                            if k == 3:
                                to[(x,y)].append((x,y+1))
                                to[(x,y+1)].append((x,y))
                            continue
                        if not state.data[nx][ny]:
                            if k == 0:
                                to[(x,y+1)].append((x+1,y+1))
                                to[(x+1,y+1)].append((x,y+1))
                            if k == 1:
                                to[(x+1,y)].append((x+1,y+1))
                                to[(x+1,y+1)].append((x+1,y))
                            if k == 2:
                                to[(x,y)].append((x+1,y))
                                to[(x+1,y)].append((x,y))
                            if k == 3:
                                to[(x,y)].append((x,y+1))
                                to[(x,y+1)].append((x,y))
                            continue
                        if vis[nx][ny]:
                            continue
                        stack.append((nx,ny))
                break
        else:
            continue
        break
    
    res = [(sx*W,sy*W)]
    px,py = -1,-1
    x,y = sx,sy
    while True:
        for nx,ny in to[(x,y)]:
            if (nx,ny) == (px,py):
                continue
            px,py = x,y
            x,y = nx,ny
            break
        if (x,y) == (sx,sy):
            break
        res.append((x*W,y*W))
    
    print(len(res))
    for x,y in res:
        print(x,y)
    
    
    
#焼きなまし
length_max = 4*10**5
state = State()
weight = 0.002
penalty = 0.1

def eval_score(score,length):
    res = score-weight*length
    if length > length_max:
        res -= (length-length_max)*penalty
    return res

x1,y1,x2,y2 = K,K,-1,-1
for i in range(K):
    for j in range(K):
        if buckets[i][j] > 30:
            x1 = min(x1,i)
            y1 = min(y1,j)
            x2 = max(x2,i)
            y2 = max(y2,j)
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        state.data[i][j] = 1
        state.size += 1
        
score,length = calc(state)
state.score,state.length = eval_score(score,length),length
#output(state)
start_temperature = 100
end_temperature = 1
time_start = time.time()
def get_temperature():
    return start_temperature-(start_temperature-end_temperature)*(time.time()-time_start)/1.8
itr = 0

while time.time()-time_start < 1.8:
    #if itr%100 == 0:
        #output(state)
    itr += 1
    x,y = random.randrange(K),random.randrange(K)
    
    if state.data[x][y]:
        #check
        if state.size == 1:
            continue
        
        #attempt
        state.data[x][y] = 0
        
        raw_score_new,length_new = calc(state)
        if raw_score_new == -1:
            #cancel
            state.data[x][y] = 1
            continue
        else:
            score_new = eval_score(raw_score_new,length_new)
            if score_new >= state.score:
                #accept
                state.score,state.length = score_new,length_new
                state.size -= 1
            else:
                if random.random() < math.exp((score_new-state.score)/get_temperature()):
                    #accept
                    state.score,state.length = score_new,length_new
                    state.size -= 1
                else:
                    #cancel
                    state.data[x][y] = 1
                    continue
    else:
        #check
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or ny < 0 or nx >= K or ny >= K:
                continue
            if state.data[nx][ny]:
                break
        else:
            continue
        
        #attempt
        state.data[x][y] = 1
        
        raw_score_new,length_new = calc(state)
        if raw_score_new == -1:
            #cancel
            state.data[x][y] = 0
            continue
        else:
            score_new = eval_score(raw_score_new,length_new)
            if score_new >= state.score:
                #accept
                state.score,state.length = score_new,length_new
                state.size += 1
            else:
                if random.random() < math.exp((score_new-state.score)/get_temperature()):
                    #accept
                    state.score,state.length = score_new,length_new
                    state.size += 1
                else:
                    #cancel
                    state.data[x][y] = 0
                    continue
        
#print(state.score,state.length,itr)
output(state)
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

