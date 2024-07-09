abc174_c.py
#############################
[WA]

K=int(input())
for i in range(1,10000):
  K2=K*i
  if set(list(str(K2)))=={'7'}:
    print(len(str(K2)))
    exit()
else:
  print(-1)

#############################
[titia]

input = sys.stdin.readline
K=int(input())
if K%2==0 or K%5==0:
    print(-1)
else:   
    NOW=0
    for i in range(1,10**6+3):
        NOW=NOW+7*pow(10,i,K)
        NOW%=K
        if NOW==0:
            print(i)
            break
    else:
        print(-1)
        
#############################
