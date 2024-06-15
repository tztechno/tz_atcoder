abc358_c.py
##########################################
先に特定商品のある店をpickupしてproductを作るのは遅い
全ての店選択組み合わせに対して商品の有無を調べる
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
n,m = map(int,input().split())
S = [input() for _ in range(n)]
ans = n
for i in range(1<<n):
  if all(any(S[k][j] == 'o' for k in range(n) if i>>k&1) for j in range(m)):
    ans = min(ans,bin(i).count('1'))
print(ans)
##########################################
N, M = map(int, input().split())
S = [int(input().translate(str.maketrans("xo", "01")), 2) for _ in range(N)]
#print(S)
ans = N
for i in range(1<<N):
  M_check = 0
  for j in range(N):
    if i>>j & 1:
      M_check |= S[j]
  if bin(M_check).count("1") == M:
    ans = min(ans, bin(i).count("1"))
print(ans)
##########################################
n,m=map(int,input().split())
s=[list(input()) for i in range(n)]

def solve(a,b):
    for i in range(m):
        if a[i]=="o" or b[i]=="o":
            a[i]="o"
    return a

ans=n
for i in range(2**n):
    t=list("x"*m)
    cnt=0
    for j in range(n):
        if i>>j&1:
            cnt+=1
            t=solve(t,s[j])
    if t.count("o")==m:
        ans=min(ans,cnt)
print(ans)
    
##########################################
# Popcorn
def bit(s: str) -> int:
    return sum(1 << i for i, c in enumerate(s) if c == 'o')


def rec(bought: int, visited: int, now, best):
    if bought == complete:
        return visited.bit_count()
    for store in range(now, N):
        if (1 << store) & visited:
            continue
        if S[store] ^ bought:
            best = min(best, rec(bought | S[store], visited | (1 << store), store, best))
    return best


N, M = map(int, input().split())
S = [bit(input()) for _ in range(N)]

complete = (1 << M) - 1
ans = rec(0, 0, 0, M * 2)
print(ans)

##########################################
n, m = map(int, input().split())
s_s = [input() for _ in range(n)]


result = m
for bit in range(1 << n):
    current_status = ["x"] * m
    str_boolean = bin(bit)[2:].zfill(n)
    for idx, boolean in enumerate(str_boolean):
        if boolean == "0":
            continue
        selected_shop = s_s[idx]
        for j in range(len(selected_shop)):
            if selected_shop[j] == "o":
                current_status[j] = "o"
        if current_status.count("o") == m:
            if result > str_boolean.count("1"):
                result = str_boolean.count("1")

print(result)
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
[my AC]
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
S=[]
for i in range(n):
  s=str(input())
  S+=[s]
ANS=set()
for i in range(1<<n):#店の組み合わせ,shop数n3,商品数m5
  shops=bin(i)[2:].zfill(n)#01の文字列
  #print(shops)
  ans='x'*m#商品が揃うかどうか
  for j,spi in enumerate(list(shops)):
    if spi=='1':#選ばれた店、S[j]購入可能商品
      ans = ''.join('o' if a=='o' or b=='o' else 'x' for a,b in zip(ans,S[j]))
      #print(ans)
  #print(ans)#　組み合わせ毎の結論
  #print(ans)
  if ans=='o'*m:#全商品が購入できた場合
    ANS.add(shops.count('1'))
#print(ANS)
print(min(ANS))
##########################################
[my AC]
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
S=[]
for i in range(n):
  s=str(input())
  s=s.replace('x','0').replace('o','1')
  S+=[s]
ANS=set()
for i in range(1<<n):#店の組み合わせ
  #print(bin(i)[2:].zfill(n))
  sp=bin(i)[2:].zfill(n)
  ans='0'*m
  for j,spi in enumerate(list(sp)):
    if spi=='1':
      ans = ''.join('1' if a == '1' or b == '1' else '0' for a, b in zip(ans,S[j]))
  #print(ans)
  if ans=='1'*m:
    ANS.add(sp.count('1'))
print(min(ANS))

##########################################
[my TLE]
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
from collections import defaultdict,deque,Counter
cnt = defaultdict(deque)
for i in range(n):
  s=list(input())
  for j in range(m):
    if s[j]=='o':
      cnt[j].append(i)
#print(cnt)
P=[]
for j in range(m):
  P+=[cnt[j]]
from itertools import product,permutations,combinations,accumulate
#print(P)
C=list(product(*P))
#print(C)
A=n
for ci in C:
  t=len(set(ci))
  A=min(A,t)
print(A)
##########################################
[my TLE]
n,m=map(int,input().split())
P=[]
for j in range(m):
  P+=[[]]
for i in range(n):
  s=list(input())
  for j in range(m):
    if s[j]=='o':
      P[j]+=[i]
#print(P)
from itertools import product,permutations,combinations,accumulate
C=list(product(*P))
#print(C)
A=n
for ci in C:
  t=len(set(ci))
  A=min(A,t)
print(A)
  
##########################################
