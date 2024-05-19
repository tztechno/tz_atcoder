arc178_b.py
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
[vwxyz AC]
T=int(input());M=998244353
while T:
 T-=1;a,b,c=map(int,input().split())
 if a>b:a,b=b,a
 x=pow(10,a-1,M);A=32*x*x+4*x
 if a==b:
  if a+1==c:A=81*x*x-A
  elif a-c:A=0
 else:
  A=(99*x-9)*x//2
  if b==c:A=81*x*pow(10,b-1,M)-A
  elif b+1-c:A=0
 print(A%M)
#####################################################
[miku AC]
MOD=998244353

def powten(a):
  return pow(10,a,MOD)

def solve (a1,a2,a3):
  #a1<=a2に固定
  if a1>a2:
    a1,a2=a2,a1 
  #impossible
  if a2!=a3 and a2+1!=a3:
    return 0
  #a3=a2+1
  if a2!=a3:
    return (81*powten(a1+a2-2)-solve(a1,a2,a2))%MOD
  if a1==a2:
    return 4*powten(a1-1)*(8*powten(a1-1)+1)%MOD
  else:
    ans=(9*powten(a2-1)-(11*powten(a1-1)-1)*pow(2,-1,MOD))%MOD
    ans=ans*9*powten(a1-1)%MOD
    return ans

T=int(input())
nums=[[None]*3]*T
for i in range(T):
  nums[i]=[int(x) for x in input().split()]
for i in range(T):
  a1,a2,a3=nums[i]
  print(solve(a1,a2,a3))
#####################################################
[shakayami AC]
mod=998244353
    
def solve(a1,a2,a3):
    inv2=pow(2,mod-2,mod)
    if a1==a2:
        b=8*pow(10,a1-1,mod)
        c=(b*(b+1)*inv2)%mod
        if a3==a1:
            return c
        elif a3==a1+1:
            return (81*pow(10,2*a1-2,mod)-c)%mod
        else:
            return 0
    elif a1>a2:
        return solve(a2,a1,a3)
    else:
        assert a1<a2
        x=9*pow(10,a1-1,mod)
        y=9*pow(10,a2-1,mod)
        ans=x*(y-pow(10,a1-1,mod))-x*(x-1)*inv2
        ans%=mod
        if a3==a2:
            return ans
        elif a3==a2+1:
            return x*y-ans
        else:
            return 0


T=int(input())
for _ in range(T):
    A1,A2,A3=map(int,input().split())
    print(solve(A1,A2,A3)%mod)

#####################################################
[titia AC]
mod=998244353

INV=pow(2,mod-2,mod)

T=int(input())
for tests in range(T):
    A,B,C=map(int,input().split())

    if A>B:
        A,B=B,A


    if A==B and B==C:
        MAX=(pow(10,A,mod)-pow(10,A-1,mod)-1-(pow(10,A-1,mod)-1))

        #print(MAX%mod)

        print((1+MAX)*MAX%mod*INV%mod)


        
        

    elif B==C:
        MAX=(pow(10,B,mod)-pow(10,A-1,mod)-1-(pow(10,B-1,mod)-1))
        ko=pow(10,A,mod)-pow(10,A-1,mod)

        print((MAX+(MAX-(ko-1)))*ko%mod*INV%mod)

        #print(MAX%mod,ko)



    elif A!=B and C==B+1:
        MAX=pow(10,A,mod)-1
        ko=pow(10,A,mod)-pow(10,A-1,mod)

        print((MAX+(MAX-(ko-1)))*ko%mod*INV%mod)



    elif A==B and C==B+1:

        MAX=(pow(10,A,mod)-pow(10,A-1,mod)-1-(pow(10,A-1,mod)-1))

        ANS=(1+MAX)*MAX%mod*INV%mod

        x=(pow(10,A,mod)-pow(10,A-1,mod))%mod

        print((x*x%mod-ANS)%mod)

    else:
        print(0)

        
        

    
#####################################################
[my TLE]
n=int(input())
mod=998244353
for i in range(n):
  a,b,c=map(int,input().split())
  t=0
  z0,z1=10**(c-1),10**c
  y0,y1=10**(b-1),10**b
  x0,x1=10**(a-1),10**a
  for x in range(x0,x1):
    for y in range(y0,y1):
      z=x+y
      if z0<=z<z1:
        t+=1
  print(t%mod)
#####################################################
