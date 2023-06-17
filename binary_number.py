n = 4 
for i in range(2**n):
    binary = bin(i)[2:].zfill(n)
    print(binary)
