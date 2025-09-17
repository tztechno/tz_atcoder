
###############################################
'''
N棟のビルが等間隔に一列に並んでいます。
手前からi番目のビルの高さはHiです。
あなたは次の条件をともに満たすようにいくつかのビルを選んで電飾で飾ろうとしています。
* 選んだビルたちは高さが等しい
* 選んだビルたちは等間隔に並んでいる
最大でいくつのビルを選ぶことができますか？　
'''
###############################################
[deepseek TLE]

def main():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    H = list(map(int, data[1:1+n]))
    
    cnt = defaultdict(list)
    for i, h in enumerate(H):
        cnt[h].append(i)
    
    ans = 1
    for key, indices in cnt.items():
        m = len(indices)
        if m <= ans:
            continue
            
        # すべての可能な公差を試す
        # ただし、隣接するインデックスの差の約数に限定
        max_len = 1
        
        # すべてのペア (i, j) を試す
        for i in range(m):
            for j in range(i+1, m):
                d = indices[j] - indices[i]
                if d == 0:
                    continue
                
                # この公差で等差数列を探す
                count = 2
                current = indices[j]
                next_idx = j + 1
                
                # 次の要素を探す
                while next_idx < m:
                    if indices[next_idx] - current == d:
                        count += 1
                        current = indices[next_idx]
                        next_idx += 1
                    elif indices[next_idx] - current > d:
                        break
                    else:
                        next_idx += 1
                
                if count > max_len:
                    max_len = count
        
        if max_len > ans:
            ans = max_len
    
    print(ans)

if __name__ == '__main__':
    main()
###############################################
###############################################
###############################################
###############################################
###############################################

###############################################
###############################################
###############################################
###############################################
###############################################

###############################################
###############################################
[cgpt]

---

#i--jが欲しい数列の範囲

```python
    dp = [defaultdict(int) for _ in range(k)]
    # dp[j][d] = 長さ（idxs[i], idxs[j]) が公差 d の等差数列
```

* DP（動的計画法）の配列を用意。
* `dp[j][d]` は「`idxs[j]` を終点とし、公差 d の等差数列の長さ - 1（対の数）」を保持する。
* `defaultdict(int)` にしておくことで、未定義の公差 d にアクセスしても自動で 0 になる。

---

```python
    for j in range(k):
        for i in range(j):
            d = idxs[j] - idxs[i]
            dp[j][d] = max(dp[j][d], dp[i][d] + 1)
            ans = max(ans, dp[j][d] + 1)  # +1 で長さに換算
```

* 同じ高さの出現位置の組 $(i,j)$ を選んで、公差 $d = idxs[j] - idxs[i]$ を計算する。
* `dp[i][d]` が「i を終点とする長さ - 1」なので、それに `+1` して j に継続する。
* つまり「等差数列を伸ばす」処理。
* 更新した値に 1 を足して、実際の長さ（要素数）に換算し、`ans` を更新。

---

## まとめ

このプログラムは：

2. そのインデックス列の中で「公差が同じ」位置を選び続け、最長の等差数列を探す
3. すべての高さについて調べ、最長の長さを答えにする

---

###############################################
[cgpt AC]
from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))

# 高さごとに出現位置を集める
pos = defaultdict(list)
for i, h in enumerate(H):
    pos[h].append(i)

ans = 1
for h, idxs in pos.items():
    k = len(idxs)
    if k <= ans:  # すでにこれより大きい答えがあるなら飛ばす
        continue

    dp = [defaultdict(int) for _ in range(k)]
    # dp[j][d] = 長さ（idxs[i], idxs[j]) が公差 d の等差数列

    for j in range(k):
        for i in range(j):
            d = idxs[j] - idxs[i]
            dp[j][d] = max(dp[j][d], dp[i][d] + 1)
            ans = max(ans, dp[j][d] + 1)  # +1 で長さに換算

print(ans)

###############################################
[my WA]
'''
N棟のビルが等間隔に一列に並んでいます。
手前からi番目のビルの高さはHiです。
あなたは次の条件をともに満たすようにいくつかのビルを選んで電飾で飾ろうとしています。
* 選んだビルたちは高さが等しい
* 選んだビルたちは等間隔に並んでいる
最大でいくつのビルを選ぶことができますか？　
'''
N=int(input())
H=list(map(int,input().split()))
from collections import defaultdict,deque,Counter
cnt = defaultdict(list)
S=set(H)
for i,h in enumerate(H):
  cnt[h].append(i)
for s in S:
  idx=cnt[s]
  count=len(idx)
  #idxのリストの中で等差の最大長を探す
  #あり得る差は1--count
  #idxのリストのiが始点、jが終点、しかし、jumpあり得る
  #DPの使い方がわからない
  #限界、ここまで

###############################################

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
