abc084_c.py
#######################
[my error]
N=int(input())
D=[]
E=[]
S=[]
for i in range(N-1):
  c,s,f=map(int,input().split())
  S+=[s]
  b0=[]#発車
  b1=[]#到着
  for j in range(4):
    b0+=[s+f*j]
    b1+=[s+f*j+c]
  D+=[b0]
  E+=[b1]
print(D)
print(E)
#######################
#######################
#######################
#######################
N = int(input())
info = []
for i in range(N - 1):
  c, s, f = map(int, input().split())
  info.append((c, s, f))

for i in range(N - 1):
  cnt = info[i][1] + info[i][0]
  for j in range(i + 1, N - 1):
    if cnt >= info[j][1] and cnt % info[j][2] == 0:
      cnt += info[j][0]
    elif cnt < info[j][1]:
      cnt = info[j][1] + info[j][0]
    else:
      m = cnt % info[j][2]
      cnt += info[j][0] + info[j][2] - m
  print(cnt)
print(0)

#######################
def main() -> None:
    import sys

    def input():
        return sys.stdin.readline().strip()

    N: int = int(input())
    CSF = []
    for _ in range(N - 1):
        CSF.append(tuple(map(int, input().split())))

    for i in range(N - 1):
        now = 0
        for j in range(i, N - 1):
            c, s, f = CSF[j]
            if now <= s:
                now = s + c
            else:
                k = -(-(now - s) // f)
                now = s + k * f + c
        print(now)
    print(0)

main()
#######################
Int = lambda: int(input())
Ints = lambda: [*map(int,input().split())]
from collections import Counter

ans = []
n=Int(); n-=1
C,S,F=[],[],[]
for i in range(n):
    c,s,f=Ints()
    C+=[c]; S+=[s]; F+=[f]

for i in range(n):
    t=0
    for j in range(i,n):
        if t<=S[j]: t=S[j]
        else: t+= (S[j]-t)%F[j]
        t+=C[j]
    ans.append(t)

for i in ans:print(i)
print(0)
#######################
