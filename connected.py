##################################################

def is_connected_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    start_vertex = vertices[0]
    dfs(start_vertex)

    return len(visited) == len(vertices)

# 例として、頂点と辺の情報を設定
vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

if is_connected_graph(vertices, edges):
    print("The graph is connected.")
else:
    print("The graph is not connected.")

##################################################

def is_connected(vertices, edges, vertex1, vertex2):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(vertex1)

    return vertex2 in visited

##################################################
