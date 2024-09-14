from collections import deque


def bipartite_graph(graph, n):
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = deque([start])

            colors[start] = 0

            while queue:
                node = queue.popleft()
                for i in graph[node]:
                    if colors[i] == -1:
                        colors[i] = 1 - colors[node]
                        queue.append(i)
                    elif colors[i] == colors[node]:
                        return False
    return True


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = {i: [] for i in range(n)}

    for _ in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    output_file.write(str(int(bipartite_graph(graph, n))))
