def convert_to_graph(directed_paths):
    graph = {}
    
    for path in directed_paths:
        start, end = path
        
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        
        if end not in graph:
            graph[end] = []
    
    return graph

# サンプルの有向の道のリスト
directed_paths = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

# グラフに変換
graph = convert_to_graph(directed_paths)

# グラフの表示
print(graph)
