//ABC304_C virus 

########################################
########################################
N,D = map(int, input().split())
X_Y=[]
stack=[0]
for i in range (N):
    x,y=map(int, input().split())
    X_Y.append([x,y,"No"])
X_Y[0][2]="Yes"
while stack:
    now=stack.pop()
    now=X_Y[now]
    for i in range (N):
        if X_Y[i][2]=="Yes":
            pass
        elif (now[0]-X_Y[i][0])**2+(now[1]-X_Y[i][1])**2<=D**2:
            stack.append(i)
            X_Y[i][2]="Yes"

for i in X_Y:
    print(i[2])
########################################
N, D = map(int, input().split())
r = [[0, 0]]
for i in range(1, N + 1): r.append(list(map(int, input().split())))
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if (r[i][0] - r[j][0])**2 + (r[i][1] - r[j][1])**2 <= D**2:
            graph[i].append(j)
            graph[j].append(i)
seen = ["No" for _ in range(N + 1)]
seen[1] = "Yes"
stack = [1]
while len(stack) > 0:
    now = stack.pop()
    for i in graph[now]:
        if seen[i] == "No":
            seen[i] = "Yes"
            stack.append(i)
for i in range(1, N + 1): print(seen[i])
########################################
N, D = map(int, input().split())

people = []
for n in range(N):
  X, Y = map(int, input().split())
  people.append((X, Y))
  
from collections import deque

virus_queue = deque()
# 初期状態で人1が感染している
virus_queue.append(people[0])
virus_holder_set = {0}
dxx2 = D ** 2

while len(virus_queue) > 0:
  virus_holder = virus_queue.pop()
  vh_x, vh_y = virus_holder
  
  for i in range(len(people)):
    if i in virus_holder_set:
      continue

    person = people[i]
    x, y = person
    
    distance = (vh_x - x) ** 2 + (vh_y - y) ** 2
    if distance <= dxx2:
      virus_queue.append(person)
      virus_holder_set.add(i)

for i in range(len(people)):
  if i in virus_holder_set:
    print('Yes')
  else:
    print('No')

########################################

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
#MY ANS

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

ANS=[0]*n
ANS[0]=1
Q=list(E[0])
Q.remove(0)

C=[0]
while Q:
  x=Q.pop()
  if x not in C:
    C+=[x]
    for ei in list(E[x]):
      if ANS[ei]==0:
        ANS[ei]=1
        Q.append(ei)

for i in range(n):
  if ANS[i]==1:
    print('Yes')
  else:
    print('No')
       
####################################
