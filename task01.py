import networkx as nx
import matplotlib.pyplot as plt

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

pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("Вузли:",G.nodes())
print("Ребра", G.edges())
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", {node: G.degree(node) for node in G.nodes()})
for edge in G.edges(data=True):
    print(f"Ребро: {edge[0]} - {edge[1]}, Вага: {edge[2]['weight']}")


plt.title("Транспортна мережа")
#plt.show()
plt.savefig("task01.png", format='png')
plt.close()
