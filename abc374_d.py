abc374_d.py
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
[my WA]

from itertools import permutations
import math
n,S,T=map(int,input().split())
P=[]
for i in range(n):
  a,b,c,d=map(int,input().split())
  P+=[[(a,b),(c,d)]]

def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

TIME=10**9
N=list(range(n))
L=list(permutations(N))
for li in L:
  time=0
  P1=(0,0)
  for bit in range(n):
    D=P[li[bit]]
    if bit & (1<<i):
      time+=dist(P1,D[0])/S
      time+=dist(D[0],D[1])/T
      P1=D[1]
    else:
      time+=dist(P1,D[1])/S
      time+=dist(D[1],D[0])/T
      P1=D[0]
  TIME=min(TIME,time)
  
print(TIME)


########################################################################################
[almost undestand][手本]
---------------------------------------------------------
if bit & (1<<i): の条件は、2進数で表したときに bit の i 番目のビットが 1であるかどうか をチェックしています。
bit & (1<<i) は、bit の2進数表現の i番目 のビットが 1 である場合に真 (True) となり、0 であれば偽 (False) となります。
---------------------------------------------------------

from itertools import permutations
import math

inf=float("inf")
N,S,T=map(int,input().split())
L=[]
for i in range(N):
    a,b,c,d=map(int,input().split())
    L.append([a,b,c,d])
#print(L)

def dis(x0,y0,x1,y1):
    res=math.sqrt((x0-x1)**2+(y0-y1)**2)
    return res

ans=inf
for p in list(permutations(range(N))):   ######
#    print(p)
    for bit in range(1<<N):
        x,y=0,0
        s=0
        for i in range(N):
            a,b,c,d=L[p[i]]
            if bit & (1<<i):   ######
                s+=dis(x,y,c,d)/S
                s+=dis(a,b,c,d)/T
                x,y=a,b
            else:
                s+=dis(x,y,a,b)/S
                s+=dis(a,b,c,d)/T
                x,y=c,d
        ans=min(ans,s)
print(ans)

########################################################################################
[not understand]

import sys
input = sys.stdin.readline
from itertools import permutations

N,S,T=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
L=list(permutations(range(N)))
ANS=1<<63

for LIST in L:
    score=0
    for j in range(2**N):
        score=0
        for i in range(len(LIST)):    
            if i==0:
                z,w=0,0
            else:
                if j & (1<<(i-1)) != 0:
                    z,w=A[LIST[i-1]][2:]
                else:
                    z,w=A[LIST[i-1]][:2]

            if j & (1<<i) != 0:
                a,b,c,d=A[LIST[i]]
            else:
                c,d,a,b=A[LIST[i]]

            score+=(((c-a)**2+(d-b)**2)**(1/2))/T
            score+=(((z-a)**2+(w-b)**2)**(1/2))/S

        #print(score)

        if ANS>score:
            ANS=score

print(ANS)

########################################################################################
[my WA]

import math
from itertools import permutations
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

n,S,T=map(int,input().split())
N=list(range(n))
P=[]
TIME=0
for i in range(n):
  a,b,c,d=map(int,input().split())
  P+=[[(a,b),(c,d)]]
  TIME+=euclidean_distance((a,b),(c,d))/T #on razor
#print(TIME)  

L=list(permutations(N))
V=[]
for i in range(2**n):
  b=bin(i)[2:].zfill(n)
  V+=[b]
  
TIME3=10**9
for li in L:#線分の順番
  for vi in V:#向のパターン
    R=[[(0,0)]]
    TIME2=TIME
    for i,vii in enumerate(list(vi)):
      #print(P[i])
      if vii=='0':
        TIME2+=euclidean_distance(R[-1][-1],P[i][0])/S
        R+=[P[i]]
      else:
        TIME2+=euclidean_distance(R[-1][-1],P[i][1])/S
        R+=[P[i][::-1]]
    #print(TIME2)
    TIME3=min(TIME3,TIME2)
print(TIME3)  

########################################################################################
