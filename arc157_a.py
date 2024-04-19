#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
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
