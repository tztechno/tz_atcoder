##################################################################
##################################################################
##################################################################
[mk]
N, M, K = [int(x) for x in input().split()]
H = sorted([int(x) for x in input().split()])
B = sorted([int(x) for x in input().split()])
i, j = 0, 0
ans = 0
while i < N and j < M:
    if H[i] <= B[j]: 
        ans += 1
        i += 1
        j += 1
    else:
        j += 1
print('Yes' if ans >= K else 'No')
##################################################################
[dho]完全理解
N,M,K=map(int,input().split())
H=list(map(int,input().split()))
B=list(map(int,input().split()))
if min(N,M)<K: print('No'); exit()
H,B=sorted(H),sorted(B)
H,B=H[:K],B[M-K:]
for i in range(K):
    if H[i]>B[i]: print('No'); exit()
print('Yes')
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
[TLE27]
n,m,k=map(int,input().split())
H=list(map(int,input().split()))#n
W=list(map(int,input().split()))#m
from collections import defaultdict,deque,Counter
from bisect import insort, bisect_left, bisect_right
H.sort()
CW=Counter(W)
cwkey=sorted(CW.keys())
t=0
for cw in cwkey:
  H2=H.copy()
  idx=bisect_right(H2,cw)
  mn=min(idx-t,CW[cw])
  t+=mn
  CW[cw]-=mn
if t>=k:
  print('Yes')
else:
  print('No')
##################################################################
[TLE28]
n,m,k=map(int,input().split())
H=list(map(int,input().split()))#n
W=list(map(int,input().split()))#m
from collections import defaultdict,deque,Counter
from bisect import insort, bisect_left, bisect_right
H.sort()
CW=Counter(W)
cwkey=sorted(CW.keys())
t=0
for cw in cwkey:
  H2=H.copy()
  idx=bisect_right(H2,cw)
  mn=min(idx,CW[cw])
  t+=mn
  CW[cw]-=mn
  H=H2[mn:]
if t>=k:
  print('Yes')
else:
  print('No')

##################################################################
[TLE29]
n,m,k=map(int,input().split())
H=list(map(int,input().split()))#n
W=list(map(int,input().split()))#m
from collections import defaultdict,deque,Counter
from bisect import insort, bisect_left, bisect_right
CH=Counter(H)
CW=Counter(W)
chkey=sorted(CH.keys())
cwkey=sorted(CW.keys())
t=0
for ch in chkey:
  for cw in cwkey:
    if ch<=cw and CH[ch]>0 and CW[cw]>0:
      nw=CW[cw]
      nh=CH[ch]
      mn=min(nh,nw)
      CH[ch]-=mn
      CW[cw]-=mn 
      t+=mn
      if CH[ch]==0:
        del CH[ch]
      if CW[cw]==0:
        del CW[cw]      
      #print(CH,CW)
if t>=k:
  print('Yes')
else:
  print('No')
##################################################################
[TLE29]
n,m,k=map(int,input().split())
H=list(map(int,input().split()))#n
W=list(map(int,input().split()))#m
from collections import defaultdict,deque,Counter
from bisect import insort, bisect_left, bisect_right
CH=Counter(H)
CW=Counter(W)
chkey=sorted(CH.keys())
cwkey=sorted(CW.keys())
t=0
for ch in chkey:
  for cw in cwkey:
    if ch<=cw and CH[ch]>0 and CW[cw]>0:
      nw=CW[cw]
      nh=CH[ch]
      mn=min(nh,nw)
      CH[ch]-=mn
      CW[cw]-=mn 
      #print(ch,cw,mn)
      t+=mn
if t>=k:
  print('Yes')
else:
  print('No')
##################################################################
[TLE27]
n,m,k=map(int,input().split())
H=list(map(int,input().split()))#n
W=list(map(int,input().split()))#m
from collections import defaultdict,deque,Counter
from bisect import insort, bisect_left, bisect_right
CH=Counter(H)
CW=Counter(W)
chkey=sorted(CH.keys())
cwkey=sorted(CW.keys())
t=0
for ch in chkey:
  idx=bisect_left(cwkey,ch)
  if idx>len(cwkey)-1:
    continue  
  nw=CW[cwkey[idx]]
  nh=CH[ch]
  mn=min(nh,nw)
  CH[ch]-=mn
  CW[cwkey[idx]]-=mn  
  t+=mn
  if CW[cwkey[idx]]==0:
    cwkey.pop(idx)  
if t>=k:
  print('Yes')
else:
  print('No')
  
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
##################################################################
