
import networkx as nx

# 町と道の情報を入力する
towns = [1, 2, 3, 4, 5]
roads = [(1,2), (2,3), (4,5)]

# 無向グラフを作成する
G = nx.Graph()

# 町をグラフに追加する
G.add_nodes_from(towns)

# 道をグラフに追加する
G.add_edges_from(roads)

# 連結成分を求める
connected_components = list(nx.connected_components(G))

# 連結成分の数を表示する
print(connected_components)
# [{1, 2, 3}, {4, 5}]
