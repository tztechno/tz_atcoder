abc373_e.py
######################################################
二分木
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################

n,X,K=map(int,input().split())
a=list(map(int,input().split()))
A=sum(a)
ans=[0]*n
a=[(a[i],i) for i in range(n)]
a.sort()
b=[v for v,_ in a]
ca=[0]+[v for v,_ in a]
for i in range(n):
  ca[i+1]+=ca[i]
from bisect import bisect_left,bisect_right
for i in range(n):
  v,p=a[i]
  ok=K+1
  ng=-1
  while ok-ng>1:
    m=(ok+ng)//2
    g=0
    r=bisect_left(b,v+m+1)
    u=n-r
    if u>=X:
      ng=m
      continue
    if i+X<n:
      g=(v+m+1)*(X-u)-(ca[n-u]-ca[n-X])
    else:
      g=(v+m+1)*(X-u)-(ca[n-u]-ca[n-X-1]-v)
    if g+m>K-A:
      ok=m
    else:
      ng=m
  ans[p]=ok if ok<=K-A else -1
print(*ans)

######################################################
[not understand]

from bisect import bisect_left
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
if m==n: exit(print(*[0]*n))
b = sorted(a); c = []; d = k-sum(a); s = b[:]
for i in range(1,n): s[-i-1] += s[-i]
s.append(0)
for v in a:
    i = bisect_left(b,v)
    if n-i<=m:
        wa = -1; ac = d+2
        while ac-wa>1:
            wj = (wa+ac)//2; j = bisect_left(b,v+wj+1)
            if m>=n-j and (v+wj+1)*(m-(n-j))-(s[-m-2]-v-s[j])>d-wj: ac = wj
            else: wa = wj
    else:
        wa = -1; ac = d+2
        while ac-wa>1:
            wj = (wa+ac)//2; j = bisect_left(b,v+wj+1)
            if m>=n-j and (v+wj+1)*(m-(n-j))-(s[-m-1]-s[j])>d-wj: ac = wj
            else: wa = wj
    c.append(ac if ac<=d else -1)
print(*c)

######################################################
[not understand]

import sys
input = sys.stdin.readline
from bisect import bisect

N,M,K=map(int,input().split())
A=list(map(int,input().split()))

if N==M:
    ANS=[0]*N
    print(*ANS)
    exit()

rest=K-sum(A)

B=[]
for i in range(N):
    B.append((A[i],i))

B.sort()

C=[B[i][0] for i in range(len(B))]
S=[0]
for c in C:
    S.append(S[-1]+c)

def check(ind,plus):
    nokori=rest-plus

    now=C[ind]+plus
    need=now+1

    x=bisect(C,need)

    #print(rest,need,nokori,x)

    if ind>=N-M:
        if x<N-M-1:
            return False
        SUM=need * (x-(N-M-1)-1) - (S[x]-S[N-M-1]-C[ind])

        #print(SUM,(x-(N-M-1)-1) , (S[x]-S[N-M-1]-C[ind]))

        if SUM<=nokori:
            return False
        else:
            return True
            
    else:
        if x<N-M:
            return False
        SUM=need * (x-(N-M)) - (S[x]-S[N-M])

        #print("?",SUM,(x-(N-M)) , (S[x]-S[N-M]))

        if SUM<=nokori:
            return False
        else:
            return True

ANS=[-1]*N

for i in range(N):
    if check(i,rest)==False:
        ANS[B[i][1]]=-1
        continue
    if check(i,0)==True:
        ANS[B[i][1]]=0
        continue

    OK=rest
    NG=0

    while OK>NG+1:
        mid=(OK+NG)//2

        if check(i,mid)==True:
            OK=mid
        else:
            NG=mid

    #print(OK)

    ANS[B[i][1]]=OK

print(*ANS)

######################################################
