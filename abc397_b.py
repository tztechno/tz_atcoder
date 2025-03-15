
###################################################
###################################################

###################################################
###################################################

###################################################
[suru]

a = list(input())
c=0
t=0
while t <= len(a)-1:
  if(t%2==0 and a[t] != "i"):
    a.insert(t, "i")
    c+=1
  elif(t%2!=0 and a[t] != "o"):
    a.insert(t, "o")
    c+=1
  t+=1

if(a[-1] != "o"):
  print(c+1)
else:
  print(c)
###################################################
[hob]理解不能

def is_subsequence(s, t):  # s は t の（連続とは限らない）部分列となっているか？
    i = 0
    for c in s:
        ok = False
        for j in range(i, len(t)):
            if c == t[j]:
                ok = True
                i = j+1
                break
        if not ok:
            return False
    return True


S = input()
c = 1
while True:
    T = 'io'*c
    if is_subsequence(S, T):
        exit(print(2*c - len(S)))
    c += 1
###################################################
[titia]

import sys
input = sys.stdin.readline

S=list(input().strip())
ANS=0

while S:
    if len(S)>=2:
        if S[0]=="i" and S[1]=="o":
            S=S[2:]
            continue
        if S[0]=="i" and S[1]=="i":
            ANS+=1
            S.pop(0)
            continue
        if S[0]=="o" and S[1]=="o":
            ANS+=1
            S.pop(0)
            continue
        if S[0]=="o" and S[1]=="i":
            ANS+=1
            S.pop(0)
            continue
    if len(S)==1:
        ANS+=1
        S.pop(0)

print(ANS)

    
###################################################
[my AC]
s=str(input())
s2=s.replace('ii','ioi').replace('oo','oio').replace('ii','ioi').replace('oo','oio')
if s2[-1]=='i':
  s2+='o'
if s2[0]=='o':
  s2='i'+s2
print(len(s2)-len(s))
###################################################
