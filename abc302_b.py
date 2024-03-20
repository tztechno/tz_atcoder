##################################################
##################################################
##################################################
import sys
input = sys.stdin.readline

H,W=map(int,input().split())
S=[input().strip() for i in range(H)]

snuke="snuke"

DX=[0,0,1,-1,1,1,-1,-1]
DY=[1,-1,0,0,1,-1,1,-1]

for i in range(H):
    for j in range(W):
        x,y=i,j

        for d in range(8):
            for k in range(5):
                if 0<=x+DX[d]*k<H and 0<=y+DY[d]*k<W and S[x+DX[d]*k][y+DY[d]*k]==snuke[k]:
                    pass
                else:
                    break
            else:
                for k in range(5):
                    print(x+DX[d]*k+1,y+DY[d]*k+1)
                exit()

##################################################
h,w=map(int,input().split())
N=["s", "n", "u", "k", "e" ]
X=[0,1,1,1,0,-1,-1,-1]
Y=[1,1,0,-1,-1,-1,0,1]
S=[input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        Stc=[]
        for k in range(8):
            for l in range(5):
                if 0<=i+X[k]*l<h and 0<=j+Y[k]*l<w:
                    Stc.append(S[i+X[k]*l][j+Y[k]*l])
            if Stc==N:
                for l in range(5):
                    print(i+X[k]*l+1,j+Y[k]*l+1)
            Stc = []
##################################################
h, w = map(int, input().split())
s = [""]*h
for i in range(h):
    s[i] = input()

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

for i in range(h):
    for j in range(w):
        for d in range(8):
            t = ""
            x, y = j, i
            for _ in range(5):
                t += s[y][x]
                x += dx[d]
                y -= dy[d]
                if x < 0 or w <= x or y < 0 or h <= y:
                    break
            if t == "snuke":
                x, y = j, i
                for _ in range(5):
                    print(y+1, x+1)
                    x += dx[d]
                    y -= dy[d]
##################################################
H,W=map(int,input().split())
S=[]
K=[]
for i in range(H):
  s=list(input())
  S+=[s]
  for j in range(W):
    if s[j]=='s':
      K+=[(i,j)]
      
#print(K)
R1=[(0,0),(0,1),(0,2),(0,3),(0,4)]
R2=[(0,0),(0,-1),(0,-2),(0,-3),(0,-4)]
V1=[(0,0),(1,0),(2,0),(3,0),(4,0)]
V2=[(0,0),(-1,0),(-2,0),(-3,0),(-4,0)]
D1=[(0,0),(1,1),(2,2),(3,3),(4,4)]
D2=[(0,0),(-1,-1),(-2,-2),(-3,-3),(-4,-4)]
E1=[(0,0),(1,-1),(2,-2),(3,-3),(4,-4)]
E2=[(0,0),(-1,1),(-2,2),(-3,3),(-4,4)]

Name=list('snuke')
for k in K:
  for rv in [R1,R2,V1,V2,D1,D2,E1,E2]:
    flag=1
    for i,r in enumerate(rv):
      if k[0]+r[0]>=H or k[1]+r[1]>=W or k[0]+r[0]<0 or k[1]+r[1]<0 or S[k[0]+r[0]][k[1]+r[1]]!=Name[i]:
        flag=0
        break
    if flag==1:
      #print(k[0]+1,k[1]+1)
      for r in rv:
        print(k[0]+r[0]+1,k[1]+r[1]+1)
##################################################
