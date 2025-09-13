#####################################
#####################################
#####################################
#####################################
#####################################
[cgpt AC]
import sys
sys.setrecursionlimit(1000000)

memo = {}

def solve(x):
    if x < 2:
        return 0
    if x in memo:
        return memo[x]
    
    a = x // 2
    b = x - a  # ceil(x/2) = x - floor(x/2)
    
    res = x + solve(a) + solve(b)
    memo[x] = res
    return res

N = int(input())
print(solve(N))

#####################################
[cgpt WA]
import math
import sys
sys.setrecursionlimit(10**6)

memo = {}

def f(x):
    if x < 2:
        return 0
    if x in memo:
        return memo[x]
    y = f(x // 2) + f(math.ceil(x / 2)) + x
    memo[x] = y
    return y

N = int(input())
print(f(N))

#####################################
[cgpt TLE]
[stackをリストでなくdequeで形成する,それだけではだめ]

from collections import deque
import math

N = int(input())
stack = deque([N])
P = 0

while stack:
    p0 = stack.popleft()  # 先頭から取り出す
    if p0 >= 2:
        P += p0
        p1 = p0 // 2
        p2 = math.ceil(p0 / 2)
        if p1 >= 2:
            stack.append(p1)
        if p2 >= 2:
            stack.append(p2)

print(P)

#####################################
[deepseek3 AC]
def main():
    N = int(input().strip())
    memo = {}
    
    stack = [N]
    while stack:
        x = stack[-1]
        
        if x <= 1:
            memo[x] = 0
            stack.pop()
            continue
            
        left = x // 2
        right = (x + 1) // 2
        
        if left not in memo:
            stack.append(left)
            continue
            
        if right not in memo:
            stack.append(right)
            continue
            
        # 両方の子が計算済み
        memo[x] = x + memo[left] + memo[right]
        stack.pop()
    
    print(memo[N])

if __name__ == '__main__':
    main()
#####################################
[deepseek2 TLE]
def main():
    N = int(input().strip())
    if N < 2:
        print(0)
        return
    
    from collections import defaultdict
    count = defaultdict(int)
    count[N] = 1
    total = 0
    
    while count:
        n, cnt = count.popitem()
        total += n * cnt
        
        if n > 1:
            left = n // 2
            right = (n + 1) // 2
            
            if left > 1:
                count[left] += cnt
            if right > 1:
                count[right] += cnt
    
    print(total)

if __name__ == '__main__':
    main()
#####################################
[deepseek TLE]
from collections import defaultdict

def main():
    N = int(input().strip())
    if N < 2:
        print(0)
        return
        
    count_map = defaultdict(int)
    count_map[N] = 1
    P = 0
    
    while count_map:
        n, cnt = count_map.popitem()
        P += n * cnt
        if n < 2:
            continue
        a = n // 2
        b = (n + 1) // 2
        if a >= 2:
            count_map[a] += cnt
        if b >= 2:
            count_map[b] += cnt
            
    print(P)

if __name__ == '__main__':
    main()
#####################################
[my TLE]
import math
N=int(input())
stack=[N]
P=0
while stack:
  p0=stack.pop(0)
  if p0>=2:
    P+=p0
    p1=p0//2
    p2=math.ceil(p0/2)
    if p1>=2:
      stack+=[p1]
    if p2>=2:
      stack+=[p2]
print(P)
  

#####################################
