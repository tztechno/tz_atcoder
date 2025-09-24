###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[AC]
import sys
from collections import Counter

# ---------- utilities ----------
def iter_ints():
    for tok in sys.stdin.read().strip().split():
        yield int(tok)

def prime_factorize(n: int):
    n0 = n
    fac = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac

# convert exponent vector -> mixed-radix index, and prepare multipliers
def prepare_mixed_radix(max_exps):
    r = len(max_exps)
    mult = [1]*r
    for i in range(1, r):
        mult[i] = mult[i-1] * (max_exps[i-1] + 1)
    S = mult[-1] * (max_exps[-1] + 1) if r>0 else 1
    return mult, S

def vec_to_index(vec, mult):
    return sum(v * m for v, m in zip(vec, mult))

def index_to_vec(idx, max_exps, mult):
    # decode idx into vector of exponents
    r = len(max_exps)
    vec = [0]*r
    for i in range(r):
        base = max_exps[i] + 1
        vec[i] = (idx // mult[i]) % base
    return vec

# ---------- main ----------
def main():
    it = iter_ints()
    try:
        N = next(it)
        X = next(it)
    except StopIteration:
        return

    # read bags
    bags = []
    for _ in range(N):
        Li = next(it)
        arr = [next(it) for _ in range(Li)]
        bags.append(arr)

    # factorize X
    if X == 0:
        print(0)
        return
    fac = prime_factorize(X)
    primes = list(fac.keys())
    max_exps = [fac[p] for p in primes]  # E_t

    r = len(primes)
    if r == 0:
        # X == 1
        # we must choose one ball from each bag, product of chosen numbers must be 1.
        # Since ai,j >=1, only choices with all chosen values ==1 count.
        ans = 1
        for arr in bags:
            ans *= sum(1 for v in arr if v == 1)
        print(ans)
        return

    mult, S = prepare_mixed_radix(max_exps)

    # Precompute for each possible divisor-vector index its vector representation (for fast check)
    state_vecs = [index_to_vec(i, max_exps, mult) for i in range(S)]

    # For each bag, compute counts of index (exponent-vector) among its balls
    bag_idx_counts = []
    for arr in bags:
        cnt = Counter()
        for v in arr:
            if v == 0:
                continue
            if X % v != 0:
                continue
            # compute exponent vector of v wrt primes
            vv = v
            vec = []
            ok = True
            for i, p in enumerate(primes):
                c = 0
                while vv % p == 0:
                    vv //= p
                    c += 1
                if c > max_exps[i]:
                    ok = False
                    break
                vec.append(c)
            if not ok:
                continue
            if vv != 1:
                # v contains a prime not in X -> cannot be used
                continue
            idx = vec_to_index(vec, mult)
            cnt[idx] += 1
        bag_idx_counts.append(cnt)

    # DP over bags
    # dp[s] = number of ways to reach exponent-vector-state s after processing some bags
    dp = [0] * S
    dp[0] = 1  # start with zero exponents

    # Precompute for each possible idx its vector for quick access and also contribution (idx itself)
    idx_vec_cache = {}
    for bag_cnt in bag_idx_counts:
        # skip quick if a bag has no usable balls -> answer 0
        if not bag_cnt:
            print(0)
            return

    # For each bag, build newdp
    for cnt in bag_idx_counts:
        newdp = [0] * S
        # enumerate unique idx present in this bag
        items = list(cnt.items())  # (idx, count)
        # for each state, try each idx
        for s in range(S):
            val = dp[s]
            if val == 0:
                continue
            svec = state_vecs[s]
            for idx, c in items:
                # check overflow by vector addition
                # we can check components quickly
                # compute target index = s + idx if valid
                # but to compute new index without decoding idx vector each time, decode idx now
                if idx not in idx_vec_cache:
                    idx_vec_cache[idx] = index_to_vec(idx, max_exps, mult)
                ivec = idx_vec_cache[idx]
                ok = True
                # compute offset contribution quickly:
                offset = 0
                for j in range(r):
                    scomp = svec[j]
                    inc = ivec[j]
                    if scomp + inc > max_exps[j]:
                        ok = False
                        break
                    offset += inc * mult[j]
                if not ok:
                    continue
                newdp[s + offset] += val * c
        dp = newdp

    target_idx = S - 1  # all exponents == max -> this is target
    print(dp[target_idx])


if __name__ == "__main__":
    main()

###############################################
[AC]
import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx]); idx += 1
    X = int(data[idx]); idx += 1
    
    lists = []
    
    for _ in range(N):
        L = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+L])); idx += L
        lists.append(arr)
    
    # メモ化再帰で分割統治法
    from functools import lru_cache
    
    # 前半部分の計算
    def compute_first_half():
        products = defaultdict(int)
        
        def dfs(i, prod):
            if i == N // 2:
                products[prod] += 1
                return
            for num in lists[i]:
                if prod <= X // num:  # オーバーフロー防止
                    dfs(i + 1, prod * num)
        
        dfs(0, 1)
        return products
    
    # 後半部分の計算
    def compute_second_half():
        products = defaultdict(int)
        
        def dfs(i, prod):
            if i == N:
                products[prod] += 1
                return
            for num in lists[i]:
                if prod <= X // num:  # オーバーフロー防止
                    dfs(i + 1, prod * num)
        
        dfs(N // 2, 1)
        return products
    
    first = compute_first_half()
    second = compute_second_half()
    
    result = 0
    for p1, cnt1 in first.items():
        if X % p1 == 0:
            p2 = X // p1
            if p2 in second:
                result += cnt1 * second[p2]
    
    print(result)

if __name__ == "__main__":
    main()
###############################################
[AC]
N,X=map(int,input().split())
bags=[]
for i in range(N):
  b=list(map(int,input().split()))
  bags+=[b[1:]]
  
ans = 0

def dfs(i, prod):
    global ans
    if prod > X: return
    if i == N:
        if prod == X: ans += 1
        return
    for v in bags[i]:
        dfs(i+1, prod*v)

dfs(0, 1)
print(ans)

###############################################
[AC]
import itertools
import math

N,X=map(int,input().split())
bags=[]
for i in range(N):
  b=list(map(int,input().split()))
  bags+=[b[1:]]

count = 0
for combination in itertools.product(*bags):
  if math.prod(combination) == X:
    count += 1

print(count)

###############################################
