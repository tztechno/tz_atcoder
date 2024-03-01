#serch the nearest neibhor
#original

N,D = map(int, input().split())
X_Y=[]#位置

for i in range (N):
    x,y=map(int, input().split())
    X_Y.append([i,x,y,-1,10**9])#自分、自分の位置、最も近いもの、その距離二乗
print(X_Y)

for i in range (N):
    now=X_Y[i]#自分
    for j in range(N):
        com=X_Y[j]#相手
        if i!=j and (now[1]-com[1])**2+(now[2]-com[2])**2<=now[4]:
            X_Y[i][4]=(now[0]-com[0])**2+(now[1]-com[1])**2
            X_Y[i][3]=j
print(X_Y)
