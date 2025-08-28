
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
[myai explanation]
N = int(input())
C = []
A = []
for i in range(N):
    c = int(input())
    a = list(map(int, input().split()))
    assert len(a) == c #関係ない
    C.append(c)
    A.append(a)

X = int(input())　#出目
minC = float("inf")

for c, a in zip(C, A):
    if X in a:
        minC = min(minC, c) #最小の賭け数を見つける

ANS = []
for i, (c, a) in enumerate(zip(C, A)):
    if c == minC and X in a: #前半だけでは条件の半分、リストの中にXがあることをここで確認
        ANS.append(i + 1)

print(len(ANS))
if ANS:
    print(*ANS)
##################################################################
[myai AC]
N = int(input())
C = []
A = []
for i in range(N):
    c = int(input())
    a = list(map(int, input().split()))
    assert len(a) == c
    C.append(c)
    A.append(a)

X = int(input())
minC = float("inf")

for c, a in zip(C, A):
    if X in a:
        minC = min(minC, c)

ANS = []
for i, (c, a) in enumerate(zip(C, A)):
    if c == minC and X in a:   
        ANS.append(i + 1)

print(len(ANS))
if ANS:
    print(*ANS)
##################################################################
[myrain WA]
N=int(input())
C=[]
A=[]
for i in range(N):
  c=int(input())
  a=list(map(int,input().split()))
  C+=[c]
  A+=[a]
X=int(input())
minC=10**9
for c,a in zip(C,A):
  if X in a:
    minC=min(minC,c)
ANS=[]
for i,(c,a) in enumerate(zip(C,A)):
  if c==minC:　#aの中に出目がある保証はない、WAの理由
    minC=min(minC,c)
    ANS+=[i+1]
print(len(ANS))
print(*ANS)
##################################################################
