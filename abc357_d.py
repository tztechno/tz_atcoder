abc357_d.py
################################################
NOT UNDERSTOOD
################################################
正整数Nに対して、NをN個つなげた整数をVN​とします。
より厳密には、Nを文字列とみなしたものをN個連結し、それを再度整数とみなしたものをVN​とします。
例えば、V3​=333,V10​=10101010101010101010です。
VN​を998244353で割った余りを求めてください。
################################################
フェルマーの小定理：
もし𝑝が素数であり、𝑎が𝑝で割り切れない任意の整数であるならば、𝑎**(𝑝−1) ≡ 1(mod𝑝)が成り立つ。
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
P = 998244353
N = int(input())
len_N = len(str(N))
x = (pow(10, N*len_N, P)-1) % P
y = pow(pow(10, len_N, P)-1, -1, P)
print((N*x*y) % P)

################################################
mod = 998244353

N = int(input())

f = [[len(str(N)), N % mod]]
for i in range(64):
	exp = pow(10, f[i][0], mod)
	f.append([f[i][0] * 2, (f[i][1] * exp + f[i][1]) % mod])


totalLen = len(str(N)) * N
curLen = len(str(N))
curVal = N % mod
while curLen < totalLen:
	targetIdx = -1
	for i in range(64):
		if curLen + f[i][0] <= totalLen:
			targetIdx = i
		else:
			break
	exp = pow(10, f[targetIdx][0], mod)
	curLen += f[targetIdx][0]
	curVal = (curVal * exp + f[targetIdx][1]) % mod

print(curVal)

################################################
N = int(input())
n = len(str(N))
mod = 998244353
ans = (N%mod)*(pow(10,n*N,mod)-1)*pow((pow(10,n)-1),-1,mod)
print(ans%mod)
################################################
N = int(input())
MOD = 998244353
r = pow(10, len(str(N)), MOD)
ans = N * (pow(r, N, MOD)-1) * pow(r-1, MOD-2, MOD)
ans %=MOD
print(ans)
################################################
[my ans2 of RE using フェルマーの小定理,RE21]           
mod=998244353#素数
ni=int(input())
if ni%mod==0:
    print(0)
    exit()
else:
    m=ni%mod
    ns=str(m).zfill(len(str(ni)))
    #print(ns)
    vs=ns*ni
    ans=int(vs)%mod
    print(ans)
################################################
[titia of AC]
import sys
input = sys.stdin.readline
N=int(input())
mod=998244353
k=pow(10,len(str(N)),mod)
ANS=N*(1-(pow(k,N,mod)))*pow(1-k,mod-2,mod)
print(ANS%mod)
################################################
[trk of AC]
N = int(input())
n = len(str(N))
mod = 998244353
ans = (N%mod)*(pow(10,n*N,mod)-1)*pow((pow(10,n)-1),-1,mod)
print(ans%mod)
################################################
[my ans of RE]
mod=998244353
ni=int(input())
ns=str(ni)
vs=ns*ni
ans=int(vs)%mod
print(ans)
################################################
