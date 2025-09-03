##################################################################
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); T = int(next(it))
    S = list(next(it))
    X = [int(next(it)) for _ in range(N)]
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[mybrain2 TLE26]同程度に遅い
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); T = int(next(it))
    S = list(next(it))
    X = [int(next(it)) for _ in range(N)]
    
    mp = {'1': 1, '0': -1}
    G = []
    for i in range(N):
        g_val = X[i] + mp[S[i]] * (T + 0.1)
        G.append(g_val)
    
    XG = list(zip(X, G))
    XG.sort(key=lambda p: p[0])   # xでソート
    #print('XG',XG)
    
    # gの値を座標圧縮
    g_list = [g for x, g in XG]
    sorted_g = sorted(set(g_list))
    #print('sorted_g',sorted_g)
    
    comp_map = {}
    for idx, val in enumerate(sorted_g):
        comp_map[val] = idx + 1   # 1-indexed
    comp_g = [comp_map[g] for g in g_list]
    #print('comp_g',comp_g)
    
    # Fenwick Treeクラス
    class Fenw:
        def __init__(self, n):
            self.n = n
            self.tree = [0] * (n+1)
        def update(self, index, delta):
            while index <= self.n:
                self.tree[index] += delta
                index += index & -index
        def query(self, index):
            s = 0
            while index:
                s += self.tree[index]
                index -= index & -index
            return s
    ans=0
    n = len(comp_g)
    for i in range(n):
      for j in range(i+1,n):
        if comp_g[i]>comp_g[j]:
          ans+=1

    print(ans)

if __name__ == '__main__':
    main()
##################################################################
[deepseek1 説明]
6 3
101010
-5 -1 0 1 2 4
---------
XG [(-5, -1.9), (-1, -4.1), (0, 3.1), (1, -2.1), (2, 5.1), (4, 0.8999999999999999)]
sorted_g [-4.1, -2.1, -1.9, 0.8999999999999999, 3.1, 5.1]
comp_g [3, 1, 5, 2, 6, 4]
ans 5
##################################################################
[deepseek1 説明]

## 問題の本質

元のコードは、すべてのペア (i, j) について以下の条件をチェックしていました：
- x_i > x_j かつ g_i < g_j
- x_i < x_j かつ g_i > g_j

これは要するに、「x座標とg座標の大小関係が逆転しているペア」を数える問題です。

## 効率化の鍵

### 1. ソートによる次元削減
x座標でソートすることで、問題を単純化します。ソート後は：
- i < j ならば必ず x_i ≤ x_j（xが同じ場合はないと仮定）
- したがって、条件は「g_i > g_j」のみを考えればよい

### 2. 転倒数問題への帰着
ソート後、問題は「gの配列の中で、i < j かつ g_i > g_j となるペアの数を数える」という**転倒数**問題に帰着されます。

### 3. Fenwick Treeによる効率的な転倒数計算
転倒数はFenwick Tree（Binary Indexed Tree）を使って効率的に計算できます：
- **後ろから前へ**処理を行う
- 各要素について、**既に処理した要素（右側の要素）の中で現在の値より小さい値の個数**を数える
- これがまさに転倒数となる

## アルゴリズムの流れ

1. **データ準備**: xとgのペアを作成
2. **xでソート**: 問題を1次元に削減
3. **座標圧縮**: gの値を連続した整数にマッピング（Fenwick Treeの効率化のため）
4. **Fenwick Treeで転倒数計算**: 後ろから処理して転倒数を累計
5. **結果出力**

## なぜこれで正しいのか？

元の条件：
- (x_i > x_j かつ g_i < g_j) または (x_i < x_j かつ g_i > g_j)

ソート後（x昇順）：
- i < j ならば x_i < x_j（xがユニークと仮定）
- したがって条件は (g_i > g_j) のみ
- もう一方の条件 (x_i > x_j かつ g_i < g_j) は、i > j の場合に対応するが、これはペア(i,j)と(j,i)が同じなので重複カウントを避けるため片方だけで十分

## 計算量の比較

- **元のコード**: O(N²) - 二重ループですべてのペアをチェック
- **改善後**: O(N log N) - ソート、座標圧縮、Fenwick Tree操作

Nが大きい場合（例: N=10⁵）、O(N²)は10¹⁰回の操作が必要ですが、O(N log N)は約10⁶回の操作で済み、劇的な改善になります。

##################################################################
[depseek1 AC]
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); T = int(next(it))
    S = list(next(it))
    X = [int(next(it)) for _ in range(N)]
    
    mp = {'1': 1, '0': -1}
    G = []
    for i in range(N):
        g_val = X[i] + mp[S[i]] * (T + 0.1)
        G.append(g_val)
    
    XG = list(zip(X, G))
    XG.sort(key=lambda p: p[0])   # xでソート
    
    # gの値を座標圧縮
    g_list = [g for x, g in XG]
    sorted_g = sorted(set(g_list))
    comp_map = {}
    for idx, val in enumerate(sorted_g):
        comp_map[val] = idx + 1   # 1-indexed
    comp_g = [comp_map[g] for g in g_list]
    
    # Fenwick Treeクラス
    class Fenw:
        def __init__(self, n):
            self.n = n
            self.tree = [0] * (n+1)
        def update(self, index, delta):
            while index <= self.n:
                self.tree[index] += delta
                index += index & -index
        def query(self, index):
            s = 0
            while index:
                s += self.tree[index]
                index -= index & -index
            return s
    
    n = len(comp_g)
    fenw = Fenw(n)
    ans = 0
    # 後ろから見ていくことで、転倒数を数える
    for i in range(n-1, -1, -1):
        idx = comp_g[i]
        ans += fenw.query(idx-1)   # 現在より小さい値の個数を加算
        fenw.update(idx, 1)
    
    print(ans)

if __name__ == '__main__':
    main()
##################################################################
[mybrain1 解釈]
mp={'1':1,'0':-1}
1は右側、-1は左側
ans=0
G=[]
for i in range(N):
  G+=[X[i]+mp[S[i]]*(T+0.1)]
どこまで進むか
XG=[]
for x,g in zip(X,G):
  XG+=[(x,g)]
自分自身のstart,goalのペア
総当たり、自分と他
位置関係が逆転しているかどうかチェックしている
for i in range(N):  
  for j in range(i+1,N):
    if XG[i][0]>XG[j][0] and XG[i][1]<XG[j][1]:
      ans+=1
    elif XG[i][0]<XG[j][0] and XG[i][1]>XG[j][1]:
      ans+=1
print(ans)
##################################################################
[mybrain1 TLE26]
N,T=map(int,input().split())
S=list(input())
X=list(map(int,input().split()))
mp={'1':1,'0':-1}
ans=0
G=[]
for i in range(N):
  G+=[X[i]+mp[S[i]]*(T+0.1)]
XG=[]
for x,g in zip(X,G):
  XG+=[(x,g)]
for i in range(N):  
  for j in range(i+1,N):
    if XG[i][0]>XG[j][0] and XG[i][1]<XG[j][1]:
      ans+=1
    elif XG[i][0]<XG[j][0] and XG[i][1]>XG[j][1]:
      ans+=1
print(ans)
##################################################################
[myai TLE]
def solve_ant_crossing_with_time(n, t, x_coords, directions):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            xi, xj = x_coords[i], x_coords[j]
            di, dj = int(directions[i]), int(directions[j])
            crossing_time = None
            if xi < xj and di == 1 and dj == 0:
                crossing_time = (xj - xi) / 2.0
            elif xi > xj and di == 0 and dj == 1:
                crossing_time = (xi - xj) / 2.0
            if crossing_time is not None and 0 <= crossing_time <= t + 0.1:
                count += 1
    return count

import sys

line1 = sys.stdin.readline().strip().split()
n = int(line1[0])
t = int(line1[1])

s = sys.stdin.readline().strip()
x_coords = list(map(int, sys.stdin.readline().strip().split()))

result = solve_ant_crossing_with_time(n, t, x_coords, s)
print(result)
##################################################################
