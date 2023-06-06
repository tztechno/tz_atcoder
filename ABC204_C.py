##################
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
##################
