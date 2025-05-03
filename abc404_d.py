
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[my parts]

N,M=map(int,input().split())
C=list(map(int,input().split()))###入場料
from collections import defaultdict,deque,Counter
animal = defaultdict(deque)
zoo = defaultdict(deque)
for i in range(M):
  ki=list(map(int,input().split()))
  for kii in ki[1:]:
    animal[kii].append(i+1)
    zoo[i+1].append(kii)
print(animal)各動物のいる動物園
print(zoo)各動物園の動物

##################################################################
[deepseek WA]

from collections import defaultdict

def min_cost_to_see_all_animals_twice(N, M, C, animal_zoos):
    zoo_animals = [[] for _ in range(N + 1)]
    for animal_id in range(1, M + 1):
        for zoo_id in animal_zoos[animal_id]:
            zoo_animals[zoo_id].append(animal_id)

    required_views = [2] * (M + 1)
    zoo_visits = [0] * (N + 1)
    total_cost = 0

    while sum(required_views[1:]) > 0:
        best_zoo = -1
        best_value = -1
        for zoo_id in range(1, N + 1):
            valuable_animals = sum(1 for animal_id in zoo_animals[zoo_id] if required_views[animal_id] > 0)
            if valuable_animals == 0:
                continue
            value = valuable_animals / C[zoo_id - 1]
            if value > best_value:
                best_value = value
                best_zoo = zoo_id
        if best_zoo == -1:
            break
        total_cost += C[best_zoo - 1]
        zoo_visits[best_zoo] += 1
        for animal_id in zoo_animals[best_zoo]:
            if required_views[animal_id] > 0:
                required_views[animal_id] -= 1
    return total_cost

N, M = map(int, input().split())
C = list(map(int, input().split()))
animal_zoos = [[] for _ in range(M + 1)]
for i in range(1, M + 1):
    ki_list = list(map(int, input().split()))
    animal_zoos[i] = ki_list[1:]
result = min_cost_to_see_all_animals_twice(N, M, C, animal_zoos)
print(result)

##################################################################
[titia]

import sys
input = sys.stdin.readline
N,M=map(int,input().split())
C=list(map(int,input().split()))

LIST=[[] for i in range(N)]

for i in range(M):
    X=list(map(int,input().split()))

    for x in X[1:]:
        LIST[x-1].append(i)

LIST+=LIST
C+=C
ANS=1<<63

for i in range(1<<(N*2)):
    money=0
    MS=[0]*M
    for j in range(2*N):
        if i & (1<<j) != 0:
            money+=C[j]
            for x in LIST[j]:
                MS[x]+=1
    if min(MS)>=2:
        ANS=min(ANS,money)

print(ANS)

##################################################################
