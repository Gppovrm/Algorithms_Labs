def is_cycle_negative_weight(graph, n):
    dist = [float('inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] < float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] < float('inf') and dist[v] > dist[u] + w:
            return 1

    return 0


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = []
    for _ in range(m):
        u, v, w = map(int, input_file.readline().split())
        graph.append((u - 1, v - 1, w))
    output_file.write(str(is_cycle_negative_weight(graph, n)))
