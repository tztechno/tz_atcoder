
abc361-f.py
#######################################
[MY TLE]
N=int(input())
A=set()
for a in range(2,N+1):
  for b in range(2,N+1):
    if a**b<=N:
      A.add(a**b)
    elif a**b>N:
      break
print(1+len(A))
#######################################
import sys
input = sys.stdin.readline

# エラトステネスの篩を用いた素因数分解・約数列挙
MAX=10**5+10 # 使いたい最大値を指定

# Sieve[i]で、iの最も小さい約数を返す。
Sieve=[i for i in range(MAX)]

for i in range(2,MAX):
    if Sieve[i]!=i:
        continue
    
    for j in range(i,MAX,i):
        if Sieve[j]==j:
            Sieve[j]=i

# 素因数分解
def fact(x):
    D=dict()
    while x!=1:
        k=Sieve[x]
        if k in D:
            D[k]+=1
        else:
            D[k]=1
        x//=k
    return D

# 約数列挙
def faclist(x):
    LIST=[1]
    while x!=1:
        k=Sieve[x]
        count=0
        while x%k==0:
            count+=1
            x//=k

        LIST2=[]
        for l in LIST:
            for i in range(1,count+1):
                LIST2.append(l*k**i)
        LIST+=LIST2

    return LIST

N=int(input())

DP=[0]*65

for i in range(2,65):
    NG=0
    OK=10**9+1

    while OK>NG+1:
        mid=(OK+NG)//2

        if mid**i>N:
            OK=mid
        else:
            NG=mid

    #print(i,OK)

    DP[i]=OK-2

ANS=1

for i in range(64,1,-1):
    ANS+=DP[i]
    for to in faclist(i):
        if i!=to:
            DP[to]-=DP[i]

print(ANS)
#######################################
