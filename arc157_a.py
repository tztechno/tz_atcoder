#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
[eijiro]

n, a, b, c, d = map(int, input().split())

if b == c == 0 and a and d:
    print("No")
elif abs(b - c) <= 1:
    print("Yes")
else:
    print("No")
    
#####################################################
[titia]

N,A,B,C,D=map(int,input().split())

if abs(B-C)>1:
    print("No")
elif B==C==0:
    if A==N-1 or D==N-1:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")

#####################################################
[MY TLE16 ANS]

import sys
input = sys.stdin.readline
from itertools import permutations

n,a,b,c,d=map(int,input().split())
counts = {'A': a, 'B': b, 'C': c, 'D': d}
chars = []
for char, count in counts.items():
    chars.extend([char] * count)
perms = permutations(chars)

for perm in perms:
    p=set()
    for i,j in zip(perm[0:-1],perm[1:]):
      p.add(i+j)
    bads=set(['AC','AD','BA','BB','CC','CD','DA','DB'])
    if p & bads ==set():
      print('Yes')
      exit()
else:
  print('No')
#####################################################
[MY TLE16 ANS]

from itertools import permutations
n,a,b,c,d=map(int,input().split())
counts = {'A': a, 'B': b, 'C': c, 'D': d}
chars = []
for char, count in counts.items():
    chars.extend([char] * count)
perms = permutations(chars)
bads=['AC','AD','BA','BB','CC','CD','DA','DB']
for perm in perms:
    p=''.join(perm)
    #print(p)
    flag=1
    for bad in bads:
      if bad in p:
        flag=0
        break
    if flag==1:
      print('Yes')
      exit()

else:
  print('No')
#####################################################
[MY TLE19 ANS]

from itertools import permutations
n,a,b,c,d=map(int,input().split())
counts = {'A': a, 'B': b, 'C': c, 'D': d}
chars = []
for char, count in counts.items():
    chars.extend([char] * count)
#print(chars)
perms = permutations(chars)
P=[]
bads=['AC','AD','BA','BB','CC','CD','DA','DB']
for perm in perms:
    p=''.join(perm)
    #print(p)
    flag=1
    for bad in bads:
      if bad in p:
        flag=0
        break
    if flag==1:
      P+=[p]
      #print(p)
#print(P)
if len(P)>0:
  print('Yes')
else:
  print('No')
#####################################################
