//ABC259_C

###########################################################################
s = input()
t = input()
j = 0

for i in range(len(t)):    
    if t[i] == s[j]:
        j += 1     
    else:
        if t[i] == s[j - 1] == s[j - 2]:
            continue
        else:
            print('No')
            exit()
    if j == len(s):
        j -= 1

print('Yes')
###########################################################################
from itertools import groupby

def solve():
    S = input()
    T = input()

    grouped_S = [(char, sum(1 for _ in group)) for char, group in groupby(S)]
    grouped_T = [(char, sum(1 for _ in group)) for char, group in groupby(T)]

    if len(grouped_S) != len(grouped_T):
        return False

    for (char_s, count_s), (char_t, count_t) in zip(grouped_S, grouped_T):
        if char_s != char_t or count_s > count_t or (count_s == 1 and count_t > 1):
            return False

    return True

print("Yes" if solve() else "No")
###########################################################################
import sys
from itertools import groupby, zip_longest

input = sys.stdin.readline

S = str(input().strip())
T = str(input().strip())

if len(list(groupby(S))) != len(list(groupby(T))):
    print("No")
    exit()

for s, t in zip(groupby(S), groupby(T)):
    if s[0] != t[0]:
        print("No")
        exit()

    s = len(list(s[1]))
    t = len(list(t[1]))
    if s == t:
        continue

    if s < t and s >= 2:
        continue

    print("No")
    exit()

print("Yes")

###########################################################################
def main():
    S = astr()
    T = astr()
    
    S = [(s, len(list(g))) for s, g in groupby(S)]
    T = [(t, len(list(g))) for t, g in groupby(T)]
    
    if len(S) != len(T):
        print("No")
        return
    
    for (s, s_len), (t, t_len) in zip(S, T):
        if s==t:
            if s_len == t_len: continue
            elif s_len >= 2 and t_len > s_len: continue
        print("No")
        return
    print("Yes")   
    
    return

from itertools import groupby
from sys import setrecursionlimit, set_int_max_str_digits, stdin, stderr
setrecursionlimit(10**6); set_int_max_str_digits(0) ;readline = stdin.readline
M998 = 998244353; M007 = 10**9+7; INF = 10**18
mulint = lambda: map(int, readline().split()); anint = lambda: int(readline())
astr = lambda: readline().rstrip(); dprint = lambda *x: print(*x, file=stderr)

if __name__ == '__main__':
    main()
###########################################################################
def readints():
  return list(map(int, input().split()))

def deep_recursion():
  import sys
  import pypyjit
  sys.setrecursionlimit(550000)
  pypyjit.set_param('max_unroll_recursion=-1')

def main():
  S = input()
  T = input()

  def rle(s):
    ret = []
    prev = s[0]
    cur = 1
    for c in s[1:]:
      if c == prev:
        cur += 1
      else:
        ret.append((prev, cur))
        prev = c
        cur = 1
    ret.append((prev, cur))
    return ret

  S = rle(S)
  T = rle(T)
  if len(S) != len(T):
    print('No')
    return
  for (char1, count1), (char2, count2) in zip(S, T):
    if char1 != char2 or count1 > count2 or count1 == 1 != count2:
      print('No')
      return
  print('Yes')


if __name__ == '__main__':
  # flush = lambda: sys.stdout.flush()
  # deep_recursion()
  main()
###########################################################################

