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
