#############################################
[my AC]

from collections import defaultdict,deque,Counter
cnt = defaultdict(deque)
N,M=map(int,input().split())
S=str(input())
C=list(map(int,input().split()))
for i in range(N):
  cnt[C[i]-1].append(S[i])
for m in range(M):
  cnt[m].rotate(1)
S2=''
for ci in C:
  S2+=cnt[ci-1].popleft()
print(S2)

#############################################
[my TLE]

N,M=map(int,input().split())
S=str(input())
C=list(map(int,input().split()))
M2=[]
for i in range(M):
  M2+=[[]]
for i in range(N):
  M2[C[i]-1]+=[S[i]]
M3=[]
for m in M2:
  M3+=[[m[-1]]+m[0:-1]]
S2=''
for ci in C:
  S2+=M3[ci-1].pop(0)
print(S2)

#############################################
