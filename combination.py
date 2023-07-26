def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    if r > n:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n-r))

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

