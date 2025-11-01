####################################################
####################################################
####################################################
####################################################

n, m, k = map(int, input().split())
N = set()

# すべての2^n通りのビットパターンを生成
for i in range(1 << n):
    # iの2進法表現で1である桁のタプルを作成
    it = tuple(j for j in range(n) if (i >> j) & 1)
    N.add(it)

# m個の条件を処理
for _ in range(m):
    lst = input().split()
    c = int(lst[0])
    r = lst[-1]
    Astr = lst[1:-1]
    A = []
    for a in Astr:
        A.append(int(a) - 1)
    
    if r == 'o':
        # Nの中でAの位置がk未満のタプルを削除
        N = {t for t in N if sum(1 for pos in A if pos in t) >= k}
    elif r == 'x':
        # Nの中でAの位置がk以上のタプルを削除
        N = {t for t in N if sum(1 for pos in A if pos in t) < k}

print(len(N))
  
####################################################

n, m, k = map(int, input().split())

# ビット集合として管理（タプルではなく整数で管理）
N = set(range(1 << n))

# m個の条件を処理
for _ in range(m):
    lst = input().split()
    c = int(lst[0])
    r = lst[-1]
    Astr = lst[1:-1]
    
    # Aのビットマスクを事前計算
    A_mask = 0
    for a in Astr:
        A_mask |= (1 << (int(a) - 1))
    
    # フィルタリング
    if r == 'o':
        # Aの位置がk個以上立っているビットパターンを残す
        N = {bits for bits in N if bin(bits & A_mask).count('1') >= k}
    else:  # r == 'x'
        # Aの位置がk個未満立っているビットパターンを残す
        N = {bits for bits in N if bin(bits & A_mask).count('1') < k}

print(len(N))

####################################################
####################################################
####################################################
