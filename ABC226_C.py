//ABC226_C.py


################################################
N = int(input())

T = []
K = []
A = []
for i in range(N):
  t, k, *a = map(int, input().split())
  T.append(t)
  K.append(k)
  A.append(a)

need = {N-1}
stack = A[-1]
while stack:
  v = stack.pop() - 1
  if v in need: continue
  need.add(v)
  for to in A[v]:
    stack.append(to)
################################################
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

#DFS
todo = [N-1] #技の番号-1
seen = [False]*N
seen[N-1] = True
ans = D[N-1][0]
while todo:
    v = todo.pop()
    for i in D[v][2:]:
        if seen[i-1]:
            continue
        todo.append(i-1)
        seen[i-1] = True
        ans += D[i-1][0]
print(ans)
################################################
import sys
def input(): return sys.stdin.readline().rstrip()
def main():
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    T = 0
    x = set([N])
    for i in range(N, 0, -1):
        t, k, *A, = L.pop()
        if i in x:
            T += t
            for a in A:
                if a not in x:
                    x.add(a)
    print(T)
if __name__ == "__main__":
    main()
################################################
