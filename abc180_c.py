
abc180_c.py
###################################################
###################################################
###################################################
###################################################
[shaka]
N=int(input())
X=set()
i=1
while(i*i<=N):
    if N%i==0:
        X.add(i)
        X.add(N//i)
    i+=1
Y=list(X)
Y.sort()
for i in Y:
    print(i)
###################################################
[titia]
import sys
input = sys.stdin.readline
N=int(input())
A=[]
for i in range(1,10**6+5):
    if N%i==0:
        A.append(i)
        A.append(N//i)
A=sorted(set(A))
print(*A)
###################################################
[My Ans TLE]

n=int(input())

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
    
F=prime_factorization(n)
#print(F)

#集合の部分集合を網羅的に作る
from itertools import chain, combinations

def all_subsets(s_list):
    return list(chain.from_iterable(combinations(s_list, r) for r in range(len(s_list) + 1)))

subsets = all_subsets(F)
#print(set(subsets))
ANS=[]
for s in set(subsets):
  ans=1
  for si in s:
    ans*=si
  ANS+=[ans]
ANS.sort()
for a in ANS:
  print(a)
###################################################
