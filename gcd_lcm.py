def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_multiple(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty list of numbers")

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = (result * numbers[i]) // gcd(result, numbers[i])
    return result
