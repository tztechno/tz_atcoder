#################################################################
#################################################################
#################################################################
#################################################################
[my AC]

from collections import defaultdict,deque,Counter
S=list(input())
M=sorted(set(S))
Sr=S
Cr=Counter(Sr)
Cl=Counter([])
T=0
for si in Sr:
  Cr[si]-=1
  t=0
  for m in M:
    t+=Cr[m]*Cl[m]
    #print(m,Cr[m],Cl[m])
  Cl[si]+=1
  T+=t
print(T)
#################################################################
[my TLE28]

from collections import defaultdict,deque,Counter
SR=list(input())
M=sorted(set(SR))
CR=Counter(SR)
SL=[]
CL=Counter(SL)
T=0
for si in SR:
  CR[si]-=1
  t=0
  for m in M:
    t+=CR[m]*CL[m]
    #print(m,CR[m],CL[m])
  SL+=[si]
  CL=Counter(SL)
  T+=t
print(T)
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
