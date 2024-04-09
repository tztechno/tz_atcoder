//abc311_c
#############################################
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

## Original https://github.com/shakayami/ACL-for-python/blob/master/scc.py
## verified by Typical_90_no_21 https://atcoder.jp/contests/typical90/tasks/typical90_u

def scc(my_edges):
    edges=[]
    N=len(my_edges)
    for u in range(N):
        for v,d in my_edges[u]:
            edges+=(u,v),
    M=len(edges)
    start=[0]*(N+1)
    elist=[0]*M
    for e in edges:
        #show(e)
        start[e[0]+1]+=1
    for i in range(1,N+1):
        start[i]+=start[i-1]
    counter=start[:]
    for e in edges:
        elist[counter[e[0]]]=e[1]
        counter[e[0]]+=1
    visited=[]
    low=[0]*N
    Ord=[-1]*N
    ids=[0]*N
    NG=[0,0]
    def dfs(v):
        stack=[(v,-1,0),(v,-1,1)]
        while stack:
            v,bef,t=stack.pop()
            if t:
                if bef!=-1 and Ord[v]!=-1:
                    low[bef]=min(low[bef],Ord[v])
                    stack.pop()
                    continue
                low[v]=NG[0]
                Ord[v]=NG[0]
                NG[0]+=1
                visited.append(v)
                for i in range(start[v],start[v+1]):
                    to=elist[i]
                    if Ord[to]==-1:
                        stack.append((to,v,0))
                        stack.append((to,v,1))
                    else:
                        low[v]=min(low[v],Ord[to])
            else:
                if low[v]==Ord[v]:
                    while(True):
                        u=visited.pop()
                        Ord[u]=N
                        ids[u]=NG[1]
                        if u==v:
                            break
                    NG[1]+=1
                low[bef]=min(low[bef],low[v])
    for i in range(N):
        if Ord[i]==-1:
            dfs(i)
    for i in range(N):
        ids[i]=NG[1]-1-ids[i]
    group_num=NG[1]
    counts=[0]*group_num
    for x in ids:
        counts[x]+=1
    groups=[[] for i in range(group_num)]
    for i in range(N):
        groups[ids[i]].append(i)
    return groups


n=I()
a=LI_()
g=[[]for i in range(n)]
for i in range(n):
    c=a[i]
    g[i]+=(c,1),
    
x=scc(g)
for l in x:
    if len(l)>1:
        t=l[0]
        ans=[t+1]
        while a[t]!=l[0]:
            t=a[t]
            ans+=t+1,
print(len(ans))
print(*ans)
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
n=int(input())
a = list(map(int, input().split()))
a.insert(0,0)
chk=[-1]*(n+1)
ans=[]
now=1
cnt=0
while chk[now]==-1:
  ans.append(now)
  chk[now]=cnt
  cnt=cnt+1
  now=a[now]
print(len(ans[chk[now]:]))
print(*ans[chk[now]:])
#############################################
#############################################

[important solution]

n = int(input())
a = [0]+list(map(int,input().split()))
now = 1
for i in range(n):
    now = a[now]
b = [now]
while b[0] != a[now]:
    b.append(a[now])
    now = a[now]
print(len(b))
print(*b)

#############################################
#############################################
[my ans]

from collections import defaultdict,deque,Counter

n = int(input())
a = [0]+list(map(int,input().split()))

now = 1
NOW=[]
for i in range(n*2):
  NOW += [now]
  now = a[now]

C=Counter(NOW)
#print(C)

ans=[]
for c in list(C):
  if C[c]>=2:
    ans+=[c]

print(len(ans))
print(*ans)

#############################################
#############################################
import sys
def input():
    return sys.stdin.readline().rstrip()

from atcoder.scc import SCCGraph
N = int(input())
A = list(map(int, input().split()))
G = SCCGraph(N)

for i in range(N):
    G.add_edge(i, A[i]-1)

s = None
gr = G.scc()
for g in gr:
    if len(g) > 1:
        s = g

now = s[0]
print(len(s))
for _ in range(len(s)):
    print(A[now], end=" ")
    now = A[now]-1

#############################################
n = int(input())
a = [x - 1 for x in map(int, input().split())]

visited = [0] * n
tmp = 0
while not visited[tmp]:
    visited[tmp] = 1
    tmp = a[tmp]

visited = [0] * n
ans = []
while not visited[tmp]:
    visited[tmp] = 1
    ans.append(tmp + 1)
    tmp = a[tmp]

print(len(ans))
print(*ans)

#############################################
import sys
input = sys.stdin.readline

n=int(input())
A=[0]+list(map(int,input().split()))

USED=[0]*(n+1)

for i in range(1,n+1):
    if USED[i]==0:
        Q=[i]
        while True:
            x=Q[-1]
            USED[x]=1
            to=A[x]

            if USED[to]==0:
                Q.append(to)
            else:
                break

        last=Q[-1]
        f=Q.index(A[last])

        ANS=Q[f:]
        print(len(ANS))
        print(*ANS)
        break
#############################################
