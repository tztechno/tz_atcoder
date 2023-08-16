######################################################################

import math
def combination(n, r):
    if r > n:
        return 0
    else:
        mod = 10**9 + 7
        return  math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) % mod

######################################################################

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(n, r):
    if r > n:
        return 0
    else:
        mod = 10**9 + 7
        return factorial(n) // (factorial(n-r) * factorial(r)) % mod

######################################################################
