##############################################
##############################################


##############################################


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




