##################################################################
##################################################################
##################################################################
##################################################################
[cgpt]

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # 初期状態では自分自身が親
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

N, Q = map(int, input().split())
uf = UnionFind(N)

for _ in range(Q):
    qr = list(map(int, input().split()))

    if qr[0] == 1:
        a, b = qr[1], qr[2]
        uf.parent[a] = b  # 鳩 a の巣を直接 b にする

    elif qr[0] == 2:
        a, b = qr[1], qr[2]
        uf.union(a, b)  # 巣 a と巣 b を統合する

    elif qr[0] == 3:
        a = qr[1]
        print(uf.find(a))  # 鳩 a のいる巣を出力



##################################################################
[titia]

import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

A=list(range(N+1))
BOX=list(range(N+1))
BOX_INV=list(range(N+1))

for tests in range(Q):
    #print(BOX,BOX_INV)
    L=list(map(int,input().split()))

    if L[0]==1:
        a,b=L[1],L[2]

        A[a]=BOX[b]

    elif L[0]==2:
        a,b=L[1],L[2]

        BOX[a],BOX[b]=BOX[b],BOX[a]

        BOX_INV[BOX[a]]=a
        BOX_INV[BOX[b]]=b

    else:
        a=L[1]
        print(BOX_INV[A[a]])

##################################################################
[my TLE]

N,Q=map(int,input().split())
Nest=list(range(0,N+1))#鳥を入れると巣がわかる

Bird=[]#巣を入れると鳥のリスト
for k in range(N+1):
  Bird+=[[]]
  
for i in range(Q):
  
  qr=list(map(int,input().split()))
  
  if qr[0]==1:
    a,b=qr[1],qr[2]
    #鳩aを今いる巣から取り出し、巣bへ移動する。
    Nest[a]=b
    
  elif qr[0]==2:
    a,b=qr[1],qr[2]
    
    for j in range(N+1):
      Bird[Nest[j]]+=[j]      

    birdsA=Bird[a]
    for c in birdsA:
      Nest[c]=b
      
    birdsB=Bird[b]
    for c in birdsB:
      Nest[c]=a
        
    for j in range(N+1):
      Bird[Nest[j]]+=[j]  
      
  elif qr[0]==3:
    a=qr[1]
    #鳩aが今いる巣の番号を報告する。
    print(Nest[a])

##################################################################
