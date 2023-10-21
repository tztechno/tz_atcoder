############################################

lst = [(a0,b0),(a1,b1),...]
sorted_lst = sorted(lst, key=lambda x: x[1])

############################################

sorted_list = sorted(my_list, key=lambda x: x[1])
sorted_list_descending = sorted(my_list, key=lambda x: x[1], reverse=True)

############################################

from operator import itemgetter
from heapq import heappop,heappush

N=int(input())
TD=[list(map(int,input().split())) for i in range(N)]

for i in range(N):
    TD[i][1]+=TD[i][0]

print(TD)

TD.sort(key=itemgetter(0))

############################################

