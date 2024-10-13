#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
[my TLE, O(n^2)]

import sys
input = sys.stdin.readline
S=list(input())
n=len(S)
t=0
for i in range(n):
  for j in range(i+2,n):
    if S[i]==S[j]:
      t+=j-i-1
print(t)

#################################################################
[almost understand]

from collections import defaultdict

def do():
    all_count = 0
    S = input()

    right_dict = defaultdict(int)
    for i in range(len(S)):
        s_i = S[i]
        right_dict[s_i] += 1

    left_dict = defaultdict(int)
    for j in range(len(S)):
        s_j = S[j]
        right_dict[s_j] -= 1
        for s_i, count in left_dict.items():
            all_count += (count * right_dict[s_i])
        left_dict[s_j] += 1

    print(all_count)
    return


if __name__ == '__main__':
    do()

#################################################################
[not understand]

import string
from collections import defaultdict
from collections import Counter

S = list(input())
lcnt = defaultdict(int)
rcnt = defaultdict(int)
rcnt = Counter(S[1:])
ans = 0
for i in range(1, len(S) - 1):
    lcnt[S[i - 1]] += 1
    rcnt[S[i]] -= 1
    #print(S[i])
    #print(lcnt)
    #print(rcnt)
    for j in list(string.ascii_uppercase):
        ans += lcnt[j] * rcnt[j]
print(ans)

#################################################################
[not understand]

S = list(input())

l = [0 for _ in range(26)]
r = [0 for _ in range(26)]
for s in S:
    r[ord(s) - ord("A")] += 1

oldc = ord(S[0]) - ord("A")
l[oldc] -= 1
ans = 0
for s in S:
    c = ord(s) - ord("A")
    l[oldc] += 1
    r[c] -= 1
    
    for i in range(26):
        ans += l[i] * r[i]
    oldc = c

print(ans)
    
#################################################################
[not understand]

import sys
input = sys.stdin.readline

S=input().strip()
A=[]
for s in S:
    A.append(ord(s)-65)
ANS=0

DP=[0]*26
DP2=[0]*26

for i in range(len(A)):
    #print(ANS,DP,DP2)

    ANS+=DP2[A[i]]
    for j in range(26):
        DP2[j]+=DP[j]
    DP[A[i]]+=1
    

print(ANS)

#################################################################
