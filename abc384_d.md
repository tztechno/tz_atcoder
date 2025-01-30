
```
############################################

############################################

############################################

############################################

[myans TLE]

N,S=map(int,input().split())
A=list(map(int,input().split()))
sa=sum(A)
for i in range(N):
  for j in range(N):
    a=sum(A[i:])
    b=sum(A[:j])
    if a+b==S%sa or a+b==S%sa+sa:
      print('Yes')
      exit()
else:
  print('No')

############################################

[titia]

import sys
input = sys.stdin.readline

N,S=map(int,input().split())
A=list(map(int,input().split()))

SUM=[0]
for a in A:
    SUM.append(SUM[-1]+a)

SUM0=SUM[-1]
S%=SUM0

for a in A:
    SUM.append(SUM[-1]+a)
for a in A:
    SUM.append(SUM[-1]+a)

SET=set(SUM)
for a in SUM:
    if S+a in SET:
        print("Yes")
        exit()

print("No")

############################################

```
