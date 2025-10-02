##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
[my WA]修正の都度、辞書順最小を選んでいない

S=list(input())
T=list(input())
ANS=[]
X=S
while X!=T:
  for i,(s,t) in enumerate(zip(X,T)):
    if s!=t:
      X[i]=t
      ANS+=[''.join(X)]
print(len(ANS))
if len(ANS)>0:
  for a in ANS:
    print(a)  

##################################################
[deepseek]

S = list(input().strip())
T = list(input().strip())
n = len(S)
diff = [i for i in range(n) if S[i] != T[i]]
current = S[:]
X = []
while diff:
    best_str = None
    best_index = -1
    for i in diff:
        temp = current[:]
        temp[i] = T[i]
        temp_str = ''.join(temp)
        if best_str is None or temp_str < best_str:
            best_str = temp_str
            best_index = i
    current[best_index] = T[best_index]
    diff.remove(best_index)
    X.append(''.join(current))
print(len(X))
if len(X)>0:
  for s in X:
      print(s)

##################################################
