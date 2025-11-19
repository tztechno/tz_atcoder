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

[nada]
def check(s,t):
    if len(s) > len(t):
        return check(t,s)
    if len(s) < len(t)-1:
        return False
    i,j,miss =0,0,0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            miss += 1
            if miss > 1:
                return False
            if len(s) == len(t):
                i +=1
            j +=1
    return True

N,T=input().split()
N=int(N)
ans =[]
for i in range(N):
    S=input()
    if check(S,T):
        ans.append(i+1)
print(len(ans))
print(" ".join(map(str, ans)))

###############################################
###############################################

[titia]
import sys
input = sys.stdin.readline

N,T=input().split()
N=int(N)

SX=[input().strip() for i in range(N)]

ANS=[]

for ix in range(N):
    S=SX[ix]
    if S==T:
        ANS.append(ix+1)
        continue

    if len(T)==len(S)+1:
        ind=0
        f=0
        for i in range(len(S)):
            if ind<len(T) and S[i]==T[ind]:
                ind+=1
                continue
            elif ind+1<len(T) and S[i]==T[ind+1]:
                ind+=2
                f+=1
                continue
            else:
                f+=10


        if f<=1:
            ANS.append(ix+1)

    if len(T)==len(S)-1:
        ind=0
        f=0
        for i in range(len(T)):
            if ind<len(S) and T[i]==S[ind]:
                ind+=1
                continue
            elif ind+1<len(S) and T[i]==S[ind+1]:
                ind+=2
                f+=1
                continue
            else:
                f+=10

        if f<=1:
            ANS.append(ix+1)

    if len(T)==len(S):
        f=0
        for i in range(len(S)):
            if S[i]!=T[i]:
                f+=1



        if f<=1:
            ANS.append(ix+1)

print(len(ANS))
print(*ANS)

###############################################
###############################################

[naga]
N, T = input().split()
N = int(N)
ans = []
for i in range(1, N + 1):
    S = input()
    s_idx = 0
    t_idx = 0
    cnt = 0
    if abs(len(S) - len(T)) > 1:
        continue
    while s_idx < len(S) and t_idx < len(T):
        if S[s_idx] != T[t_idx]:
            if len(S) > len(T):
                s_idx += 1
            elif len(S) < len(T):
                t_idx += 1
            else:
                s_idx += 1
                t_idx += 1
            cnt += 1
        else:
            s_idx += 1
            t_idx += 1
    if cnt <= 1 and abs(s_idx - t_idx) <= 1:
        ans.append(i)

print(len(ans))
print(*ans)

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[AC]
import sys

try:
    line = sys.stdin.readline().split()
    if not line:
        N, T = 0, ""
    else:
        N = int(line[0])
        T = line[1]
except:
    N, T = 0, ""

len_T = len(T)

def judge_fast(S, len_S):
    if S == T:
        return True
    
    if abs(len_S - len_T) > 1:
        return False

    if len_S == len_T:
        diff_count = 0
        for s_char, t_char in zip(S, T):
            if s_char != t_char:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1
    
    i = 0
    j = 0
    
    while i < len_S and j < len_T:
        if S[i] != T[j]:
            if len_S > len_T:
                i += 1
            elif len_T > len_S:
                j += 1
            else:
                return False
            
            return S[i:] == T[j:]

        i += 1
        j += 1
        
    return True

matching_indices = []

for i in range(1, N + 1):
    try:
        S = sys.stdin.readline().strip()
    except:
        break
    
    if not S and i <= N: 
        continue 
    
    len_S = len(S)
    
    if abs(len_S - len_T) > 1:
        continue
        
    if judge_fast(S, len_S):
        matching_indices.append(i)

print(len(matching_indices))
print(*(matching_indices))
###############################################
###############################################
###############################################
[TLE11]
n0,t=map(str,input().split())
n=int(n0)

#s--t
def judge(t,s):
  result=False
  T=list(t)
  S=list(s)
  if  t==s:
    result=True
  elif len(S)==len(T):
    wg=0
    for s,t in zip(S,T):
      if s!=t:
        wg+=1
    if wg==1:
      result=True
  elif len(S)==len(T)+1:
    for i,s in enumerate(T):
      if S[i]!=T[i] and S[0:i]+S[i+1:]==T:
        result=True
      elif S[0:len(T)]==T:
        result=True
  elif len(S)+1==len(T):
    for i,t in enumerate(S):
      if T[i]!=S[i] and T[0:i]+T[i+1:]==S:
        result=True
      elif T[0:len(S)]==S:
        result=True
  return result
  
ans=0
iss=[]
for i in range(n):
  s=str(input())
  result=judge(s,t)
  if result==True:
    iss+=[i+1]
    ans+=1
print(ans)
print(*iss)
  
###############################################
###############################################
###############################################
###############################################
