#ABC293_C
#Make Takahashi Happy

################################################

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(1 << (H + W - 2)):
    seen = set()
    pi = pj = 0
    seen.add(A[0][0])
    for j in range(H + W - 2):
        if (i >> j) & 1:
            pi += 1
        else:
            pj += 1
        if pi >= H or pj >= W:
            break
        if A[pi][pj] in seen:
            break
        seen.add(A[pi][pj])
    else:
        # print(pi, pj)
        if pi != H - 1 or pj != W - 1:
            continue
        ans += 1

print(ans)

################################################

H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

from itertools import product
ans=0
for pro in product((1,0),repeat=H+W-2):
    if sum(pro)!=H-1:continue
    st=set()
    st.add(A[0][0])
    x,y=0,0
    for i in range(H+W-2):
        if pro[i]==1:
            y+=1
        else:
            x+=1

        st.add(A[y][x])

    if len(st)==H+W-1:
        ans+=1

print(ans)

###############################################
### my revision using product w/AC

from itertools import product,permutations,combinations,accumulate

H,W=map(int,input().split())
A0=[]
for i in range(H):
  A0+=[list(map(int,input().split()))]

def check(ci):
  P=[0,0]
  R=[A0[0][0]]
  for cii in ci:
    if cii==0:
      P[1]+=1
    elif cii==1:
      P[0]+=1
    R+=[A0[P[0]][P[1]]]
  return R

D=['R']*(W-1)+['D']*(H-1)
C0=list(product((1,0),repeat=H+W-2))
C1=[]
for ci in C0:
  if sum(ci)==H-1:
    C1+=[ci]
#print(C1)
T=0
for ci in C1:
  R=check(ci)
  if len(set(R))==H+W-1:
    T+=1

print(T)
    

###############################################
# MYBEST w/TLE21
# permutations is the cause of delay

from itertools import product,permutations,combinations,accumulate

H,W=map(int,input().split())
A0=[]
for i in range(H):
  A0+=[list(map(int,input().split()))]

def check(ci):
  P=[0,0]
  R=[A0[0][0]]
  for cii in ci:
    if cii=='R':
      P[1]+=1
    elif cii=='D':
      P[0]+=1
    R+=[A0[P[0]][P[1]]]
  return R

D=['R']*(W-1)+['D']*(H-1)
C0=list(permutations(D))
C1=sorted(set(C0))

T=0
for ci in C1:
  R=check(ci)
  if len(set(R))==H+W-1:
    T+=1

print(T)
