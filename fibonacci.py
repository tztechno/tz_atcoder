#########################################################
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#########################################################

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 50
memo_dict = {}
result = fibonacci(n, memo_dict)
print(f"Result: {result}")
print(f"Memo: {memo_dict}")

#########################################################
