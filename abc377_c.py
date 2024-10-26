#####################################################
#####################################################
#####################################################
[my TLE]

import sys
input = sys.stdin.readline

N,M=map(int,input().split())

def BI(P):
  i=P[0]-1
  j=P[1]-1
  OUT=set([(i,j),(i+2,j+1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i-2,j-1),(i-1,j-2),(i+1,j-2),(i+2,j-1)])
  return OUT

OUT2=set()
for i in range(M):
  a,b=map(int,input().split())
  OUT2=OUT2|BI((a,b))
  
OUT3=set()
for p in OUT2:
  if 0<=p[0]<N and 0<=p[1]<N:
    OUT3.add(p)
print(N*N-len(OUT3))


#####################################################
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

SET=set()

for i in range(M):
    a,b=map(int,input().split())
    SET.add((a,b))

    for x,y in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
        if 1<=a+x<=N and 1<=b+y<=N:
            SET.add((a+x,b+y))

print(N*N-len(SET))
#####################################################
