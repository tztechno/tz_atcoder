###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[TLE16]
n=int(input())
#ab+cd=n
AB=[]
C=[]
for ab in range(1,n):
  for a in range(1,n):
    if ab%a==0:
      b=ab//a
      AB+=[(a,b,ab)]
      C+=[ab]
t=0
ANS=[]
for abi in AB:
  a,b,ab =abi
  cd=n-ab
  if cd in C:
    for c in range(1,n):
      if cd%c==0:
        d=cd//c
        ANS+=[(a,b,c,d)]
        t+=1
print(t)

###############################################
[TLE16]
n=int(input())
#ab+cd=n
from collections import defaultdict,deque,Counter
cnt = defaultdict(list)
C=[]
for ab in range(1,n):
  for a in range(1,n):
    if ab%a==0:
      b=ab//a
      cnt[ab].append((a,b))
      C+=[ab]
#print(cnt)
t=0
#ANS=[]
for ab in cnt.keys():
  cd=n-ab
  if cd in C:
    t+=len(cnt[cd])*len(cnt[ab])
print(t)

###############################################
[TLE15]
n=int(input())
#ab+cd=n
from collections import defaultdict,deque,Counter
cnt = defaultdict(int)
for ab in range(1,n):
  for a in range(1,n):
    if ab%a==0:
      b=ab//a
      cnt[ab]+=1
#print(cnt)
t=0
#ANS=[]
for ab in cnt.keys():
  cd=n-ab
  if cd in cnt.keys():
    t+=cnt[cd]*cnt[ab]
print(t)

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
