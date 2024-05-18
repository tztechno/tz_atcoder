abc345_c.py
###############################################
[titia AC]
import sys
input = sys.stdin.readline

n=int(input())
L=[]
for i in range(n):
    x,y=map(int,input().split())
    L.append((x,-y,i+1))

L.sort()

MAX=[-1<<60]*(n+1)
for i in range(n-1,-1,-1):
    MAX[i]=max(MAX[i+1],L[i][1])

D=set()

for i in range(n):
    if L[i][1]<MAX[i+1]:
        D.add(L[i][2])

ANS=set(range(1,n+1))-D

print(len(ANS))
print(*sorted(ANS))

###############################################
[shakayami AC]
N=int(input())
card=[]
for i in range(N):
    a,c=map(int,input().split())
    card.append((i,a,c))
card.sort(key=lambda x:-x[1])
ans=[]
minC=10**18
for i,a,c in card:
    if c<minC:
        ans.append(i+1)
    minC=min(c,minC)
ans.sort()
print(len(ans))
print(*ans)

###############################################
[kotatsu cpp AC]
#include<iostream>
#include<algorithm>
#include<vector>
#include<cassert>
using namespace std;
int A[2<<17],C[2<<17];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;cin>>N;
	vector<int>id(N);
	for(int i=0;i<N;i++)
	{
		cin>>A[i]>>C[i];
		id[i]=i;
	}
	sort(id.begin(),id.end(),[](int i,int j){return A[i]>A[j];});
	vector<int>ans;
	int mn=2e9;
	for(int i:id)
	{
		if(mn>C[i])mn=C[i],ans.push_back(i);
	}
	sort(ans.begin(),ans.end());
	cout<<ans.size()<<"\n";
	for(int v:ans)cout<<v+1<<" ";
	cout<<endl;
}
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[my TLE14]
[強さでソートして、コストの逆転を拾い上げる]
[i,jで全ての組み合わせを調べるところが時間の無駄]
N=int(input())
A=[]
for i in range(N):
  a,c=map(int,input().split())
  A+=[[a,c,i+1]]
A2=sorted(A)[::-1]
#print(A2)
M=list(range(1,N+1))
DEL=[]
for i in range(N-1):
  for j in range(i+1,N):
    if A2[i][1]<A2[j][1]:
      DEL+=[A2[j][2]]
ANS=set(M)-set(DEL)
print(len(ANS))
print(*list(ANS))
###############################################
