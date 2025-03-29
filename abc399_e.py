
#######################################################
[]
1000文字以下が少ない
#######################################################
[]
#######################################################
[]
#######################################################
[]
#######################################################
[]
#######################################################
[]
#######################################################
[dni]
import sys

n = int(input())
s = input().strip()
t = input().strip()

if s == t:
    print(0)
    sys.exit()

need = [-1] * 26
for i in range(n):
    c = s[i]
    j = ord(c) - 97

    d = ord(t[i]) - 97

    if need[j] == -1 or need[j] == d:
        need[j] = d
        continue

    print(-1)
    sys.exit()

if -1 not in need and len(set(need)) == 26:
    print(-1)
    sys.exit()

ind = [0] * 27

out = 0
for i in range(26):
    ind[need[i]] += 1
    if need[i] > -1 and need[i] != i:
        out += 1

marked = [1000] * 26
for i in range(26):
    j = i

    z = []
    for _ in range(50):
        if ind[j] != 1:
            break
        
        if marked[j] < i:
            break
        marked[j] = i
        
        j = need[j]
        if j == -1:
            break
        z.append(j)
    else:
        out += z[-1] != z[-2]
print(out)

#######################################################
[sasa]
n=int(input())
s=input()
t=input()
N=26
m=N-len(set(list(s+t)))
e=[[] for i in range(N)]
for i in range(n):
  e[ord(s[i])-ord("a")]+=[ord(t[i])-ord("a")]
for i in range(N):
  e[i]=sorted(set(e[i]))
  if len(e[i])>=2:
    print(-1)
    exit()
  if len(e[i])==1 and e[i][0]==i:
    e[i]=[]
d=[0]*N
for i in range(N):
  for j in e[i]:
    d[j]+=1
ans=sum(d)
q=[i for i in range(N) if d[i]==0]
f=[0]*N
o=[]
for s in q:
  o+=[s]
  m+=len(e[s])!=0
  for t in e[s]:
    d[t]-=1
    f[t]=1
    if d[t]==0:
      q+=[t]
from atcoder import dsu
g=dsu.DSU(N)
for i in range(N):
  if d[i]:
    g.merge(i,e[i][0])
c1=sum(any(f[i]==1 for i in group) for group in g.groups() if len(group)>1)
c2=sum(all(f[i]==0 for i in group) for group in g.groups() if len(group)>1)
if c2==0:
  print(ans)
else:
  print(ans+c2 if m+c1>0 else -1)
#######################################################
[tiku]
from atcoder.dsu import DSU
eng="abcdefghijklmnopqrstuvwxyz"
engd=dict()
for i in range(26) : engd[eng[i]]=i
N=int(input())
S=input()
T=input()
d=dict()
for i in range(N):
    if engd[S[i]] not in d : d[engd[S[i]]]=engd[T[i]]
    elif d[engd[S[i]]]!=engd[T[i]] : exit(print(-1))
uf=DSU(26)
sets=set()
for k,v in d.items():
    uf.merge(k,v)
    sets.add(v)

ans=0
for li in uf.groups():
    if len(li)==1 : continue
    start,now=li[0],li[0]
    for i in range(len(li)+1):
        if now in d : now=d[now]
        else : i=0 ; break
        if now==start : break
    if i==len(li)-1 : ans+=len(li)+1
    else : ans+=sum((i in d) and (i!=d[i]) for i in li)
if len(sets)==26 and ans!=0 : print(-1)
else : print(ans)
#######################################################
[16384]
import sys
from math import factorial, sin, cos, tan, asin, acos, atan, pi, log, log2, log10, ceil, perm, comb, gcd, lcm, sqrt
from itertools import permutations, combinations, combinations_with_replacement
from functools import reduce, cache
from random import randrange, randint, shuffle
from heapq import heappush, heappop, heapify
from copy import deepcopy
from collections import Counter, deque
from decimal import Decimal
from bisect import bisect_left, bisect_right
from fractions import Fraction
from time import time
inp = lambda : sys.stdin.readline().rstrip()
Inp = lambda : [*map(int, sys.stdin.readline().split())]
Fnp = lambda: [*map(float, sys.stdin.readline().split())]
inf = float('inf')

n, = Inp()
A = [ord(c)-ord('a') for c in inp()]
B = [ord(c)-ord('a') for c in inp()]

X = [-1]*26
for i in range(n):
    if X[A[i]] == -1:
        X[A[i]] = B[i]
    elif X[A[i]] != B[i]:
        print(-1)
        sys.exit()

G = [[] for _ in range(26)]
ans = 0
C = [0]*26
for i in range(26):
    if X[i] != -1:
        C[i] = 1
        C[X[i]] = 1
    if X[i] != -1 and i != X[i]:
        G[i].append(X[i])
        ans += 1
        G[X[i]].append(i)

V = [0]*26
g = 0
# print(G)
for i in range(26):
    if V[i] == 0:
        Q = [(i, -1)]
        V[i] = 1
        f = 0
        L = []
        while Q:
            s, p = Q.pop()
            L.append(s)
            for e in G[s]:
                if V[e] == 0:
                    V[e] = 1
                    Q.append((e, s))
                elif e != p:
                    f = 1
        if all(len(G[x]) == 2 for x in L):
            ans += 1
        elif len(L) > 1:
            g = 1

# print(G)
c = sum(C)
if c == 26 and g == 0 and ans:
    print(-1)
else:
    print(ans)
#######################################################
[tiia]
import sys
input = sys.stdin.readline

N=int(input())
S=input().strip()
T=input().strip()

if S==T:
    print(0)
    exit()

# UnionFind

Group = [i for i in range(30)] # グループ分け
Nodes = [1]*(30) # 各グループのノードの数

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:
            
            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)
            
        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)


X=[set() for i in range(26)]

for i in range(N):
    s=ord(S[i])-97
    t=ord(T[i])-97

    X[s].add(t)

for i in range(26):
    if len(X[i])>=2:
        print(-1)
        exit()

E=[[] for i in range(26)]
E_INV=[[] for i in range(26)]

for i in range(26):
    if X[i]==set():
        continue
    t=X[i].pop()

    E[i].append(t)
    E_INV[t].append(i)
    Union(i,t)

# なもりはOK
# 単純なサイクルのみ+1

ANS=0
CYS=0

for i in range(26):
    if find(i)==i:
        if Nodes[find(i)]==1:
            if len(E[i])==1 and len(E_INV[i])==1:
                CYS+=1
            continue
        LIST=[]

        for j in range(26):
            if find(j)==i:
                LIST.append(j)

        W=0
        c=0
        minus=0

        for x in LIST:
            if len(E[x])==1 and len(E_INV[x])==1:
                W+=1
            if len(E[x])==1:
                c+=1
            if E[x] and E[x][0]==x:
                minus=1

        if W==len(LIST):
            ANS+=W+1
            CYS+=W
        else:
            ANS+=c-minus

if CYS==26:
    print(-1)
else:
    print(ANS)

#######################################################
