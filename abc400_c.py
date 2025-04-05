######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
[tomer]
from math import isqrt
N = int(input())
b=2
s=0
x= int(isqrt(N//b))
if (x+1)*(x+1)*b <= N:
    x+=1
s+=x
b=b<<1
x= int(isqrt(N//b))
if (x+1)*(x+1)*b <= N:
    x+=1
s+=x

print(s)
######################################################################
[miz]
from math import*
n=int(input())
print(isqrt(n>>1)+isqrt(n>>2))
######################################################################
[titia]
import sys
input = sys.stdin.readline

n=int(input())
ANS=0

for a in range(1,100):
    if 2**a>n:
        break
    else:
        OK=1
        NG=10**9
        while NG>OK+1:
            mid=(OK+NG)//2
            if (2**a)*(mid**2)<=n:
                OK=mid
            else:
                NG=mid
        ANS+=(OK+1)//2

print(ANS)

######################################################################
[AC]
import math

def count_good_integers(N):
    count = 0
    max_k = math.floor(math.log2(N))
    for k in range(1, max_k + 1):
        max_t = math.isqrt(N // (2 ** k))
        count += (max_t + 1) // 2
    return count

N=int(input())
print(count_good_integers(N))
######################################################################
[TLE]
import math

def count_good_integers(N):
    seen = set()
    max_b = int(math.isqrt(N)) + 1
    for b in range(1, max_b + 1):
        b_squared = b * b
        if b_squared > N:
            continue
        max_power = N // b_squared
        a = 1
        while True:
            power_of_two = 2 ** a
            if power_of_two > max_power:
                break
            x = power_of_two * b_squared
            seen.add(x)
            a += 1
    return len(seen)

N = int(input())
print(count_good_integers(N))
######################################################################
[TLE]
def count(N):
    seen = set()
    b = 1
    while True:
        b_squared = b * b
        if 2 * b_squared > N:
            break
        max_k = N // b_squared
        max_power = 1 << (max_k.bit_length() - 1)
        if max_power > max_k:
            max_power >>= 1
        power = 2
        while power <= max_k:
            seen.add(power * b_squared)
            power <<= 1
        b += 1
    return len(seen)

N = int(input())
print(count(N))
######################################################################
[TLE]
def count(N):
    good_numbers = set()
    b = 1
    while True:
        b_squared = b * b
        if b_squared > N:
            break
        x = b_squared * 2  
        while x <= N:
            good_numbers.add(x)
            x *= 2
        b += 1
    return len(good_numbers)

N = int(input())
print(count(N))
######################################################################
