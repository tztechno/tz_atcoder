//abc330_b.py
####################################
####################################
####################################
####################################
####################################
####################################
n, l, r = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

for i in range(n):
    if a[i] < l:
        print(l, end=" ")
    elif r < a[i]:
        print(r, end=" ")
    else:
        print(a[i], end=" ")
print("")
####################################
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for num in A:
    if num <= L:
        ans.append(L)
    elif num >= R:
        ans.append(R)
    else:
        ans.append(num)
print(' '.join(map(str, ans)))

####################################
import sys
input = sys.stdin.readline

N,L,R=map(int,input().split())
A=list(map(int,input().split()))

for a in A:
    if L<=a<=R:
        print(a)
    elif a<L:
        print(L)
    else:
        print(R)
####################################
N,L,R=map(int,input().split())
A=list(map(int,input().split()))
for a in A:
    if L<=a<=R:
        print(a)
    elif a<L:
        print(L)
    else:
        print(R)
要素との差が最小の数字、L,R,Ai
####################################
[MY TLE]
N,L,R=map(int,input().split())
A=list(map(int,input().split()))
ANS=[]
for i in range(N):
  MIN=10**9
  minj=10**9
  for j in range(L,R+1):
    if MIN>abs(j-A[i]):
      MIN=abs(j-A[i])
      minj=j
  ANS+=[minj]
print(*ANS)  
####################################
