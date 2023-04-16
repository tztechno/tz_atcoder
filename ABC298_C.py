import sys
input = sys.stdin.readline
n=int(input())
q=int(input())
B=[]
for i in range(n+1):
  B+=[[]]
NUM=[]
for i in range(200001):
  NUM+=[set()]
for i in range(q):
  Q=list(map(int,input().split()))
  if Q[0]==1:
    i,j=Q[1],Q[2]
    B[j]+=[i]
    NUM[i].add(j)
  elif Q[0]==2:
    i=Q[1]
    print(*sorted(B[i]))
  elif Q[0]==3:
    i=Q[1]
    print(*sorted(list(NUM[i])))
