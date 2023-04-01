
def pair_factors(n):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    factors = sorted(set(factors))
    C0=[]
    for i in range(len(factors)//2):
        C0+=[(factors[i],factors[-i-1])]
    if len(factors) % 2 == 1:
        C0+=[(factors[len(factors)//2],factors[len(factors)//2])]
    return C0
  
