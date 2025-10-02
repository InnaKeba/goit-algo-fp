import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней: нескінченність для всіх, крім стартової вершини
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Бінарна купа (піраміда): (відстань, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за збережену — пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перебір сусідів
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Оновлення відстані, якщо знайдена коротша
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Створення графа
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
    'E': [('C', 10), ('D', 2), ('Z', 3)],
    'Z': [('D', 6), ('E', 3)]
}

# Запуск алгоритму
start_vertex = input("Введіть стартову вершину (A, B, C, D, E, Z). Наприклад, D або C: ").strip()
if start_vertex not in graph:
    print("Такої вершини немає в графі.")
else:
    shortest_paths = dijkstra(graph, start_vertex)
    print(f"\nНайкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"  до {vertex}: {distance}")