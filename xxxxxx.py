####################################
##grid search version

#library block
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV    
import sys
input = sys.stdin.readline

#input block
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
    
#function block
def objective(parameters):
    MS = [1] * m
    PS = [10] * n
    cost = 0
    for i in range(m):
        MS[i] = parameters['m' + str(i)]
        cost += UVW[i][2] * MS[i]
    for j in range(n):
        PS[j] = parameters['p' + str(j)]
        cost += PS[j] ** 2
    return cost

# Define the parameter grid for GridSearchCV
parameter_grid = {}
for i in range(m):
    parameter_grid['m'+str(i)] = [0,1]
for j in range(n):
    parameter_grid['p'+str(j)] = list(range(10001))

# Perform grid search
grid_search = GridSearchCV(estimator=None, 
                           param_grid=parameter_grid, 
                           scoring='neg_mean_squared_error', 
                           cv=5)
grid_search.fit(XY,AB)

best_params = grid_search.best_params_

P = []
for i in range(n):
    P.append(best_params['p'+str(i)])
B = []
for i in range(m):
    B.append(best_params['m'+str(i)])

print(*P)
print(*B)

####################################
##optuna version

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
####################################
