
##################################################################
##################################################################
##################################################################
##################################################################
[claude]

N, Q = map(int, input().split())

# 初期化（各鳩はそれぞれの番号の巣に入っている）
A = list(range(N + 1))
BOX = list(range(N + 1))
BOX_INV = list(range(N + 1))

for _ in range(Q):
    L = list(map(int, input().split()))

    if L[0] == 1:
        a, b = L[1], L[2]
        # 鳩 a を巣 b に入れる
        BOX_INV[a] = b

    elif L[0] == 2:
        a, b = L[1], L[2]
        # 巣 a と巣 b の鳩を交換
        tmp_a, tmp_b = BOX[a], BOX[b]
        BOX[a], BOX[b] = tmp_b, tmp_a
        BOX_INV[tmp_a], BOX_INV[tmp_b] = b, a

    else:
        a = L[1]
        print(BOX_INV[a])

##################################################################
[cgpt2,TLE]

N, Q = map(int, input().split())

# 鳩がどの巣にいるかを記録（初期状態では鳩 i は巣 i にいる）
Nest = list(range(N + 1))

# 巣ごとの鳩リスト（遅延更新）
BirdsInNest = None

for _ in range(Q):
    qr = list(map(int, input().split()))

    if qr[0] == 1:
        a, b = qr[1], qr[2]
        # 鳩 a の巣情報を変更（リストの更新は遅延）
        Nest[a] = b  

    elif qr[0] == 2:
        a, b = qr[1], qr[2]

        # `BirdsInNest` を作り直す
        BirdsInNest = {i: [] for i in range(N + 1)}
        for bird in range(N + 1):
            BirdsInNest[Nest[bird]].append(bird)

        # 巣 a と巣 b の鳩を入れ替える
        BirdsInNest[a], BirdsInNest[b] = BirdsInNest[b], BirdsInNest[a]

        # `Nest` の情報を更新
        for bird in BirdsInNest[a]:
            Nest[bird] = a
        for bird in BirdsInNest[b]:
            Nest[bird] = b

    elif qr[0] == 3:
        a = qr[1]
        print(Nest[a])  # 鳩 a の現在の巣を出力

##################################################################
[cgpt,TLE]

N, Q = map(int, input().split())

# 鳩がどの巣にいるかを記録（初期状態では鳩 i は巣 i にいる）
Nest = list(range(N + 1))

# 巣ごとの鳩リストを管理（初期状態では巣 i に鳩 i のみがいる）
BirdsInNest = {i: [i] for i in range(N + 1)}

for _ in range(Q):
    qr = list(map(int, input().split()))

    if qr[0] == 1:
        a, b = qr[1], qr[2]
        # 鳩 a を現在の巣から削除し、新しい巣 b に移動
        prev_nest = Nest[a]
        BirdsInNest[prev_nest].remove(a)  # 以前の巣から削除
        BirdsInNest[b].append(a)          # 新しい巣に追加
        Nest[a] = b  # 鳩 a の巣情報を更新

    elif qr[0] == 2:
        a, b = qr[1], qr[2]
        # 巣 a と巣 b の鳩を交換
        BirdsInNest[a], BirdsInNest[b] = BirdsInNest[b], BirdsInNest[a]

        # 鳩の巣情報を更新
        for bird in BirdsInNest[a]:
            Nest[bird] = a
        for bird in BirdsInNest[b]:
            Nest[bird] = b

    elif qr[0] == 3:
        a = qr[1]
        print(Nest[a])  # 鳩 a のいる巣を出力

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
