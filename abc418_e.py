
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[hobbit]
from collections import defaultdict
import math

def solve():
    N = int(input())
    XY = [(*map(int,input().split()),) for _ in range(N)]
    
    P = defaultdict(lambda:defaultdict(int))
    for i in range(N):
        xi, yi = XY[i]
        for j in range(i): # i<j
            xj, yj = XY[j]
            num, den = yi-yj, xi-xj # num/den = 分子/分母
            d = num*num + den*den
            g = math.gcd(num, den)
            num, den = num//g, den//g
            if num < 0 or (num == 0 and den < 0):
                num *= -1
                den *= -1
            P[num, den][d] += 1

    ans = 0
    for C in P.values():
        c1 = sum(c for c in C.values())
        c2 = sum(c*(c-1)//2 for c in C.values())
        ans += c1*(c1-1) - c2
    print(ans//2)


solve()

##################################################################
[lazy]
from math import gcd

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

def grad(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x = x1 - x2
    y = y1 - y2
    if x < 0 or (x == 0 and y < 0):
        x = -x
        y = -y
    
    return (x // gcd(x, y), y // gcd(x, y))

d = {}
centers = {}

for i in range(N):
    for j in range(i + 1, N):
        g = grad(points[i], points[j])
        if g not in d:
            d[g] = 0
        d[g] += 1
        
        c = (points[i][0] + points[j][0], points[i][1] + points[j][1])
        if c not in centers:
            centers[c] = 0
        centers[c] += 1

ans = 0

for k, v in d.items():
    if v > 1:
        ans += v * (v - 1) // 2

for k, v in centers.items():
    if v > 1:
        ans -= v * (v - 1) // 2

print(ans)

##################################################################
[katsu]
from math import gcd

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

def grad(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x = x1 - x2
    y = y1 - y2
    if x < 0 or (x == 0 and y < 0):
        x = -x
        y = -y
    
    return (x // gcd(x, y), y // gcd(x, y))

d = {}
centers = {}

for i in range(N):
    for j in range(i + 1, N):
        g = grad(points[i], points[j])
        if g not in d:
            d[g] = 0
        d[g] += 1
        
        c = (points[i][0] + points[j][0], points[i][1] + points[j][1])
        if c not in centers:
            centers[c] = 0
        centers[c] += 1

ans = 0

for k, v in d.items():
    if v > 1:
        ans += v * (v - 1) // 2

for k, v in centers.items():
    if v > 1:
        ans -= v * (v - 1) // 2

print(ans)

##################################################################
[titia]
import sys
input = sys.stdin.readline

from collections import defaultdict
from math import gcd

from random import randint

from collections import Counter

randinf=randint(10**16,10**17)
rand0=randint(10**16,10**17)
rand1=randint(10**16,10**17)

rand2=randint(10**16,10**17)
rand3=randint(10**16,10**17)
rand4=randint(10**16,10**17)
rand5=randint(10**16,10**17)

N=int(input())
P=[list(map(int,input().split())) for i in range(N)]

D=defaultdict(list)

for i in range(N):
    for j in range(i+1,N):
        x,y=P[i]
        z,w=P[j]

        length=(x-z)*(x-z)+(y-w)*(y-w)

        if x==z:
            D[randinf].append(length)
        else:
            c=y-w
            d=x-z

            G=gcd(c,d)

            c//=G
            d//=G

            if c==0:
                D[rand0].append(length)
            elif c>=0:
                D[c*rand1+d*rand2].append(length)
            else:
                D[(-c)*rand1+(-d)*rand2].append(length)

ANS=0

double=0
for d in D:
    LIST=D[d]

    ANS+=len(LIST)*(len(LIST)-1)//2

    if len(LIST)>=1:
        C=Counter(LIST)
        for c in C:
            if C[c]>=2:
                double+=C[c]*(C[c]-1)//2

print(ANS-double//2)
            


##################################################################
[MyAi AC]
import sys
from math import gcd

def solve():
    input = sys.stdin.readline

    n = int(input())
    if n < 4:
        print(0)
        return

    points = [tuple(map(int, input().split())) for _ in range(n)]

    def get_slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            return ('inf', 0)
        g = gcd(dy, dx)
        dy //= g
        dx //= g
        # 分母を正に統一
        if dx < 0:
            dx = -dx
            dy = -dy
        return (dy, dx)

    slope_counts = dict()
    for i in range(n):
        p_i = points[i]
        for j in range(i + 1, n):
            slope = get_slope(p_i, points[j])
            slope_counts[slope] = slope_counts.get(slope, 0) + 1

    potential_trapezoids = 0
    for k in slope_counts.values():
        potential_trapezoids += k * (k - 1) // 2

    collinear_pairs = 0
    for i in range(n):
        slopes_from_i = dict()
        p_i = points[i]
        for j in range(i + 1, n):
            slope = get_slope(p_i, points[j])
            slopes_from_i[slope] = slopes_from_i.get(slope, 0) + 1
        for k in slopes_from_i.values():
            collinear_pairs += k * (k - 1) // 2

    corrected_count = potential_trapezoids - collinear_pairs

    midpoint_counts = dict()
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            mx2 = x1 + x2
            my2 = y1 + y2
            midpoint_counts[(mx2, my2)] = midpoint_counts.get((mx2, my2), 0) + 1

    num_parallelograms = 0
    for k in midpoint_counts.values():
        num_parallelograms += k * (k - 1) // 2

    total_trapezoids = corrected_count - num_parallelograms

    print(total_trapezoids)

if __name__ == "__main__":
    solve()

##################################################################
