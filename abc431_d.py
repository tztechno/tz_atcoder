###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[claude modified, TLE34]
n = int(input())
WHB = []
tw = 0
for _ in range(n):
    w, h, b = map(int, input().split())
    WHB.append((w, h, b))
    tw += w

DP = {(0, 0): (0, 0)}

for w, h, b in WHB:
    DP2 = {}
    for (hw, bw), (hj, bj) in DP.items():

        key1 = (hw, bw + w)
        val1 = (hj, bj + b)
        if key1 not in DP2 or hj + bj + b > DP2[key1][0] + DP2[key1][1]:
            DP2[key1] = val1

        if hw + w <= tw // 2:
            key2 = (hw + w, bw)
            val2 = (hj + h, bj)
            if key2 not in DP2 or hj + h + bj > DP2[key2][0] + DP2[key2][1]:
                DP2[key2] = val2
    
    DP = DP2

jmax = 0
for (hw, bw), (hj, bj) in DP.items():
    jmax = max(jmax, hj + bj)

print(jmax)
###############################################
[MLE46]
n=int(input())
WHB=[]
tw=0
for _ in range(n):
  w,h,b=map(int,input().split())
  WHB+=[(w,h,b)]
  tw+=w
DP=[(0,0,0,0)]#HW,BW,HJ,BJ
for i,(w,h,b) in enumerate(WHB):
  DP2=[]
  for dpi in DP:
    DP2+=[(dpi[0],dpi[1]+w,dpi[2],dpi[3]+b)]
    if dpi[0]+w<=tw//2:
      DP2+=[(dpi[0]+w,dpi[1],dpi[2]+h,dpi[3])]    
  DP=DP2
  #print(DP)
jmax=0
for dpi in DP:
  j=dpi[2]+dpi[3]
  jmax=max(jmax,j)
print(jmax)
###############################################
[TLE46]
n=int(input())
W=[]
for _ in range(n):
  w,h,b=map(int,input().split())
  W+=[(w,h,b)]
max_value=-1  
for i in range(1<<n):
  H_w=0  
  H_h=0  
  W_w=0  
  W_b=0  
  for j in range(n):
    if i & (1 << j):  
      H_w += W[j][0]  
      H_h += W[j][1]  
    else:
      W_w += W[j][0]  
      W_b += W[j][2]  
  if H_w <= W_w:
    total = H_h + W_b
    max_value = max(max_value, total)
print(max_value)
###############################################
###############################################
###############################################
###############################################
[claude,AC]
n = int(input())
items = []
total_w = 0
total_b = 0

for _ in range(n):
    w, h, b = map(int, input().split())
    items.append((w, h, b))
    total_w += w
    total_b += b

INF = float('inf')
dp = [-INF] * (total_w + 1)
dp[0] = 0

for w, h, b in items:
    for cur_w in range(total_w, w - 1, -1):
        if dp[cur_w - w] > -INF:
            dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + h)

max_value = -1

for h_w in range(total_w + 1):
    w_w = total_w - h_w
    if h_w <= w_w and dp[h_w] > -INF:
        pass

dp = {}
dp[0] = (0, 0)  

for w, h, b in items:
    new_dp = dp.copy()
    for cur_w, (cur_h, cur_b) in dp.items():
        new_w = cur_w + w
        new_h = cur_h + h
        new_b = cur_b + b
        if new_w not in new_dp or new_dp[new_w][0] + (total_b - new_dp[new_w][1]) < new_h + (total_b - new_b):
            new_dp[new_w] = (new_h, new_b)
    dp = new_dp

max_value = -1
for h_w, (h_h, h_b) in dp.items():
    w_w = total_w - h_w
    if h_w <= w_w:
        w_b = total_b - h_b
        total = h_h + w_b
        max_value = max(max_value, total)

print(max_value)
###############################################
[jala,AC]
n = int(input())
dp = [0] # i:全体重量のうち体の占める重量
inf = -10**18

for _ in range(n):
    w,h,b = map(int,input().split())
    l = len(dp)
    dp += [inf]*w
    for i in range(l-1,-1,-1):
        old=dp[i]
        if dp[i] == inf : continue
        
        dp[i]=max(old, old+h) #頭につける（体の重さは変わらないので、indexは変化なし）
        dp[i+w]=max(dp[i+w],old+b) #体につける（indexがwだけ移動）

ans = max(dp[(len(dp)//2):])
print(ans)
###############################################
[one,AC]
n = int(input())
whb = [ list(map(int, input().split())) for _ in range(n) ]

sm = sum(w for w,_,_ in whb)

mx = 501*n
dp = [0] * (mx+550)
for i in range(n):
  ndp = [0] * (mx+550)
  for j in range(mx):
    ndp[j+whb[i][0]] = max(ndp[j+whb[i][0]], dp[j]+whb[i][1])
    ndp[j] = max(ndp[j], dp[j]+whb[i][2])
  dp = ndp
ans = 0
for i in range(mx):
  if i *2 <= sm:
    ans = max(ans, dp[i])
print(ans)
###############################################
###############################################
###############################################
###############################################
###############################################
