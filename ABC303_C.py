########################################
#WA,TLE

import sys
input = sys.stdin.readline

n,m,h,k=map(int,input().split())
S=list(input())

XY=[]
for i in range(m):
  x,y=map(int,input().split())
  XY+=[[x,y]]

def position(S):
  P=[[0,0]]
  for s in S:
    PX=P[-1]
    if s=='R':
      PX=[PX[0]+1,PX[1]]
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
 
P=position(S)
 
pw=h          
for pi in P[1:]:
  pw-=1
  if pw<0:
    print('No')
    exit()
  elif pi in XY and pw<k:
    pw=k
print('Yes')

########################################
#titia

import sys
input = sys.stdin.readline
 
N,M,H,K=map(int,input().split())
S=input().strip()
 
P=set([tuple(map(int,input().split())) for i in range(M)])
 
x=0
y=0
 
for s in S:
    if s=="R":
        x+=1
    elif s=="L":
        x-=1
    elif s=="U":
        y+=1
    elif s=="D":
        y-=1
 
    H-=1
 
    if H<0:
        print("No")
        exit()
 
    if (x,y) in P and H<K:
        H=K
        P.remove((x,y))
 
if H>=0:
    print("Yes")
else:
    print("No")
########################################
