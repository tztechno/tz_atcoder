
```
############################################

############################################

############################################

[myans AC]

N,S = map(int,input().split())
A = list(map(int,input().split()))

B = [0]
for a in A:
  B+ = [B[-1]+a]

SUM = B[-1]
S% = SUM
C = set(B)#累積和

for b in B:
  if (S+b)%SUM in C:  #(S+B[i])%SUM==B[j] #inを使えばi,j不要
    print("Yes")
    exit()

print("No")

############################################

[myans TLE]

N,S=map(int,input().split())
A=list(map(int,input().split()))
B=[0]
C=[0]
for i in range(N):
  B+=[B[-1]+A[i]]
  C+=[C[-1]+A[N-1-i]]
sa=B[-1]  
D=set()
for b in B:
  for c in C:
    D.add((b+c)%sa)
if S%sa in D:
  print('Yes')
else:
  print('No')

-------------------------------------

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
