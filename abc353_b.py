abc353_b.py
##################################################
##################################################
##################################################
##################################################
##################################################
[shakayami]
N,K=map(int,input().split())
A=[int(i) for i in input().split()][::-1]

ans=0
X=0
while(A):
    if X+A[-1]<=K:
        X+=A.pop()
    else:
        ans+=1
        X=0
if X>0:
    ans+=1
print(ans)

##################################################
[titia]
input = sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

ANS=0
NOW=0
for i in range(N):
    if NOW==0:
        NOW+=A[i]
        ANS+=1
    else:
        if NOW+A[i]<=K:
            NOW+=A[i]
        else:
            ANS+=1
            NOW=A[i]

print(ANS)
##################################################
[dmi]
def main():
    import sys
    _, K = [int(v) for v in sys.stdin.readline().split()]
    A = [int(v) for v in sys.stdin.readline().split()]
    i = 0
    ans = 0
    while i < len(A):
        j = i
        k = 0
        while j < len(A) and k + A[j] <= K:
            k += A[j]
            j += 1
        ans += 1
        i = j
    print(ans)


if __name__ == "__main__":
    main()
##################################################
[boo]
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
count = 0
for i in range(N):
    if count + A[i] <= K:
        count += A[i]
    else:
        count = A[i]
        ans += 1
print(ans)
##################################################
[ksy]
from typing import List

def B(n:int, k:int, a:List[int]):
    remain_k = k
    attraction_start_count = 0
    for _ in range(n):
        n_person = a.pop()
        if n_person <= remain_k:
            remain_k -= n_person
        else:
            attraction_start_count += 1
            remain_k = k - n_person
    if remain_k != k:
        attraction_start_count += 1
        remain_k = k
    print(attraction_start_count)

if __name__ == '__main__':

    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    B(n, k, a)
##################################################
[my AC]
N,K=map(int,input().split())
A=list(map(int,input().split()))
T=0
R=K
for i,a in enumerate(A):
  if R==K:
    T+=1
    R-=a
  elif R<K and R>=a:
    R-=a
  elif R<K and R<a:
    R=K
    T+=1
    R-=a
print(T)
##################################################
