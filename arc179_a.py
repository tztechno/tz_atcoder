arc179_a.py
##############################################
##############################################
##############################################
##############################################
##############################################
[moon]
n,k,*a=map(int,open(0).read().split())
a.sort()
if k<=0:
  a=a[::-1]
b=[0]
for i in a:
  b+=b[-1]+i,
f=0
for i in b:
  if f and i<k:
    exit(print('No'))
  if i>=k:
    f=1
print('Yes')
##############################################
[wtm]
n, k = map(int, input().split())
a = list(map(int, input().split()))
sm=sum(a)
if k==0 and sm<0 or k<0 and sm<k:
    print('No')
else:
    is_rev=k<=sm
    a.sort(reverse=is_rev)
    print('Yes')
    print(*a)
##############################################
[shaka]
N,K=map(int,input().split())
A=[int(i) for i in input().split()]
def check(a):
    n=len(a)
    S=[0 for i in range(n+1)]
    for i in range(n):
        S[i+1]=S[i]+a[i]
    for i in range(n):
        if S[i]>=K and S[i+1]<K:
            return False
    return True

A.sort()
if check(A):
    print("Yes")
    print(*A)
else:
    A.sort(reverse=True)
    if check(A):
        print("Yes")
        print(*A)
    else:
        print("No")
##############################################
[titia]
import sys
input = sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

A.sort()
S=[0]
for a in A:
    S.append(S[-1]+a)

M=[]
P=[]
for i in range(len(S)):
    if S[i]<K:
        M.append(i)
    else:
        P.append(i)

if M==[] or P==[] or max(M)<min(P):
    print("Yes")
    print(*A)
    exit()

A.sort(reverse=True)
S=[0]
for a in A:
    S.append(S[-1]+a)

M=[]
P=[]
for i in range(len(S)):
    if S[i]<K:
        M.append(i)
    else:
        P.append(i)

if M==[] or P==[] or max(M)<min(P):
    print("Yes")
    print(*A)
    exit()

print("No")

##############################################
[double sorted pattern only AC]
N,K=map(int,input().split())
A=sorted(list(map(int,input().split())))
B=[A,A[::-1]]

def rightmost(lst, x):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < x:
            return i
    return -1  
    
def leftmost(lst, x):
    for i in range(len(lst)):
        if lst[i] >= x:
            return i
    return -1  

for b in B:
  x=[0]
  for i in range(N):
    x+=[x[-1]+b[i]]
  if rightmost(x, K)!=-1 and leftmost(x, K)!=-1 and rightmost(x, K)<leftmost(x, K):  
    print('Yes')
    print(*b)
    exit()
  elif rightmost(x, K)==-1 or leftmost(x, K)==-1:  
    print('Yes')
    print(*b)
    exit()
else:
  print('No')
##############################################
[sorted pattern only WA11]
N,K=map(int,input().split())
b=sorted(list(map(int,input().split())))

def rightmost(lst, x):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < x:
            return i
    return -1  
    
def leftmost(lst, x):
    for i in range(len(lst)):
        if lst[i] >= x:
            return i
    return -1  

x=[0]
for i in range(N):
  x+=[x[-1]+b[i]]
if rightmost(x, K)!=-1 and leftmost(x, K)!=-1 and rightmost(x, K)<leftmost(x, K):  
  print('Yes')
  print(*b)
  exit()
elif rightmost(x, K)==-1 or leftmost(x, K)==-1:  
  print('Yes')
  print(*b)
  exit()
else:
  print('No')
##############################################
[My Best TLE31]
from itertools import product,permutations,combinations,accumulate
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=set(list(permutations(A)))

def rightmost(lst, x):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < x:
            return i
    return -1  
    
def leftmost(lst, x):
    for i in range(len(lst)):
        if lst[i] >= x:
            return i
    return -1  

for b in B:
  x=[0]
  for i in range(N):
    x+=[x[-1]+b[i]]
  if rightmost(x, K)!=-1 and leftmost(x, K)!=-1 and rightmost(x, K)<leftmost(x, K):  
    print('Yes')
    print(*b)
    exit()
  elif rightmost(x, K)==-1 or leftmost(x, K)==-1:  
    print('Yes')
    print(*b)
    exit()
else:
  print('No')
##############################################
