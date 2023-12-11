# ABC332_E

for s in range(1<<N):
  w = sum( A[i] for i in range(N) if (s>>i)&1 )
  w_list[s]=w


w = 0
for i in range(N):
    if (s>>i)&1:
        w += A[i]


// i番目のビットが次のバイナリ表現で設定されているかどうかを確認します。
// true の場合、i 番目の項目が現在のサブセットに含まれていることを意味します。


dp=[w**2 for w in w_list]

for _ in range(2,D+1):
  new_dp=[3*10**18]*(1<<N)
  for s in range(1<<N):
    t=s
    while t:
      new_dp[s]=min(new_dp[s],dp[s^t]+w_list[t]**2)
      t=(t-1)&s
  dp=new_dp


