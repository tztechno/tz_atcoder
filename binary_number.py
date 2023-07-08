n = 4 
for i in range(2**n):
    binary = bin(i)[2:].zfill(n)
    print(binary)

############################

for i in range(9):
    binary = bin(i)[2:].zfill(4)
    print(binary)
