import networkx as nx 
from graph_utils import create_city_graph, visualize_city_graph, coordinates_data, distances_from_table

def analyze_and_display_graph_properties():
    """
    Створює граф, відображає його основні характеристики
    та візуалізує його.
    """
    print("--- Аналіз та візуалізація графу міст України ---")

    # 1. Створення графу
    ukraine_graph = create_city_graph(coordinates_data, distances_from_table)
    print("\nГраф успішно створено.")

    # 2. Відображення вузлів (міст)
    print("\n--- Вузли (міста) графу ---")
    print(list(ukraine_graph.nodes()))

    # 3. Відображення ребер (доріг)
    print("\n--- Ребра (дороги) графу ---")
    # Ребра містять атрибут 'weight' (вагу/відстань)
    for u, v, data in ukraine_graph.edges(data=True):
        print(f"({u} -- {v}): Відстань {data['weight']} км")

    # 4. Кількість вершин та ребер
    print("\n--- Загальна інформація про граф ---")
    print(f"Кількість вершин (міст): {ukraine_graph.number_of_nodes()}")
    print(f"Кількість ребер (доріг): {ukraine_graph.number_of_edges()}")

    # 5. Ступінь вузлів (кількість доріг, що ведуть з міста)
    print("\n--- Ступінь кожного вузла (міста) ---")
    # nx.degree повертає об'єкт типу DegreeView, який можна перетворити на словник
    node_degrees = dict(ukraine_graph.degree())
    for city, degree in node_degrees.items():
        print(f"{city}: {degree} доріг")

    # 6. Візуалізація графу
    # print("\n--- Візуалізація графу ---")
    # зберегти файл і показати його
    # visualize_city_graph(ukraine_graph, coordinates_data,
    #                      title="Карта доріг України",
    #                      save_path="ukraine_city_map.png",
    #                      show=True)
    
    print("\n--- Збереження зображення ---")
    # зберегти, не показуючи вікно
    visualize_city_graph(ukraine_graph, coordinates_data,
                         title="Карта доріг України",
                         save_path="ukraine_city_map.png",
                         show=False)
    
    print("\nАналіз та візуалізацію завершено.")


if __name__ == "__main__":
    analyze_and_display_graph_properties()
    