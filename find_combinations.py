def find_integer_combinations(N):
    combinations = []
    for i in range(1, N):
        if i > N // 2:
            break
        j = N - i
        combinations.append((i, j))
    return combinations

N = 10  # 和をNにしたい場合
combinations = find_integer_combinations(N)
print(combinations)
