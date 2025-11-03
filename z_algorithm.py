def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    i, j = 1, 0
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i, j = i + k, max(j - k, 0)
    return z

T = int(input())
for _ in range(T):
    A = input().strip()
    B = input().strip()
    s = B + "$" + A * 2
    z = z_algorithm(s)
    
    result = -1
    for i in range(len(B) + 1, len(s)):
        if z[i] >= len(B):
            result = i - len(B) - 1 
            break
    print(result)
