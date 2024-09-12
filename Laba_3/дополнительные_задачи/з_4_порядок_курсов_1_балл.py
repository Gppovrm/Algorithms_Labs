def topological_sort(n, graph):
    visited = [False for _ in range(n)]
    topo_sort_s = []

    def dfs(node):
        visited[node] = True
        for i in range(n):
            if graph[node][i] and not visited[i]:
                dfs(i)
        topo_sort_s.append(node + 1)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return topo_sort_s[::-1]


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u - 1][v - 1] = True

    result = topological_sort(n, graph)
    output_file.write(" ".join(map(str, result)))


# from collections import deque
#
# def topological_sort(n, graph):
#     in_edges = [0] * n
#     for row in graph:
#         for v, edge in enumerate(row):
#             if edge:
#                 in_edges[v] += 1
#
#     queue = deque(i for i, d in enumerate(in_edges) if d == 0)
#     topo_sort = []
#
#     while queue:
#         u = queue.popleft()
#         topo_sort.append(u + 1)
#         for v, edge in enumerate(graph[u]):
#             if edge:
#                 in_edges[v] -= 1
#                 if in_edges[v] == 0:
#                     queue.append(v)
#
#     return topo_sort
#
# with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
#     n, m = map(int, input_file.readline().split())
#     graph = [[False] * n for _ in range(n)]
#
#     for _ in range(m):
#         u, v = map(int, input_file.readline().split())
#         graph[u - 1][v - 1] = True
#
#     output_file.write(" ".join(map(str, topological_sort(n, graph))))
