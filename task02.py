import networkx as nx
from collections import deque


def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex])) 

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  


def main():
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

    # створюємо список суміжності
    adjacency_list = {node: [] for node in G.nodes()}

    for u, v in G.edges():
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    print("список суміжності")
    print(adjacency_list)

    print("DFS: ", end='')
    dfs_iterative(adjacency_list, 'A')
    print("")
    print("BFS: ", end='')
    bfs_iterative(adjacency_list, 'A')
    print("")


if __name__ == "__main__":
    main()