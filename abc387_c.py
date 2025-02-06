#################################################
#################################################
#################################################
#################################################
[titia]

import sys
input = sys.stdin.readline

#L,R=map(int,input().split())

def calc(x):
    ANS=0
    for keta  in range(1,19):
        for head in range(1,10):
            #print(head*(10**keta),ANS)
            if x//(10**keta)<head:
                break

            elif x//(10**keta)>head:
                #print("!?",x,(head+1)*(10**keta))
                ANS+=head**keta
            else:
                #print("!!",keta,head,ANS)
                flag=1
                S=str(x)
                for j in range(1,len(S)):
                    p=int(S[j])
                    #print(p,head,keta,j,min(head,p)**(keta+1-j),ANS)

                    ANS+=min(head,p)*(head**(keta-j))

                    if p>=head:
                        flag=0
                        break

                    #print(ANS)

                if hebi(x):
                    ANS+=1

    return ANS

def hebi(x):
    if x==0:
        return 0
    S=str(x)
    head=int(S[0])

    for i in range(1,len(S)):
        if head<=int(S[i]):
            return False

    return True

def calc2(x):
    ANS=0
    for i in range(10,x+1):
        if hebi(i)==True:
            ANS+=1
    return ANS

L,R=map(int,input().split())

print(calc(R)-calc(L-1))

for i in range(1,1010):
    #print(i)
    assert calc(i)==calc2(i)
        
    

#################################################
#################################################
#################################################
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

ans=0
for i in range(l,r+1):
  X=list(str(i))
  t=1
  for xi in set(X[1:]):
    if X[0]<=xi:
      t=0
      break
  ans+=t
print(ans)
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

ans=0
for i in range(l,r+1):
  X=list(str(i))
  if X[0]>max(set(X[1:])):
    ans+=1
print(ans)
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

def judge(x):
  X=list(str(x))
  t=int(X[0])
  S=set(X[1:])
  if t>int(max(S)):
    return 1
  else:
    return 0

ans=0
for i in range(l,r+1):
  ans+=judge(i)
print(ans)
#################################################
[my TLE]

import sys
input = sys.stdin.readline
l,r=map(int,input().split())

from collections import defaultdict,deque,Counter

def judge(x):
  X=list(str(x))
  C=Counter(X)
  mx=max(C.keys())
  if C[mx]==1 and X[0]==str(mx):
    return 1
  else:
    return 0

ans=0
for i in range(l,r+1):
  ans+=judge(i)
print(ans)
#################################################

