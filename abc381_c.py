################################################
################################################
################################################
[myans AC]

N=int(input())
S=list(input())
did=[]
for i,si in enumerate(S):
  if si=='/':
    did+=[i]
m=0
for di in did:
  MAX=[]
  for i in range(min(di,N-di+1)):
    if di-1-i>=0 and di+1+i<N and S[di-1-i]=='1' and S[di+1+i]=='2':
      MAX+=[i]
    else:
      break
  #print(MAX)
  m=max(m,len(MAX))
print(m*2+1)

################################################
[myans TLE]

N=int(input())
S=list(input())

def judge(S):
  m=len(S)//2
  if len(S)%2==1 and S[0:m]==['1']*m and S[m]=='/' and S[m+1:]==['2']*m:
    return m*2+1
  else:
    return 0
    
MAX=0
for i in range(N):
  for j in range(i,N):
    S2=S[i:j+1]
    MAX=max(MAX,judge(S2))
print(MAX)
    

################################################
