abc119_a.py
########################################
S = str(input())
import pandas as pd
S2 = pd.to_datetime([S])
if S2<='2019-04-30':
  print('Heisei')
else:
  print('TBD')
########################################
from datetime import datetime
S = input()
date_input = datetime.strptime(S,'%Y/%m/%d')
date_threshold = datetime(2019,4,30)
if date_input <= date_threshold:
    print('Heisei')
else:
    print('TBD')
########################################
y,m,d=map(int,input().split('/'))

if y<2019:
    print("Heisei")
else:
    if m<4:
        print("Heisei")
    else:
        if m==4 and d<=30:
            print("Heisei")
        else:
            print("TBD")
########################################
S =input()
s = S.split("/")
if int(s[1]) <=4:
  print("Heisei")
else:
  print("TBD")
########################################
########################################
########################################
