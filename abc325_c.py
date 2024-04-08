//abc325_c.py
###############################################
[keroru]
import sys
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()
import bisect,string,math,time,functools,random,fractions
from bisect import*
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
import itertools
rep=range;R=range
def I():return int(input())
def LI():return [int(i) for i in input().split()]
def SLI():return sorted([int(i) for i in input().split()])
def LI_():return [int(i)-1 for i in input().split()]
def S_():return input()
def IS():return input().split()
def LS():return [i for i in input().split()]
def NI(n):return [int(input()) for i in range(n)]
def NI_(n):return [int(input())-1 for i in range(n)]
def NLI(n):return [[int(i) for i in input().split()] for i in range(n)]
def NLI_(n):return [[int(i)-1 for i in input().split()] for i in range(n)]
def StoLI():return [ord(i)-97 for i in input()] 
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RLI(n=8,a=1,b=10):return [random.randint(a,b)for i in range(n)]
def RI(a=1,b=10):return random.randint(a,b)
def GI(V,E,ls=None,Directed=False,index=1):
    org_inp=[];g=[[] for i in range(V)]
    FromStdin=True if ls==None else False
    for i in range(E):
        if FromStdin:
            inp=LI()
            org_inp.append(inp)
        else:
            inp=ls[i]
        if len(inp)==2:a,b=inp;c=1
        else:a,b,c=inp
        if index==1:a-=1;b-=1
        aa=a,c,;bb=b,c,;g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp
def RE(E):
    rt=[[]for i in range(len(E))]
    for i in range(len(E)):
        for nb,d in E[i]:
            rt[nb]+=(i,d),
    return rt
def RLE(it):
    rt=[]
    for i in it:
        if rt and rt[-1][0]==i:rt[-1][1]+=1
        else:rt+=[i,1],
    return rt
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
    #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
    mp=[boundary]*(w+2);found={}
    for i in R(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[boundary]+[mp_def[j] for j in s]+[boundary]
    mp+=[boundary]*(w+2)
    return h+2,w+2,mp,found
def TI(n):return GI(n,n-1)
def accum(ls):
    rt=[0]
    for i in ls:rt+=[rt[-1]+i]
    return rt
def bit_combination(n,base=2):
    rt=[]
    for tb in R(base**n):s=[tb//(base**bt)%base for bt in R(n)];rt+=[s]
    return rt
def gcd(x,y):
    if y==0:return x
    if x%y==0:return y
    while x%y!=0:x,y=y,x%y
    return y
def YN(x):print(['NO','YES'][x])
def Yn(x):print(['No','Yes'][x])
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)

inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('UDRL',FourNb));HexNb=[(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0)]
alp=[chr(ord('a')+i)for i in range(26)]
#sys.setrecursionlimit(10**7)

def gcj(t,*a):
    print('Case #{}:'.format(t+1),*a)

def INP():
    N=80
    n=random.randint(1,N)
    m=random.randint(1,N)
    a=RLI(n,1,10)
    return n,m,a
def Rtest(T):
    case,err=0,0
    for i in range(T):
        inp=INP()
        #show(inp)
        a1=naive(*inp)
        a2=solve(*inp)
        if a1!=a2:
            print(inp)
            #n,d,k=inp
            #a,b=bin(n)[2:],bin(x)[2:]
            #show(n,d,k)
            print('naive',a1)
            print('solve',a2)
            err+=1
        case+=1
    print('Tested',case,'case with',err,'errors')

def graph():
    g=[[]for i in range(n)]
    for i in range(m):
        u,v=LI()
        g[u]+=v,
        g[v]+=u,
    
mo=998244353
#mo=10**9+7

show_flg=False
show_flg=True

ans=0



## Tested by ABC264-E
## https://atcoder.jp/contests/abc264/tasks/abc264_e
## Tested by ABC120-D
## https://atcoder.jp/contests/abc120/tasks/abc120_d

class UnionFind:
    def __init__(self,n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.parent=[-1]*n
        # 連結成分の個数を管理
        self._size=[1]*n
 
    def root(self,x):
        if self.parent[x]<0:
            return x
        else:
            # 経路の圧縮
            self.parent[x]=self.root(self.parent[x])
            return self.parent[x]
 
    def same(self,x,y):
        return self.root(x)==self.root(y)
 
    def union(self,x,y):
        r1=self.root(x)
        r2=self.root(y)
        if r1==r2:
            return
        # ランクの取得
        d1=self.parent[r1]
        d2=self.parent[r2]
        if d1<=d2:
            self.parent[r2]=r1
            self._size[r1]+=self._size[r2]
            if d1==d2:
                self.parent[r1]-=1
        else:
            self.parent[r1]=r2
            self._size[r2]+=self._size[r1]
    
    def size(self,x):
        return self._size[self.root(x)]
        
    def __str__(self):
        rt=[i if j<0 else j for i,j in enumerate(self.parent)]
        return str(rt)

h,w=LI()
a=[]
    
for i in range(h):
    a+=[1 if i=='#' else 0 for i in input()],

b=[[0]*w for i in range(h)]


c=0
uf=UnionFind(h*w)
for i in range(h):
    for j in range(w):
        if a[i][j]>0:
            for di,dj in EightNb:
                ni=i+di
                nj=j+dj
                if 0<=ni<h and 0<=nj<w and a[ni][nj]==1:
                    uf.union(i*w+j,ni*w+nj)
ans=set()
for i in range(h):
    for j in range(w):
        if a[i][j]>0:
            ans.add(uf.root(i*w+j))

print(len(ans))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[shoppy]
#グラフを使って解く問題BFSやDFS
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def dfs(y, x):
    t = [(y, x)]
    while t:
        # print(t)
        y, x = t.pop()
        S[y][x] = "."
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                y2, x2 = y + dy, x + dx
                if 0 <= y2 < H and 0 <= x2 < W and S[y2][x2] == "#":
                    t.append((y2, x2))


ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            dfs(y, x)
            ans += 1
print(ans)

###############################################
[reimo]
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
def Judge(i,j):
    t=[[i,j]]
    while len(t)>0:
        x,y=t.pop()
        s[x][y]="."
        for di in range(-1,2):
            for dj in range(-1,2):
                a_x=x+di
                a_y=y+dj
                if 0<=a_x<h and 0<=a_y<w and s[a_x][a_y]=="#":
                    t.append([a_x,a_y])
ans=0
for i in range(h):  
    for j in range(w):
        if s[i][j]=="#":
            Judge(i,j)
            ans+=1
print(ans)
###############################################
[chame]
from sys import setrecursionlimit
setrecursionlimit(10**7)
h,w=map(int,input().split())
grid=[['.' for _ in range(w+2)]]
for _ in range(h):
    grid.append(['.']+list(input())+['.'])
grid.append(['.' for _ in range(w+2)])

visited=set()
def dfs(i,j,grid,visited):
    visited.add((i,j))
    for x in range(-1,2):
        for y in range(-1,2):
            if (x,y)!=(0,0) and grid[i+x][j+y]=='#' and not((i+x,j+y) in visited):
                dfs(i+x,j+y,grid,visited)
    return 1

count=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j]=='#' and not((i,j) in visited):
            count+=dfs(i,j,grid,visited)

print(count)
###############################################
[titia]
import sys
input = sys.stdin.readline

H,W=map(int,input().split())
MAP=[input().strip() for i in range(H)]

USE=[[0]*W for i in range(H)]

ANS=0

for i in range(H):
    for j in range(W):
        if MAP[i][j]=="#" and USE[i][j]==0:
            ANS+=1
            Q=[(i,j)]

            while Q:
                x,y=Q.pop()
                for z in range(x-1,x+2):
                    for w in range(y-1,y+2):
                        if 0<=z<H and 0<=w<W and USE[z][w]==0 and MAP[z][w]=="#":
                            USE[z][w]=1
                            Q.append((z,w))

print(ANS)
###############################################

[input sample]
3 3
#.#
.#.
#.#
###############################################

[stpete WA & TLE ans]

h,w=map(int,input().split())
S=[]
P=[]
t=0
for i in range(h):
  s=list(input())
  S+=[s]
  for j,si in enumerate(s):
    if si=='#':
      t+=1
      P+=[(i,j)]

T=[]
for i in range(t):
  T+=[set([i])]
  
for i in range(t):
  for j in range(i+1,t):
    if abs(P[i][0]-P[j][0])<=2 and abs(P[i][1]-P[j][1])<=2:
      T[i].add(j)
  
for i in range(len(T)):
  for j in range(i,len(T)):
    if T[i] & T[j] !=set():
      T[i]=T[i]|T[j]
      T[j]=T[i]|T[j]

T2=[]
for t in T:
  T2+=[str(sorted(t))]

print(len(set(T2)))
###############################################
###############################################
