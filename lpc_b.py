###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[ant]
from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree
from atcoder.dsu import DSU as UnionFind
inf = 10**15
# --------------------------------------------------------
n,q = map(int, input().split())
seg = SegTree(lambda x, y: x + y,0, list(map(int, input().split())))
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 0:
        tmp = seg.get(x)
        seg.set(x, y+tmp)
    else:
        print(seg.prod(x, y))
###############################################
[futa]
import sys
from atcoder.fenwicktree import FenwickTree

n,q = map(int,input().split())
fenwick_tree = FenwickTree(n)

a = list(map(int,input().split()))
for i, ai in enumerate(a):
    fenwick_tree.add(i, ai)

for _ in range(q):
    t, x, y = map(int,input().split())
    if t == 0:
        fenwick_tree.add(x, y)
    if t == 1:
        print(fenwick_tree.sum(x, y))
###############################################
[deepseek AC]
class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e()] * (2 * self._size)
        
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        return self._d[p + self._size]
    
    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        
        return self._op(sml, smr)
    
    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

# 区間和
def op(x, y): return x + y
def e(): return 0

N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(op, e, N, A)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:  # update
        p, x = q[1], q[2]
        seg.set(p, seg.get(p) + x)
    elif q[0] == 1:  # query
        l, r = q[1], q[2]
        print(seg.prod(l, r))

###############################################
[claude AC] #SegTree

from atcoder.segtree import SegTree

# 区間和
def op(x, y): 
    return x + y

def e(): 
    return 0

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Create SegTree with the operation function and identity element
seg = SegTree(op, 0, A)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:  # update
        p, x = q[1], q[2]
        seg.set(p, seg.get(p) + x)
    elif q[0] == 1:  # query
        l, r = q[1], q[2]
        print(seg.prod(l, r))

###############################################
[cgpt AC] #FenwickTree

import sys
from atcoder.fenwicktree import FenwickTree

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

fw = FenwickTree(N)
for i, a in enumerate(A):
    fw.add(i, a)  # 初期値セット

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:  # update: A[p] += x
        p, x = q[1], q[2]
        fw.add(p, x)
    elif q[0] == 1:  # query: sum(l, r)
        l, r = q[1], q[2]
        print(fw.sum(l, r))  # [l, r)

###############################################
[my TLE9]

N,Q=map(int,input().split())
A=list(map(int,input().split()))
for i in range(Q):
  q=list(map(int,input().split()))
  if q[0]==0:
    p,x=q[1],q[2]
    A[p]+=x
  elif q[0]==1:
    l,r=q[1],q[2]  
    print(sum(A[l:r]))
###############################################
[my TLE9]

N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[0]
for a in A:
  B+=[B[-1]+a]
for i in range(Q):
  q=list(map(int,input().split()))
  if q[0]==0:
    p,x=q[1],q[2]
    for j in range(p+1,N+1):
      B[j]+=x
  elif q[0]==1:
    l,r=q[1],q[2]  
    print(B[r]-B[l])

###############################################
###############################################
###############################################

