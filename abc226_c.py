###############################################
###############################################
###############################################
###############################################
###############################################
[WA20,TLE1]
n=int(input())
time=0#total
mastered=set()#master id
A=[]#i,t,a
required=set()#for n
for i in range(n):
  lst=list(map(int,input().split()))
  t=lst[0]
  k=lst[1]
  if k==0:
    time+=t
    mastered.add(i+1)
  elif k!=0:  
    a=lst[2:]
    A+=[(i+1,t,a)]
  if i==n-1 and k!=0:
    required=set(lst[2:])
#print(mastered,required)
while required>=mastered:
  Ai=A.pop()
  req=set(Ai[2])
  if req <= mastered:
    time+=Ai[1]
    mastered.add(Ai[0])
  else:
    A.append(Ai)
  #print(A)
#print(required-mastered)
print(time)

###############################################
###############################################
[tky]
from collections import deque
N=int(input())
T=[]
A=[]
for i in range(N):
    t,k,*a=map(int,input().split())
    T.append(t)
    A.append(a)
ans=0
L=[0 for _ in range(N)]
Q=deque([N-1])
while Q:
    now=Q.popleft()
    if L[now]:continue
    ans+=T[now]
    L[now]=1
    for pre in A[now]:
        if L[pre-1]:continue
        Q.append(pre-1)
print(ans)

###############################################
[tky]
# --- 入力処理 ---
from collections import deque

N = int(input())              # スキル数（タスク数）
T = []                        # 各スキルを習得するのに必要な時間
A = []                        # 各スキルの前提スキル一覧（1-indexed）

for i in range(N):
    t, k, *a = map(int, input().split())  # t:時間, k:前提数, a:前提スキル番号
    T.append(t)
    A.append(a)

# --- 前提を遡って必要なスキルをすべて習得する BFS ---
ans = 0
L = [0] * N                   # L[i] = 1 なら i 番スキルは習得済み
Q = deque([N - 1])            # 最後（N番目のスキル）からスタート

while Q:
    now = Q.popleft()         # 現在処理したいスキルを取り出す

    if L[now]:                # すでに習得済みならスキップ
        continue

    ans += T[now]             # このスキルを習得する時間を加算
    L[now] = 1                # 習得済みにマーク

    # 前提スキルをキューへ追加（A[now] は 1-indexed → 0-indexed に変換）
    for pre in A[now]:
        if not L[pre - 1]:    # 未習得なら追加
            Q.append(pre - 1)

print(ans)                     # 最終的に必要な時間の合計を出力

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
