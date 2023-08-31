
############################

n = 4 
for i in range(2**n):
    binary = bin(i)[2:].zfill(n)
    print(binary)

############################

for i in range(9):
    binary = bin(i)[2:].zfill(4)
    print(binary)

############################

A = (1, 2, 3)
B = (4, 5, 6)

result = tuple(a | b for a, b in zip(A, B))
print(result)  # 出力: (5, 7, 9)

############################
