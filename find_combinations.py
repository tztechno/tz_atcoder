def find_integer_combinations(N, current_sum=0, current_combination=None):
    if current_combination is None:
        current_combination = []

    if current_sum == N:
        return [tuple(current_combination)]
    if current_sum > N:
        return []

    combinations = []
    for i in range(1, N + 1):
        if not current_combination or i >= current_combination[-1]:
            new_combination = current_combination.copy()
            new_combination.append(i)
            combinations.extend(find_integer_combinations(N, current_sum + i, new_combination))

    return combinations
