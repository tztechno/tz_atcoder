##################################################################
長さNの非負整数列A=(A1​,A2​,…,AN​),B=(B1​,B2​,…,BN​)と正整数Mが与えられます。
Aの要素を自由に並び替えることが出来るとき、i=1∑N​((Ai​+Bi​)modM)としてありうる最小値を求めて下さい。
T個のテストケースが与えられるので、それぞれについて答えを求めてください。
##################################################################

この問題に対して、現在の**貪欲法（Greedy Algorithm）が常に最適解を与える**ことを、**数学的・アルゴリズム的に証明**してみましょう。

---

## 🔧 問題の定式化

与えられた：

* 整数の列 $A = [a_1, a_2, ..., a_n]$
* 整数の列 $B = [b_1, b_2, ..., b_n]$
* 整数のしきい値 $M$

各 $a_i \in A$, $b_j \in B$ からペア $(a_i, b_j)$ を1対1で選び、
**$a_i + b_j \geq M$** を満たすペアの数を最大化したい。

---

## 🧠 主張（Theorem）

> 並び替えた $A$（降順）と $B$（昇順）に対して、
> **左から順に貪欲に $a_i + b_j \geq M$ を満たすペアを作る戦略は、常に最適なペア数を与える。**

---

## ✅ 証明の概要（交換法による貪欲法の最適性の証明）

この種の問題では、以下の手法が有効です：

* **貪欲法による解を「最適解と比較」し、必要なら交換によって貪欲解に変換可能であることを示す**。

---

### ステップ 1: ソート前提

まず、以下のように並べ替える：

* $A = [a_1, ..., a_n]$, ただし $a_1 \geq a_2 \geq \cdots \geq a_n$
* $B = [b_1, ..., b_n]$, ただし $b_1 \leq b_2 \leq \cdots \leq b_n$

貪欲法は：

* $a_1$ に最小の $b_j$ を割り当てて $a_1 + b_j \geq M$ になる最小の $j$ を探し、使う。
* 以下、残りも同様。

---

### ステップ 2: 最適解との比較

任意の最適解を考える。
それも 1対1 のペアであり、個数を最大化する。

仮に最適解の中に「貪欲法とは異なる選択」をしている部分があるとする。

#### 例（矛盾を導くための構成）：

* 貪欲法では $(a_1, b_1)$ を選んだが、
* 最適解では $(a_1, b_2), (a_2, b_1)$ のように異なる割り当てをしている。

このとき：

* $a_1 \geq a_2$
* $b_1 \leq b_2$

なので：

$$
a_1 + b_1 \geq a_2 + b_1,\quad a_1 + b_1 \geq a_1 + b_2
$$

つまり、**ペアの交換により条件を悪化させることはない**。

→ よって、最適解を「貪欲法の順に合わせて書き換える」ことができる。

---

### ステップ 3: 交換操作の繰り返し

最適解と貪欲法解の間に「違うマッチング」があったとしても：

* 上記の交換操作を繰り返すことで、
* **最適解を貪欲法のペア列に変換できる**
* しかもペア数は減らない（条件を満たすペアだけを使っている）

→ したがって、貪欲法と同じかそれ以上のペア数になる。

---

## ✅ 結論

最適解は、貪欲法の手順で得られるペア列に変形できる。
よって、**貪欲法で得られる解は最適である**。

---

## 📚 補足：これは「マッチング問題」の特殊ケース

この問題は実は「二部マッチング（bipartite matching）」の簡略版です：

* $A$ 側と $B$ 側をノードとし、条件 $a_i + b_j \geq M$ を満たす辺を張る。
* このグラフ上で**最大マッチングを求める問題**。

通常はホップクロフト–カルプ法などを使って解く必要がありますが、
この問題のように**AとBに明確な順序（単調性）を持たせた場合**は、
貪欲法が最適解を与えることが知られています。

---

## 🏁 結論まとめ

| 項目   | 内容                                  |
| ---- | ----------------------------------- |
| 問題   | AとBから、$a_i + b_j \geq M$ を満たすペアの最大数 |
| 戦略   | A: 降順、B: 昇順にソートして左から順に貪欲に組む         |
| 証明方法 | 最適解との交換操作による一致（交換法）                 |
| 結論   | この貪欲法は常に最適解を与える                     |

---

##################################################################

##################################################################

##################################################################
[ngid] modify
T = int(input())
cases = []
for i in range(T):
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A = sorted(A)
    B = sorted(B, reverse=True)
    n = len(A)
    pairs = 0
    i = 0
    j = 0
    for i in range(n):
        while j < n and A[i] + B[j] < M:
            j += 1
        if j >= n:
            break
        pairs += 1
        j += 1
    res = sum(A) + sum(B) - pairs * M
    print(res)
##################################################################
[claude WA]
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # BをMで割った余りでグループ分け
    b_groups = [[] for _ in range(M)]
    for i, b in enumerate(B):
        b_groups[b % M].append(b % M)
    
    # AをMで割った余りでソート（昇順）
    a_remainders = sorted([a % M for a in A])
    
    total_sum = 0
    a_idx = 0
    
    # 各余りクラスに対して最適な割り当てを行う
    for remainder in range(M):
        group_size = len(b_groups[remainder])
        if group_size == 0:
            continue
        
        # この余りクラスに対して最小コストを計算
        min_cost = float('inf')
        best_start = 0
        
        # 全ての可能な開始位置を試す
        for start in range(N):
            cost = 0
            temp_idx = start
            for _ in range(group_size):
                cost += (a_remainders[temp_idx % N] + remainder) % M
                temp_idx += 1
            
            if cost < min_cost:
                min_cost = cost
                best_start = start
        
        total_sum += min_cost
        
        # 使用したAの要素を削除（実際には別のアプローチを使用）
        
    return total_sum

# より効率的な解法
def solve_optimized():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # BをMで割った余りでカウント
    b_count = [0] * M
    for b in B:
        b_count[b % M] += 1
    
    # AをMで割った余りでソート
    a_remainders = sorted([a % M for a in A])
    
    total_sum = 0
    used = [False] * N
    
    # 各余りクラスr（0からM-1）について処理
    for r in range(M):
        if b_count[r] == 0:
            continue
        
        # このrに対して最適なAの要素を選択
        candidates = []
        for i in range(N):
            if not used[i]:
                cost = (a_remainders[i] + r) % M
                candidates.append((cost, i))
        
        # コストでソートして最小のものを選択
        candidates.sort()
        
        for j in range(min(b_count[r], len(candidates))):
            cost, idx = candidates[j]
            total_sum += cost * 1  # この余りクラスでの使用回数
            used[idx] = True
            b_count[r] -= 1
    
    return total_sum

# 最も効率的な解法
def solve_final():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # BをMで割った余りでカウント
    b_count = [0] * M
    for b in B:
        b_count[b % M] += 1
    
    # AをMで割った余りでカウント
    a_count = [0] * M
    for a in A:
        a_count[a % M] += 1
    
    total_sum = 0
    
    # 各Bの余りクラスについて、最適なAの余りクラスとのペアリングを見つける
    for b_rem in range(M):
        if b_count[b_rem] == 0:
            continue
        
        # このb_remに対して、最小コストとなるa_remを見つける
        min_cost_per_pair = float('inf')
        best_a_rem = -1
        
        for a_rem in range(M):
            if a_count[a_rem] > 0:
                cost = (a_rem + b_rem) % M
                if cost < min_cost_per_pair:
                    min_cost_per_pair = cost
                    best_a_rem = a_rem
        
        # 使用できる分だけペアリング
        pairs = min(b_count[b_rem], a_count[best_a_rem])
        total_sum += min_cost_per_pair * pairs
        
        # カウントを更新
        b_count[b_rem] -= pairs
        a_count[best_a_rem] -= pairs
    
    return total_sum

# メイン処理
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # BをMで割った余りでカウント
    b_count = [0] * M
    for b in B:
        b_count[b % M] += 1
    
    # AをMで割った余りでカウント  
    a_count = [0] * M
    for a in A:
        a_count[a % M] += 1
    
    total_sum = 0
    
    # 貪欲法：各ステップで最小コストのペアを選択
    while sum(b_count) > 0:
        min_cost = float('inf')
        best_a_rem = -1
        best_b_rem = -1
        
        for b_rem in range(M):
            if b_count[b_rem] == 0:
                continue
            for a_rem in range(M):
                if a_count[a_rem] == 0:
                    continue
                cost = (a_rem + b_rem) % M
                if cost < min_cost:
                    min_cost = cost
                    best_a_rem = a_rem
                    best_b_rem = b_rem
        
        if best_a_rem == -1:
            break
            
        total_sum += min_cost
        b_count[best_b_rem] -= 1
        a_count[best_a_rem] -= 1
    
    print(total_sum)  
##################################################################
[stepa]
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        A = list(map(int, data[index:index + N]))
        index += N
        B = list(map(int, data[index:index + N]))
        index += N
        
        total_sum = sum(A) + sum(B)
        A.sort()
        B.sort()
        i = 0
        k = 0
        for j in range(N - 1, -1, -1):
            if i >= N:
                break
            while i < N and A[i] + B[j] < M:
                i += 1
            if i < N:
                k += 1
                i += 1
        ans = total_sum - M * k
        results.append(str(ans))
    print("\n".join(results))

if __name__ == "__main__":
    main()
##################################################################
[oliver] same as ngid
T = int(input())
for t in range(T):
  N, M = map(int,input().split())
  A = sorted(list(map(int,input().split())), reverse=True)
  B = sorted(list(map(int,input().split())))
  c, idx = 0, 0
  for v in A:
    while idx < N and B[idx] + v < M:
      idx += 1
    if idx >= N:
      break
    c += 1
    idx += 1
  print(sum(A)+sum(B)-M*c)
##################################################################
[my WA]
T=int(input())
for i in range(T):
  N,M=map(int,input().split())
  A=sorted(list(map(int,input().split())))
  B=sorted(list(map(int,input().split())))
  ans=0
  for a,b in zip(A,B):
    ans+=(a+b)%M
  print(ans)
##################################################################
[my WA]
T=int(input())
for i in range(T):
  N,M=map(int,input().split())
  A=sorted(list(map(int,input().split())))
  B=sorted(list(map(int,input().split())))[::-1]
  ans=0
  for a,b in zip(A,B):
    ans+=(a+b)%M
  print(ans)
##################################################################
[ngid]
T = int(input())
cases = []
for i in range(T):
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A = sorted(A, reverse=True)
    B = sorted(B)
    n = len(A)
    pairs = 0
    i = 0
    j = 0
    for i in range(n):
        while j < n and A[i] + B[j] < M:
            j += 1
        if j >= n:
            break
        pairs += 1
        j += 1
    res = sum(A) + sum(B) - pairs * M
    print(res)
##################################################################
[hey]
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))
    c, idx = 0, 0
    for v in a:
        while idx < n and b[idx] + v < m:
            idx += 1
        if idx >= n:
            break
        c += 1
        idx += 1
    print(sum(a) + sum(b) - m * c)

##################################################################
[titia]
import sys
input = sys.stdin.readline

N,M=map(int,input().split())

D=[[1<<60]*(N+1) for i in range(N+1)]

for i in range(N+1):
    D[i][i]=0

for i in range(M):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    c*=2
    D[a][b]=min(D[a][b],c)
    D[b][a]=min(D[b][a],c)

K,T=map(int,input().split())
Air=list(map(int,input().split()))

for air in Air:
    D[air-1][N]=T
    D[N][air-1]=T

for k in range(N+1): # k個までの町を使ってのDisが知れているときに
    for i in range(N+1): # 町iと
        for j in range(N+1): # 町jとの最短距離は、
            length=D[i][k]+D[j][k]
            if D[i][j]>length:
                D[i][j]=D[j][i]=length

ANS=0
for i in range(N):
    for j in range(N):
        if D[i][j]<(1<<60):
            ANS+=D[i][j]

Q=int(input())
LANS=[]

for tests in range(Q):
    L=list(map(int,input().split()))
    #print(L,D)

    if L[0]==3:
        LANS.append(ANS//2)
    elif L[0]==2:
        x=L[1]-1
        D[x][N]=T
        D[N][x]=T

        for i in range(N+1):
            for j in range(i+1,N+1):
                length=min(D[i][x]+T+D[j][N],D[i][N]+T+D[j][x])

                if length<D[i][j]:
                    if i<N and j<N:
                        if D[i][j]>=(1<<60):
                            ANS+=length*2
                        else:
                            ANS-=(D[i][j]-length)*2
                    D[i][j]=length
                    D[j][i]=length
    elif L[0]==1:
        #print("!!",ANS)
        x,y,z=L[1],L[2],L[3]
        x-=1
        y-=1
        z*=2

        if D[x][y]>z:
            for i in range(N+1):
                for j in range(i+1,N+1):
                    length=min(D[i][x]+z+D[j][y],D[i][y]+z+D[j][x])

                    if length<D[i][j]:
                    
                        if i<N and j<N:
                            if D[i][j]>=(1<<60):
                                ANS+=length*2
                            else:
                                ANS-=(D[i][j]-length)*2

                        #print(D[i][j],length,ANS)
                        D[i][j]=length
                        D[j][i]=length

print(*LANS)
##################################################################
[my TLE]
import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        N, M = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        B = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        A.sort()
        B.sort()
        
        min_sum = float('inf')
        
        for i in range(N):
            current_sum = 0
            for j in range(N):
                current_sum += (A[j] + B[(j + i) % N]) % M
            min_sum = min(min_sum, current_sum)
            
            if i == 0:
                B.reverse()
                current_sum = 0
                for j in range(N):
                    current_sum += (A[j] + B[j]) % M
                min_sum = min(min_sum, current_sum)
        
        print(min_sum)

solve()
##################################################################
[my TLE]
import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    
    for _ in range(T):
        N, M = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        B = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        A.sort()
        B.sort()
        
        min_sum = float('inf')
        
        for shift in range(N):
            current_sum = 0
            for i in range(N):
                current_sum += (A[i] + B[(i + shift) % N]) % M
            min_sum = min(min_sum, current_sum)
        
        B.sort(reverse=True)
        
        for shift in range(N):
            current_sum = 0
            for i in range(N):
                current_sum += (A[i] + B[(i + shift) % N]) % M
            min_sum = min(min_sum, current_sum)
        
        print(min_sum)

solve()
##################################################################
