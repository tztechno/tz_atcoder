def pop_left(lst, i):
    return [lst.pop(0) for _ in range(i)]

def pop_right(lst, j):
    return [lst.pop() for _ in range(j)]
