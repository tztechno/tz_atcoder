###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[TLE6]
n=int(input())
from collections import defaultdict
cnt = defaultdict(list)

for _ in range(n):
  a,b=map(int,input().split())
  cnt[a].append(b)
  cnt[b].append(a)
  
M=set()#到達範囲
M.add(1)
checked=set()#check済み

while len(M-checked)>0:
  #print(M-checked)
  M2=set()#拡大
  adchecked=set()
  for li in list(M-checked):
    lst2=cnt[li]
    adchecked.add(li)    
    M2|=set(lst2)
  if M2==set():
    break
  else:
    M|=M2
    checked|=adchecked
print(max(list(M)))

###############################################
###############################################
###############################################
###############################################
[deepseek]
from collections import defaultdict, deque

def main():
    n = int(input())
    graph = defaultdict(list)
    
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set([1])
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    print(max(visited))

if __name__ == "__main__":
    main()
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
