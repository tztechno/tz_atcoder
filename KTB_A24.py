#stpete AC

from bisect import bisect_left
N=int(input())
A=list(map(int,input().split()))
R=[0]
for i in range(N):
  ai=A[i]
  if R[-1]<ai:
    R+=[ai]
  elif R[-1]>ai:
    position = bisect_left(R,ai)
    R[position]=ai
print(len(R[1:]))
