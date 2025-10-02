import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from colorsys import hsv_to_rgb  # Для генерації контрастних кольорів

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(heap_list, index=0):
    if index >= len(heap_list):
        return None
    node = Node(heap_list[index])
    node.left = build_heap_tree(heap_list, 2 * index + 1)
    node.right = build_heap_tree(heap_list, 2 * index + 2)
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_contrast_colors(n):
    colors = []
    for i in range(n):
        hue = 0.6 - 0.6 * (i / max(n - 1, 1))  # Від синього до червоного
        saturation = 0.9
        value = 0.9
        r, g, b = hsv_to_rgb(hue, saturation, value)
        hex_color = f'#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}'
        colors.append(hex_color)
    return colors

def bfs_color(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

def dfs_color(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited

def draw_colored_traversal(root, visited_nodes, title, filename):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    gradient = generate_contrast_colors(len(visited_nodes))  # 🔸 Заміна градієнту
    for i, node in enumerate(visited_nodes):
        node.color = gradient[i]

    for node in visited_nodes:
        if node.id in tree.nodes:
            tree.nodes[node.id]['color'] = node.color

    colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.savefig(filename, format='png') #Збереження зображення у файл
    plt.show()

heap = [0, 4, 1, 5, 10, 3]

# BFS
root = build_heap_tree(heap)
bfs_nodes = bfs_color(root)
draw_colored_traversal(root, bfs_nodes, "Обхід у ширину (BFS)", "task_5_bfs.png")

# DFS
root = build_heap_tree(heap)
dfs_nodes = dfs_color(root)
draw_colored_traversal(root, dfs_nodes, "Обхід у глибину (DFS)", "task_5_dfs.png")