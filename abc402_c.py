##################################################################

##################################################################
[MyPlan + DeepSeek AC]

N, M = map(int, input().split())
K = []
for _ in range(M):
    ki = list(map(int, input().split()))
    K.append(ki[1:])  # Skip the first value (number of ingredients), store only ingredients
B = list(map(int, input().split()))

# Dictionary to record on which day each ingredient is conquered
ingredient_day = {}
for day in range(N):
    ingredient = B[day]
    # Be careful whether ingredients are 1-based or 0-based; assuming 1-based here
    ingredient_day[ingredient] = day + 1  # Record the day as 1-based

max_day_per_dish = []
for kj in K:
    max_day = 0
    for ingredient in kj:
        if ingredient in ingredient_day:
            day = ingredient_day[ingredient]
            if day > max_day:
                max_day = day
        else:
            # This ingredient is not in list B, so the dish can never be eaten
            max_day = -1
            break
    if max_day != -1:
        max_day_per_dish.append(max_day)

# Count how many dishes have their max_day on each day
count_per_day = [0] * (N + 2)  # Using 1-based index for days 1 to N
for day in max_day_per_dish:
    count_per_day[day] += 1

# Calculate cumulative count up to each day
current = 0
result = []
for day in range(1, N + 1):
    current += count_per_day[day]
    result.append(current)

print('\n'.join(map(str, result)))

##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

L=[list(map(int,input().split()))[1:] for i in range(M)]

B=list(map(int,input().split()))
D={B[i]:i for i in range(len(B))}

for i in range(M):
    for j in range(len(L[i])):
        L[i][j]=D[L[i][j]]

ANS=[0]*N

for i in range(M):
    MAX=max(L[i])
    ANS[MAX]+=1


for i in range(1,len(ANS)):
    ANS[i]+=ANS[i-1]

print(*ANS)

##################################################################
[DeepSeek AC]
import sys
from collections import defaultdict

def main():
    data = sys.stdin.buffer.read()
    ptr = 0
    size = len(data)
    
    def readint():
        nonlocal ptr
        while ptr < size and data[ptr] < 48:
            ptr += 1
        n = 0
        while ptr < size and 48 <= data[ptr] <= 57:
            n = n * 10 + (data[ptr] - 48)
            ptr += 1
        return n
    
    N, M = readint(), readint()

    K_sets = []
    element_indices = defaultdict(list)
    for i in range(M):
        k_len = readint()
        elements = tuple(readint() for _ in range(k_len))
        K_sets.append(elements)
        for num in elements:
            element_indices[num].append(i)

    B = [readint() for _ in range(N)]

    current_elements = set()
    active_counts = [0] * M
    results = []
    total = 0
    
    for num in B:
        if num not in current_elements:
            current_elements.add(num)
            for idx in element_indices.get(num, []):
                if active_counts[idx] == len(K_sets[idx]) - 1:
                    total += 1
                active_counts[idx] += 1
        results.append(total)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
  
##################################################################
[my TLE18]

import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N, M = int(data[ptr]), int(data[ptr+1])
    ptr += 2

    K = []
    for _ in range(M):
        ki_len = int(data[ptr])
        ki = list(map(int, data[ptr+1:ptr+1+ki_len]))
        mask = 0
        for num in ki:
            mask |= 1 << (num - 1)  
        K.append(mask)
        ptr += 1 + ki_len

    B = list(map(int, data[ptr:ptr+N]))
    ptr += N

    current_mask = 0
    for num in B:
        current_mask |= 1 << (num - 1) 
        count = 0
        for mask in K:
            if (mask & current_mask) == mask:  
                count += 1
        print(count)

if __name__ == "__main__":
    main()
  
##################################################################
[my TLE18]

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    K = []
    for _ in range(M):
        ki = list(map(int, input().split()))
        K.append(set(ki[1:]))  
    
    B = list(map(int, input().split()))
    
    current_elements = set()
    for i in range(N):
        current_elements.add(B[i])  
        count = 0
        for kj in K:
            if kj.issubset(current_elements):
                count += 1
        print(count)

if __name__ == "__main__":
    main()
  
##################################################################
[my TLE25]

import sys
input = sys.stdin.readline
N,M=map(int,input().split())
t=0
K=[]
for i in range(M):
  ki=list(map(int,input().split()))
  K+=[ki[1:]]
  
B=list(map(int,input().split()))

for i in range(N):  
  t=0
  for kj in K:
    if set(kj)-set(B[0:i+1])==set():
      t+=1
  print(t)

##################################################################
