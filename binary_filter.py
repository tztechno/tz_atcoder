
for s in range(1<<N):
  w = sum( A[i] for i in range(N) if (s>>i)&1 )
  w_list[s]=w


w = 0
for i in range(N):
    if (s>>i)&1:
        w += A[i]


// i番目のビットが次のバイナリ表現で設定されているかどうかを確認します。
// true の場合、i 番目の項目が現在のサブセットに含まれていることを意味します。
