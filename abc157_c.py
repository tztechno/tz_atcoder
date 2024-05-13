abc157_c.py
#################################################
以下の条件を満たす0以上の整数が存在すれば、それらのうち最小のものを出力してください。
そのような整数が存在しなければ、-1と出力してください。
十進表記で丁度N桁である。
(0は1桁の整数とする。その他の整数については、先頭に0をつけた表記は認めない。)
左から数えてsi​桁目はci​である。(i=1,2,⋯,M)
#################################################
#################################################
#################################################
n, m = map(int, input().split())

s = [0] * m
c = [0] * m
a = [0] * n

for i in range(m):
    s[i], c[i] = map(int, input().split())

for i in range(m):
    if s[i] == 1 and c[i] == 0 and n != 1:
        print(-1)
        exit()
    for j in range(i+1, m):
        if s[i] == s[j] and c[i] != c[j]:
            print(-1)
            exit()

for i in range(m):
    a[s[i]-1] = c[i]

if a[0] == 0 and n != 1:
    a[0] = 1

ans = ''

for i in range(n):
    ans += str(a[i])

print(int(ans))
#################################################
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
C=[list(map(int,input().split())) for i in range(M)]

for i in range(1000):
    S=str(i)
    if len(S)==N:
        for s,c in C:
            s-=1
            if S[s]==str(c):
                True
            else:
                break
        else:
            print(i)
            sys.exit()

print(-1)
            
#################################################
n,m=map(int,input().split())
condition=[]

for _ in range(m):
    s,c=map(int,input().split())
    condition.append((s-1,str(c)))
l,r=10**(n-1),10**n
if n==1:
    l=0
for num in range(l,r):
    is_valid=1
    num=str(num)
    for s,c in condition:
        if num[s]!=c:
            is_valid=0
    if is_valid:
        print(num)
        exit()
print(-1)
#################################################
a,b=map(int,input().split())
x=[]
y=0
for i in range(b):
    x.append(list(map(int,input().split())))
#print(x)
for i in range(10**5):
    if len(str(i))==a:
        y=0
        for j in range(b):
            if str(i)[x[j][0]-1]!=str(x[j][1]):
                y=1
                break
        if y==0:
            print(i)
            exit()
print(-1)
#################################################
N, M = map(int, input().split())
l = []
for _ in range(M):
  l.append(list(map(int, input().split())))

for i in range(10**(N-1) - (4-N)//3, 10**N):
  li = [int(x) for x in list(str(i))]
  point = 0
  for j in range(M):
    if li[l[j][0]-1] == l[j][1]:
      point += 1
  if point == M:
    print(i)
    exit()

print(-1)
#################################################
[WA5,MY BEST]
N,M=map(int,input().split())
A=[]
for i in range(N):
  A+=['0']
cnt={}
for i in range(M):
    s,c=map(int,input().split())
    if cnt.get(s-1,'x')=='x':
      cnt[s-1]=c
      A[s-1]=str(c)
    elif cnt.get(s-1,'x')!='x' and cnt.get(s-1,'x')!=c:
      print(-1)
      exit()
if N>1 and A[0]=='0':
  print(-1)
else:
  print(''.join(A))
#################################################
