#####################################

import math
n = 5
result = math.factorial(n)
print(f"{n} の階乗は {result} です。")

#####################################

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
#####################################
