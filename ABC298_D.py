###################################

#AC by DEQUE VERSION
import sys
input = sys.stdin.readline
from collections import deque
mod=998244353
Q=int(input())
X=deque()
X.append(1)
ANS=1
for tests in range(Q):
    L=list(map(int,input().split()))
    if L[0]==1:
        x=L[1]
        X.append(x)
        ANS=(ANS*10+x)%mod
    elif L[0]==2:
        x=X.popleft()
        ANS=(ANS-x*pow(10,len(X),mod))%mod #powの第３引数としてmodを入れることで高速化
    else:
        print(ANS%mod)       
        
###################################

#TLE by DEQUE VERSION
import sys
input = sys.stdin.readline
from collections import deque
mod=998244353
Q=int(input())
X=deque()
X.append(1)
ANS=1

for tests in range(Q):
    L=list(map(int,input().split()))
    if L[0]==1:
        x=L[1]
        X.append(x)
        ANS=(ANS*10+x)%mod　#都度ANSを更新
    elif L[0]==2:
        x=X.popleft()　#xは削除する数字
        ANS=(ANS-x*pow(10,len(X)))%mod
    else:
        print(ANS%mod)
        
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
