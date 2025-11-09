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
##################################################################
##################################################################
##################################################################
##################################################################
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
