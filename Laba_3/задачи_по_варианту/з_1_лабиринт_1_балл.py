def dfs(graph, u, v, visited):
    if u == v:
        return True
    visited[u] = True
    for node in range(len(graph)):
        if graph[u][node] and not visited[node]:
            if dfs(graph, node, v, visited):
                return True
    return False


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True

    visited = [False for _ in range(n)]

    output_file.write('1' if dfs(graph, u - 1, v - 1, visited) else '0')
