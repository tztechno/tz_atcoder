##################################################################
##################################################################
##################################################################
##################################################################
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
