import heapq

def prim(graph):
    mst = []  # 最小全域木の辺を格納するリスト
    visited = set()  # 訪れたノードを格納するセット
    start_node = list(graph.keys())[0]  # 開始ノードを任意に選ぶ
    visited.add(start_node)
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]

    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst

# グラフの例
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 4), ('D', 6)],
    'C': [('A', 3), ('B', 4), ('D', 2)],
    'D': [('B', 6), ('C', 2)]
}

minimum_spanning_tree = prim(graph)
print(minimum_spanning_tree)

###############################################################################

def find(parents, node):
    while parents[node] != node:
        node = parents[node]
    return node

def union(parents, ranks, node1, node2):
    root1 = find(parents, node1)
    root2 = find(parents, node2)

    if root1 != root2:
        if ranks[root1] > ranks[root2]:
            parents[root2] = root1
        else:
            parents[root1] = root2
            if ranks[root1] == ranks[root2]:
                ranks[root2] += 1

def kruskal(graph):
    mst = []  # 最小全域木の辺を格納するリスト
    edges = []

    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    edges.sort()  # 辺を重みの昇順にソート

    parents = {node: node for node in graph}
    ranks = {node: 0 for node in graph}

    for weight, u, v in edges:
        if find(parents, u) != find(parents, v):
            mst.append((u, v, weight))
            union(parents, ranks, u, v)

    return mst

# グラフの例
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 4), ('D', 6)],
    'C': [('A', 3), ('B', 4), ('D', 2)],
    'D': [('B', 6), ('C', 2)]
}

minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)
