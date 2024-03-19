//abc345_b.py
####################################
####################################
####################################
####################################
####################################
####################################
X = int(input())
# di: 商
# mo: 余り
di, mo = divmod(X, 10)
# 余りがある時
if(mo != 0):
  print(di+1)
# 余りが無い時
else:
  print(di)
####################################
X=int(input())
print((X+9)//10)
####################################
import math
X = int(input())
if X%10 == 0:
    print(X//10)
else:
    print(X//10+1)
####################################
#my best but 1 WA

import math
x=str(input())
if x[0]=='-':
    y=x[1:]
    if len(y)>=2:
        z0=y[0:-2]
        z1=y[-2:]
        ans='-'+z0+str(math.floor(int(z1)/10))
    elif len(y)==1:
        ans='0'
else:
    y=x
    if len(y)>=2:
        z0=y[0:-2]
        z1=y[-2:]
        ans=z0+str(math.ceil(int(z1)/10))
    elif len(y)==1:
        z=y[-1]
        ans=str(math.ceil(int(z)/10))
print(ans) 
####################################
