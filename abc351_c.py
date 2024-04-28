abc351_c.py
#################################################
#################################################
#################################################
#################################################
#################################################
[shakayami]
N=int(input())
A=[int(i) for i in input().split()]
stack=[A[0]]
for i in range(1,N):
    if stack[-1]==A[i]:
        stack[-1]+=1
    else:
        stack.append(A[i])
    
    while(len(stack)>=2 and stack[-1]==stack[-2]):
        stack.pop()
        stack[-1]+=1

print(len(stack))
#################################################
[titia]
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

Q=[]

for a in A:
    Q.append(a)

    while len(Q)>=2:
        if Q[-1]==Q[-2]:
            x=Q.pop()
            y=Q.pop()
            Q.append(x+1)
        else:
            break

print(len(Q))
#################################################
[AC]
[popで端から削りながら取得するか、削らずappendを使うか]

import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

stock=[]
for ai in A:####DIFFERENCE
  stock+=[ai]###DIFFERENCE
  while len(stock)>=2:
    if stock[-2]==stock[-1]:
      a=stock.pop()
      b=stock.pop()
      stock+=[a+1]
    else:
      break

print(len(stock))
#################################################    
[my TLE]
[この操作はリストの長さに比例して時間がかかります。要素を取り出した後にリスト全体が1つずつずれるためです。
 そのため、リストの先頭から順番に要素を取り出すたびに、リスト全体をシフトする必要があり、処理に時間がかかります。]

import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

stock=[]
for i in range(N):
  stock+=[A.pop(0)]
  while len(stock)>=2:
    if stock[-2]==stock[-1]:
      a=stock.pop()
      b=stock.pop()
      stock+=[a+1]
    else:
      break

print(len(stock))
#################################################
[AC]
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

stock=[]
for ai in A:######DIFFERENCE
  stock+=[ai]#####DIFFERENCE
  while len(stock)>=2 and stock[-2]==stock[-1]:
    a=stock.pop()
    b=stock.pop()
    stock+=[a+1]
 
print(len(stock))
#################################################
[my TLE]
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

stock=[]
for i in range(N):
  stock+=[A.pop(0)]
  while len(stock)>=2 and stock[-2]==stock[-1]:
    a=stock.pop()
    b=stock.pop()
    stock+=[a+1]
 
print(len(stock))
#################################################
