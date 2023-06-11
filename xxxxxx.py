import sys
input = sys.stdin.readline
import optuna

n,m,k=map(int,input().split())

XY=[]
for i in range(n):
    x,y=map(int,input().split())
    XY+=[(x,y)]
    
UVW=[]
for i in range(m):
    u,v,w=map(int,input().split())
    UVW+=[(u,v,w)]
    
AB=[]
for i in range(k):
    a,b=map(int,input().split())
    AB+=[(a,b)]

def objective(trial):
    MS=[1]*m
    PS=[10]*n
    cost=0
    for i in range(m):
        MS[i]=trial.suggest_categorical('m'+str(i),[0,1]) 
        cost+=UVW[i][2]*MS[i]
    for j in range(n):
        PS[i]=trial.suggest_int('p'+str(j),0,10000) 
        cost+=PS[i]**2
    return cost

study = optuna.create_study(direction='minimize') 
study.optimize(objective, n_trials=100)
best_trial= study.best_trial.params

P=[]
for i in range(n):
    P+=[best_trial['p'+str(i)]]
B=[]
for i in range(m):
    B+=[best_trial['m'+str(i)]]
print(*P)
print(*B)
