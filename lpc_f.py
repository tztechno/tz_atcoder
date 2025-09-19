###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[ring]
import sys
import itertools as it
import numpy as np

def nttconvolve(A, B, *, it = it, np = np):
    MOD = 998244353

    def imul(A, B): A *= B; return A;
    
    def iaddm(A, B): A += B; A %= MOD; return A;

    def imulm(A, B): A *= B; A %= MOD; return A;

    def ntt(A, roots):
        roots = roots[:-1]
        L, R = A[:M], A[M:]

        for i in range(1, log2M+1):
            s, t = 1<<i, M>>i
            A = A.reshape(s<<1, t)
            R[...] = L
            L[...] = iaddm(A[::2], imul(A[1::2], roots[::t])).ravel()

        return A.ravel()

    N = A.size + B.size - 1
    log2M = (N-1).bit_length()
    M = 1 << log2M
    
    roots = np.fromiter(it.accumulate(it.repeat(pow(3, (MOD^1)>>log2M, MOD)),
                                      lambda t,r: t*r % MOD,
                                      initial = 1),
                        "i8", M + 1)[..., None]
    inv_M = pow(499122177, log2M, MOD)

    A.resize(M << 1, refcheck = False); B.resize(M << 1, refcheck = False);

    return imulm(ntt(imulm(ntt(A, roots), ntt(B, roots)), roots[::-1].copy())[:N], inv_M)

def main(input = sys.stdin.readline, output = sys.stdout, *, np = np):
    N, M = map(int, input().split())
    A = np.fromstring(input(), "i8", N, sep = ' ')
    B = np.fromstring(input(), "i8", M, sep = ' ')
    nttconvolve(A, B).tofile(output, ' ', '%i')

if __name__ == '__main__':
    main()
###############################################
[miya]
#numpyは遅かった
#おそらくPyPy用に高速化はされていないのだろう

class NTT:
    MOD = 998244353 # = 119 * 2^23 + 1
    W = 31 #2^23乗根 g^(119*2^23/N) = (g^119)^(2^23/N) で、g^119 = 31 が最小ぽい？
    M = 23

    def __init__(self):
        self.w = [0] * self.M + [self.W] #2^i乗根
        self.iw = [0] * self.M + [pow(self.W, self.MOD-2, self.MOD)]
        for i in range(self.M,0,-1):
            self.w[i-1] = (self.w[i] * self.w[i]) % self.MOD
            self.iw[i-1] = (self.iw[i] * self.iw[i]) % self.MOD
    
    def dif(self,x):
        n = len(x) >> 1
        for i in range(n.bit_length(),0,-1):
            for j in range(0,len(x),n*2):
                w = 1
                for k in range(n):
                    s = x[j+k]
                    t = x[j+k+n]
                    x[j+k] = (s + t) % self.MOD
                    x[j+k+n] = w * (s - t) % self.MOD
                    w = (w * self.w[i]) % self.MOD
            n >>= 1
        return x
    
    def dit(self,x):
        n = 1
        for i in range(1,len(x).bit_length()):
            for j in range(0,len(x),n*2):
                w = 1
                for k in range(n):
                    s = x[j+k]
                    t = x[j+k+n]
                    x[j+k] = (s + w * t) % self.MOD
                    x[j+k+n] = (s - w * t) % self.MOD
                    w = (w * self.iw[i]) % self.MOD
            n <<= 1
        x = [(xi * pow(n,self.MOD-2,self.MOD)) % self.MOD for xi in x]
        return x
    
    def ntt(self,x):
        x = self.dif(x)
        #ビットリバース順に
        return x
    
    def intt(self,x):
        #ビットリバース順に
        x = self.dit(x)
        return x
    
    def convolution(self,a,b):
        n = 1 << (len(a) + len(b) - 2).bit_length()
        a += [0] * (n - len(a))
        b += [0] * (n - len(b))
        c = self.dit([i*j%ntt.MOD for i,j in zip(self.dif(a),self.dif(b))])
        return c


ntt = NTT()
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = ntt.convolution(a,b)

for i in range(n+m-1):
    print(c[i],end=" ")
###############################################
[rin]
import sys
import ctypes
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
  with open('create_root_array.cpp', 'wb') as f:
    f.write(b'#define LL long long\nextern "C" void create_root_array(LL *arr, const int len, const LL root) { arr[0] = 1LL; for (int i = 0; i < len-1; i++) { arr[i+1] = arr[i] * root % 998244353LL; }}\n')
  import subprocess
  subprocess.run(['g++', '-fPIC', '--shared', 'create_root_array.cpp', '-o', 'lib_cra.so'])

def create_root_array(len, root):

  longlong = ctypes.c_longlong
  int = ctypes.c_int
  longlongarray = longlong * len

  cra = ctypes.cdll.LoadLibrary("./lib_cra.so").create_root_array
  cra.argtypes = (longlongarray, int, longlong)

  arr = longlongarray()
  cra(arr, int(len), longlong(root))
  return np.ctypeslib.as_array(arr)

def main(input = sys.stdin.readline, output = sys.stdout, *, np = np):

  MOD = 998244353

  _imul = np.ndarray.__imul__
  _iadd = np.ndarray.__iadd__
  _imod = np.ndarray.__imod__

  def ntt(A, roots):
    for i in range(1, log2K+1):
      s, t = 1<<i, K>>i
      A.shape = (s<<1,t)
      A[s:] = A[:s]
      np.mod(_iadd(_imul(A[1::2], roots[::t]), A[::2]), MOD, A[:s])

    A.shape = (K2,)
    return A

  N, M = map(int, input().split())

  L = N + M - 1
  log2K = (L-1).bit_length()
  K = 1 << log2K
  K2 = K << 1

  A = np.fromstring(input(), 'i8', N, sep = ' '); A.resize(K2);
  B = np.fromstring(input(), 'i8', M, sep = ' '); B.resize(K2);

  roots = create_root_array(K|1, pow(3, (MOD^1)>>log2K, MOD))[..., None]
  inv_M = pow(499122177, log2K, MOD)

  _imod(_imul(ntt(A, roots[:-1]), ntt(B, roots[:-1])), MOD)
  _imod(_imul(ntt(A, roots[:0:-1])[:L], inv_M), MOD).tofile(output, ' ', '%i')

if __name__ == '__main__':
  main()

###############################################
[titia]
import sys
input = sys.stdin.readline

# mod=998244353　における、NTTによる高速フーリエ変換、畳み込み
# FFTは、ふるやんさんの記事を主に参照。https://www.creativ.xyz/fast-fourier-transform/
# NTTは、Senさんの記事で理解しました。https://qiita.com/Sen_comp/items/9401382df736e51564c1#mod-p%E3%81%AE%E4%B8%96%E7%95%8C%E3%81%AE%E5%8E%9F%E5%A7%8B%E6%A0%B9

mod=998244353

Weight=[1, 998244352, 911660635, 372528824, 929031873, 452798380, 922799308, 781712469, 476477967, 166035806, 258648936, 584193783, 63912897, 350007156, 666702199, 968855178, 629671588, 24514907, 996173970, 363395222, 565042129, 733596141, 267099868, 15311432, 0]

def fft(A,n,h,inverse=0):
        
    for i in range(n): # バタフライ演算用の並び替え
        j=0
        for k in range(h):
            j |= (i >> k & 1) << (h - 1 - k)
            
        if i<j:
            A[i],A[j]=A[j],A[i]

    b=1
    wb=1
    while b<n:
        for j in range(b):
            #w=pow(Weight[wb],j,mod)
            # 重み w = W_2b^j  FFTだと、1 の原始 2^b 乗根の j 乗

            if inverse==0:
                w=pow(Weight[wb],j,mod)
            else:
                w=pow(pow(Weight[wb],mod-2,mod),j,mod)

            for k in range(0,n,2*b):
                s=A[j+k]
                t=A[j+k+b]*w%mod

                A[j+k]=(s+t)%mod
                A[j+k+b]=(s-t)%mod
        b*=2
        wb+=1

    if inverse==1:
        INV_n=pow(n,mod-2,mod)
        for i in range(n):
            A[i]=A[i]*INV_n%mod

    return A

def convolution(A,B,n,h): # A, Bは同じサイズで2ベキ

    A_FFT=fft(A,n,h)
    B_FFT=fft(B,n,h)

    for i in range(len(A)):
        A[i]=A[i]*B[i]%mod

    A=fft(A,n,h,1)

    return A

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

FFTLEN=len(A)+len(B)-1
h=FFTLEN.bit_length()
LEN=2**h

A+=[0]*(LEN-len(A))
B+=[0]*(LEN-len(B))

C=convolution(A,B,LEN,h)

print(*C[:FFTLEN])

###############################################
[gemini AC]
#
# Number Theoretic Transform (NTT) for Polynomial Multiplication
#
# c_i = sum(a_j * b_{i-j}) mod P
#
# Constraints:
# 1 <= N, M <= 524288
# 0 <= a_i, b_i < 998244353
#

MOD = 998244353
PRIMITIVE_ROOT = 3

# 高速べき乗
def power(base, exp):
    res = 1
    base %= MOD
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return res

# 逆元
def modInverse(n):
    return power(n, MOD - 2)

# NTTの主関数
def ntt(a, inverse=False):
    n = len(a)
    
    # ビット反転
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    # バタフライ演算
    length = 2
    while length <= n:
        w_len = power(PRIMITIVE_ROOT, (MOD - 1) // length)
        if inverse:
            w_len = modInverse(w_len)
        
        for i in range(0, n, length):
            w = 1
            for j in range(length // 2):
                u = a[i + j]
                v = (a[i + j + length // 2] * w) % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + length // 2] = (u - v + MOD) % MOD
                w = (w * w_len) % MOD
        length *= 2
    
    if inverse:
        inv_n = modInverse(n)
        for i in range(n):
            a[i] = (a[i] * inv_n) % MOD

# 畳み込み
def convolution(a, b):
    # 結果の長さ
    len_c = len(a) + len(b) - 1
    
    # 配列の長さを2のべき乗に
    n = 1
    while n < len_c:
        n *= 2
    
    # パディング
    a.extend([0] * (n - len(a)))
    b.extend([0] * (n - len(b)))
    
    # NTT
    ntt(a)
    ntt(b)
    
    # 要素ごとの積
    c = [0] * n
    for i in range(n):
        c[i] = (a[i] * b[i]) % MOD
        
    # 逆NTT
    ntt(c, inverse=True)
    
    # 結果を返す
    return c[:len_c]

# --- メイン処理 ---
if __name__ == '__main__':
    # 例
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = convolution(a, b)
    
    print(*result)
###############################################
###############################################
###############################################
###############################################
###############################################
