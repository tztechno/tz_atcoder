
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.cycle_edges = set()
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, v, visited, parent):
        visited[v] = True
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, v):
                    self.cycle_edges.add((min(v, neighbor), max(v, neighbor)))
                    return True
            elif neighbor != parent:
                self.cycle_edges.add((min(v, neighbor), max(v, neighbor)))
                return True
        return False
    
    def find_cycles(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.dfs(i, visited, -1):
                    pass
    
    def get_edges(self):
        all_edges = set()
        for u in self.graph:
            for v in self.graph[u]:
                all_edges.add((min(u, v), max(u, v)))
        
        cycle_edges = self.cycle_edges
        non_cycle_edges = all_edges - cycle_edges
        
        return list(cycle_edges), list(non_cycle_edges)

# 使用例
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1), (4, 5)]
g = Graph(6)

for u, v in edges:
    g.add_edge(u, v)

g.find_cycles()
cycle_edges, non_cycle_edges = g.get_edges()

print("サイクルに属する辺:", cycle_edges)
print("サイクルに属さない辺:", non_cycle_edges)
