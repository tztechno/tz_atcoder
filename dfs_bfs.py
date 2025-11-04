##########################################################
def dfs_shortest_path(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = dfs_shortest_path(graph, node, end, path + [node])
            if new_path is not None:
                if shortest is None or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest

# 使用例
# C-----F
# |     |
# A--B--E
#    |
#    D
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'},
}

start_node = 'A'
end_node = 'F'
result = dfs_shortest_path(graph, start_node, end_node)
print(result)  # ['A', 'C', 'F']
##########################################################
from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    visited = set([start])
    queue = deque([(start, [])])
    while queue:
        (node, path) = queue.popleft()
        for neighbor in graph[node] - visited:
            if neighbor == end:
                return path + [node, neighbor]
            else:
                visited.add(neighbor)
                queue.append((neighbor, path + [node]))
    return None

# 使用例
# C-----F
# |     |
# A--B--E
#    |
#    D
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'},
}

start_node = 'A'
end_node = 'F'
result = bfs_shortest_path(graph, start_node, end_node)
print(result)  # ['A', 'C', 'F']

##########################################################

def dfs(s):
    res = [-1] * n
    res[s] = 0
    stack = [[s, 0]]
    while stack:
        i, d = stack.pop()
        for j in path[i]:
            if res[j] >= 0:
                continue
            res[j] = d + 1
            stack.append([j, d + 1])
    return res

s	    探索の開始ノード（頂点）のインデックス。
res	    各ノードへの最短距離を格納した配列。
path	グラフの隣接リスト。

##########################################################

##########################################################
