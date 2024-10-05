abc374_d.py
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
[not understand]

import sys
input = sys.stdin.readline
from itertools import permutations

N,S,T=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
L=list(permutations(range(N)))
ANS=1<<63

for LIST in L:
    score=0
    for j in range(2**N):
        score=0
        for i in range(len(LIST)):    
            if i==0:
                z,w=0,0
            else:
                if j & (1<<(i-1)) != 0:
                    z,w=A[LIST[i-1]][2:]
                else:
                    z,w=A[LIST[i-1]][:2]

            if j & (1<<i) != 0:
                a,b,c,d=A[LIST[i]]
            else:
                c,d,a,b=A[LIST[i]]

            score+=(((c-a)**2+(d-b)**2)**(1/2))/T
            score+=(((z-a)**2+(w-b)**2)**(1/2))/S

        #print(score)

        if ANS>score:
            ANS=score

print(ANS)

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
