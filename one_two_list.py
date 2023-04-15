#1,2のリストで合計がn-1になるケースをリストアップする
#original

from itertools import permutations

AB=[]
for a in range(n-1):
  for b in range(n-1):
    if a+b*2==n-1:
      AB+=[(a,b)]
print(AB)

C0=[]
for abi in AB:
  P=[]
  a=abi[0]
  b=abi[1]
  P+=[1]*a+[2]*b
  C0+=list(permutations(P))
C2=list(set(C0))
print(C2)
