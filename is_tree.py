def is_tree(adj_list):
    n = len(adj_list)  # 頂点の数
    visited = [False] * n  # 頂点の訪問状態
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    if dfs(0, -1) and all(visited):
        return True
    else:
        return False
