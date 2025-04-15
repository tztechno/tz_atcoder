###############################################################################
###############################################################################
###############################################################################
[titia]
import sys
input = sys.stdin.readline

N,K=map(int,input().split())
S=input().strip()

ANS=[";"]*N

for i in range(N):
    if S[i]!="?":
        ANS[i]=S[i]

for i in range(N):
    if ANS[i]=="o":
        if i-1>=0:
            ANS[i-1]="."
        if i+1<N:
            ANS[i+1]="."

C=ANS.count(";")
O=ANS.count("o")
SO=S.count("o")

LIST=[]

#print(ANS)

count=0
for i in range(N):
    if ANS[i]==";":
        count+=1
    else:
        if count>0:
            LIST.append(count)
        count=0

if count!=0:
    LIST.append(count)


O2=0
for x in LIST:
    O2+=(x+1)//2
    

if O==K:
    for i in range(N):
        if ANS[i]==";":
            ANS[i]="."
elif O+O2==K:
    ind=0
    for i in range(N):
        if ANS[i]==";" and (i==0 or ANS[i-1]!=";"):
            if LIST[ind]%2==1:
                for j in range(LIST[ind]):
                    if j%2==0:
                        ANS[i+j]="o"
                    else:
                        ANS[i+j]="."
            else:
                for j in range(LIST[ind]):
                    ANS[i+j]="?"
                    
            ind+=1
                
else:
    for i in range(N):
        if ANS[i]==";":
            ANS[i]="?"

print("".join(ANS))


###############################################################################
[yukimi]
N,K=map(int,input().split())
S=list(input())
cnt=S.count('o')
if cnt==K:
    S=["." if x == "?" else x for x in S]
    exit(print(*S,sep=''))
for i in range(N-1):
    if S[i]=='o' and S[i+1]=='?':
        S[i+1]='.'
    elif S[i]=='?' and S[i+1]=='o':
        S[i]='.'
tmp = S[:]
for i in range(N):
    if tmp[i] == '?':
      if i==0 or tmp[i-1]!='o':
        tmp[i] = 'o'
M=tmp.count('o')
if M>K:exit(print(*S,sep=''))
final_s = S[:]
i = 0
while i < N:
    if final_s[i] == "?":
        start = i
        while i < N and final_s[i] == "?":
            i += 1
        seg_len = i - start
        if seg_len % 2 == 1:
            for j in range(seg_len):
                final_s[start + j] = "o" if j % 2 == 0 else "."
    else:i += 1
print("".join(final_s))
###############################################################################
[kemuri]
N, K = map(int, input().split())
S = list(input())

for i in range(N):
  if S[i] != 'o':
    continue
  
  if i > 0:
    S[i - 1] = '.'
  if i < N - 1:
    S[i + 1] = '.'

rem = K - S.count('o')

if not rem:
  ans = "".join(S).replace('?', '.')
  print(ans)
  exit()

block = []
i = 0

while i < N:
  
  if S[i] != '?':
    i += 1
    continue
  
  l = i
  
  while i < N and S[i] == '?':
    r = i
    i += 1
  
  block.append((l, r))

space = sum((r - l + 2) // 2 for l, r in block)

if space == rem:
  for l, r in block:
    w = r - l + 1
    
    if w % 2:
      for i in range(w):
        S[l + i] = "o."[i % 2]

ans = "".join(S)
print(ans)

###############################################################################
[cgpt, TLE]

N, K = map(int, input().split())
S = input()

from collections import defaultdict

dp = [{} for _ in range(N+1)]
dp[0][(0, 0)] = [''] * N  

for i in range(N):
    next_dp = defaultdict(list)
    c = S[i]

    for (o_count, prev_o), states in dp[i].items():
        if c in '.?':
            key = (o_count, 0)
            if key not in next_dp:
                next_dp[key] = states[:]
            else:
                for j in range(N):
                    if next_dp[key][j] == '':
                        next_dp[key][j] = states[j]
                    elif next_dp[key][j] != '.' and states[j] != '.':
                        next_dp[key][j] = '?'
        if c in 'o?':
            if prev_o == 0 and o_count + 1 <= K:
                key = (o_count + 1, 1)
                if key not in next_dp:
                    new_states = states[:]
                    new_states[i] = 'o'
                    next_dp[key] = new_states
                else:
                    for j in range(N):
                        if j == i:
                            if next_dp[key][j] == '':
                                next_dp[key][j] = 'o'
                            elif next_dp[key][j] != 'o':
                                next_dp[key][j] = '?'
                        else:
                            if next_dp[key][j] == '':
                                next_dp[key][j] = states[j]
                            elif next_dp[key][j] != states[j] and states[j] != '':
                                next_dp[key][j] = '?'

    dp[i+1] = next_dp

possible = list(dp[N].items())
valid_Ts = [state for (o_cnt, _), state in possible if o_cnt == K]

ans = ['?'] * N
for i in range(N):
    chars = set(state[i] if state[i] else '.' for state in valid_Ts)
    if len(chars) == 1:
        ans[i] = chars.pop()
    else:
        ans[i] = '?'

print(''.join(ans))
###############################################################################
[gemini,TLE]
def solve():
    N, K = map(int, input().split())
    S = input()
    
    T = ['?'] * N
    
    for i in range(N):
        dot_count = 0
        o_count = 0
        
        for j in range(1 << S.count('?')):
            temp_S = list(S)
            binary = bin(j)[2:].zfill(S.count('?'))
            
            binary_index = 0
            for k in range(N):
                if temp_S[k] == '?':
                    if binary[binary_index] == '0':
                        temp_S[k] = '.'
                    else:
                        temp_S[k] = 'o'
                    binary_index += 1
            
            temp_S_str = "".join(temp_S)
            
            if temp_S_str.count('o') == K and 'oo' not in temp_S_str:
                if temp_S_str[i] == '.':
                    dot_count += 1
                else:
                    o_count += 1
        
        if dot_count > 0 and o_count == 0:
            T[i] = '.'
        elif dot_count == 0 and o_count > 0:
            T[i] = 'o'
        else:
            T[i] = '?'
            
    print("".join(T))

solve()
###############################################################################
[my WA]
###############################################################################
[my WA]

N,K=map(int,input().split())
S=list(input())

for i in range(N-1):
  if S[i]=='o':
    S[i+1]='.'
  if S[N-1-i]=='o':
    S[N-2-i]='.'

ANS=''.join(S)
if S.count('o')+S.count('?')==K:
  ANS=ANS.replace('?','o')
  
print(ANS)
###############################################################################
