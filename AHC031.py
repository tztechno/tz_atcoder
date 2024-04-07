##################################
[MY BEST ANS]

import math

W,D,N = map(int, input().split())
P=[]
for i in range(1,D+1):
    A = sorted(map(int, input().split()))[::-1]
    P+=[A] 

POSI=0
for d in range(D):
    sx=W//2
    ## day毎にresetされるもの
    #S=np.zeros((W,W,3), dtype=np.uint8) 
    B0,B1=W,W
    B0s,B1s=0,0 
        
    for i in range(N):
   
        pi=P[d][i]

        sy= (math.ceil(pi/(sx*6)))*5   ######
        
        if B0>=sy:
            x=0
            y=B0s
            B0-=sy
            B0s+=sy
            x2,y2=W//2,B0s
            #S[x:x2,y:y2]=normal_map[i%14]  
            #print(B0,B1)
            posi=[x,y,x2,y2]
            print(* posi)
            POSI+=1
            
        elif B1>=sy:
            x=W//2
            y=B1s
            B1-=sy
            B1s+=sy
            x2,y2=W,B1s
            #S[x:x2,y:y2]=normal_map[i%14]  
            #print(B0,B1) 
            posi=[x,y,x2,y2]
            print(* posi)
            POSI+=1
##################################
