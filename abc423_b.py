###############################################
問題文
N+1個の部屋が一列に並んでおり、順に0,1,…,Nの番号が付けられています。
部屋の間にはN個のドアがあり、1,2,…,Nの番号が付けられています。
ドアiは部屋i−1と部屋iの間にあります。
各ドアについて鍵の状態を表す値Li​が与えられ、Li​=0のときドアiの鍵は開いており、Li​=1のときドアiの鍵は閉まっています。
2人の人がおり、1人は部屋0に、もう1人は部屋Nにいます。
それぞれの人は、ドアiの鍵が開いているときに限り、部屋i−1と部屋iの間を移動することができます。
このとき、2人のいずれも到達できない部屋の個数を求めてください。
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
###############################################
###############################################
###############################################
###############################################
###############################################
[titia AC]
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

if max(A)==0:
    print(0)
    exit()

ANS=N-1

for i in range(N):
    if A[i]==0:
        ANS-=1
    else:
        break

for i in range(N-1,-1,-1):
    if A[i]==0:
        ANS-=1
    else:
        break

print(ANS)
###############################################
[ai AC]
N=int(input())
L=list(map(int,input().split()))

def unreachable_rooms(N, L):
    left = 0
    for i in range(1, N+1):
        if L[i-1] == 0:  
            left = i
        else:
            break
    left_reachable = set(range(0, left+1))
    right = N
    for i in range(N, 0, -1):
        if L[i-1] == 0:
            right = i-1
        else:
            break
    right_reachable = set(range(right, N+1))
    all_rooms = set(range(N+1))
    unreachable = all_rooms - (left_reachable | right_reachable)
    return len(unreachable)

print(unreachable_rooms(N, L))  
###############################################
[mybrain WA]
N=int(input())
A=list(map(int,input().split()))
B=A[::-1]
I=0
for i in range(N):
  if A[i]==1:
    I=i
    break
J=N-1
for i in range(N):
  if B[i]==1:
    J=N-1-i
    break
if J>I:
  print(J-I)
else:
  print(0)
###############################################
[mybrain RE]
N=int(input())
L=list(map(int,input().split()))
a = L.index(1) 
b= len(L) - 1 - L[::-1].index(1) 
print(b-a)
###############################################
[mybrain RE]
N=int(input())
L=list(map(int,input().split()))#N
if 0 not in L:
  print(0)
  exit()
a = L.index(1) 
b = L[::-1].index(1)
c = N-b-1
#print(a,b,c)
print(c-a)
###############################################
[mybrain WA]
N=int(input())
L=list(map(int,input().split()))#N
B=[1]*N
for i,l in enumerate(L):
  if l==0:
    B[i]=0
  elif l==1:
    B[i]=0
    break
for i,l in enumerate(L[::-1]):
  if l==0:
    B[N-1-i]=0
  elif l==1:
    B[N-1-i]=0
    break
print(sum(B)+1)  
###############################################
