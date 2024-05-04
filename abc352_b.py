abc352_b.py
###########################################
###########################################
###########################################
###########################################
S = input()
T = input()
L = list()
L.append(0)
for i in range(len(S)):
  L.append(T.find(S[i]) + 1 + L[i])
  T = T[T.find(S[i])+1:]
L.pop(0)
print(*L)
###########################################
[titia][dequeを使わない方法]
import sys
input = sys.stdin.readline
S=input().strip()
T=input().strip()
ANS=[]
ind=0
for i in range(len(S)):
    while T[ind]!=S[i]:
        ind+=1
    ANS.append(ind+1)
    ind+=1
print(*ANS)
###########################################
S=input()
T=input()
result=[]
i=0
for j in range(len(T)):
    if S[i]==T[j]:
        result.append(j+1)
        i+=1
r=list(set(result))
r.sort()
print(*r)
###########################################
s = input()
t = input()
i = 0
for j in range(len(t)):
	if s[i] == t[j]:
		print(j+1, end=" ")
		i+=1
###########################################
S=input()
T=input()
result=[]
i=0
for j in range(len(T)):
    if S[i]==T[j]:
        result.append(j+1)
        i+=1
r=list(set(result))
r.sort()
print(*r)
###########################################
[cGPT create, but WA]
S=list(input())
T=list(input())
# T内の各文字の位置を記録するハッシュマップを作成する
T_map = {}
for i, char in enumerate(T):
    if char not in T_map:
        T_map[char] = i
# 出力を格納するリスト
A = []
# S内の各文字について処理を行う
p = 0
for s in S:
    # ハッシュマップから文字sの位置を取得し、出力リストに追加
    if s in T_map:
        A.append(T_map[s] + 1)
        p = T_map[s] + 1  # 次の検索の開始位置を更新する
print(*A)
###########################################
[my AC][順番の逆転を回避する仕組みを加える]
from collections import defaultdict,deque,Counter
cnt = defaultdict(deque)
S=list(input())
T=list(input())
for i,t in enumerate(T):
  cnt[t].append(i+1)
A=[0]
for s in S:
  #print(cnt[s])
  nx=cnt[s].popleft()
  while nx<=A[-1]:
    nx=cnt[s].popleft()
  if nx>A[-1]:
    A+=[nx]
print(*A[1:])
###########################################
[my WA15]
from collections import defaultdict,deque,Counter
cnt = defaultdict(deque)
S=list(input())
T=list(input())
for i,t in enumerate(T):
  cnt[t].append(i+1)
A=[]
for s in S:
  A+=[cnt[s].popleft()]
print(*A)
###########################################
[my TLE3]
S=list(input())
T=list(input())
TR=list(range(1,len(T)+1))
A=[]
p=0
for s in S:
  ts=T[p:].index(s)
  A+=[TR[p:][ts]]
  p+=ts+1
print(*A)
###########################################
[my TLE2]
S=list(input())
T=list(input())
TR=list(range(1,len(T)+1))
A=[]
for s in S:
  ts=T.index(s)
  A+=[TR[ts]]
  T=T[ts+1:]
  TR=TR[ts+1:]
print(*A)
###########################################
[my TLE1]
S=list(input())
T=list(input())
T2=[]
for i,t in enumerate(T):
  T2+=[(t,i+1)]
A=[]
for s in S:
  ts=T.index(s)
  A+=[T2[ts][1]]
  T=T[ts+1:]
  T2=T2[ts+1:]
print(*A)
###########################################
