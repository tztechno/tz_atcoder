
#########################################################

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

#########################################################

AB=[tuple(map(int,input().split())) for i in range(N)]
AB.sort()

#########################################################

N,K=map(int,input().split())

#########################################################

import sys
input = sys.stdin.readline
M=int(input())
S=[input().strip() for i in range(3)]
print(S)

#########################################################

import sys
input = sys.stdin.readline
    
S = [input()[:-1] for _ in range(N)]: 

# 末尾の改行文字 ([:-1]) を削除し、Sリストに格納します

#########################################################

input = stdin.buffer.readline
n, w = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

#########################################################

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

#########################################################

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

#########################################################

N,K=map(int,input().split())
A=[int(i) for i in input().split()]

#########################################################

*a, k, n = map(int, open(0).read().split()[::-1]) 

# 7 10 (n,k)
# 11 12 16 22 27 28 31 (a)

#########################################################

import sys
N, *PA = map(int, sys.stdin.buffer.read().split())

# 4
# 4 20
# 3 30
# 2 40
# 1 10

#########################################################

N = int(input())
P = [ None ] * N
A = [ None ] * N
for i in range(N):
    P[i], A[i] = map(int, input().split())

#########################################################

# Captures the input as a binary number and converts it to a decimal number and outputs it
a = []
for _ in range(m):
    a.append(int(input().replace(" ", ""), 2))
print(a)

#########################################################
