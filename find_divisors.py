def find_divisors(n):
    """
    整数nの約数をリストで返す関数。
    """
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors
