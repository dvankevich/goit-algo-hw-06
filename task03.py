import networkx as nx

G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_weighted_edges_from([
    ('A', 'B', 5),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 1),
    ('D', 'E', 3)
])

# Знаходження найкоротших шляхів між всіма парами вершин
def all_pairs_shortest_paths(graph):
    return dict(nx.all_pairs_dijkstra(graph))

shortest_paths = all_pairs_shortest_paths(G)

#print(shortest_paths)

for start_node, (distances, paths) in shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node in distances:
        print(f"  до {end_node}: відстань = {distances[end_node]}, шлях = {paths[end_node]}")