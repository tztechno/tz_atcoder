##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[torugam]
N = int(input())
P = list(map(int,input().split()))

hash = []
for i in range(len(P)-1):
    if P[i]<P[i+1]:
        hash.append("<")
    else:
        hash.append(">")

run_length = []
value = hash[0]
index = 0
for i in range(1,len(hash)):
    if value == hash[i]:
        continue
    else:
        run_length.append((value,i-index))
        value = hash[i]
        index = i
else:
    run_length.append((value,len(hash)-index))

# print(hash)
# print(run_length)

count = 0
before = 0
for i in range(len(run_length)):
    if run_length[i][0] == "<":
        count += before*run_length[i][1]
        before = run_length[i][1]
print(count)
##################################################################
[karu]
ans = 0
n = int(input())
a = [*map(int, input().split())] + [-1]
b, c = 0, 0
for i in range(n):
    if a[i + 1] > a[i]:
        c += 1
    elif c > 0:
        ans += c * b
        b, c = c, 0
print(ans)
##################################################################
[my WA]

N=int(input())
A=list(map(int,input().split()))
C=''
for i in range(N-1):
  if A[i]<A[i+1]:
    C+='<'
  else:
    C+='>'
C=C.replace('<>','aa').replace('><','bb')

ANS=set()
for i in range(N-1):
  for j in range(i+1,N-1):
    if j-i>=4 and C[i:j+1].count('aa')==1 and C[i:j+1].count('bb')==1 and (C[i]=='a' or C[i]=='<'):
      ANS.add(C[i:j+1])
print(len(ANS))

      
##################################################################
[titia]
import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

LIST=[0]*n

for i in range(1,n-1):
    if A[i-1]<A[i] and A[i]>A[i+1]:
        LIST[i]=1
    if A[i-1]>A[i] and A[i]<A[i+1]:
        LIST[i]=-1

#print(LIST)

X=[(0,10)]

for i in range(n):
    if LIST[i]==1:
        X.append((i,1))
    elif LIST[i]==-1:
        X.append((i,-1))

X.append((n-1,10))

ANS=0
for i in range(1,len(X)):
    if X[i][1]==1:
        if i+2<len(X):
            ANS+=(X[i][0]-X[i-1][0])*(X[i+2][0]-X[i+1][0])

print(ANS)

##################################################################

##################################################################

##################################################################
