
_INPUT = """\

"""
if sys.argv[-1] == 'DEBUG':
    import io
    sys.stdin = io.StringIO(_INPUT)


from collections import defaultdict,deque,Counter
from itertools import product,permutations,combinations,accumulate
from bisect import bisect_left,bisect_right,bisect
from math import gcd,sqrt,log,exp,inf,pi,nan
from heapq import heappush,heappop,heapify,heappushpop,heapreplace,merge,nlargest,nsmallest
import sys
input = sys.stdin.readline
