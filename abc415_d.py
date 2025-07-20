##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(M)]

AB.sort(key=lambda x:x[0]-x[1])

now=N
ANS=0

for a,b in AB:
    x=a-b
    if now>=a:
        k=(now-a)//x

        ANS+=k
        now-=x*k

    while now>=a:
        now-=x
        ANS+=1

print(ANS)

##################################################################
[hawk]
N, M = map(int, input().split())
AB = []
min_req = float('inf')
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b, a-b))
    min_req = min(min_req, a)

AB = sorted(AB, key = lambda x: x[2])
count = N
i = 0
ans = 0
while count >= min_req:
    if count >= AB[i][0]:
        repeat = (count - AB[i][0]) // AB[i][2] + 1
        count -= (repeat * AB[i][2])
        ans += repeat
    else:
        i += 1
print(ans)
##################################################################

##################################################################

##################################################################
[my TLE]
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
exchanges = []
for _ in range(M):
    A, B = map(int, input().split())
    exchanges.append((A, B))

memo = {}

def dp(bottles):
    if bottles == 0:
        return 0
    
    if bottles in memo:
        return memo[bottles]
    
    max_stickers = 0
    
    for A, B in exchanges:
        if bottles >= A and A > B:
            remaining = bottles - A + B
            stickers = 1 + dp(remaining)
            max_stickers = max(max_stickers, stickers)
    
    memo[bottles] = max_stickers
    return max_stickers

print(dp(N))
##################################################################
[sato]
# コーラの本数 N と、交換パターンの数 M を標準入力から読み込む
N, M = map(int, input().split())

# 交換パターンを格納するリスト
A = []

# 各交換パターン (ai, bi) を読み込む
# ai: 必要なコーラの本数, bi: 交換後に戻ってくるコーラの本数
for _ in range(M):
    ai, bi = map(int, input().split())
    A.append((ai - bi, ai))  # 実質的に消費されるコーラの数(ai - bi)とaiをタプルとして保存

# 実質消費(ai - bi)が小さい順にソート（コスパの良い順に処理するため）
A.sort()

# 獲得したシール数（最終的な答え）を初期化
sheel = 0

# 現在手元にあるコーラの本数
coke = N

# コスパの良い順に交換パターンを試す
for i in range(M):
    # 現在のコーラの本数が、その交換に必要な本数(ai)以上であれば
    if coke >= A[i][1]:
        # 何回交換できるかを計算
        # 残った本数 (coke - ai) であと何回分の「純粋な消費(ai - bi)」を賄えるか
        x = (coke - A[i][1]) // A[i][0] + 1

        # その分だけコーラを消費
        coke -= A[i][0] * x

        # シールを獲得
        sheel += x

# 獲得したシールの総数を出力
print(sheel)

##################################################################
[usms]
N, M = map(int,input().split())
AB = []
for _ in range(M):
    a, b = map(int,input().split())
    AB.append((a - b, a))
AB.sort()

ans = 0
for i in range(M):
    x, y = AB[i]
    if y <= N:
        d = (N - (y - 1) + (x - 1)) // x
        ans += d
        N -= x * d
print(ans)
##################################################################
