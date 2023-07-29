import sys
# import pypyjit
import itertools
import heapq
import math
from collections import deque, defaultdict
import string
import functools
import bisect
 
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# pypyjit.set_param('max_unroll_recursion=-1')
 
 
def readints(): return map(int, input().split())
def readlist(): return list(map(int, input().split()))
def readstr(): return input()[:-1]
