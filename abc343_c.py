abc343_c.py
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
[yuki]
def kaibun(v):
  str_v = str(v)
  if str_v == str_v[::-1]:
    return True
  else:
    return False

N = int(input())
ans = 1

for t in range(1, 1_000_001):
  v = t**3
  if v > N:
    break
  if kaibun(v):
    ans = v

print(ans)
#############################################
[keroru]
ans=0
n=I()
for i in range(int(n**(1/3)+10)):
    x=i**3
    if x>n:
        break
    if str(x)==str(x)[::-1]:
        ans=x
print(ans)

#############################################
[titia]

LIST=[]

for i in range(10**6+5):
    s=i*i*i
    S=str(s)

    if S==S[::-1]:
        LIST.append(s)

N=int(input())
for l in LIST:
    if l<=N:
        OK=l

print(OK)
#############################################
#############################################
#############################################
#############################################
#############################################
[my AC]
N=int(input())
m=int(N**(1/3))+10 ##### 1以上を足さないと漏れが生じる
# 最低限ACのために加える数字は1であった
# 何も加えない場合は WA12
for i in range(m,0,-1):
  s=str(i**3)
  if s==s[::-1] and i**3<=N:
    print(s)
    exit()
#############################################
[my WA]
N=int(input())
m=int(N**(1/3))
for i in range(m,0,-1):
  s=str(i**3)
  if s==s[::-1]:
    print(s)
    exit()
#############################################
[my WA]

N=int(input())
if N<10**7:
  m=int(N**(1/3))
  for i in range(m,0,-1):
    s=str(i**3)
    if s==s[::-1]:
      print(s)
      exit()
elif N<10**10:
  m=int((N//10**6)**(1/3))
  for i in range((m+1)*100,0,-1):
    s=str(i**3)
    if s==s[::-1] and i**3<=N:
      print(s)
      exit()
else:
  m=int((N//10**9)**(1/3))
  for i in range((m+1)*1000,0,-1):
    s=str(i**3)
    if s==s[::-1] and i**3<=N:
      print(s)
      exit()
#############################################
