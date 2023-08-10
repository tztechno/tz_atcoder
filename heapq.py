#heapq.heappush,heapq.nsmallest,heapq.heappop

import heapq
S = []
Q=int(input())
for i in range(Q):
  qi=list(map(int,input().split()))
  if qi[0]==1:
    heapq.heappush(S,qi[1])
  elif qi[0]==2:
    svalue = heapq.nsmallest(1,S)[0]#最も小さい値を示す（取り去らない）
    print(svalue)
  else:
    heapq.heappop(S)#最も小さい値を取り去る
