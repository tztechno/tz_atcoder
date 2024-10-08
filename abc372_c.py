
abc372_c.py

#######################################

長さNの文字列Sが与えられます。
クエリがQ個与えられるので、順番に処理してください。
i番目のクエリは以下の通りです。
整数Xi​と文字Ci​が与えられるので、SのXi​番目の文字をCi​に置き換える。
その後、Sに文字列ABCが部分文字列として何箇所含まれるかを出力する。
ここで、Sの部分文字列とは、Sの先頭から0文字以上、末尾から0文字以上削除して得られる文字列のことをいいます。
例えば、abはabcの部分文字列ですが、acはabcの部分文字列ではありません。

#######################################
[ok]

N, Q = map(int, input().split())
S = list(input())

count_ABC = 0
for i in range(N-2):
    if S[i:i+3] == ['A', 'B', 'C']:
        count_ABC += 1

for i in range(Q):
    x, c = input().split()
    x = int(x) - 1 

    for j in range(max(0, x-2), min(N-2, x+1)):
        if S[j:j+3] == ['A', 'B', 'C']:
            count_ABC -= 1 

    S[x] = c

    for j in range(max(0, x-2), min(N-2, x+1)):
        if S[j:j+3] == ['A', 'B', 'C']:
            count_ABC += 1  

    print(count_ABC)
    
#######################################

import sys
input = sys.stdin.readline

N,Q=map(int,input().split())
S=list(input().strip())

ANS=0
for i in range(len(S)):
    if S[i:i+3]==["A","B","C"]:
        ANS+=1

for tests in range(Q):
    x,c=input().split()

    x=int(x)-1

    if S[x:x+3]==["A","B","C"]:
        ANS-=1

    if x-1>=0 and S[x-1:x+2]==["A","B","C"]:
        ANS-=1


    if x-2>=0 and S[x-2:x+1]==["A","B","C"]:
        ANS-=1

    S[x]=c

    if S[x:x+3]==["A","B","C"]:
        ANS+=1

    if x-1>=0 and S[x-1:x+2]==["A","B","C"]:
        ANS+=1


    if x-2>=0 and S[x-2:x+1]==["A","B","C"]:
        ANS+=1

    print(ANS)

#######################################
[ok]

n, q = map(int, input().split())
s=list(input())

def find(s,p,q):
    global n
    a=[]
    for i in range(p,q-1):
        if i+2<n:
            if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
                a.append([i,i+2])
    return a
a=find(s,0,n)
res=len(a)
for i in range(q):
    pos,ch=map(str, input().split())
    pos=int(pos)-1
    old = find(s,max(0, pos - 2), min(n , pos+2))
    s[pos]=ch
    new=find(s, max(0, pos - 2), min(n, pos+2))
    res=res-len(old)+len(new)
    print(res)
    
#######################################

N, Q = map(int, input().split())
s = '..'+input()+'..'
c0 = s.count('ABC')
S = list(s)
S_old = list(s)


def couABC(S, x):
    ss = S[x-1]+S[x]+S[x+1]+S[x+2]+S[x+3]
    return ss.count('ABC')

for i in range(Q):
    x, c = map(str, input().split())
    x = int(x)

    S[x+1] = c
    c0 += couABC(S, x) - couABC(S_old, x)
    S_old[x+1] = c
    
    print(c0)   
    
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
