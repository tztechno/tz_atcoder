
import sys
input = sys.stdin.readline
#S=input().strip()#改行除く
#S=input()[0:-1]#改行除く
sys.setrecursionlimit(10**8)
from math import gcd,sqrt,log,exp,inf,pi,nan
from collections import defaultdict,deque,Counter
from itertools import product,permutations,combinations,accumulate
from bisect import bisect_left,bisect_right,bisect
from heapq import heappush,heappop,heapify,heappushpop,heapreplace,merge,nlargest,nsmallest
import networkx as nx
from collections import defaultdict
cnt = defaultdict(int)

INF = float("INF")
FourNb=[(-1,0),(1,0),(0,1),(0,-1)]
cursol=dict(zip('UDRL',FourNb))
alp=[chr(ord('a')+i) for i in range(26)]


input_data = '''
6
6 2 5 3 1 4
'''

# You can use the `splitlines()` method to split the input data into lines.
lines = input_data.strip().splitlines()

# Extract N from the first line and A from the second line.
N = int(lines[0])
A = list(map(int, lines[1].split()))

### N = int(input())
### A = list(map(int,input().split()))
