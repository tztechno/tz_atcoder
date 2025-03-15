######################################################
######################################################

######################################################

######################################################

######################################################

######################################################

######################################################
[sato]

S = input()

ans = 0
nx = 1
txt = ""
for s in S:
    if nx and s=="i":
        txt = txt + s
        nx = 0
    elif nx==1 and s=="o":
        txt = txt + "i" + s
        nx = 1
        ans += 1
    elif nx==0 and s=="i":
        txt = txt + "o" + s
        nx = 0
        ans += 1
    elif nx==0 and s=="o":
        txt = txt + s
        nx = 1
    # print("check",txt,nx,ans)


if S[-1] =="i":
    txt = txt + "o"
    ans += 1

print(ans)


######################################################
[one]

s = input()

c = 0

if s[0] == 'o':
    c += 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    
if (len(s) + c) % 2 != 0:
    c += 1
print(c)


######################################################
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

    

######################################################

######################################################
