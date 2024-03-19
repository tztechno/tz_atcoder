//abc100_b.py
####################################
####################################
####################################
####################################
####################################
####################################
D,N=map(int,input().split())
if D==0:
    if N!=100:
        print(1*N)
    else:
        print(101)
else:
    if N!=100:
        print(100**D*N)
    else:
        print(100**D*N+100**D)
####################################
D, N = map(int, input().split())
result = []
if D == 0:
    result = [i for i in range(1, 102) if i != 100]
elif D == 1:
    result = [i * 100 for i in range(1, 102) if i != 100]
else:
    result = [i * 10000 for i in range(1, 102) if i != 100]
print(result[N-1])
####################################
d,n=map(int,input().split())
print((n+n//100)*100**d)
####################################
[MY ANS]
d,n=map(int,input().split())
if d==0:
  t=0
  for i in range(1,2*n):
    if i%100!=0:
      t+=1
    if t==n:
      print(i)
      break
elif d==1 and n!=100:
  ans=n*(100)
  print(ans)
elif d==1 and n==100:#select 101st
  ans=10100
  print(ans)  
elif d==2 and n!=100:
  ans=n*(10000)
  print(ans)  
elif d==2 and n==100:#select 101st
  ans=1010000
  print(ans)   
####################################
