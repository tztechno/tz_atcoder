
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

########################################

'''
# nx.algorithms.xxxxxx

NetworkX provides a wide range of algorithms for various graph-related tasks under the nx.algorithms namespace. 

### Graph Algorithms:

is_connected: Check if a graph is connected.
is_bipartite: Check if a graph is bipartite.
is_tree: Check if a graph is a tree.
shortest_path: Find the shortest path between nodes.
minimum_spanning_tree: Find a minimum spanning tree of a graph.
transitive_closure: Compute the transitive closure of a directed graph.

### Centrality Measures:

degree_centrality: Compute degree centrality for nodes.
betweenness_centrality: Compute betweenness centrality for nodes.
closeness_centrality: Compute closeness centrality for nodes.
eigenvector_centrality: Compute eigenvector centrality for nodes.

### Clustering and Community Detection:

clustering: Compute the clustering coefficient for nodes.
community: Community detection algorithms like Louvain, Girvan-Newman, etc.

### Matching and Flows:

max_weight_matching: Find a maximum weight matching in a graph.
minimum_cut: Find a minimum cut in a graph.
maximum_flow: Compute the maximum flow in a flow network.

### Shortest Paths:

shortest_path: Find the shortest path between nodes.
all_pairs_shortest_path: Compute all shortest paths between pairs of nodes.

### Isomorphism and Graph Comparison:

is_isomorphic: Check if two graphs are isomorphic.
graph_edit_distance: Compute the graph edit distance between two graphs.


'''
