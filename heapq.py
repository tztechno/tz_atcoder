##################################################

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

##################################################

import heapq

# シンプルなリストをヒープに変換
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(data)
print("Heapified Data:", data)

# ヒープから最小の要素を取り出す
min_element = heapq.heappop(data)
print("Min Element:", min_element)
print("Remaining Data:", data)

# 新しい要素をヒープに挿入
heapq.heappush(data, 0)
print("Data after Pushing 0:", data)

# 複数のソート済みイテラブルをマージする
sorted_data1 = [1, 3, 5, 7]
sorted_data2 = [2, 4, 6, 8]
merged_data = list(heapq.merge(sorted_data1, sorted_data2))
print("Merged Data:", merged_data)

##################################################
