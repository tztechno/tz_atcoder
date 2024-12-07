#######################################

#######################################

#######################################

#######################################
[keroru]

import sys
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()
try:sys.set_int_max_str_digits(0)
except:pass
import string,math,time,functools,random,fractions
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
def StoLI():
    s=input()
    return [ord(i)-97 for i in s]
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
sys.setrecursionlimit(10**7)

def gcj(t,*a):
    print('Case #{}:'.format(t+1),*a)

def INP():
    N=80
    n=random.randint(1,N)
    x=random.randint(1,N)
    n,d=RLI(2,1,10)
    k=RI(1,n)
    return n,d,k
  
def Rtest(T):
    case,err=0,0
    for i in range(T):
        inp=INP()
        #show(inp)
        a1=naive(*inp)
        a2=solve(*inp)
        if a1!=a2:
            print(inp)
            n,d,k=inp
            #a,b=bin(n)[2:],bin(x)[2:]
            show(n,d,k)
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

show_flg=False
show_flg=True

h,w,d=LI()
a=[]
q=deque([])
for i in range(h):
    s=input()
    a+=s,
    for j in range(w):
        if s[j]=='H':
            q+=(i,j),

v=[[0]*w for j in range(h)]

for r,c in q:
    v[r][c]=d+1
while q:
    r,c=q.popleft()
    if v[r][c]<=1:
        continue
    for dr,dc in FourNb:
        nr=dr+r
        nc=dc+c
        if 0<=nr<h and 0<=nc<w:
            
            if a[nr][nc]=='.' or a[nr][nc]=='H':
                if v[nr][nc]==0:
                    q+=(nr,nc),
                    v[nr][nc]=v[r][c]-1

for i in range(h):
    for j in range(w):
        if v[i][j]>=1:
            ans+=1
print(ans)

#######################################
[shaka]

from collections import deque
H,W,D=map(int,input().split())
S=[list(input())for i in range(H)]
dist=[[-1 for j in range(W)]for i in range(H)]
deq=deque()
for i in range(H):
    for j in range(W):
        if S[i][j]=="H":
            deq.append((i,j))
            dist[i][j]=0
di=[-1,0,1,0]
dj=[0,1,0,-1]
while(deq):
    i,j=deq.popleft()
    for k in range(4):
        ni=i+di[k]
        nj=j+dj[k]
        if 0<=ni and ni<H and 0<=nj and nj<W:
            if S[ni][nj]!="#" and dist[ni][nj]==-1:
                deq.append((ni,nj))
                dist[ni][nj]=dist[i][j]+1
ans=0
for i in range(H):
    for j in range(W):
        if 0<=dist[i][j]<=D:
            ans+=1
print(ans)

#######################################
[titia]

import sys
input = sys.stdin.readline

from collections import deque

H,W,D=map(int,input().split())

MAP=[input().strip() for i in range(H)]
LIST=[[1<<30]*W for i in range(H)]

Q=deque()
for i in range(H):
    for j in range(W):
        if MAP[i][j]=="H":
            LIST[i][j]=D
            Q.append((i,j))

while Q:
    x,y=Q.popleft()
    if LIST[x][y]==0:
        continue
    for z,w in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=z<H and 0<=w<W:
            if MAP[z][w]=="#":
                continue
            if LIST[z][w]>H*W+10:
                LIST[z][w]=LIST[x][y]-1
                Q.append((z,w))

ANS=0
for i in range(H):
    for j in range(W):
        if LIST[i][j]<=D:
            ANS+=1

print(ANS)

#######################################
[my tle]
import copy

H,W,D=map(int,input().split())

S=[]
K=[]
U0=[]
for i in range(H):
  row=list(input())
  U0+=[row]
  for j in range(W):
    if row[j]=='.':
      S+=[(i,j)]
    if row[j]=='H':
      K+=[(i,j)]
      
#print(U0)
T=[]
for i in range(len(S)):
  for j in range(i+1,len(S)):
    T+=[[S[i],S[j]]]

def effect(U,P,D):
  x1,y1=P[0],P[1]
  for e,si in enumerate(S):
    i,j=si[0],si[1]
    if abs(x1-i)+abs(y1-j)<=D:
      U[i][j]='o'
  return U
  
U1=copy.deepcopy(U0)
for k in K:
  U1=effect(U1,k,D)

#print(U1)  
flat_list = [item for sublist in U1 for item in sublist]
ANS=flat_list.count('o')
print(ANS+len(K))

#######################################
[my tle]

import sys
input = sys.stdin.readline
import copy

H,W,D=map(int,input().split())

S=[]
K=[]
U0=[]
for i in range(H):
  row=list(input())
  U0+=[row]
  for j in range(W):
    if row[j]=='.':
      S+=[(i,j)]
    if row[j]=='H':
      K+=[(i,j)]
      
#print(U0)
T=[]
for i in range(len(S)):
  for j in range(i+1,len(S)):
    T+=[[S[i],S[j]]]

def effect(U,P,D):
  x1,y1=P[0],P[1]
  for i in range(H):
    for j in range(W):
      if abs(x1-i)+abs(y1-j)<=D and U[i][j]=='.':
        U[i][j]='o'
  return U
  
ANS=0
U1=copy.deepcopy(U0)
for k in K:
  U1=effect(U1,k,D)
  #print(t,'U0',U0,'U1',U1,'U2',U2)
  flat_list = [item for sublist in U1 for item in sublist]
  ANS=max(ANS,flat_list.count('o'))
print(ANS+len(K))

#######################################



