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
[my AC]

N,Q=map(int,input().split())
L=1
R=2
T=0
for i in range(Q):
  h,t=map(str,input().split())
  if h=='R':
    R2=int(t)
    add=0
    if L<R<R2:
      add=R2-R
    elif L<R2<R:
      add=R-R2
    elif R<L<R2:
      add=R+(N-R2)
    elif R<R2<L:
      add=R2-R      
    elif R2<L<R:
      add=R2+(N-R)
    elif R2<R<L:
      add=R-R2      
    T+=add
    R=R2
  elif h=='L':
    L2=int(t)
    add=0
    if L<R<L2:
      add=L+(N-L2)
    elif L<L2<R:
      add=L2-L       
    elif R<L<L2:
      add=L2-L        
    elif R<L2<L:
      add=L-L2        
    elif L2<L<R:
      add=L-L2           
    elif L2<R<L:
      add=L2+(N-L)
    T+=add
    L=L2
print(T)
#####################################################
