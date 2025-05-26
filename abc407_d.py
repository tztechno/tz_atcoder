##################################################################
H行W列のマス目があります。上からi行目(1≤i≤H)、左からj列目(1≤j≤W)のマスをマス(i,j)と呼ぶことにします。マス(i,j)(1≤i≤H,1≤j≤W)には非負整数Ai,j​が書かれています。
このマス目にドミノを0個以上置きます。1つのドミノは隣り合う2つのマス、つまり1≤i≤H,1≤j<Wに対するマス(i,j)とマス(i,j+1)1≤i<H,1≤j≤Wに対するマス(i,j)とマス(i+1,j)のどれかに置くことができます。
ただし、同じマスに対して複数のドミノを置くことはできません。ドミノの置き方に対して、置き方のスコアをドミノが置かれていないマスに書かれた整数すべてのビットごとの排他的論理和として定めます。
ドミノの置き方のスコアとしてありうる最大値を求めてください。
ビットごとの排他的論理和とは非負整数A,Bのビットごとの排他的論理和A⊕Bは、以下のように定義されます。
A⊕Bを二進表記した際の2k(k≥0)の位の数は、A,Bを二進表記した際の2kの位の数のうち一方のみが1であれば1、そうでなければ0である。
例えば、3⊕5=6となります(二進表記すると:011⊕101=110)。
一般にk個の非負整数p1​,p2​,p3​,…,pk​のビット単位XORは(…((p1​⊕p2​)⊕p3​)⊕⋯⊕pk​)と定義され、これはp1​,p2​,p3​,…,pk​の順番によらないことが証明できます。
##################################################################
difficulty=930
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[hobit]
H, W = map(int, input().split())
A = sum([[*map(int, input().split())] for _ in range(H)], [])
N = H*W

dp = {0}
for i in range(N):
    h, w = divmod(i, W)
    for domino in [*dp]:
        if domino >> i & 1:
            continue
        nd = domino ^ 1 << i
        for j in [0, 1]:
            nh, nw = h+j, w+(1-j)
            ni = nh*W + nw
            if nh < H and nw < W and not (domino >> ni & 1):
                dp.add(nd ^ 1 << ni)

ans = 0
for d in dp:
    x = 0
    for i in range(N):
        if not (d >> i & 1):
            x ^= A[i]
    ans = max(ans, x)
print(ans)

##################################################################
[kumak]
h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
dominopattern = {0}
for i in range(h):
    for j in range(w):
        for d in list(dominopattern):
            if not d & 1 << (i*w + j):
                if i + 1 < h and not d & 1 << ((i+1)*w + j):
                    dominopattern.add(
                    	d | 1 << (i*w + j) | 1 << ((i+1)*w + j))
                if j + 1 < w and not d & 1 << (i*w + j + 1):
                    dominopattern.add(
                    	d | 3 << (i*w + j))
ans = 0
for d in dominopattern:
    xor = 0
    for i in range(h):
        for j in range(w):
            if not d & 1 << (i*w + j):
                xor ^= a[i][j]
    ans = max(ans,xor)
print(ans)

##################################################################
[titia]
import sys
input = sys.stdin.readline
from collections import defaultdict,deque

H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
XOR=0

for a in A:
    for x in a:
        XOR^=x

LANS=XOR

for bb in range(1<<(H*W)):
    V=H*W+2
    start=V-2
    goal=V-1
    EDGE=[defaultdict(int) for i in range(V)]

    count=0
    X=[[0]*W for i in range(H)]
    score=0

    for i in range(H*W):
        if bb & (1<<i) != 0:
            count+=1
            X[i//W][i%W]=1
            score^=A[i//W][i%W]

    if score^XOR<=LANS:
        continue

    if count%2==1:
        continue
    fflag=0

    for i in range(H):
        if fflag==1:
            break
        for j in range(W):
            if X[i][j]==1:
                if (i+j)%2==0:
                    u,v,c=start,i*W+j,1
                    EDGE[u][v]=c

                    flag=0

                    for z,w in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=z<H and 0<=w<W and X[z][w]==1:
                            flag=1
                            u,v,c=i*W+j,z*W+w,1
                            EDGE[u][v]=1

                    if flag==0:
                        fflag=1
                        break

                else:
                    u,v,c=i*W+j,goal,1
                    EDGE[u][v]=c

    if fflag==1:
        continue

    ANS=0
    while True:
        # まずBFSする

        DIS=[-1]*V
        Q=deque([start])
        DIS[start]=0
        EDGE2=[[] for i in range(V)]

        while Q:
            x=Q.popleft()
            for to in EDGE[x]:
                if EDGE[x][to]==0:
                    continue
                
                if DIS[to]==-1:
                    DIS[to]=DIS[x]+1
                    Q.append(to)
                    EDGE2[x].append(to)
                    
                elif DIS[to]==DIS[x]+1:
                    EDGE2[x].append(to)

        if DIS[goal]==-1:
            break

        # BFSしたときのEDGEを使ってDFSする

        MINCOST=[float("inf")]*V
        NOW=start
        ROUTE=[-1]*V
        
        while NOW!=-1: # DFS

            cost=MINCOST[NOW]
            
            if NOW==goal:
                ANS+=cost
                i=goal
                
                while i!=start: # goalからたどり,Routeを使ってEDGEの更新
                    j=ROUTE[i]
                    if EDGE[j][i]==cost:
                        NOW=j
                        EDGE2[j].pop()
                    
                    EDGE[j][i]-=cost # 使ったルートをいけなく更新
                    MINCOST[j]-=cost                
                    EDGE[i][j]+=cost # 逆向きに進めるようにする.
                    i=j
                continue

            if EDGE2[NOW]:
                to=EDGE2[NOW][-1]
                ROUTE[to]=NOW
                MINCOST[to]=min(cost,EDGE[NOW][to])
                NOW=to

            else:
                if NOW==start:
                    break
                EDGE2[ROUTE[NOW]].pop()
                NOW=ROUTE[NOW]

    #print(ANS)

    if ANS==count//2:
        LANS=max(LANS,score^XOR)

print(LANS)
        

##################################################################
ドミノの置き方パターン、残り数字のパターン

##################################################################
H,W=map(int,input().split())
S=[]
for i in range(H):
  s=list(map(int,input().split()))
  S+=[s]
print(S)

##################################################################
