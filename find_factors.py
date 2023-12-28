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


def prime_factorization(n):
    factors = []
    # 2で割り切れる限り割り続ける
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # 3以上の奇数で割り切れる限り割り続ける
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # nが素数の場合
    if n > 2:
        factors.append(n)

    return factors
