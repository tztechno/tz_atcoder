##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[my AC] #default version

N,M=map(int,input().split())

A=[]
for i in range(M):
  l,r=map(int,input().split())
  A+=[(l,1),(r+1,-1)]

from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
for order,val in A:
  cnt[order]+=val

t=0
ans=M

if sorted(cnt)[0]>1 or sorted(cnt)[-1]<N:
  print(0)
  exit()
  
else:
  for c in sorted(cnt):
    if 1<=c<=N:
      t+=cnt[c]
      ans=min(ans,t)
    else:
      break
  print(ans)
##################################################################
[my AC] #全体リスト作る
N,M=map(int,input().split())
B=[0]*(N+1)
for i in range(M):
  l,r=map(int,input().split())
  B[l-1]+=1
  B[r]-=1
C=[0]
for b in B:
  C+=[C[-1]+b]
print(min(C[1:-1]))
##################################################################
[mana]
n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

b = [0] * (n + 1)
for i in range(m):
    b[a[i][0] - 1] += 1
    b[a[i][1]] += -1

for j in range(1, n):
    b[j] += b[j - 1]

print(min(b[:n]))
##################################################################
[tani]
n, m = map(int, input().split())
a = [0]*n

for _ in range(m):
    l, r = map(int, input().split())
    a[l-1] += 1
    if r < n :
        a[r] -= 1

for i in range(1,n) :
    a[i] += a[i-1]

print(min(a[:n]))
##################################################################
[soma]
N, M = map(int, input().split())
A = [0] * (N + 1)

for _ in range(M):
    L, R = map(int, input().split())
    A[L - 1] += 1
    A[R] -= 1
for i in range(1, N):
    A[i] += A[i - 1]
print(min(A[:N]))

##################################################################
[titia]

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
LIST=[0]*(N+1)

for i in range(M):
    l,r=map(int,input().split())
    LIST[l-1]+=1
    LIST[r]-=1

for i in range(1,N+1):
    LIST[i]=LIST[i]+LIST[i-1]

LIST.pop()

print(min(LIST))
##################################################################
[my WA1]

N,M=map(int,input().split())

A=[]
for i in range(M):
  l,r=map(int,input().split())
  A+=[(l,1)]
  A+=[(r+1,-1)]

from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
for a in A:
  cnt[a[0]]+=a[1]

t=0
ans=M
for c in sorted(cnt):
  if 1<=c<=N:
    t+=cnt[c]
    ans=min(ans,t)
  else:
    break

print(ans)
##################################################################
