###############################################
AtCoderのコンテストでは
ACLが標準で利用可能です
importしてすぐ使える状態になっています
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
[tai]
from atcoder.math import floor_sum
t = int(input())
for i in range(t):
  n,m,a,b = map(int,input().split())
  print(floor_sum(n,m,a,b))
###############################################
[deepseek AC]
def floor_sum(n, m, a, b):
    """
    計算: Σ_{i=0}^{n-1} floor((a*i + b)/m)
    """
    ans = 0
    while True:
        if a == 0:
            return ans
        
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
            if a == 0:
                return ans
        
        if b >= m:
            ans += n * (b // m)
            b %= m
        
        y_max = (a * n + b) // m
        if y_max == 0:
            return ans
        
        x_max = m * y_max - b
        if x_max < 0:
            x_max += m
            y_max -= 1
        
        cnt = (x_max + a - 1) // a
        ans += (n - cnt) * y_max
        
        n = y_max
        b = (a - x_max % a) % a
        a, m = m, a

T = int(input())

for _ in range(T):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
###############################################
[deepseek AC]
def floor_sum(n, m, a, b):
    """
    計算: Σ_{i=0}^{n-1} floor((a*i + b)/m)
    """
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    
    y_max = (a * n + b) // m
    x_max = m * y_max - b
    
    if y_max == 0:
        return ans
    
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    
    return ans

T = int(input())

for _ in range(T):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
###############################################
[my TLE]
import math
T=int(input())

for i in range(T):
  n,m,a,b=map(int,input().split())
  ans=0
  for i in range(n):
    ans+=math.floor((a*i+b)/m)
  print(ans)
  
###############################################
###############################################
###############################################
###############################################
###############################################
