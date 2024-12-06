import csv

def load_graph_from_csv(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = int(row['source'])
            tgt = int(row['target'])
            if src not in graph:
                graph[src] = set()
            if tgt not in graph:
                graph[tgt] = set()
            graph[src].add(tgt)
            graph[tgt].add(src)
    return graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Đường dẫn tới file CSV
csv_file_path = 'graph.csv'

# Đọc đồ thị từ file CSV
graph = load_graph_from_csv(csv_file_path)

# Gọi hàm dfs
start_node = 1
visited_nodes = dfs(graph, start_node)
print("Các nút đã thăm:", visited_nodes)
