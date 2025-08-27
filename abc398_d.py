##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################

##################################################################
[CGPT AC]理解不能

def solve():
    import sys
    input = sys.stdin.readline

    N,R,C = map(int, input().split())
    S = input().strip()

    # 移動ベクトル
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    # 累積位置 P_t
    x, y = 0, 0
    P = [(0,0)]
    for ch in S:
        dx, dy = move[ch]
        x += dx
        y += dy
        P.append((x,y))

    ans = []
    seen = set()
    for t in range(N+1):
        seen.add(P[t])  # P_t を登録
        if t >= 1:
            target = (P[t][0] - R, P[t][1] - C)
            if target in seen:
                ans.append("1")
            else:
                ans.append("0")

    print("".join(ans))

solve()
##################################################################
[Claude TLE]
# 正しい入力形式に対応
N,R, C = map(int, input().split())
S = input().strip()

# 方向のマッピング
directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1)
}

# 累積移動を計算
cumulative = [(0, 0)]
for i in range(N):
    prev_r, prev_c = cumulative[-1]
    dr, dc = directions[S[i]]
    cumulative.append((prev_r + dr, prev_c + dc))

# 結果を格納する文字列
result = ""

# 各時刻について判定
for t in range(1, N + 1):
    found = False
    
    # 時刻tで(R,C)にある煙の出発時刻を逆算
    target_r, target_c = cumulative[t][0] - R, cumulative[t][1] - C
    
    # この位置が過去の累積移動にあるかチェック
    for start_time in range(t + 1):
        if cumulative[start_time] == (target_r, target_c):
            found = True
            break
    
    result += "1" if found else "0"

print(result)
##################################################################
[mybrain TLE]
N,R,C=map(int,input().split())
S=list(input())
P1=[(0,0)]
ANS=''
for si in S:
  P2=[(0,0)]
  if si=='N':
    for p in P1+[(0,0)]:
      P2+=[(p[0]-1,p[1])]
  elif si=='S':
    for p in P1+[(0,0)]:
      P2+=[(p[0]+1,p[1])]
  elif si=='E':
    for p in P1+[(0,0)]:
      P2+=[(p[0],p[1]+1)]
  elif si=='W':
    for p in P1+[(0,0)]:
      P2+=[(p[0],p[1]-1)]      
  #print(P2)
  if (R,C) in P2:
    ANS+='1'
  else:
    ANS+='0'
  P1=list(set(P2))
print(ANS)
##################################################################
[kota]
N, R, C = map(int, input().split())
S = list(input())
wind = {
  "N": (-1, 0),
  "W": (0, -1),
  "S": (1, 0),
  "E": (0, 1)
}

p = set()
p.add((0, 0))
wx, wy = 0, 0
ans = []

for i in range(N):
  dx, dy = wind[S[i]]
  wx += dx
  wy += dy
  
  target_vec = (wx - R, wy - C)
  
  if target_vec in p:
    ans.append("1")
  else:
    ans.append("0")
    
  p.add((wx, wy))
  
print("".join(ans))
##################################################################
[yura]
n, r, c = map(int, input().split())
s = input()

smokes = {(0, 0)}
x, y = 0, 0
for ch in s:
    x = x - 1 if ch == 'N' else x + 1 if ch == 'S' else x
    y = y - 1 if ch == 'W' else y + 1 if ch == 'E' else y
    smokes.add((-x, -y))
    print(1 if (r - x, c - y) in smokes else 0, end='')
##################################################################
[titia]
import sys
input = sys.stdin.readline

N,R,C=map(int,input().split())
S=input().strip()

NOW={(0,0)}
x=y=0
ANS=[]

for s in S:
    if s=="N":
        R+=1
        x+=1
    elif s=="S":
        R-=1
        x-=1
    elif s=="E":
        C-=1
        y-=1
    else:
        C+=1
        y+=1
    NOW.add((x,y))

    #print((R,C),NOW)

    if (R,C) in NOW:
        ANS.append(1)
    else:
        ANS.append(0)

print("".join(map(str,ANS)))
##################################################################

##################################################################
