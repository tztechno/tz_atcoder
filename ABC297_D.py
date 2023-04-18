＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
#AC
a, b = map(int, input().split())
t = 0
while a != b:
    if a > b:
        a, b = b, a
  if a > b:
    if a % b==0:
      t += -1+(a//b)
      a = b
    else:
      t += a//b
      a %= b
print(t)
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
#TLE
a, b = map(int, input().split())
t = 0 
while a != b:
    if a > b:
        a, b = b, a
    if a < b:
        b = b - a
        t += 1
print(t)
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
#TLE
a, b = map(int, input().split())
t = 0
while a != b:
    if a > b:
        a = a - b
        t += 1
    elif a < b:
        b = b - a
        t += 1 
print(t)
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
