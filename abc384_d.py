############################################
[myans TLE]

import sys
input = sys.stdin.readline
N,S=map(int,input().split())
A=list(map(int,input().split()))
suma=sum(A)
R=S%suma
V=set()
AR=A[::-1]
AF=[0]
AB=[0]
for a in A:
  AF+=[AF[-1]+a]
for ar in AR:
  AB+=[AB[-1]+ar]
for af in set(AF):
  for ab in set(AB):
    if R==(ab+af)%suma:
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
############################################
############################################
############################################
