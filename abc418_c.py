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
j番目の質問は以下の通りです。難易度Bj​のゲームに勝利するためにはじめに宣言する必要がある整数xの最小値を答えよ。
勝利が不可能であれば、代わりに−1と答えよ。
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
