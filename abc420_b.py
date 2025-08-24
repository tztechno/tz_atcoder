##################################################################
問題文人1,2,…,N(Nは奇数)が、M回の0か1かを選択する投票を行いました。
各人の各回の投票はN個の長さMの0,1からなる文字列S1​,S2​,…,SN​として与えられ、Si​のj文字目は人iのj回目の投票への内容を表します。
各回の投票で、少数派であった人は1点を得ます。より厳密には、次のルールで得点が与えられます。
その回の投票で0を選択した人がx人、1を選択した人がy人いたとします。
x=0またはy=0である場合、その投票では全員に1点が与えられる。
そうでなくx<yである場合、その投票で0に投票した人のみに1点が与えられる。
そうでない場合、その投票で1に投票した人のみに1点が与えられる。
なお、Nが奇数であることからx=yとなることはないことに留意してください。
M回の投票を終えた後、それらの投票における合計の得点が最も高い人を全員求めてください。
制約Nは1≤N≤99を満たす奇数Mは1≤M≤100を満たす整数Si​は長さMの0,1からなる文字列
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

##################################################################

##################################################################
[mybrain AC]
N,M=map(int,input().split())
S=[]
for i in range(N):
  s=list(input())
  S+=[s]
St = [list(col) for col in zip(*S)]
P=[0]*N
for si in St:
  if len(set(si))==1:
    for i in range(N):
      P[i]+=1
  elif si.count('0')>si.count('1'):
    for i,sii in enumerate(si):
      if sii=='1':
        P[i]+=1
  elif si.count('1')>si.count('0'):
    for i,sii in enumerate(si):
      if sii=='0':
        P[i]+=1    
ans=[]
for i,pi in enumerate(P):
  if pi==max(P):
    ans+=[i+1]
print(*ans)
##################################################################
[mybrain AC]
import numpy as np
N,M=map(int,input().split())
S=[]
for i in range(N):
  s=list(input())
  S+=[s]
Sa=np.array(S)
Sb1=np.rot90(Sa)
Sb2=np.rot90(Sb1)
Sb3=np.rot90(Sb2)
#print(Sb3)
P=[0]*N
P2=np.array(P)
for si in Sb3:
  if len(set(list(si)))==1:
    P2+=1
  elif list(si).count('0')>list(si).count('1'):
    for i,sii in enumerate(si):
      if sii=='1':
        P2[i]+=1
  elif list(si).count('1')>list(si).count('0'):
    for i,sii in enumerate(si):
      if sii=='0':
        P2[i]+=1    
P3=P2[::-1] 
#print(P3)
m=max(P3)
ans=[]
for i,pi in enumerate(P3):
  if pi==m:
    ans+=[i+1]
print(*ans)
##################################################################
[myai AC]
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

scores = [0] * N

for j in range(M):
    count0 = sum(S[i][j] == '0' for i in range(N))
    count1 = N - count0
    
    if count0 == 0 or count1 == 0:
        for i in range(N):
            scores[i] += 1
    elif count0 < count1:
        for i in range(N):
            if S[i][j] == '0':
                scores[i] += 1
    else:
        for i in range(N):
            if S[i][j] == '1':
                scores[i] += 1

max_score = max(scores)
winners = [i+1 for i, s in enumerate(scores) if s == max_score]

print(*winners)

##################################################################
