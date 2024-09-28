

abc372_d.py
######################################################
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

Q=[]

TO=[-1]*N

for i in range(N):
    a=A[i]
    if Q and Q[-1][0]>a:
        Q.append((a,i))

    else:
        while Q and Q[-1][0]<a:
            x,ind=Q.pop()
            TO[ind]=i

        Q.append((a,i))

DP=[1]*N

for i in range(N-1,-1,-1):
    if TO[i]==-1:
        pass
    else:
        DP[i]=DP[TO[i]]+1
    

DP.append(0)

print(*DP[1:])
######################################################
N=int(input())
h=list(map(int,input().split()))
stc=[]
ans=[0]*N
for i in range(N-2,-1,-1):
  while stc and h[stc[-1]]<h[i+1]:
    stc.pop()
  stc.append(i+1)
  ans[i]=len(stc)
print(*ans)
######################################################
n = int(input())
h = list(map(int, input().split()))
ans = []
stack = []
for hi in h[::-1]:
    ans.append(len(stack))
    while stack and hi > stack[-1]: #not if
        stack.pop()
    stack.append(hi)
print(*ans[::-1])

######################################################
