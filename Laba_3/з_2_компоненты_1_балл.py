def dfs(graph, u, visited):
    visited[u] = True
    for node in graph[u]:
        if not visited[node]:
            dfs(graph, node, visited)


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [False for _ in range(n)]

    counter = 0

    for node in range(n):
        if not visited[node]:
            dfs(graph, node, visited)
            counter += 1

    output_file.write(str(counter))
