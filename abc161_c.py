abc161_c.py
########################################
########################################
########################################
N, K = map(int,input().split())
a = N // K 
num = N
ans = N
if N >= K:
  num = N - a*K
for i in range(2):
  p = K - num
  ans = min(ans,p)
  num = p
print(ans)
########################################
N,K=map(int,input().split())
R1=N%K
R2=abs(K-R1)
print(min(R1,R2))
########################################
[my WA]
N,K=map(int,input().split())
R1=N%K
R2=K%R1
print(min(R1,R2))
########################################
[my WA]
N,K=map(int,input().split())
def change(x):
  x=abs(x-K)
  return x
ANS=set()
for i in range(N):
  N=change(N)
  ANS.add(change(N))
print(min(ANS))
########################################
