##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[ai TLE]
import sys
input = sys.stdin.readline
from itertools import combinations

N,M=map(int,input().split())
X=sorted(map(int,input().split()))

def all_ordered_partitions(nums, k):
    n = len(nums)
    if k > n:
        return []
    results = []
    for dividers in combinations(range(1, n), k - 1):
        parts = []
        start = 0
        for div in dividers:
            parts.append(nums[start:div])
            start = div
        parts.append(nums[start:])
        results.append(parts)
    return results

def max_min_sum(parts):
    total = 0
    for part in parts:
        if len(part) > 1:
            total += max(part) - min(part)
    return total
    
partitions = all_ordered_partitions(X, M)

ans=10**13
for parts in partitions:
    diff_sum = max_min_sum(parts)
    ans=min(ans,diff_sum)
    
print(ans)
##################################################################
[ai AC]
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    
    if N <= M:
        print(0)
        return

    diffs = [X[i+1] - X[i] for i in range(N-1)]
    diffs.sort(reverse=True)

    total = X[-1] - X[0]
    if M == 1:
        print(total)
    else:
        remove = sum(diffs[:M-1])
        print(total - remove)

if __name__ == '__main__':
    main()
##################################################################
