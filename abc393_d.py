
################################################################
[my WA]
#同時処理の形にしたが

N,Q=map(int,input().split())

bird2bag=[] #birdを入力するとbagがわかる
bag2nest=[] #bagを入力するとnestがわかる
nest2bag=[] #nestを入力するとbagがわかる

for i in range(N+1):
  bird2bag+=[i]
  bag2nest+=[i]
  nest2bag+=[i]
  
for i in range(Q):
  qr= tuple(map(int,input().split()))
  if qr[0]==1:
    a,b=qr[1],qr[2]
    bagi=nest2bag[b]
    bird2bag[a]=bagi #birdを正しいbagに入れる、nestは知らん
    
  elif qr[0]==2:
    a,b=qr[1],qr[2] #nestの情報であって、bagの情報はわからない前提
    bag_b=bag2nest[a] #nestのbagを調べる
    bag_a=bag2nest[b] 
    nest2bag[a],nest2bag[b]=bag_b,bag_a  #同時処理の形
    bag2nest[bag_a],bag2nest[bag_b]=a,b  #同時処理の形

  elif qr[0]==3:
    a=qr[1]
    bagi=bird2bag[a]
    nesti=bag2nest[bagi]
    print(nesti)
    

##################################################################
[my WA]

'''
種類1:整数a,bが与えられる。鳩aを今いる巣から取り出し、巣bへ移動する。
種類2:整数a,bが与えられる。巣aにいる鳩をすべて巣bへ移動し、巣bにいる鳩をすべて巣aへ移動する。
種類3:整数a(1≤a≤N)が与えられる。鳩aが今いる巣の番号を報告する。
'''
N,Q=map(int,input().split())

bird2bag=[] #birdを入力するとbagがわかる
bag2nest=[] #bagを入力するとnestがわかる
nest2bag=[] #nestを入力するとbagがわかる

for i in range(N+1):
  bird2bag+=[i]
  bag2nest+=[i]
  nest2bag+=[i]
  
for i in range(Q):
  qr= tuple(map(int,input().split()))
  if qr[0]==1:
    a,b=qr[1],qr[2]
    bagi=nest2bag[b]
    bird2bag[a]=bagi #birdを正しいbagに入れる、nestは知らん
    
  elif qr[0]==2:
    a,b=qr[1],qr[2] #nestの情報であって、bagの情報はわからない前提
    bag_b=bag2nest[a] #nestのbagを調べる
    bag_a=bag2nest[b] 
    nest2bag[a]=bag_b 
    nest2bag[b]=bag_a 
    bag2nest[bag_a]=a
    bag2nest[bag_b]=b

  elif qr[0]==3:
    a=qr[1]
    bagi=bird2bag[a]
    nesti=bag2nest[bagi]
    print(nesti)
    
    

##################################################################
[poe]
N, Q = map(int, input().split())

# 鳥, 場所, 箱
bird_to_place = list(range(N))
place_to_box = list(range(N))
box_to_place = list(range(N))
for _ in range(Q):
    query = tuple(map(lambda x: int(x)-1, input().split()))
    op = query[0]
    if op == 0:
        # 鳥の場所を箱の場所に更新する(鳥→場所, 箱→場所)
        a, b = query[1], query[2]
        place = box_to_place[b]
        bird_to_place[a] = place
    if op == 1:
        # 箱Aの場所を箱Bの場所と入れ替える(場所→箱)
        a, b = query[1], query[2]
        place_a, place_b = box_to_place[a], box_to_place[b]
        place_to_box[place_a], place_to_box[place_b] = b, a
        box_to_place[a], box_to_place[b] = place_b, place_a
    if op == 2:
        # 鳥の場所の箱を参照する(鳥→場所→箱)
        a = query[1]
        place = bird_to_place[a]
        box = place_to_box[place]
        print(box+1)

##################################################################
[irb]

N, Q = map(int, input().split())

hato = [i for i in range(N+1)]
index2su = [i for i in range(N+1)]
su2index = [i for i in range(N+1)]
for _ in range(Q):
  op = list(map(int, input().split()))
  if op[0] == 1:
    a, b = op[1:]
    hato[a] = su2index[b]
  elif op[0] == 2:
    a, b = op[1:]
    index2su[su2index[a]] = b
    index2su[su2index[b]] = a
    su2index[a], su2index[b] = su2index[b], su2index[a]
  else:
    print(index2su[hato[op[1]]])

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
