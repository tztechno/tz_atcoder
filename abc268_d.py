###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[my WA]
N,M=map(int,input().split())
S=[]
t=N-1
for i in range(N):
  s=str(input())  
  S+=[s]
  t+=len(s)
T=set()
for i in range(M):
  T.add(str(input()))
if t>16 or t<3:
  print(-1)
  exit()
from itertools import product,permutations,combinations,accumulate  
C=list(permutations(S))
for c in C:
  X='_'.join(list(c))
  if X not in T:
    print(X)
    exit()
print(-1)
###############################################
###############################################
###############################################
[ds]
def solve():
    import sys
    from itertools import permutations

    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    S = []
    idx = 2
    for i in range(N):
        S.append(data[idx])
        idx += 1
    
    T = set()
    for i in range(M):
        T.add(data[idx])
        idx += 1
    
    # 必要な文字数の計算
    total_length = sum(len(s) for s in S)
    min_length = total_length + (N - 1)  # アンダースコアが最低1つずつ
    max_length = 16
    
    if min_length > max_length:
        print(-1)
        return
    
    # 使用可能なアンダースコアの総数
    available_underscores = max_length - total_length
    
    # アンダースコアを(N-1)個の隙間に分配する全ての組み合わせを生成
    for perm in permutations(S):
        # 隙間の数
        gaps = N - 1
        
        # 各隙間に割り当てるアンダースコアの数を全探索
        # 各隙間に最低1つ、合計でavailable_underscores以下のアンダースコア
        from itertools import product
        
        # 各隙間のアンダースコア数を表すリストの生成
        for underscores in product(range(1, available_underscores - gaps + 2), repeat=gaps):
            if sum(underscores) > available_underscores:
                continue
            
            # 文字列を構築
            result = perm[0]
            for i in range(gaps):
                result += '_' * underscores[i] + perm[i + 1]
            
            # 長さチェック
            if len(result) < 3 or len(result) > 16:
                continue
            
            # Tに含まれていないかチェック
            if result not in T:
                print(result)
                return
    
    print(-1)

if __name__ == "__main__":
    solve()
###############################################
[ds mod1]

from itertools import permutations

N,M=map(int,input().split())

S = []
idx = 2
for i in range(N):
    S.append(input())
    idx += 1

T = set()
for i in range(M):
    T.add(input())
    idx += 1

# 必要な文字数の計算
total_length = sum(len(s) for s in S)
min_length = total_length + (N - 1)  # アンダースコアが最低1つずつ
max_length = 16

if min_length > max_length:
    print(-1)

# 使用可能なアンダースコアの総数
available_underscores = max_length - total_length

# アンダースコアを(N-1)個の隙間に分配する全ての組み合わせを生成
for perm in permutations(S):
    # 隙間の数
    gaps = N - 1
    
    # 各隙間に割り当てるアンダースコアの数を全探索
    # 各隙間に最低1つ、合計でavailable_underscores以下のアンダースコア
    from itertools import product
    
    # 各隙間のアンダースコア数を表すリストの生成
    for underscores in product(range(1, available_underscores - gaps + 2), repeat=gaps):
        if sum(underscores) > available_underscores:
            continue
        
        # 文字列を構築
        result = perm[0]
        for i in range(gaps):
            result += '_' * underscores[i] + perm[i + 1]
        
        # 長さチェック
        if len(result) < 3 or len(result) > 16:
            continue
        
        # Tに含まれていないかチェック
        if result not in T:
            print(result)
            exit()

print(-1)
###############################################
[ds mod2]完全理解

from itertools import product,permutations,combinations,accumulate
N,M=map(int,input().split())

S = []
for i in range(N):
    S.append(input())
T = set()
for i in range(M):
    T.add(input())
    
tot_len = sum(len(s) for s in S)#文字合計、usなし
min_len = tot_len + (N - 1)#文字合計、us入り
max_len = 16#上限

if min_len > max_len:
    print(-1)
    exit()

avail_us = max_len - tot_len

for perm in permutations(S):#各文字列順列について
    gaps = N - 1
    for us in product(range(1, avail_us - gaps + 2), repeat=gaps):#us,各隙間に置くus数
        if sum(us) > avail_us:
            continue

        result = perm[0]#文字列、us結合
        for i in range(gaps):
            result += '_' * us[i] + perm[i + 1]

        if len(result) < 3 or len(result) > 16:
            continue
          
        if result not in T:
            print(result)
            exit()

print(-1)
###############################################
[cgpt]
def solve():
    import sys
    from itertools import permutations, product

    n, m = map(int, sys.stdin.readline().split())
    s_list = [sys.stdin.readline().strip() for _ in range(n)]
    banned = {sys.stdin.readline().strip() for _ in range(m)}

    base_len = sum(len(s) for s in s_list)
    # 最低限のアンダースコアを入れた長さ
    if base_len + n - 1 > 16:
        print(-1)
        return

    max_us = 16 - base_len
    gap_count = n - 1

    # gaps に入れるアンダースコア数の列を事前生成
    # 各隙間に必ず1個以上必要なので、その分を引いて計算する
    for order in permutations(s_list):
        for extra in product(range(max_us - gap_count + 2), repeat=gap_count):
            # まず全ての隙間に最低1個ずつ入れて、さらに extra 分追加
            if sum(extra) > max_us - gap_count:
                continue
            parts = [order[0]]
            for i, add in enumerate(extra):
                parts.append('_' * (1 + add))
                parts.append(order[i + 1])
            candidate = ''.join(parts)
            if 3 <= len(candidate) <= 16 and candidate not in banned:
                print(candidate)
                return
    print(-1)

if __name__ == "__main__":
    solve()

###############################################
###############################################
###############################################
for perm in permutations(S):
    gaps = N - 1
    for underscores in product(range(1, available_underscores - gaps + 2), repeat=gaps):
###############################################
