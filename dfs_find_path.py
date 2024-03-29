####################################################################################################

# 深さ優先探索を行う関数（pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値）
def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

# グラフの隣接リスト表現
G = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

# 頂点の青色の情報を格納するリスト
visited = [False] * len(G)

# 深さ優先探索を位置 0 から開始
dfs(0, G, visited)

# 頂点の青色の状態を表示
for i, is_blue in enumerate(visited):
    if is_blue:
        print(f"頂点 {i} は青色です。")
    else:
        print(f"頂点 {i} は青色ではありません。")

####################################################################################################

n=int(input())
A=[0]+list(map(int,input().split()))

USED=[0]*(n+1)

for i in range(1,n+1):
    if USED[i]==0:
        Q=[i]
        while True:
            x=Q[-1]
            USED[x]=1
            to=A[x]

            if USED[to]==0:
                Q.append(to)
            else:
                break

        last=Q[-1]
        f=Q.index(A[last])

        ANS=Q[f:]
        print(len(ANS))
        print(*ANS)
        break

####################################################################################################

def find_path(graph, start, end, path=[]):
    path = path + [start]  # 現在の道に現在のノードを追加する

    if start == end:  # 終点に到達した場合、道を返す
        return path

    if start not in graph:  # グラフ内に開始点が存在しない場合、道は存在しない
        return None

    for node in graph[start]:  # 開始点から出る各道を探索する
        if node not in path:  # まだ通過していないノードのみを探索する
            new_path = find_path(graph, node, end, path)  # 再帰的に道を探索する
            if new_path:
                return new_path

    return None  # 開始点から終点への道が見つからない場合

# サンプルグラフの定義
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'

result = find_path(graph, start_node, end_node)
if result:
    print(f"開始点 '{start_node}' から終点 '{end_node}' への道: {result}")
else:
    print(f"開始点 '{start_node}' から終点 '{end_node}' への道は存在しません。")

####################################################################################################

def find_path(graph, start, end, path=[]):
    path = path + [start]  # 現在の道に現在のノードを追加する

    if start == end:  # 終点に到達した場合、道を返す
        return path

    if start not in graph:  # グラフ内に開始点が存在しない場合、道は存在しない
        return None

    for node in graph[start]:  # 開始点から出る各道を探索する
        if node not in path:  # まだ通過していないノードのみを探索する
            new_path = find_path(graph, node, end, path)  # 再帰的に道を探索する
            if new_path:
                return new_path

    return None  # 開始点から終点への道が見つからない場合

# サンプルグラフの定義
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'

# 必ず使う道のリスト
required_paths = [('A', 'B'), ('B', 'D'), ('D', 'F')]

# グラフに必ず使う道を追加
for path in required_paths:
    start, end = path
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

result = find_path(graph, start_node, end_node)
if result:
    print(f"開始点 '{start_node}' から終点 '{end_node}' への道: {result}")
else:
    print(f"開始点 '{start_node}' から終点 '{end_node}' への道は存在しません。")

####################################################################################################
