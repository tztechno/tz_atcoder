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
