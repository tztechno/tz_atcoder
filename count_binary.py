#####################################

def select_coupons(M,j):
    selected = []
    for i in range(M):
        if j & (1<<i):
            selected.append(i+1)
    return selected

#####################################

def count_ones_in_binary(j):
    count = 0
    while j > 0:
        if j & 1:
            count += 1
        j >>= 1
    return count

#####################################
