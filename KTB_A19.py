#######################################################
#stpete AC 
N,WL=map(int,input().split())
W=[0]
V=[0]
for i in range(N):
  w,v=map(int,input().split())
  W+=[w]
  V+=[v]
DP=[]
for i in range(N+1):
  DP+=[[0]*(WL+1)]
 
for i in range(1,N+1):
  for j in range(WL+1):
    if j-W[i]>=0:
      DP[i][j]=max(DP[i-1][j],DP[i-1][j-W[i]]+V[i])
    else:
      DP[i][j]=DP[i-1][j]
print(DP[N][WL])
#######################################################

#######################################################
