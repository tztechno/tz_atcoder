https://atcoder.jp/contests/abc418
##################################################################
0と1からなる空でない文字列Sが次の条件を満たす時、Sを美しい文字列と呼びます。
(条件)次の一連の操作をSの長さが1になるまで行い、Sに残った唯一の文字を1にすることができる。
1≤i≤∣S∣−1を満たす整数iを自由に選ぶ。整数xを次のように定義する。
Si​=0かつSi+1​=0である場合、x=1とする。
Si​=0かつSi+1​=1である場合、x=0とする。
Si​=1かつSi+1​=0である場合、x=0とする。
Si​=1かつSi+1​=1である場合、x=1とする。
Si​とSi+1​を取り除き、それらがあった場所にxを数字とみなしたものを1個挿入する。
例えばS=10101に対してi=2を選んで操作を行った場合、操作後の文字列は1001になる。
0と1からなる長さNの文字列Tがあります。
Tの部分文字列である美しい文字列の個数を求めてください。
ただし、2つの部分文字列が文字列として同じでも、取り出す位置が異なるならば別々に数えます。
##################################################################
30
011011100101110111100010011010
-------------------
225
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[zae]
n = int(input())
T = input()
dp = [[0,0] for _ in range(n+1)]    
for i in range(n):
    if T[i] == '0':
        dp[i+1][0] = dp[i][1]
        dp[i+1][1] = dp[i][0] + 1
    else:
        dp[i+1][0] = dp[i][0] + 1
        dp[i+1][1] = dp[i][1]
print(sum(dp[i][0] for i in range(n+1)) )
##################################################################
[MyAi WA]
N = int(input())
s = input()
ans = 0
for i in range(N):
    result = int(s[i])
    for j in range(i + 1, N):
        b = int(s[j])
        result ^= b  # XOR
        if result == 1:
            ans += 1
print(ans)
##################################################################
[MyAi WA]
# 最適化されたバージョン
N = int(input())
s = str(input())

ans = 0

# 各開始位置から美しい部分文字列を探す
for i in range(N):
    # 長さ1の部分文字列は常に美しい（1文字なので結果は常にその文字）
    if s[i] == '1':
        ans += 1
    
    # 長さ2以上の部分文字列
    result = int(s[i])  # 最初の文字
    for j in range(i + 1, N):
        # 現在の文字との演算を実行
        b = int(s[j])
        result = 1 if result == b else 0
        
        # 結果が1なら美しい部分文字列
        if result == 1:
            ans += 1
        
        # 結果が0になった時点で、これ以上長い部分文字列は美しくならない
        # （0に何を演算しても結果は0になるため）
        if result == 0:
            break

print(ans)
##################################################################
[MyAi TLE]
N=int(input())
s=str(input())
T=[]
for i in range(N+1):
  for j in range(i+1,N+1):
    T+=[s[i:j]]

def is_beautiful(subs: str) -> bool:
    result = int(subs[0])
    for ch in subs[1:]:
        b = int(ch)
        result = 1 if result == b else 0
    return result == 1

ans=0
for t in T:
  ans+=is_beautiful(t)
print(ans) 
##################################################################
[titia]
import sys
input = sys.stdin.readline
N=int(input())
T=input().strip()

S=[0]
for t in T:
    if t=="0":
        S.append(S[-1]+1)
    else:
        S.append(S[-1])

E=0
O=0
for s in S:
    if s%2==0:
        E+=1
    else:
        O+=1

ANS=0

for s in S:
    if s%2==0:
        E-=1
        ANS+=E
    else:
        O-=1
        ANS+=O

print(ANS)
##################################################################
[MyAi TLE]
import sys
sys.setrecursionlimit(10**7)

def calc_x(a, b):
    if a == b:
        return 1
    else:
        return 0

def solve(T):
    n = len(T)
    dp = [[[False]*2 for _ in range(n+1)] for __ in range(n+1)]

    for i in range(n):
        c = int(T[i])
        dp[i][i+1][c] = True

    for length in range(2, n+1):
        for l in range(n - length + 1):
            r = l + length
            for m in range(l+1, r):
                for left_c in [0,1]:
                    if not dp[l][m][left_c]:
                        continue
                    for right_c in [0,1]:
                        if not dp[m][r][right_c]:
                            continue
                        z = calc_x(left_c, right_c)
                        if not dp[l][r][z]:
                            dp[l][r][z] = True

    count = 0
    for l in range(n):
        for r in range(l+1, n+1):
            if dp[l][r][1]:
                count += 1
    return count


N = int(input())
T = input().strip()
result = solve(T)
print(result)
##################################################################
[MyAi AC]
def solve_fast(T):
    n = len(T)
    T_int = [int(c) for c in T]
    
    prefix_xnor = [1] * (n + 1)
    for i in range(n):
        prefix_xnor[i+1] = (prefix_xnor[i] == T_int[i])

    counts = {0: 0, 1: 0}
    for val in prefix_xnor:
        counts[val] += 1
        
    count = 0

    for val in counts:
        k = counts[val]
        count += k * (k - 1) // 2
        
    return count

N = int(input())
T = input().strip()
result = solve_fast(T)
print(result)
##################################################################

