BFS

----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------


----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------


----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------


----------------------------------------------------------------------
from collections import deque

def bfs(graph, start):
    """
    Performs Breadth-First Search (BFS) on the given graph starting from the specified node.

    Args:
        graph: A dictionary representing the graph, where keys are nodes and values are lists of adjacent nodes.
        start: The starting node for the BFS traversal.

    Returns:
        A list containing the visited nodes in BFS order.
    """

    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS traversal

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return visited

----------------------------------------------------------------------
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
----------------------------------------------------------------------
from collections import deque

# グラフを隣接リストとして表現
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

def bfs(start):
    visited = set()        # 訪問済みノードを記録するセット
    queue = deque([start]) # キューを初期化、最初は開始ノード
    visited.add(start)     # 開始ノードを訪問済みにする

    while queue:
        node = queue.popleft()  # キューの先頭からノードを取り出す
        print(node, end=" ")    # ノードを処理 (この場合は出力)

        # 隣接するすべてのノードに対して処理を行う
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)   # 訪問済みとして記録
                queue.append(neighbor)  # キューに追加

# 1 から探索を始める
bfs(1)

----------------------------------------------------------------------


