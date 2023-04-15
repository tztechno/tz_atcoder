#A1７
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

T=[0]*n
T[0]=0
T[1]=T[0]+A[0]
T[2]=min(T[1]+A[1],T[0]+B[0])

for i in range(3,n):
  T[i]=min(T[i-1]+A[i-1],T[i-2]+B[i-2])
print(T)
print(T[n-1])
