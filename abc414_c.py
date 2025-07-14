##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[tako]

A, N = map(int, open(0))

ans = 0
for i in range(1, 10 ** 6):
    S = str(i)
    for o in map(int, (S + S[::-1][1:], S + S[::-1])):
        if o > N:
            continue
        q = o
        B = []
        while q > 0:
            q, r = divmod(q, A)
            B += r,
        if B == B[::-1]:
            ans += o

print(ans)
##################################################################
[kocha]

a=int(input())
n=int(input())

kai=set()
for i in range(1,10):
  kai.add(i)
cnt=len(list(str(n)))-1

d=(len(list(str(n))))//2

for i in range(10**d):
  s=str(i)
  if s==s[::-1]:
    kai.add(i)
  kai.add(int(s+s[::-1]))
  for j in range(0,10):
    if i>=10**5:
      break
    jt=str(j)
    if s==str(0):
      break
    kai.add(int(s+jt+s[::-1]))
#kai=sorted(kai)
#print(kai)

def f(v):
  sn=''
  while v:
    if v%a>=10:
      return -1
    sn+=str(v%a)
    v//=a
  if sn==sn[::-1]:
    return True
  else:
    return False
ans=0
for i in kai:
  if i>n:
    continue
  if f(i):
    ans+=i

print(ans)
##################################################################
import sys
input = sys.stdin.readline
A=int(input())
N=int(input())
LIST=[]

10進数の回文数だけを作る
def calc(S):
    if S[0]!="0":
        LIST.append(S)
    if len(S)<=10:
        for i in range(10):
            T=str(i)+S+str(i)
            if len(T)<=13:
                calc(T)
              
奇数と偶数桁の回文生成
for i in range(10):
    S=str(i)
    calc(S)
    calc(S+S)


C=[]
Aの累乗を事前計算
for i in range(50):
    if A**i<=10**12:
        C.append(A**i)

ANS=0

for x in LIST:
    k=int(x)
    if k>N:
        continue

    L=[]

    flag=0
    for i in range(len(C)-1,-1,-1):
        if k<C[i]:
            if flag==0:
                continue
            else:
                L.append(0)
        else:
            flag=1
            u=k//C[i]
            L.append(u)
            k=k%C[i]

    #print(x,L,ANS)

    if L==L[::-1]:
        ANS+=int(x)

print(ANS)
##################################################################
[titia] #cannot understand

import sys
input = sys.stdin.readline

A=int(input())
N=int(input())

LIST=[]

def calc(S):
    if S[0]!="0":
        LIST.append(S)

    if len(S)<=10:

        for i in range(10):
            T=str(i)+S+str(i)

            if len(T)<=13:
                calc(T)

for i in range(10):
    S=str(i)
    calc(S)
    calc(S+S)


C=[]

for i in range(50):
    if A**i<=10**12:
        C.append(A**i)

ANS=0

for x in LIST:
    k=int(x)
    if k>N:
        continue

    L=[]

    flag=0
    for i in range(len(C)-1,-1,-1):
        if k<C[i]:
            if flag==0:
                continue
            else:
                L.append(0)
        else:
            flag=1
            u=k//C[i]
            L.append(u)
            k=k%C[i]

    #print(x,L,ANS)

    if L==L[::-1]:
        ANS+=int(x)

print(ANS)

##################################################################


---

```python
A（進数）と N（上限）を入力
A = int(input())  # Target base
N = int(input())  # Upper limit

10進数での回文をすべて生成（N以下）
decimal_palindromes = generate_palindromes_up_to(N)
result = 0

for num in decimal_palindromes:
    各回文をA進数に変換
    base_A_str = decimal_to_base(num, A)
  
    A進数でも回文なら result に加算
    if is_palindrome(base_A_str):
        result += num

print(result)
```

##################################################################
[ai ac]
def is_palindrome(s):
    return s == s[::-1]

def decimal_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    return ''.join(map(str, digits[::-1]))

def generate_palindromes_up_to(N):
    palindromes = []
    max_length = len(str(N))
    for length in range(1, max_length + 1):
        half_length = (length + 1) // 2
        start = 10 ** (half_length - 1)
        end = 10 ** half_length
        for first_half in range(start, end):
            first_half_str = str(first_half)
            if length % 2 == 0:
                palindrome_str = first_half_str + first_half_str[::-1]
            else:
                palindrome_str = first_half_str + first_half_str[:-1][::-1]
            palindrome = int(palindrome_str)
            if palindrome <= N:
                palindromes.append(palindrome)
    return palindromes

A = int(input())
N = int(input())

decimal_palindromes = generate_palindromes_up_to(N)
result = 0
for num in decimal_palindromes:
    base_A_str = decimal_to_base(num, A)
    if is_palindrome(base_A_str):
        result += num
print(result)
##################################################################
