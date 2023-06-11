n,m,k=3,2,3
XYP=[(0,0,5),(95,-67,4),(-42,-50,3),]
UVW=[(1, 2, 3284),(0, 1, 3284)]
AB=[(-58, 40),(-17, 51),(32, -36)]

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

x = range(-100, 101)
y = range(-100, 101)

for x,y,p in XYP:
    plt.scatter(x,y,c='red')
    circle = Circle((x,y), p, edgecolor='red', facecolor='none')
    plt.gca().add_patch(circle)
    
for a,b in AB:
    plt.scatter(a,b,c='blue')
    
for u,v,w in UVW:
    (x0,y0)=XY[u]
    (x1,y1)=XY[v]
    x=[x0,x1]
    y=[y0,y1]
    plt.plot(x,y, color='yellow')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot')
plt.grid(True)
plt.show()
