
###################################################
###################################################

###################################################
###################################################

###################################################
###################################################
[hob]

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
