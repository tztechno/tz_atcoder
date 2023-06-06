####################################
#TLE

n,D=map(int,input().split())
XY=[]
for i in range(n):
  x,y=map(int,input().split())
  XY+=[(x,y)]
#print(XY)
E=[]
for i in range(n):
  E+=[[i]]
#print(E)
for i in range(n):
  for j in range(n):
    if i!=j:
      (x0,y0)=XY[i]
      (x1,y1)=XY[j]
      if (x1-x0)**2+(y1-y0)**2<=D**2:
        E[i]+=[j]
        E[j]+=[i]
E2=[]
for i in range(n):
  E2+=[set(E[i])]
for i in range(n):
  for j in range(n):
    if E2[i] & E2[j]!=set():
      E2[i]=E2[i]|E2[j]
      E2[j]=E2[i]|E2[j]
#print(E2)
E3=sorted(E2[0])
for i in range(n):
  if i in E3:
    print('Yes')
  else:
    print('No')
    
####################################
#TLE

n,D=map(int,input().split())
XY=[]
for i in range(n):
  x,y=map(int,input().split())
  XY+=[(x,y)]
#print(XY)
E=[]
for i in range(n):
  E+=[set([i])]
#print(E)
for i in range(n):
  for j in range(n):
    if i!=j:
      (x0,y0)=XY[i]
      (x1,y1)=XY[j]
      if (x1-x0)**2+(y1-y0)**2<=D**2:
        E[i].add(j)
        E[j].add(i)

for i in range(n):
  for j in range(n):
    if E[i] & E[j]!=set():
      E[i]=E[i]|E[j]
      E[j]=E[i]|E[j]
#print(E2)
E3=sorted(E[0])
for i in range(n):
  if i in E3:
    print('Yes')
  else:
    print('No')

####################################
#TLE

import sys
input = sys.stdin.readline
n,D=map(int,input().split())
XY=[]
for i in range(n):
  x,y=map(int,input().split())
  XY+=[(x,y)]
E=[]
for i in range(n):
  E+=[set([i])]
for i in range(n):
  for j in range(i+1,n):
    (x0,y0)=XY[i]
    (x1,y1)=XY[j]
    if (x1-x0)**2+(y1-y0)**2<=D**2:
      E[i].add(j)
      E[j].add(i)
      
for k in range(2):
  for i in range(n):
    for j in range(i+1,n):
      if E[i] & E[j]!=set():
        E[i],E[j]=E[i]|E[j],E[i]|E[j]
 
E3=list(E[0])
for i in range(n):
  if i in E3:
    print('Yes')
  else:
    print('No')
    
####################################
#titia

N,D=map(int,input().split())
XY=[list(map(int,input().split())) for i in range(N)]
E=[[] for i in range(N)]
for i in range(N):
    for j in range(i):
        a,b=XY[i]
        c,d=XY[j]
        if (a-c)**2+(b-d)**2<=D*D:
            E[i].append(j)
            E[j].append(i)
#print(E)#各ポイントの近隣

Q=[0]#0とついながっているところ、作業用
USED=[0]*N
USED[0]=1#0とついながっているところ、結果蓄積用
 
while Q:#要素がなくなるまで
  x=Q.pop()#右端を出す
  for to in E[x]:#E[0]と繋がった各要素to、USEDとQに加えるべき
    if USED[to]==0:#toはまだカウントされていない
      USED[to]=1#toをカウントした
      Q.append(to)#to各要素をQに加える、次段階でtoと繋がった要素をリストアップ

for i in range(N):
    if USED[i]==0:
        print("No")
    else:
        print("Yes")
    
####################################
