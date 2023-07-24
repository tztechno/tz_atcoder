def calculate_grundy(n):
    if n == 0:
        return 0
    
    grundy_set = set()
    
    for i in range(1, n + 1):
        next_nimber = calculate_grundy(n - i)
        grundy_set.add(next_nimber)
    
    mex = 0
    while mex in grundy_set:
        mex += 1
    
    return mex

def nim_winner(piles):
    nim_sum = 0
    for pile_size in piles:
        nim_sum ^= calculate_grundy(pile_size)
    
    if nim_sum == 0:
        return "Second"
    else:
        return "First"

# Example usage:
piles = [3, 4, 5]
winner = nim_winner(piles)
print(f"The winner of the Nim game is: {winner}")
