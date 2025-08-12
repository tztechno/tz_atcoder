##################################################################
https://atcoder.jp/contests/abc418/submissions
##################################################################
ポーカーテーブルの上にN種類のフレーバーのティーバッグが置かれています。
フレーバーには1からNまでの番号が付けられており、フレーバーi(1≤i≤N)のティーバッグはAi​個あります。
あなたはこれらのティーバッグを使ったゲームに参加します。
ゲームには1以上A1​+⋯+AN​以下の難易度が設定されており，難易度bのゲームは以下の流れで行われます。
あなたは整数xを宣言する。このとき、b≤x≤A1​+⋯+AN​を満たす必要がある。
ディーラーはポーカーテーブルの上にあるティーバッグの中からちょうどx個を選び、あなたに渡す。
あなたは渡されたx個のティーバッグのフレーバーを確認し、その中からb個のティーバッグを選ぶ。
あなたが選んだb個のティーバッグがすべて同じフレーバーであれば、あなたは勝利する。
そうでなければ、あなたは敗北する。ディーラーはあなたが敗北するように最善を尽くすものとします。
Q個の質問が与えられるので、それぞれに答えてください。
j番目の質問は以下の通りです。
難易度Bj​のゲームに勝利するためにはじめに宣言する必要がある整数xの最小値を答えよ。
勝利が不可能であれば、代わりに−1と答えよ。
##################################################################
4 5
4 1 8 4
1
8
5
2
10
----------------------
1
17
14
5
-1
##################################################################
[cgpt wa]
N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

for _ in range(Q):
    b = int(input())
    ans = float('inf')
    for a in A:
        if a >= b:  # b個そろえるポテンシャルがあるフレーバー
            x_needed = b + (S - a)
            if x_needed <= S:
                ans = min(ans, max(b, x_needed))
    print(ans if ans != float('inf') else -1)
##################################################################
[cgpt AC]
import sys
import bisect

def solve():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    A.sort()  # ascending
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i+1] = pref[i] + A[i]

    for _ in range(Q):
        b = int(input().strip())
        t = b - 1
        if t <= 0:
            C = 0
        else:
            k = bisect.bisect_right(A, t)  # A[0..k-1] <= t
            C = pref[k] + (N - k) * t
        x_min = max(b, C + 1)
        print(x_min if x_min <= S else -1)

if __name__ == "__main__":
    solve()
##################################################################
[my+cgpt AC]
from bisect import bisect_right
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
S = sum(A)

C = [0]
for a in A:
    C.append(C[-1] + a)

for _ in range(M):
    b = int(input())
    t = b - 1
    if t <= 0:
        Cb = 0
    else:
        k = bisect_right(A, t)
        Cb = C[k] + (N - k)*t  ####

    x_min = max(b, Cb + 1)
    print(x_min if x_min <= S else -1)
##################################################################

##################################################################

##################################################################

##################################################################
[MyBrain AC]
import bisect
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
S = sum(A)
C=[0]
for a in A:
  C+=[C[-1]+a]
#x:勝利するためにはじめに宣言する必要がある整数 
for _ in range(Q):
    b = int(input())#難易度、必要なフラッシュ個数
    #--------------
    t=bisect.bisect_right(A,b-1)
    x=C[t]+(b-1)*(N-t)+1　#aを全部使う部分（境界線の左）+定数を加える（境界線の右）+1
    #--------------
    if x>S:
      print(-1)
    else:
      print(x)    
##################################################################
[MyBrain TLE6]
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
S = sum(A)
C=[0]
for a in A:
  C+=[C[-1]+a]
#x:勝利するために宣言する必要がある整数 
for _ in range(Q):
    b = int(input())#難易度、必要なフラッシュの枚数
    #--------------
    x=1
    for a in A:
      if a>=b-1:
        x+=b-1 #定数を加える、勝たない範囲でできるだけ多く
      elif a<b-1:
        x+=a   #aを全部使う
    #--------------          
    if x>S:
      print(-1)
    else:
      print(x)    
##################################################################
[titia]
import sys
input = sys.stdin.readline

N,Q=map(int,input().split())
A=list(map(int,input().split()))

A.sort()
MAX=max(A)
LIST=[0]*(MAX+1)
now=0

for i in range(2,MAX+1):
    while A[now]<i-1:
        now+=1

    LIST[i]=LIST[i-1]+(N-now)
    
for tests in range(Q):
    x=int(input())
    if x>MAX:
        print(-1)
    else:
        print(LIST[x]+1)

##################################################################
[my tle]
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
A.sort()

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

def sum_min(b_minus_1):

    import bisect
    k = b_minus_1
    idx = bisect.bisect_right(A, k)

    return prefix[idx] + (N - idx) * k

for _ in range(Q):
    b = int(input())
    if max(A) < b:
        print(-1)
        continue
    safe = sum_min(b - 1)
    x_min = max(b, safe + 1)
    if x_min > S:
        print(-1)
    else:
        print(x_min)
##################################################################
[my tle]
import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
A.sort()
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

queries = []
for _ in range(Q):
    b = int(input())
    queries.append(b)

maxA = A[-1]
sorted_queries = sorted((b, idx) for idx, b in enumerate(queries))
answers = [-1] * Q
pos = 0  

for b, idx in sorted_queries:
    if maxA < b:
        answers[idx] = -1
        continue
    k = b - 1
    i = bisect.bisect_right(A, k)
    safe = prefix[i] + (N - i) * k
    x_min = max(b, safe + 1)
    if x_min > S:
        answers[idx] = -1
    else:
        answers[idx] = x_min

print('\n'.join(map(str, answers)))

##################################################################
[my ac]
import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
A.sort()
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

queries = []
for _ in range(Q):
    b = int(input())
    queries.append(b)

maxA = A[-1]

sorted_queries = sorted((b, idx) for idx, b in enumerate(queries))
answers = [-1] * Q
pos = 0  

for b, idx in sorted_queries:
    if maxA < b:
        answers[idx] = -1
        continue
    k = b - 1
    i = bisect.bisect_right(A, k)
    safe = prefix[i] + (N - i) * k
    x_min = max(b, safe + 1)
    if x_min > S:
        answers[idx] = -1
    else:
        answers[idx] = x_min

print('\n'.join(map(str, answers)))

##################################################################
