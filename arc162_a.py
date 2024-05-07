arc162_a.py
######################################
[titia]
[このコードは、与えられた配列Aの要素を入れ替え、その配列に基づいて
 最長増加部分列(Longest Increasing Subsequence, LIS)の長さを求めています。]

import sys
input = sys.stdin.readline

T=int(input())
for tests in range(T):
    n=int(input())
    A=list(map(int,input().split()))

    for i in range(n):
        A[i]-=1

    A_INV=[-1]*n

    for i in range(n):
        A_INV[A[i]]=i

    A=A_INV

    NG=[0]*(n+1)

    for i in range(n):
        for j in range(i):
            if A[i]<A[j]:
                NG[A[i]-1]=1

    print(n-sum(NG))
######################################
