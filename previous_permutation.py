def previous_permutation(n, p):
    for i in range(n - 1, 0, -1):
        if p[i - 1] > p[i]:
            for j in range(n - 1, i - 1, -1):
                if p[j] < p[i - 1]:
                    p[i - 1], p[j] = p[j], p[i - 1]
                    p[i:] = reversed(p[i:])
                    return p
