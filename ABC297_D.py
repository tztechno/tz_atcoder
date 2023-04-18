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
