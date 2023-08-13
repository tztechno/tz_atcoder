 def rolling_hash(s):
    n = len(s)
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(n):
        h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
        p[i+1] = p[i] * BASE % MOD
    return h, p
