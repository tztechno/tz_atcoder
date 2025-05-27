##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[my TLE,WA]

N=int(input())
A=list(map(int,input().split()))
#print(A)
B=''
for i in range(N-1):
  if A[i]<A[i+1]:
    B+='i'
  else:
    B+='d'
#print(B)
from itertools import product,permutations,combinations,accumulate
C0=combinations(list(range(N)),2)
d=0
for ci in C0:
  t=B[ci[0]:ci[1]]
  di=0
  id=0
  for i in range(len(t)-1):
    if t[i:i+2]=='di':
      di+=1
    elif t[i:i+2]=='id':
      id+=1
  if di==1 and id==1:
    d+=1
print(d)
    
##################################################################
[my TLE,WA]
# the condition that number of each part be one is ignored. 

N=int(input())
A=list(map(int,input().split()))
#print(A)
B=''
for i in range(N-1):
  if A[i]<A[i+1]:
    B+='i'
  else:
    B+='d'
#print(B)
from itertools import product,permutations,combinations,accumulate
C0=combinations(list(range(N)),2)
d=0
for ci in C0:
  t=B[ci[0]:ci[1]]
  if 'id' in t and 'di' in t:
    d+=1
print(d)
    
##################################################################
[torugam]

N = int(input())
P = list(map(int,input().split()))

hash = []
for i in range(len(P)-1):
    if P[i]<P[i+1]:
        hash.append("<")
    else:
        hash.append(">")

run_length = []
value = hash[0]
index = 0
for i in range(1,len(hash)):
    if value == hash[i]:
        continue
    else:
        run_length.append((value,i-index))
        value = hash[i]
        index = i
else:
    run_length.append((value,len(hash)-index))

# print(hash)
# print(run_length)

count = 0
before = 0
for i in range(len(run_length)):
    if run_length[i][0] == "<":
        count += before*run_length[i][1]
        before = run_length[i][1]
print(count)
##################################################################
[karu HIGH]

ans = 0
n = int(input())
a = [*map(int, input().split())] + [-1]
b, c = 0, 0
for i in range(n):
    if a[i + 1] > a[i]:
        c += 1
    elif c > 0:
        ans += c * b
        b, c = c, 0
print(ans)
##################################################################

[titia]

import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

LIST=[0]*n

for i in range(1,n-1):
    if A[i-1]<A[i] and A[i]>A[i+1]:
        LIST[i]=1
    if A[i-1]>A[i] and A[i]<A[i+1]:
        LIST[i]=-1

#print(LIST)

X=[(0,10)]

for i in range(n):
    if LIST[i]==1:
        X.append((i,1))
    elif LIST[i]==-1:
        X.append((i,-1))

X.append((n-1,10))

ANS=0
for i in range(1,len(X)):
    if X[i][1]==1:
        if i+2<len(X):
            ANS+=(X[i][0]-X[i-1][0])*(X[i+2][0]-X[i+1][0])

print(ANS)
##################################################################

