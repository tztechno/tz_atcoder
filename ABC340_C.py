


###############################################
###############################################
###############################################
###############################################
###############################################
n=int(input())
k=0
while 2**k < n:
  k+=1
print(n * k - (2 ** k - n))
###############################################
def calc(x):
    if x < 2:
        return 0
    if x in mp:
        return mp[x]
    mp[x] = calc(x // 2) + calc((x + 1) // 2) + x
    return mp[x]

mp = {}

n = int(input())
print(calc(n))
###############################################
import sys
from collections import defaultdict

def input():
    return (sys.stdin.readline()).rstrip()
    
def devide(n):
    if d[n]!=-1:
        pass
    elif n==2:
        d[n]=2
    elif n==3:
        d[n]=devide(2)+3
    elif n%2==0:
        d[n]=devide(n//2)*2+n
    else:
        d[n]=devide(n//2)+devide((n//2)+1)+n
    return d[n]

result=int()
#s=input()
n=int(input())
#h,w=map(int,input().split())
#a=list(map(int,input().split()))
d=defaultdict(lambda:-1)
result=devide(n)
print(result)
###############################################
import sys
input = sys.stdin.readline

n=int(input())
from functools import lru_cache
@lru_cache(maxsize=None)

def calc(n):
    if n<=1:
        return 0
    return n+calc(n//2)+calc((n+1)//2)

print(calc(n))
###############################################
