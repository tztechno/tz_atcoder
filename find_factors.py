def find_factors(n):
    """
    整数nの因数を求める関数。n=a*bとなる(a,b)の組み合わせを返す。
    """
    factors = []
    for a in range(1, int(n**0.5)+1):
        if n % a == 0:
            b = n // a
            factors.append((a, b))
    return factors
