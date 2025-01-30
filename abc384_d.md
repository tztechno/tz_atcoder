
```
############################################

############################################

############################################

############################################

[myans TLE]

N,S=map(int,input().split())
A=list(map(int,input().split()))
B=[0]
for a in A:
  B+=[B[-1]+a]
sa=B[-1]  

for i in range(N):
  for j in range(N):
    ab=sa-B[i]+B[j]
    if ab%sa==S%sa:
      print('Yes')
      exit()
else:
  print('No')

-----------------------------------------

N,S=map(int,input().split())
A=list(map(int,input().split()))
sa=sum(A)

for i in range(N):
  for j in range(N):
    ab=sum(A[i:])+sum(A[0:j])
    if ab%sa==S%sa:
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
