def bellman_ford(graph, n, s):
    dist = [float('inf')] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] < float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] < float('inf') and dist[v] > dist[u] + w:
                dist[v] = float('-inf')

    return dist


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = []
    for _ in range(m):
        u, v, w = map(int, input_file.readline().split())
        graph.append((u - 1, v - 1, w))

    s = int(input_file.readline().strip()) - 1

    dist = bellman_ford(graph, n, s)

    result = []
    for d in dist:
        if d == float('inf'):
            result.append("*")
        elif d == float('-inf'):
            result.append("-")
        else:
            result.append(str(d))
    output_file.write("\n".join(result))
