###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[mogura]
M = int(input())
S1 = list(input())
S2 = list(input())
S3 = list(input())
S1*=3
S2*=3
S3*=3

ans=10**18
for n in range(10):
    #1→2→3
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S1[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S2[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S3[l])==n:
            temp=l
            break
    ans=min(ans,temp)

    #1→3→2
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S1[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S3[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S2[l])==n:
            temp=l
            break
    ans=min(ans,temp)

    #2→1→3
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S2[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S1[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S3[l])==n:
            temp=l
            break
    ans=min(ans,temp)

    #2→3→1
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S2[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S3[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S1[l])==n:
            temp=l
            break
    ans=min(ans,temp)

    #3→1→2
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S3[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S1[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S2[l])==n:
            temp=l
            break
    ans=min(ans,temp)

    #3→2→1
    first=10**18
    second=10**18
    temp=10**18
    for j in range(3*M):
        if int(S3[j])==n:
            first=j
            break
    for k in range(first+1,3*M):
        if int(S2[k])==n:
            second=k
            break
    for l in range(second+1,3*M):
        if int(S1[l])==n:
            temp=l
            break
    ans=min(ans,temp)

if ans==10**18:
    print(-1)
else:
    print(ans)
###############################################
###############################################
[titia]
import sys
input = sys.stdin.readline

M=int(input())
S=[input().strip() for i in range(3)]

ANS=1<<60

for i in range(420):
    for j in range(420):
        for k in range(420):
            if i==j or j==k or i==k:
                continue
            if S[0][i%M]==S[1][j%M]==S[2][k%M]:
                ANS=min(ANS,max(i,j,k))

if ANS==1<<60:
    print(-1)
else:
    print(ANS)

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
