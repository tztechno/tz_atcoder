# 部分集合を列挙する

from itertools import chain, combinations

def enumerate_subsets(s):
    # 元の集合の要素をリスト化
    elements = list(s)
    n = len(elements)
    # 空集合を含むために range(n + 1) としている
    for r in range(n + 1):
        # itertools.combinations を使って r 個の要素からなる部分集合を列挙
        for subset in combinations(elements, r):
            yield set(subset)

# テスト用の集合
my_set = {1, 2, 3}
# 部分集合を列挙
for subset in enumerate_subsets(my_set):
    print(subset)


#############################################################
#abc180_c [WA]

n=int(input())

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
    
F=prime_factorization(n)
#print(F)

#集合の部分集合を網羅的に作る
from itertools import chain, combinations

def all_subsets(s_list):
    "集合 s のすべての部分集合を生成する"
    return list(chain.from_iterable(combinations(s_list, r) for r in range(len(s_list) + 1)))

subsets = all_subsets(F)
#print(set(subsets))

for s in set(subsets):
  ans=1
  for si in s:
    ans*=si
  print(ans)
