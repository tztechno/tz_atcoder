#####################################
問題文
黒板に整数Nが1個書かれています。
高橋君は黒板に書かれている2以上の整数が全て無くなるまで以下の一連の操作を繰り返します。
黒板に書かれている2以上の整数を1つ選びxとする。
黒板からxを1個消す。
そして、2個の整数⌊2x​⌋,⌈2x​⌉を新たに黒板に書く。
この一連の操作を行うために高橋君はx円払う必要がある。
ここで⌊a⌋はa以下の整数のうち最大のものを、⌈a⌉はa以上の整数のうち最小のものを意味します。
操作を行えなくなった時点で高橋君が払った金額の総和は何円ですか？
なお、どのような順番で操作を行っても高橋君が払う金額の総和は一定であることが証明できます。
制約
2≤N≤10**17
#####################################
[balance AC]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
N = int(input())
d = {}
def f(n):
    if n == 1:
        return 0
    if n in d:
        return d[n]
    d[n] = f(n //2) + f((n + 1) // 2) + n
    return d[n]
print(f(N))
#####################################
[riz AC]
memo = {} # メモ用の辞書

def f(x):
  # xが1以下のときはコスト0なので、ここで処理を終える
  if x <= 1:
    return 0

  # 1. memo の中に答えがあるかチェック
  if x in memo:
    return memo[x]

  # 2. なければ計算する
  result = x + f(x // 2) + f((x + 1) // 2)

  # 3. 計算結果をメモに保存
  memo[x] = result

  # 4. 結果を返す
  return result

N = int(input())
print(f(N))

#####################################
[kkc AC]
N = int(input())
for i in range(60):
    if (1 << i) >= N:
        break
ans = N * (i - 1) + 2 * (N - 2 ** (i - 1))
print(ans)
#####################################
[titia AC]
import sys
input = sys.stdin.readline
n=int(input())
from functools import lru_cache
@lru_cache(maxsize=None)
def calc(n):
    if n<=1:
        return 0
    return n+calc(n//2)+calc((n+1)//2)
print(calc(n))
#####################################
[cgpt AC]
import sys
sys.setrecursionlimit(1000000)
memo = {}
def solve(x):
    if x < 2:
        return 0
    if x in memo:
        return memo[x]
    a = x // 2
    b = x - a  # ceil(x/2) = x - floor(x/2)
    res = x + solve(a) + solve(b)
    memo[x] = res
    return res
N = int(input())
print(solve(N))
#####################################
[deepseek AC]
def main():
    N = int(input().strip())
    memo = {}
    stack = [N]
    while stack:
        x = stack[-1]
        if x <= 1:
            memo[x] = 0
            stack.pop()
            continue
        left = x // 2
        right = (x + 1) // 2
        if left not in memo:
            stack.append(left)
            continue
        if right not in memo:
            stack.append(right)
            continue
        # 両方の子が計算済み
        memo[x] = x + memo[left] + memo[right]
        stack.pop()
    print(memo[N])
if __name__ == '__main__':
    main()
#####################################
[cgpt TLE]
[stackをdequeで形成する]
from collections import deque
import math
N = int(input())
stack = deque([N])
P = 0
while stack:
    p0 = stack.popleft()  # 先頭から取り出す
    if p0 >= 2:
        P += p0
        p1 = p0 // 2
        p2 = math.ceil(p0 / 2)
        if p1 >= 2:
            stack.append(p1)
        if p2 >= 2:
            stack.append(p2)
print(P)
#####################################
[my TLE]
import math
N=int(input())
stack=[N]
P=0
while stack:
  p0=stack.pop(0)
  if p0>=2:
    P+=p0
    p1=p0//2
    p2=math.ceil(p0/2)
    if p1>=2:
      stack+=[p1]
    if p2>=2:
      stack+=[p2]
print(P)
#####################################
