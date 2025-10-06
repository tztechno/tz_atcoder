###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[cgpt1 TLE,RE]
N,X=map(int,input().split())
AB=[]
for i in range(N):
  a,b=map(int,input().split())
  AB+=[(a+b,b)]
  
from typing import List
from math import comb

def enumerate_compositions_at_most_N(X: int, N: int) -> List[List[int]]:
    res = []
    if X <= 0 or N <= 0:
        return res
    def dfs(remaining: int, cur: List[int]):
        if remaining == 0:
            res.append(cur.copy())
            return
        if len(cur) == N:  
            return
        for v in range(1, remaining+1):
            cur.append(v)
            dfs(remaining - v, cur)
            cur.pop()
    dfs(X, [])
    return res

MIN=10**19
for c in enumerate_compositions_at_most_N(X,N):
    t=0
    for i,ci in enumerate(list(c)):
      if ci==1:
        t+=AB[i][0]
      else:
        t+=AB[i][0]+AB[i][1]*(ci-1)
    #print(list(c),t)
    MIN=min(MIN,t)
print(MIN)

###############################################
###############################################
[deepseek1 AC]
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    X = int(data[1])
    AB = []
    idx = 2
    for i in range(N):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        AB.append((a, b))
    
    result = float('inf')
    
    # ステージkまで進んで、ステージkを複数回クリアする場合を考える
    base = 0
    for k in range(min(N, X)):
        base += AB[k][0] + AB[k][1]  # 各ステージを1回ずつクリア
        remaining = X - (k + 1)  # 残りのクリア回数
        
        # ステージ0〜kの中で最も効率的なステージを選んで残り回数をクリア
        current_time = base + remaining * AB[k][1]
        result = min(result, current_time)
    
    print(result)

if __name__ == "__main__":
    main()
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
