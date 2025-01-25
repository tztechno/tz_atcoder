##############################################

from more_itertools import set_partitions

data = [1, 2, 3]
partitions = list(set_partitions(data))
print(partitions)

##############################################

[my TLE]

from more_itertools import set_partitions
N=int(input())
A=list(map(int,input().split()))
partitions = list(set_partitions(A))
B=set()
for parts in partitions:
  ans=0
  for p in parts:
    ans^=sum(p)
  B.add(ans)
print(len(B))

------------------------------------

from more_itertools import set_partitions
N=int(input())
A=list(map(int,input().split()))
B=set()
for parts in list(set_partitions(A)):
  ans=0
  for p in parts:
    s=0
    for pi in p:
      s+=pi
    ans^=s
  B.add(ans)
print(len(B))

##############################################

[shogo314]

from more_itertools import set_partitions

N = int(input())
A = list(map(int, input().split()))
s = []
for p in set_partitions(A):
    t = 0
    for x in p:
        y = 0
        for i in x:
            y += i
        t ^= y
    s.append(t)
print(len(set(s)))

##############################################

N = int(input())
A = list(map(int, input().split()))

stk = []
stk.append((0, []))

res = set()
while stk:
    idx, box = stk.pop()
    if idx == N:
        now = 0
        for b in box:
            now ^= b
        res.add(now)
        continue
    a = A[idx]
    for i in range(len(box)):
        b_2 = box[:]
        b_2[i] += a
        stk.append((idx + 1, b_2))
    box.append(a)
    stk.append((idx + 1, box))

print(len(res))

##############################################

import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

def calc(X,ind):
    if ind==len(A):
        ANS=0
        for a in X:
            ANS^=a
        LANS.append(ANS)
        return
    a=A[ind]

    for i in range(len(X)):
        X[i]+=a
        calc(X,ind+1)
        X[i]-=a

    X.append(a)
    calc(X,ind+1)
    X.pop()

LANS=[]
calc([],0)

print(len(set(LANS)))

##############################################

[my TLE]

import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

from itertools import product

def distribute_and_sum(numbers, num_boxes):
    all_distributions = []
    for boxes in product(range(num_boxes), repeat=len(numbers)):
        distribution = [0] * num_boxes  
        for num, box in zip(numbers, boxes):
            distribution[box] += num
        all_distributions.append(distribution)
    return all_distributions

distributions = distribute_and_sum(A, N)

D=set()
for dist in distributions:
  ans=0
  for d in dist:
    ans^=d
  D.add(ans)
#print(D)
print(len(D))

##############################################




