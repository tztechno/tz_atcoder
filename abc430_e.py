########################################
https://atcoder.jp/contests/abc430/tasks/abc430_e
########################################
文字列の find() メソッドの実装アルゴリズムの違い

[CPython の場合]
Python 3.x以降、Boyer-Moore-Horspool (BMH) アルゴリズムなど、高度な文字列検索アルゴリズムを使用
平均的な計算量: O(n) に近い効率的な処理
特に長い文字列での検索が高速

[PyPy の場合]
JITコンパイラによる最適化が得意ですが、find() の実装は単純なアルゴリズム(ナイーブサーチに近い)を使っている可能性
最悪計算量: O(n×m) (nは検索対象文字列の長さ、mはパターンの長さ)
特定のケースで非常に遅くなる
########################################
########################################
########################################
########################################
[PyPy,TLE16][CPython,AC]

T = int(input())
for _ in range(T):
  A = input().strip()
  B = input().strip()
  print((A*2).find(B))
########################################
[stn,pypy]

t = int(input())
B1 = 100000007
B2 = 1000000007
for _ in range(t):
    a = input()
    b = input()
    n = len(a)
    ah, bh = 0, 0
    for i in range(n):
        ah = (ah*B1 + (int(a[i])))%B2
        bh = (bh*B1 + (int(b[i])))%B2
    th = 1
    for i in range(n-1):
        th = (th*B1)%B2
    ans = -1
    for i in range(n):
        if ah==bh:
            ans = i
            break
        ah = (ah-th*int(a[i])+B2)%B2
        ah = (ah*B1+int(a[i]))%B2
    print(ans)
########################################
[titia,pypy]

import sys
input = sys.stdin.readline

mod=67280421310721
mod2=2147483647
mod3=998244353

INV=pow(2,mod-2,mod)
INV2=pow(2,mod2-2,mod2)
INV3=pow(2,mod3-2,mod3)

T=int(input())

for tests in range(T):
    A=input().strip()
    B=input().strip()

    A2=0
    B2=0

    A3=0
    B3=0

    A4=0
    B4=0

    now2=1
    now3=1
    now4=1

    for i in range(len(A)):
        if A[i]=="1":
            A2=(A2+now2)%mod
            A3=(A3+now3)%mod2
            A4=(A4+now4)%mod3
        if B[i]=="1":
            B2=(B2+now2)%mod
            B3=(B3+now3)%mod2
            B4=(B4+now4)%mod3

        if i<len(A)-1:
            now2=now2*2%mod
            now3=now3*2%mod2
            now4=now4*2%mod3

    if A2==B2 and A3==B3 and A4==B4:
        print(0)
        continue

    ANS=-1

    for i in range(len(A)):
        if A[i]=="1":
            A2-=1
            A2=A2*INV%mod
            A2=(A2+now2)%mod

            A3-=1
            A3=A3*INV2%mod2
            A3=(A3+now3)%mod2

            A4-=1
            A4=A4*INV3%mod3
            A4=(A4+now4)%mod3
        else:
            A2=A2*INV%mod
            A3=A3*INV2%mod2
            A4=A4*INV3%mod3

        if A2==B2 and A3==B3 and A4==B4:
            ANS=i+1
            break

    print(ANS)

########################################
########################################
########################################
