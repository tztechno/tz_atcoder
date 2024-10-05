abc374_d.py
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
[my WA]
N,S,T=map(int,input().split())

P=[]
mapping={}
for i in range(N):
  a,b,c,d=map(int,input().split())
  P+=[(a,b),(c,d)]
  mapping[(a,b)]=(c,d)
  mapping[(c,d)]=(a,b)

import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_nearest_point(target_point, points_list):
    nearest_point = None
    min_distance = float('inf')
    for point in points_list:
        distance = euclidean_distance(target_point, point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = point
    return nearest_point, min_distance

NOTVISITED=P
START=(0,0)
TIME=0
while NOTVISITED:
  nearest,dist=find_nearest_point(START,NOTVISITED)
  NOTVISITED.remove(nearest)
  NOTVISITED.remove(mapping[nearest])
  TIME+=dist/S
  TIME+=euclidean_distance(nearest,mapping[nearest])/T
  START=mapping[nearest]

print(TIME) 
########################################################################################
