
def prime_factorization(n):
  
    factors = {}
    # 2で割り切れるだけ割り続ける
    while n % 2 == 0:
        if 2 not in factors:
            factors[2] = 1
        else:
            factors[2] += 1
        n = n // 2

    # 奇数の素因数を調べる
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors[i] = 1
            else:
                factors[i] += 1
            n = n // i

    # nが素数の場合
    if n > 2:
        factors[n] = 1

    return factors

# 使用例
number = 36
result = prime_factorization(number)
print(f"{number} の素因数分解: {result}")
