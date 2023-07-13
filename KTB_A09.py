#KTB_A09
#stpete solution

H,W,N=map(int,input().split())
A=[]
for i in range(N):
  y0,x0,y1,x1=map(int,input().split())
  A+=[(y0,x0,y1,x1)]
S=[]
for i in range(H+1):
  S+=[[0]*(W+1)]
#print(S)
T=S.copy()
#UL(y0,x0)
#DL(y1,x0)
#UR(y0,x1)
#DR(y1,x1)
for i in range(N):
  (y0,x0,y1,x1)=A[i]
  S[y0-1][x0-1]+=1
  S[y1][x0-1]-=1
  S[y0-1][x1]-=1
  S[y1][x1]+=1
#print(S)
for i in range(1,H+1):
  for j in range(W+1):
    T[i][j]=T[i-1][j]+S[i][j]
#print(T)    
for i in range(H+1):
  for j in range(1,W+1):
    T[i][j]=T[i][j-1]+T[i][j]
#print(T)    
for i in range(H):
  print(*T[i][0:W])
  
