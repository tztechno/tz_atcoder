
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[myai]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.black_count = [0]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.black_count[x] += self.black_count[y]

    def add_black(self, x, delta):
        r = self.find(x)
        self.black_count[r] += delta

    def has_black(self, x):
        r = self.find(x)
        return self.black_count[r] > 0


N, Q = map(int, input().split())
dsu = DSU(N)
color = [0]*N

out = []
for _ in range(Q):
    q = input().split()
    t = int(q[0])
    if t == 1:
        u, v = int(q[1])-1, int(q[2])-1
        dsu.union(u, v)
    elif t == 2:
        v = int(q[1])-1
        if color[v] == 0:
            color[v] = 1
            dsu.add_black(v, 1)
        else:
            color[v] = 0
            dsu.add_black(v, -1)
    else:
        v = int(q[1])-1
        out.append("Yes" if dsu.has_black(v) else "No")

print("\n".join(out))
##################################################################
