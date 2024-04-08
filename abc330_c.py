//abc330_c.py
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
[mobile]

from math import sqrt
d = int(input())

ans = float("inf")
for x in range(1, d+1):
    if x**2 > d:
        break

    y = int(sqrt(d - x**2))
    ans = min(ans, abs(x**2+y**2-d))
    ans = min(ans, abs(x**2+(y+1)**2-d))

print(ans)
#######################################
[titia]

import sys
input = sys.stdin.readline

n=int(input())

ANS=n

for x in range(2000020):
    MIN=0
    MAX=2000000

    while MAX>MIN+5:
        mid1=MIN+(MAX-MIN)//3
        mid2=MIN+(MAX-MIN)//3*2

        a1=abs(x*x+mid1*mid1-n)
        a2=abs(x*x+mid2*mid2-n)

        if a1<a2:
            MAX=mid2
        else:
            MIN=mid1

    for y in range(MIN,MAX+1):
        ANS=min(ANS,abs(x*x+y*y-n))

print(ANS)
#######################################
[my TLE ans]

import math
d=int(input())
ANS=10**9
d2=int(math.sqrt(d))+1
for x in range(d2):
  for y in range(d2):
    z=x**2+y**2
    ANS=min(abs(d-z),ANS)
print(ANS)
#######################################
