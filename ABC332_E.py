#ABC332_E
#kyopro_friends


N,D=map(int,input().split())
A=list(map(int,input().split()))

w_list=[3*10**18]*(1<<N)
for s in range(1,1<<N):
  w=sum(A[i] for i in range(N) if (s>>i)&1)
  w_list[s]=w

dp=[w**2 for w in w_list]
for _ in range(2,D+1):
  new_dp=[3*10**18]*(1<<N)
  for s in range(1,1<<N):
    t=s
    while True:
      t=(t-1)&s
      if t==0: break
      new_dp[s]=min(new_dp[s],dp[s^t]+w_list[t]**2)
  dp=new_dp

print((dp[-1]*D-sum(A)**2)/D**2)

