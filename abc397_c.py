#########################################################
#########################################################

#########################################################

#########################################################

#########################################################
[my TLE]

N=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(1,N):
  A1=len(set(A[0:i]))
  A2=len(set(A[i:]))
  ans=max(ans,A1+A2)
print(ans)

#########################################################
[claude]

N = int(input())
A = list(map(int, input().split()))

left_set = set()
left_counts = [0] * N

for i in range(N):
    left_set.add(A[i])
    left_counts[i] = len(left_set)

right_set = set()
right_counts = [0] * N

for i in range(N-1, -1, -1):
    right_set.add(A[i])
    right_counts[i] = len(right_set)

ans = max(left_counts[i] + right_counts[i+1] for i in range(N-1))
print(ans)

#########################################################
[titia]
import sys
input = sys.stdin.readline

from collections import Counter

n=int(input())
A=list(map(int,input().split()))

C1=Counter()
C2=Counter(A)

ANS=len(C2)

for a in A:
    C1[a]+=1
    C2[a]-=1

    if C2[a]==0:
        del C2[a]

    ANS=max(ANS,len(C1)+len(C2))

print(ANS)


#########################################################
