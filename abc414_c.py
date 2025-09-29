
###############################################
414 の十進法での表記は 414 であり、これは回文です。 また、
414 の八進法での表記は 636 であり、これも回文です。 
これを踏まえて、以下の問題を解いてください。
正の整数 A,N が与えられます。 
1 以上 N 以下の整数のうち、十進法での表記も 
A 進法での表記も回文であるようなものの総和を求めてください。
なお、この問題の制約下で答えは 
2**63 未満であることが証明できます。
###############################################
[titia AC]
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

###############################################
[cgpt AC]
a = int(input())
N = int(input())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n: int, base: int) -> str:
    if n == 0:
        return '0'
    res = []
    while n > 0:
        n, r = divmod(n, base)
        res.append(digits[r])
    res.reverse()
    return ''.join(res)

def is_palindrome_str(s: str) -> bool:
    return s == s[::-1]

ans = 0
max_len = len(str(N))

# 桁数ごとに10進回文を生成
for length in range(1, max_len + 1):
    half_len = (length + 1) // 2
    start = 10 ** (half_len - 1) if half_len > 1 else 1
    end = 10 ** half_len
    for half in range(start, end):
        half_str = str(half)
        if length % 2 == 0:
            pal_str = half_str + half_str[::-1]
        else:
            pal_str = half_str + half_str[-2::-1]
        n = int(pal_str)
        if n > N:
            break
        # a進でも回文か調べる
        if is_palindrome_str(to_base(n, a)):
            ans += n

print(ans)

###############################################
###############################################
###############################################
###############################################
[my TLE]
a=int(input())
N=int(input())

def to_base(n: int, base: int) -> str:
    if n == 0:
        return '0'
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sign = ''
    if n < 0:
        sign = '-'
        n = -n
    result = ''
    while n > 0:
        n, r = divmod(n, base)
        result = digits[r] + result
    return sign + result

def is_palindrome(n: int) -> bool:
    s = str(n)          
    return s == s[::-1]
  
ans=0    
for i in range(1,N+1):
  if is_palindrome(i)==True:
    b=to_base(i,a)
    if is_palindrome(b)==True:
      ans+=i
      
print(ans)
  
###############################################
###############################################
###############################################
