#################################################
#################################################

#################################################

#################################################

#################################################

#################################################

#################################################

import sys,pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**8)
sys.set_int_max_str_digits(0)
# ================固定
def search(ok:int,ng:int,f:bool)->int: #二分探索原型
    # okは条件を満たす領域の外側
    # ngは条件を満たさない領域の外側
    # fは条件を満たすかどうかの評価関数
        # lambda i:a[i]<x xを含まない最大のiを返す
        # lambda i:a[i]<=x xを含む最大のiを返す
    while 1<abs(ok-ng):
        mid=(ng+ok)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def check(y,x,r):
    return (x+0.5)**2+(y+0.5)**2<=r
R = int(input())
r=R**2
c=0
for i in range(1,R+1):
    c+=search(0,R,lambda x:check(i,x,r))
c*=4
c+=(R-1)*4+1
print(c)

#################################################
def pd (x, y):
    return (2*x+1)**2 + (2*y+1)**2 <= 4*r**2

r =int(input())
count = 0
l = r-1

for i in range(1,r):
    while not pd(i,l):
        l -= 1
    count += l
    
count = 4*(r-1)+1+count*4
print(count)

#################################################
[titia]

import sys
input = sys.stdin.readline

R=int(input())

# (1/2)^2 + (1/2+x)^2 <= R^2  → x*2+1個
# (1/2+k)^2 + (1/2+x)^2 <= R^2  → (x*2+1)*2個

ANS=0
OK=-1
NG=10**9

while NG>OK+1:
    mid=(OK+NG)//2
    if (1/2)**2 + (1/2+mid)**2 <= R**2:
        OK=mid
    else:
        NG=mid
if OK>=0:
    ANS+=OK*2+1
else:
    print(0)
    exit()

now=OK

for k in range(1,10**9):
    while (1/2+k)**2 + (1/2+now)**2 > R**2:
        now-=1
        if now<0:
            break
    if now>=0:
        ANS+=(now*2+1)*2
    else:
        break

print(ANS)

#################################################
[my TLE]

r=int(input())
S=set()
for x in range(r+1):
  for y in range(r+1):
    if (x+0.5)**2+(y+0.5)**2<=r*r:
      S.add((x,y))
      S.add((-x,y))      
      S.add((x,-y))      
      S.add((-x,-y))      
print(len(S))      
#################################################
