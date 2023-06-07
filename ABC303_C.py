########################################
#TLE

n,m,h,k=map(int,input().split())
S=list(input())#移動方法

XY=[]
for i in range(m):
  x,y=map(int,input().split())
  XY+=[[x,y]]

 
def position(S):
  P=[[0,0]]
  for s in S:
    PX=P[-1]
    #print(PX)
    if s=='R':
      PX=[PX[0]+1,PX[1]]
      #print(PX)
      P+=[PX]
    elif s=='L':
      PX=[PX[0]-1,PX[1]]
      P+=[PX]
    elif s=='U':
      PX=[PX[0],PX[1]+1]
      P+=[PX]    
    elif s=='D':
      PX=[PX[0],PX[1]-1]
      P+=[PX]
  return P
 
P=position(S) #軌跡を作る
#print(P)
 
pw=h          
for pi in P[1:]:
  pw-=1
  if pw<0:
    print('No')
    exit()
  if pi in XY and pw<k:
    pw=k
  #print(pw)
print('Yes')

########################################
