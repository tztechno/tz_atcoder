    
###################################

#TLE by DEQUE VERSION
from collections import deque
import sys
input = sys.stdin.readline

q = int(input())
S = deque([1]) 
mod = 998244353

for i in range(q):
  Q = list(map(int, input().split()))
  if Q[0] == 1:
    x = Q[1]
    S.append(x)#右側から要素を加える
  elif Q[0] == 2:
    S.popleft()#左端の要素お削除する 
  elif Q[0] == 3:
    num = 0
    for si in S:
      num = num * 10 + si #要素が１桁の数字なので数値のまま変換
    print(num % mod)
    
###################################

#TLE by LIST VERSION
import sys
input = sys.stdin.readline
q=int(input())
S=[1]
mod=998244353
for i in range(q):
  Q=list(map(int,input().split()))
  #print(Q)
  if Q[0]==1:
    x=Q[1]
    S+=[x]#右側から要素を加える
  elif Q[0]==2:
    S=S[1:]#左端の要素を削除する
  elif Q[0]==3:
    s=''
    for si in S:
      s+=str(si)
    print(int(s)%mod)
    
###################################
