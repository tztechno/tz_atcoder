#################################################
```
[titia]

import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

ANS=1
for i in range(n):
    for j in range(1,n):
        now=i
        score=0
        while True:
            if now<n and A[now]==A[i]:
                score+=1
            else:
                break
            now+=j

        ANS=max(ANS,score)

print(ANS)
```        
#################################################
#################################################
#################################################
#################################################
#################################################
