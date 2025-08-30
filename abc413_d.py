##################################################################
問題文
長さNの整数列A=(A1​,A2​,…,AN​)が与えられます。
ここで、どのi(1≤i≤N)についてもAi​が0でないことが保証されます。
Aを適切に並べ替えた数列B=(B1​,B2​,…,BN​)が等比数列になることがあるか判定してください。
ただし、数列S=(S1​,S2​,…,SN​)が等比数列であるとは、ある実数rが存在してすべての整数1≤i<Nに対してSi+1​=rSi​が成り立つことをいいます。
1つの入力ファイルにつき、T個のテストケースを解いてください。
制約
1≤T≤10**5
2≤N≤2×10**5
−10**9≤Ai​≤10**9(1≤i≤N)
Ai​!=0(1≤i≤N)
1つの入力ファイルにおけるNの総和は2×10**5以下
入力はすべて整数
##################################################################
3
5
1 8 2 4 16
5
-16 24 54 81 -36
7
90000 8100 -27000 729 -300000 -2430 1000000
---
Yes
No
Yes
##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[claude WA]

from fractions import Fraction
from itertools import permutations

def can_form_geometric_sequence(A):
    n = len(A)
    if n <= 1:
        return True

    for start_val in A:
        if start_val == 0:
            continue

        for second_val in A:
            if second_val == start_val:
                continue

            r = Fraction(second_val, start_val)
            geometric_seq = []
            current = Fraction(start_val)
            
            for i in range(n):
                if current.denominator != 1:
                    break
                geometric_seq.append(int(current))
                current *= r

            if len(geometric_seq) == n:
                if sorted(geometric_seq) == sorted(A):
                    return True
    
    return False

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        
        result = can_form_geometric_sequence(A)
        print("Yes" if result else "No")

if __name__ == "__main__":
    solve()

##################################################################
[soo]
def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    if n==2:
        print('Yes')
        return
    f=arr[0]
    if all(abs(arr[x])==abs(f) for x in range(1,n)):
        s=sum([1 if arr[i]>0 else 0 for i in range(n)])
        print('Yes' if (s==0 or s==n or s==n//2 or n-s==n//2) else 'No')
        return
        
    arr.sort(key=lambda x:abs(x))
    for i in range(1,n-1):
        if arr[i]*arr[i]!=arr[i-1]*arr[i+1]:
            print('No')
            return
    print('Yes')

t=int(input())
for _ in range(t):
    solve()
##################################################################
[ito]
T=int(input())
for _ in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    a=[(abs(A[i]),A[i]>0) for i in range(n)]
    if n==2:
        print('Yes')
        continue
    a.sort()
    for i in range(n-2):
        if a[i+2][0]*a[0][0]!=a[i+1][0]*a[1][0]:
            break
    else:
        for i in range(n-2):
            if (a[i+1][1]==a[i+2][1])!=(a[1][1]==a[0][1]):
                break
        else:
            print('Yes')
            continue
        for i in range(n):
            if a[i][0]!=a[0][0]:
                break
        else:
            c=0
            for i in range(n):
                if a[i][1]:
                    c+=1
            if c==n//2 or c==(n+1)//2:
                print('Yes')
                continue
    print('No')
##################################################################
[sus]
T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    for b in a:
        if not abs(a[0]) == abs(b):
            break
    else:
        if abs(a.count(a[0]) * 2 - n) <= 1 or a.count(a[0]) == n:
            print('Yes')
        else:
            print('No')
        continue

    a.sort(key=abs)
    for i in range(n-2):
        if a[i] * a[i+2] != a[i+1]**2:
            print('No')
            break
    else:
        print('Yes')
##################################################################
[ali]
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: abs(x))
    print('Yes' if all([a[i] ** 2 == a[i - 1] * a[i + 1] for i in range(1, n - 1)]) or (abs(a[0]) == abs(a[-1]) and abs(2 * a.count(min(a)) - n) < 2) else 'No')
##################################################################
[titia]
import sys
input = sys.stdin.readline

T=int(input())
for tests in range(T):
    N=int(input())
    A=list(map(int,input().split()))

    if len(set(A))==1:
        print("Yes")
        continue

    A.sort(key=lambda x:abs(x))

    if abs(A[0])==abs(A[-1]):
        plus=0
        minus=0

        for a in A:
            if a>=0:
                plus+=1
            else:
                minus+=1

        if N%2==0:
            if plus==minus:
                print("Yes")
            else:
                print("No")
            continue
        else:
            if abs(plus-minus)==1:
                print("Yes")
            else:
                print("No")
            continue
        

    flag=1

    for i in range(1,len(A)-1):
        a=A[i-1]
        b=A[i]
        c=A[i+1]

        if b*b==a*c:
            pass
        else:
            flag=0
            break

    if flag:
        print("Yes")
    else:
        print("No")
                

            

##################################################################
