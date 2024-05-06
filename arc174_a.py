arc174_a.py
################################################
################################################
################################################
################################################
################################################
################################################
[titia]
import sys
input = sys.stdin.readline

N,C=map(int,input().split())
A=list(map(int,input().split()))

S=[0]
for a in A:
    S.append(S[-1]+a)

MAX=[-1<<63]*(len(S))
MIN=[1<<63]*(len(S))

for i in range(len(S)):
    MIN[i]=min(MIN[i],S[i])
    if i>=1:
        MIN[i]=min(MIN[i],MIN[i-1])

for i in range(len(S)-1,-1,-1):
    MAX[i]=max(MAX[i],S[i])
    if i<len(S)-1:
        MAX[i]=max(MAX[i],MAX[i+1])


M=-1<<63

for i in range(len(S)):
    M=max(M,MAX[i]-MIN[i])


MAX=[-1<<63]*(len(S))
MIN=[1<<63]*(len(S))

for i in range(len(S)):
    MAX[i]=max(MAX[i],S[i])
    if i>=1:
        MAX[i]=max(MAX[i],MAX[i-1])

for i in range(len(S)-1,-1,-1):
    MIN[i]=min(MIN[i],S[i])
    if i<len(S)-1:
        MIN[i]=min(MIN[i],MIN[i+1])


M2=1<<63

for i in range(len(S)):
    M2=min(M2,MIN[i]-MAX[i])


SUM=sum(A)
ANS1=SUM+(C-1)*M
ANS2=SUM+(C-1)*M2

print(max(SUM,ANS1,ANS2))

################################################
n,c=map(int,(input().split()))
a=list(map(int,input().split()))

ans=sum(a)
r=0
csum=0
m=0

if c>=1:
  for v in a:
    csum+=v
    m=min(m,csum)
    r=max(r,csum-m)
else:
  for v in a:
    csum+=v
    m=max(m,csum)
    r=min(r,csum-m)

ans+=(c-1)*r
print(ans)
################################################
[MY WA,TLE]
N,C=map(int,input().split())
A=list(map(int,input().split()))
R=[0]
for a in A:
  R+=[R[-1]+a]
WMIN=10**12
WMAX=0
for l in range(1,N+1):
  for r in range(l,N+1):
    W=R[r]-R[l-1]
    WMAX=max(WMAX,W)
    WMIN=min(WMIN,W)
if C<0:
  print(R[-1]+WMIN*(C-1))
elif C>0:
  print(R[-1]+WMAX*(C-1))
elif C==0:
  print(R[-1]-WMAX)
################################################
