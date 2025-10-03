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
[ds]
import math

def max_cheb_for_k(n, rK, cK, rD, cD, k):
    r_lo = rK
    r_hi = min(n, rK + k)
    if r_lo > r_hi:
        return -10**30
    
    best = -10**30
    candidates = set()
    
    candidates.add(r_lo)
    candidates.add(r_hi)
    
    if r_lo <= rD <= r_hi:
        candidates.add(rD)
    
    r_left_bound = rK + k - cK
    if r_lo <= r_left_bound <= r_hi:
        candidates.add(r_left_bound)
    
    r_right_bound = rK + k - (n - cK)
    if r_lo <= r_right_bound <= r_hi:
        candidates.add(r_right_bound)
    
    r_candidate1 = (rD - cK + k + rK + cD) // 2
    if r_lo <= r_candidate1 <= r_hi:
        candidates.add(r_candidate1)
    
    r_candidate2 = (rD + cK + k + rK - cD) // 2
    if r_lo <= r_candidate2 <= r_hi:
        candidates.add(r_candidate2)
    
    temp_list = list(candidates)
    for r in temp_list:
        for dr in [-1, 0, 1]:
            neighbor = r + dr
            if r_lo <= neighbor <= r_hi:
                candidates.add(neighbor)
    
    for r in candidates:
        horiz = k - (r - rK)
        if horiz < 0:
            continue
            
        c_left = max(0, cK - horiz)
        c_right = min(n, cK + horiz)
        
        cheb = max(abs(r - rD), abs(c_left - cD), abs(c_right - cD))
        if cheb > best:
            best = cheb
    
    return best

def solve_one(n, rK, cK, rD, cD):
    if rK == rD and cK == cD:
        return 0
    
    min_steps = max(abs(rK - rD), abs(cK - cD))
    L = max(1, min_steps - 2)
    R = min(2 * n, min_steps + 2 * n)
    
    ans = -1
    
    while L <= R:
        mid = (L + R) // 2
        max_cheb = max_cheb_for_k(n, rK, cK, rD, cD, mid)
        
        if max_cheb <= mid:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    
    return ans

t = int(input())
out = []
for _ in range(t):
    n, rK, cK, rD, cD = map(int, input().split())
    out.append(str(solve_one(n, rK, cK, rD, cD)))
print("\n".join(out))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
