#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################

n, q = map(int, input().split())
ht = [ list(input().split()) for _ in range(q) ]

l, r = 0, 1
ans = 0

def f(s, g, y):
  s, g = min(s, g), max(s, g)
  if s <= y <= g:
    return n - (g-s)
  else:
    return g-s

for h, t in ht:
  t = int(t) - 1
  if h=='R':
    ans += f(r, t, l)
    r = t
  else:
    ans += f(l, t, r)
    l = t
print(ans)
#####################################################

import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

left=1
right=2
ANS=0
for tests in range(Q):
    com,ind=input().split()
    ind=int(ind)

    if com=="L":
        if left<right:
            if left<ind<right:
                ANS+=ind-left
            else:
                ANS+=(left-ind)%N
        else:
            if right<ind<left:
                ANS+=left-ind
            else:
                ANS+=(ind-left)%N

        left=ind

    else:
        if left<right:
            if left<ind<right:
                ANS+=right-ind
            else:
                ANS+=(ind-right)%N
        else:
            if right<ind<left:
                ANS+=ind-right
            else:
                ANS+=(right-ind)%N

        right=ind

print(ANS)

        

#####################################################
[my WA]

N,Q=map(int,input().split())
L=1
R=2
T=0
for i in range(Q):
  h,t=map(str,input().split())
  if h=='R':
    R2=int(t)
    add=(R2-R)%N
    #print('R',add,R,R2)
    T+=add
    R=R2
  elif h=='L':
    L2=int(t)
    add=(L2-L)%N
    #print('L',add,L,L2)
    T+=add
    L=L2
print(T)
#####################################################
