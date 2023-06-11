with open('/kaggle/input/my-atcoder/in/0000.txt', 'r') as f:
    data = f.read()
lines = data.split('\n')

XY=[]
UVW=[]
AB=[]
for i,line in enumerate(lines):

    if i==0:
        n,m,k=map(int,line.split())
    elif 1<=i<1+n:
        x,y=map(int,line.split())
        XY+=[(x,y)]
        if i==+n:
            print(line)
    elif 1+n<=i<1+n+m:
        u,v,w=map(int,line.split())
        UVW+=[(u,v,w)]
        if i==+n+m:
            print(line)        
    elif 1+n+m<=i<1+n+m+k:
        a,b=map(int,line.split())
        AB+=[(a,b)]
        if i==+n+m+k:
            print(line)
        
print('n,m,k')
print(n,m,k) 
print('XY')
print(XY[0:3])
print('UVWQ')
print(UVW[0:3])
print('AB')
print(AB[0:3])
