##################################################################
[cgpt AC]
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
max_x = 0
for i in range(N):
    x = i + 1  
    if A[i] >= x:
        max_x = x
    else:
        break
print(max_x)
##################################################################
問題文長さNの非負整数列A=(A1​,A2​,…,AN​)が与えられます。
次を満たす最大の非負整数xを求めてください。
Aに、x以上の要素が重複を含めてx回以上現れる。
制約1≤N≤100,0≤Ai​≤10**9入力はすべて整数
##################################################################
[cgpt AC]
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
max_x = 0
for i,a in enumerate(A):
    x = i+1  
    if a >= x:
        max_x = x
    else:
        break
print(max_x)
##################################################################
[cgpt+my AC]
回数のmaxを求める
条件が適合した時だけ更新する
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
max_x = 0
for i,a in enumerate(A):
    x = i+1  
    if a >= x:
        max_x = max(max_x,x)
print(max_x)
##################################################################

##################################################################
[my AC]
#a以上の要素がa回以上の考え方
#xとa都度小さい方で（どちらもいい）、より大きいものを探す

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
max_ax = 0
for i,a in enumerate(A):
  x=i+1
  if x>=a:
    max_ax=max(max_ax,a)
  elif a>=x:
    max_ax=max(max_ax,x)
print(max_ax)
##################################################################
[my AC]
N = int(input())
A = list(map(int,input().split()))
#print(A)
A.sort(reverse=True)

#a以上の要素がa回以上(a<=t,a>=t)
#回数tのmaxを求める

#print('a,t')
ans=0
t=0#回数
for a in A:
  t+=1
  if a>=t: #aは減って、tは増えて
    ans=max(ans,t)
    #print(a,t)
print(ans)
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
#print(A)
A.sort(reverse=True)
t=0#回数
#a以上の要素がa回以上(a<=t)
#print('a,t')
ans=0
for a in A:
  t+=1
  #print(a,t)
  if a<=t:
    ans=max(ans,min(a,t))
print(ans)
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
#print(A)
A.sort(reverse=True)
t=0#回数
#a以上の要素がa回以上(a<=t)
#print('a,t')
ans=0
for a in A:
  t+=1
  #print(a,t)
  if a<=t:
    ans=max(ans,min(a,t))
print(ans)
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
#print(A)
A.sort(reverse=True)
t=0#回数
#a以上の要素がa回以上(a<=t)
#print('a,t')
for a in A:
    t+=1
    #print(a,t)
    if a<=t:
        print(min(a,t))
        break
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
#print(A)
A.sort(reverse=True)
t=0#回数
#a以上の要素がa回以上(a<=t)
#print('a,t')
for a in A:
    t+=1
    #print(a,t)
    if a<=t:
        print(a)
        break
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
for i in range(N):
  x=i+1#回数
  a=A[i]#要素
  if x>=a: ###回数が要素以上
    print(a)
    exit()
##################################################################
[titia]
import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
ANS=[0]*200
for a in A:
    MIN=min(a,199)
    for i in range(MIN,-1,-1):
        ANS[i]+=1
score=0
for i in range(len(ANS)):
    if ANS[i]>=i:
        score=i
print(score)
##################################################################
[not use counter,check all,then select max]
[my WA]
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
t=0
for i in range(N):
  x=i+1
  a=A[i]
  if a>=x: ### 要素aがx以上で、x回現れる
    t+=1
    if t>=x:
      print(x)
      exit()
##################################################################
[my WA]
N = int(input())
A = list(map(int,input().split()))
from collections import defaultdict,deque,Counter
C=Counter(A)
S=sorted(list(C))[::-1]
#print(S)
t=0
for si in S:
  t+=C[si]
  if t>=si:
    print(si)
    exit()
##################################################################
