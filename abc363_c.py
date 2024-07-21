abc363_c.py
#################################################
[TLE]
from itertools import permutations

N, K = map(int, input().split())
S = list(input())

def is_non_palindromic(s, k):
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if substring == substring[::-1]:
            return False
    return True

unique_permutations = set(permutations(S))

count = 0
for perm in unique_permutations:
    if is_non_palindromic(perm, K):
        count += 1

print(count)
