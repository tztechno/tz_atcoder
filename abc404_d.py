
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

for i in range(1<<(N*2)):
    for j in range(2*N):
        if i & (1<<j) != 0:

このコードは、整数 i のビット表現の中で、j 番目のビットが立っている（つまり1である）かどうかを判定しています。

1 << j の意味
まず、1 << j は「1を左に j ビットシフトする」というビット演算です。具体的には、以下のようになります。
* j = 0 のとき: 1 << 0 は 00...0001 (2進数)
* j = 1 のとき: 1 << 1 は 00...0010 (2進数)
* j = 2 のとき: 1 << 2 は 00...0100 (2進数)
* ...
* j = k のとき: 00...010...00 (2進数、右から k+1 番目のビットが1)

つまり、1 << j は j 番目のビットだけが1で、他のビットはすべて0であるような整数を作り出します。

i & (1 << j) の意味
次に、& はビットごとのAND演算子です。これは、2つの整数の対応するビット同士を比較し、両方のビットが1である場合にのみ結果のビットを1にし、それ以外の場合は0にします。
したがって、i & (1 << j) は、整数 i のビット表現と 1 << j のビット表現のAND演算を行います。

!= 0 の意味
最後に、!= 0 は「0ではない」という比較演算子です。

全体の意味
これらを組み合わせると、if i & (1 << j) != 0: という条件は、
「整数 i のビット表現において、j 番目のビットが1であるならば」
ということを意味します。

for i in range(1<<(N*2)) の意味
外側のループ for i in range(1<<(N*2)) は、i を 0 から 22N−1 までの整数で順番に回します。これは、2N ビットで表現できるすべての可能な組み合わせを生成することを意味します。

コード全体の役割
この二重ループは、i が持つ 2N 個のビットのそれぞれについて、j 番目のビットが立っているかどうかをチェックしています。一般的に、このような構造は、ある集合（この場合は 2N 個の要素に対応するビット）の部分集合を列挙したり、ビットの状態に基づいて何らかの処理を行ったりする際に用いられます。
例えば、N=2 の場合、2N=4 なので、i は 0 から 24−1=15 までの値を取ります。それぞれの i のビット表現は以下のようになります。
i = 0: 0000
i = 1: 0001  (j=0 で条件成立)
i = 2: 0010  (j=1 で条件成立)
i = 3: 0011  (j=0, 1 で条件成立)
i = 4: 0100  (j=2 で条件成立)
...
i = 15: 1111 (j=0, 1, 2, 3 で条件成立)
内側のループでは、それぞれの i に対して、j を 0 から 2N−1 まで変化させながら、i の各ビットが立っているかどうかを確認しているわけです。

##################################################################
[rukou]

import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
C=list(map(int,input().split()))
K,A=[-1]*m,[[] for _ in range(n)]
for i in range(m):
    K[i],*a=map(int,input().split())
    for ai in a:
        A[ai-1].append(i)
        
def rec(pos,vis):
    if pos==n:
        return 0 if all(v>=2 for v in vis) else float('inf')
    
    res=float('inf')
    for i in range(3):
        for a in A[pos]:
            vis[a]+=i
        res=min(res,rec(pos+1,vis)+C[pos]*i)
        for a in A[pos]:
            vis[a]-=i
    return res

print(rec(0,[0]*(m)))
##################################################################
[mimam]

N,M = map(int, input().split())
C = list(map(int, input().split()))
zoo = [[] for _ in range(N)] # 園別に見られる動物
for i in range(M):
    A = list(map(int, input().split()))[1:]
    for a in A:
        zoo[a-1].append(i)

ans = sum(C) * 2
for i in range(2**(2*N)):
    price = 0
    animal = [0] * M
    for j in range((2*N)):
        if ((i >> j) & 1):
            k = j % N
            price += C[k]
            for z in zoo[k]:
                animal[z] += 1
    all_seen = sum([a>=2 for a in animal])
    if all_seen == M and price < ans:
        ans = price
print(ans)
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
