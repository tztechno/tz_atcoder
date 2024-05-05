abc190_c.py
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
[AC, cGPT created]
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = [list(map(int, input().split())) for _ in range(K)]

ANS = 0
for i in range(1 << K):
    T = [C[j][0] if (i >> j) & 1 == 0 else C[j][1] for j in range(K)]
    ans = sum(1 for a in A if all(x in T for x in a))
    ANS = max(ANS, ans)

print(ANS)
#####################################
[AC, cGPT fix my cords]
[##### if (i >> j) & 1 == 0: #####]
    
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = [list(map(int, input().split())) for _ in range(K)]

ANS = 0
for i in range(1 << K):
    T = []
    ans = 0
    for j in range(K):  # 修正点
        if (i >> j) & 1 == 0:  # 修正点
            T.append(C[j][0])  # 修正点
        else:
            T.append(C[j][1])  # 修正点
    for a in A:
        if a[0] in T and a[1] in T:
            ans += 1
    ANS = max(ANS, ans)

print(ANS)
#####################################
[AC, cGPT fix my cords]
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = [list(map(int, input().split())) for _ in range(K)]

ANS = 0
for i in range(1 << K):
    T = []
    ans = 0
    bit_string = bin(i)[2:].zfill(K)  # ビット列を K 桁に拡張
    for j, b in enumerate(bit_string):
        if b == '0':
            T.append(C[j][0])
        else:
            T.append(C[j][1])
    for a in A:
        if a[0] in T and a[1] in T:
            ans += 1
    ANS = max(ANS, ans)

print(ANS)    
#####################################    
[My WA]
N,M=map(int,input().split())
A=[]
for i in range(M):
  a,b=map(int,input().split())
  A+=[[a,b]]
K=int(input())
C=[]
for i in range(K):
  c,d=map(int,input().split())
  C+=[[c,d]]
ANS=0
for i in range(1<<K):
  T=[]
  ans=0
  for j,b in enumerate(list(bin(i)[2:])):
    
    if b=='0':
      T+=[C[j][0]]
    else:
      T+=[C[j][1]]
  for a in A:
    if a[0] in T and a[1] in T:
      ans+=1
  ANS=max(ANS,ans)
print(ANS)      
    
#####################################
