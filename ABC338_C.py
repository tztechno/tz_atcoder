//ABC338_C Leftover Recipes
##################################################
##################################################
import sys
input = sys.stdin.readline
n=int(input())
Q=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ANS=0
for i in range(10**6+1):
    REST=[(Q[j]-A[j]*i) for j in range(n)]
    if min(REST)<0:
        break
    #print(REST)
    MIN=10**6
    for j in range(n):
        if B[j]!=0:
            MIN=min(MIN,REST[j]//B[j])
    ANS=max(ANS,i+MIN)
print(ANS)
##################################################
import copy
n = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = 10**10
for i in range(n):
    if A[i] == 0: continue
    a = min(a, Q[i]//A[i])
ans = a
for i in range(a+1):
    b = 10**10
    nowQ = copy.deepcopy(Q)
    for j in range(n):
        nowQ[j] -= (a-i)*A[j]
    for j in range(n):
        if B[j] == 0: continue
        b = min(b, nowQ[j]//B[j])
    ans = max(ans, a-i+b)
print(ans)
##################################################
n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(10**6 + 1):
    aa = 10**6
    f = True
    for k in range(n):
        if (q[k] - a[k] * i) < 0:
            aa = 0
            f = False
            break
        rem = (q[k] - a[k] * i) // b[k] if b[k] != 0 else 10 **6
        aa = min(aa, rem)
    if f:
        ans = max(ans, i+aa)
print(ans)
##################################################
N=int(input())
Q=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans = 0
for x in range(10**6 + 1):
    Q1 = [qi - x * ai for qi, ai in zip(Q, A)]
    if min(Q1) < 0:
        break
    y = min([qi // bi for qi, bi in zip(Q1, B) if bi > 0])
    ans = max(x + y, ans)
print(ans)
##################################################
N=int(input())
Q=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
mx=10**9
for k in range(N):
  if A[k]!=0:
    mx=min(mx,Q[k]//A[k])
p=0
for a in range(mx+1):
  b=10**9
  for k in range(N):
    if Q[k]-A[k]*a>=0 and B[k]!=0:
      b=min(b,(Q[k]-A[k]*a)//B[k])
  p=max(p,a+b)
print(p)
##################################################
